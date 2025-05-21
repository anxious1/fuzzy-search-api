$projectDir = "$env:USERPROFILE\fuzzy-search-api"
$repoUrl    = "https://github.com/anxious1/fuzzy-search-api.git"

if (-not (Test-Path $projectDir)) {
    git clone $repoUrl $projectDir
}

Set-Location $projectDir

if (-not (Test-Path ".\venv")) {
    python -m venv venv
}

Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned -Force
. .\venv\Scripts\Activate.ps1

python -m pip install --upgrade pip
python -m pip install -r requirements.txt

python .\scripts\init_db.py

python -m uvicorn app.main:app --reload
