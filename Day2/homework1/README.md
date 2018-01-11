# **Python 정리**

## 기본 자료형

### 1. 숫자형

- ##### 파이썬과 같은 동적 언어는 **할당되는 순간 데이터 타입이 정해짐**

- int, float 자료형에 대한 구분 없이 `var1=1`, `var2=1.0` 과 같이 선언 가능

  - `print(type(val1))` <!--결과: <class 'int'>-->
  - `print(type(val2))` <!--결과: <class 'float'>-->

### 2. 순서형 자료형 (Sequence)

- ##### 양의 정수로 인덱스되게 순서대로 객체들이 나열된 모음

- ##### 반복 가능한 객체 (iterable)

  - `a="abcd"`	# 문자열
  - `b = ['a', 'b', 'c', 'd']`  # 리스트
  - `c = ('a', 'b', 'c', 'd')`  # 튜플

### 3. 문자열

- ##### 변경 불가능한 순서열 객체

- ##### 문자형 객체의 연속된 묶음

- 아래와 같이 **큰따옴표, 작은따옴표** 모두 지원

  - `str1='Hello World'`

  - `str2="Python is fun"`

  - `str3='''Life is too short,` <!--여러 줄인 경우 따옴표 3개 사용-->

    `You need to enjoy the life'''`

  - `str4="""Hello I'm Jiwoo.`

    `Nice to meet you."""`

#### - 문자열 포매팅

- 문자열 내에 어떤 값을 삽입하는 방법

  - 숫자 바로 대입:  `"I eat %d apples." % 3`

  - 문자열 바로 대입:`"I eat %s apples." % "five"`

  - 숫자 값을 나타내는 변수로 대입: `number =3`

    `"I eat %d apples." % number`

  - 2개 이상의 값 대입: `number = 10`

     `day = "three"`

     `"I ate %d apples. so I was sick for %s days." % (number, day)`

#### - 문자열 슬라이싱

위의 문자열에서 원하는 문자열을 추출하고 싶을때 <u>시작 번호, 끝 번호</u>를 지정하여 출력 가능

- `str1[0:5]` 	<!--'Hello' 출력-->
- `str2[10:]`     <!--'fun' 출력-->

###4. 리스트와 튜플

#### - 리스트

- **순서를 갖는** 다양한 객체들의 시퀀스
- **변경 가능한** 객체
- 리스트명 = [요소1, 요소2, 요소3, ...]
  -  `a = [ ]` 또는 `a=list()` #비어 있는 리스트
  - `b = [1, 2, 3]`
  - `c = ['Life', 'is', 'too', 'short']`
  - `d = [1, 2, 'Life', 'is']`
  - `e = [1, 2, ['Life', 'is']]`

#### - 튜플

- 상수 리스트
- **변경 불가능한** 객체
- 튜플명 = (요소1, 요소2, 요소3, ...)
  - `t1=()`
  - `t2=(1,)`
  - `t3=(1,2,3)`
  - `t4=1,2,3`
  - `t5=('a','b',('ab','cd'))`

#### - Sequence Packing/Unpacking

- ##### Packing:  여러 항목을 리스트나 튜플에 넣는 것

   - 여러 개의 데이터를 하나의 변수에 담는 코드 :
     - `numbers={1, 2, 3, 4, 5}`
     - `numbers=1, 2, 3, 4, 5`

- ##### Unpacking: 리스트나 튜플에 있는 항목을 변수들로 풀어 헤쳐 담는 것

   - 변수의 튜플을 이용해 시퀀스의 데이터 나누어 대입하는 코드:
     - `(a, b, c, d, e) = numbers`
     - `a, b, c, d, e = numbers`

  undefined대입문에서 양 변의 시퀀스 길이는 일치해야 한다!
    * ~~`a, b, c = numbers`~~ 	#에러
      * <!--Traceback (most recent call last):  File "<stdin>", line 1, in <module>ValueError: too many values to unpack (expected 3)-->

    * `a, b, c, d, _ = numbers` # **필요 없는 원소를 _ 변수에 대입**

      ​

### 5. 딕셔너리

