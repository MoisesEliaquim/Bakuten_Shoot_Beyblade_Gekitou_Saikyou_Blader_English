$ErrorActionPreference = 'Stop'
$appPath = Join-Path $PSScriptRoot 'local_app.py'
$runtimePath = Join-Path $env:USERPROFILE '.cache\codex-runtimes\codex-primary-runtime\dependencies\python\pythonw.exe'
if (-not (Test-Path -LiteralPath $runtimePath)) {
    $pythonCommand = Get-Command pythonw.exe -ErrorAction SilentlyContinue
    if (-not $pythonCommand -or $pythonCommand.Source -like '*WindowsApps*') {
        throw 'Python local nao encontrado. Use Python 3.12 com Pillow ou configure o caminho em launch_local.ps1.'
    }
    $runtimePath = $pythonCommand.Source
}
Start-Process -FilePath $runtimePath -ArgumentList @('"' + $appPath + '"') -WorkingDirectory (Split-Path $PSScriptRoot -Parent) -WindowStyle Hidden
