Pystargram Tutorial

### 1. Pystargram 기획

#### 

#### 1. 개요 

- Pystagram = Instagram + Python

- 이용자가 사진 올리고 필터 적용하는 기능 제공

  ​

#### 2. Pystagram 기능 

사진
- 사진  올리기 <!--로그인한 사용자만 올린다!-->  
  - 기본 URL: `/photos/upload/`
  - 필터 적용 <!--사진 올릴 때에만 적용 가능하다!--> 
  - 미리보기 이미지 (Thumnail)
  - 사진 자르기, 크기 조절 <!--640 * 640 지원--> 
- 사진 보기 <!--사진 생성 정보: 사진, 작성자, 작성일시, 본문-->  
  - 기본 URL: `/photos/<사진 ID="">`
  - 좋아요 표시 남기기 `/photos/<사진 ID="">/like`
  - 댓글 남기기, 지우기 <!--작성자, 댓글 본문, 작성일시, 댓글 삭제 버튼, 사용자 지정 댓글 달기-->
    - 댓글 달기: `/photos/<사진 ID="">/comment`
    - 댓글 가져오기: `/photos/<사진 ID="">/get_comments/`
    - 댓글 삭제하기: ``/photos/<사진 ID="">/comment/<댓글 ID=""/delete`
- 사진 삭제
  - 기본 URL: `photos/<사진 ID="">/delete`
- 태그 달기
  - 기본 URL: `/photos/<사진 ID="">/tag/`

    ​

이용자/회원
- 회원 가입과 탈퇴: `/accounts/registration/`

- 로그인, 로그아웃:  `/accounts/login/`,  `/accounts/logout/`

- 비밀번호 찾기

- 프로필 보기: `/users/<이용자 ID="">/`
  - 간단한 소개
  - 팔로잉, 팔로워:  `/users/<이용자 ID="">/following`,  `/users/<이용자 ID="">/follower`
  - 이용자가 올린 사진

- 팔로잉 기능:  `/users/<이용자 ID="">/follow`

  ​

사진 모아보기
- 타임라인: 친구 사진 보기

- 인기 사진 보기

- 특정 이용자의 사진 보기

  ​



#### 3. 페이지 구성

- 첫페이지
  - 회원가입
  - ID/비밀번호 찾기
  - 로그인
- 타임라인
  - 사진 보기
    - 좋아요 표시
    - 댓글 남기기
    - 댓글 지우기 
    - 사진 지우기
    - 태그 달기
- 사진 올리기
- 인기 사진
- 이용자 프로필
  - 팔로잉하기
  - 팔로워 리스트
  - 팔로잉 리스트
  - 로그아웃
  - 회원 탈퇴
  - 계정 설정 및 프로필 수정