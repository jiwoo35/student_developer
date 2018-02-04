Pystargram Tutorial

### 2. 개발 환경 꾸리기

####  

#### 1. Python 설치

- `python --version` 확인

- <!--3.6.3-->

  ​



#### 2. 개발 환경 구축

- pip 설치 

  - Python에 사용되는 각종 패키지를 설치하거나 업그레이드, 삭제 등을 하는 관리 도구
  - 파이썬 3.6 버전에서는 pip를 자동으로 설치해준다

- virtualenv 설치

  - 가상으로 Python 환경 만드는 도구
  - `python -m venv`

- SQLite 설치

  - 데이터를 저장하는데 필요한 데이터베이스
  - Python에 기본 내장되어 있음 `import sqlite3`

  ​

#### 3. Django 설치

- 가상 환경 생성과 진입

  - 생성: `python -m venv venv`
  - 진입: `venv\Scripts\activate.bat`

- Django 설치

  - `pip install django`
  - `python -c "import django; print(django.__file__)"`
    - django 설치 경로 확인: .../**venv**/lib/site-packages/django

  ​

#### 4. 편리한 도구 설치

- Postman - REST Client: HTTP 기반으로 동작하는 API를 편리하게 호출하는 Client

- 편집기 : PyCharm 사용

  ​



#### 5. Python

- 기본적인 Python 문법
- Soft tab 방식 사용
  - Space 4칸 = Tab 1칸