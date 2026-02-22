# init_git.ps1
# Run this in PowerShell from the workspace root to initialize a git repo

if (-not (Get-Command git -ErrorAction SilentlyContinue)) {
    Write-Host "Git is not installed or not in PATH. Please install Git for Windows: https://git-scm.com/download/win"
    exit 1
}

git init
git add lca-sachet
git commit -m "Add initial LCA sachet project files and scripts"
Write-Host "Initialized git repo and created initial commit. Open VS Code Source Control to view history."
