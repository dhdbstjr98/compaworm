# Compaworm API

## Requirement
- python3
- django
- djangorestframework
- django-cors-headers
- requests

## APIs
### /api/user/me
- GET : 이름, 프로필 조회
- POST : OAuth 로그인

### /api/comparison/:obj1/:obj2
- GET : 비교 정보(횟수) 조회
- PUT : 비교 추가, 수정(토글)
- DELETE : 비교 삭제

### /api/comment/:obj1/:obj2
- GET : 코멘트 조회
- POST : 코멘트 작성
