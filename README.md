## 회원가입 구현
1. 일반 user
- 필드: email, nickname, name, phone_num, child_name, child_birth, password
-> 아이 키, 몸무게도 필요한가?

2. 관리자 user
- 필드: email, nickname, name, phone_num, child_name, child_birth, password

로그인은 뭘 이용해서?
ID: nickname
PW: password

3. API test: postman 이용
회원가입 -> admin 페이지에서 user 정보 확인 가능
로그인 -> admin 페이지에서 로그인 시간 확인 가능
- API 작동 확인: https://www.postman.com/

### 1월 21일
- detection-app 생성
- model 정의 => Object Detection과 Pose Detection 을 위한 스키마 생성
- 개인 로컬에서 테스트하기 편하도록 sqlite로 임시 변경


- views.py 작업해야 합니다
