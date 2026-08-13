param(
    [string]$Root = "$env:USERPROFILE\Documents",
    [string]$RepositoryUrl = ""
)

$ErrorActionPreference = "Stop"
$ProjectPath = Join-Path $Root "chatgpt-remote-sync-test"

if (Test-Path $ProjectPath) {
    throw "이미 경로가 존재합니다: $ProjectPath"
}

if ($RepositoryUrl) {
    git clone $RepositoryUrl $ProjectPath
} else {
    New-Item -ItemType Directory -Path $ProjectPath | Out-Null
    git -C $ProjectPath init -b main
}

Write-Host "샘플 디렉터리 준비 완료: $ProjectPath"
Write-Host "ChatGPT 데스크톱 앱에서 이 폴더를 로컬 프로젝트로 추가하세요."

