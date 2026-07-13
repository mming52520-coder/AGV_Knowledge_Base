$ErrorActionPreference = "Stop"

$root = Split-Path -Parent $MyInvocation.MyCommand.Path
$manifestPath = Join-Path $root "MANIFEST.sha256"
$treeHashPath = Join-Path $root "BUNDLE_TREE_SHA256.txt"

if (-not (Test-Path -LiteralPath $manifestPath -PathType Leaf)) {
    throw "Missing manifest: $manifestPath"
}
if (-not (Test-Path -LiteralPath $treeHashPath -PathType Leaf)) {
    throw "Missing tree hash: $treeHashPath"
}

$manifestEntries = @()
foreach ($line in Get-Content -LiteralPath $manifestPath -Encoding UTF8) {
    if ([string]::IsNullOrWhiteSpace($line)) {
        continue
    }
    if ($line -notmatch '^([0-9a-f]{64}) \*(.+)$') {
        throw "Invalid manifest line: $line"
    }
    $relative = $Matches[2].Replace('/', [IO.Path]::DirectorySeparatorChar)
    $path = Join-Path $root $relative
    if (-not (Test-Path -LiteralPath $path -PathType Leaf)) {
        throw "Missing file from manifest: $relative"
    }
    $actual = (Get-FileHash -LiteralPath $path -Algorithm SHA256).Hash.ToLowerInvariant()
    $expected = $Matches[1]
    if ($actual -ne $expected) {
        throw "Hash mismatch: $relative expected=$expected actual=$actual"
    }
    $manifestEntries += $relative
    Write-Output "OK  $relative"
}

$treeFiles = Get-ChildItem -LiteralPath $root -Recurse -File | Where-Object {
    $_.FullName -ne $treeHashPath
}
$relativePaths = [System.Collections.Generic.List[string]]::new()
foreach ($file in $treeFiles) {
    $relativePaths.Add($file.FullName.Substring($root.Length + 1).Replace('\', '/'))
}
$relativePaths.Sort([StringComparer]::Ordinal)

$treeLines = foreach ($relative in $relativePaths) {
    $nativeRelative = $relative.Replace('/', [IO.Path]::DirectorySeparatorChar)
    $path = Join-Path $root $nativeRelative
    $hash = (Get-FileHash -LiteralPath $path -Algorithm SHA256).Hash.ToLowerInvariant()
    "$hash *$relative"
}
$canonical = ($treeLines -join "`n") + "`n"
$utf8 = [Text.UTF8Encoding]::new($false)
$sha256 = [Security.Cryptography.SHA256]::Create()
try {
    $actualTreeHash = ([BitConverter]::ToString($sha256.ComputeHash($utf8.GetBytes($canonical)))).Replace('-', '').ToLowerInvariant()
}
finally {
    $sha256.Dispose()
}
$expectedTreeHash = (Get-Content -Raw -LiteralPath $treeHashPath -Encoding UTF8).Trim().ToLowerInvariant()
if ($expectedTreeHash -notmatch '^[0-9a-f]{64}$') {
    throw "Invalid expected tree hash: $expectedTreeHash"
}
if ($actualTreeHash -ne $expectedTreeHash) {
    throw "Tree hash mismatch: expected=$expectedTreeHash actual=$actualTreeHash"
}

Write-Output "TREE $actualTreeHash"
Write-Output "Bundle verification passed ($($manifestEntries.Count) manifest files, $($relativePaths.Count) tree files)."
