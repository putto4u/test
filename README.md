# ChatGPT Remote GitHub 연동 테스트

북5의 로컬 Git 저장소를 ChatGPT 데스크톱 앱의 로컬 프로젝트로 열고,
S22의 Remote에서 같은 호스트와 작업 스레드를 제어하는지 검증하기 위한 최소 샘플입니다.

## 실행

```powershell
python app.py "북5와 S22 연동 성공"
python -m unittest discover -s tests -v
```

정상 출력 예시:

```text
ChatGPT Remote Test: 북5와 S22 연동 성공
```

## 연동 검수용 작업

S22의 ChatGPT 앱에서 Remote로 북5에 접속한 뒤 다음과 같이 지시합니다.

> 이 프로젝트의 `app.py` 기본 메시지를 `S22에서 수정 완료`로 변경하고 테스트를 실행해 줘. 변경 내용을 보여주되 아직 커밋하지 마.

북5에서 diff와 테스트 결과를 확인한 다음 다음과 같이 지시합니다.

> 변경을 `test: verify S22 remote edit`라는 메시지로 커밋하고 GitHub에 push해 줘.

