# Run the four groups in order. All suites run even if an earlier one fails.
# Run from the project root: .\run_suites.ps1
$failed = $false
foreach ($suite in @('student', 'teacher', 'auth', 'csvdata')) {
    Write-Host "`nRunning $suite suite..."
    python -m pytest test/ -m $suite -v --tb=short
    if ($LASTEXITCODE -ne 0) { $failed = $true }
}
if ($failed) { exit 1 }
exit 0
