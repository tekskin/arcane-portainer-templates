param(
  [Parameter(Mandatory=$true)]
  [string]$BaseUrl
)

$ErrorActionPreference = "Stop"
python .\build_arcane_registry.py --base-url $BaseUrl
if ($LASTEXITCODE -ne 0) { throw "Conversion failed." }

if (Get-Command python -ErrorAction SilentlyContinue) {
  python .\validate_arcane_registry.py
}
