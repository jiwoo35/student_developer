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
  -  `b = [1, 2, 3]`
  -  `c = ['Life', 'is', 'too', 'short']`
  -  `d = [1, 2, 'Life', 'is']`
  -  `e = [1, 2, ['Life', 'is']]`

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
    
      

### 5. 딕셔너리

- Key와 Value 형태로 짝지어진 사전 자료형
- 시퀀스 자료형과 달리 순서를 보장하지 않음
- **변경 가능한** 객체
  - `dic = {'name':'Jiwoo', 'phone':'01022643318'}` # Key: name, phone, Value: Jiwoo, 01022643318
  - `dic.items()` # 키, 값 가져오기
  - `dic.keys()` # 키 가져오기
  - `dic.values()` # 값 가져오기



## 코드 구조

### 1. 컴프리헨션

iterator를 사용하여 조건문, 반복문을 간편하게 작성할 수 있는 방법

#### - 리스트 컴프리헨션

- `'list1 = [1, 4, 6, 8}` 
- `print([x * 2 for x in list1 if x%2==0])`  # [8,12,16] 출력

#### - 사전 컴프리헨션

- `dict1={'int':1, 'float':2.5, 'string':'test'}`
- `print({value:key for key, value in dict1.items()})` # key와 value 값 반대로 출력 

#### - 집합 컴프리헨션

- `set1 = set(range(10))`

- `print(set1)`

- `print(x ** 2 for x in set1)` #set의 제곱수 출력

  ​

### 2. 모듈과 패키지

#### - 모듈 

##### - 파이썬 파일 (.py)

- 함수, 변수 또는 클래스들을 모아 놓은 파일

- from 모듈이름 import 모듈함수

- 모듈함수 정의 

  - 예) # mod1.py

    `def sum(a,b):`

    ​	`return a+b`

- 모듈함수 사용

  - `from mod1 import sum`

    `sum(3,4)` #7 반환

#### - 패키지 

##### - 파일 디렉토리와 모듈

- '점(.)'를 이용하여 파이썬 모듈을 계층적으로 관리
- game/
  - *__init__.py*
  - sound/
    - __init__.py
    - echo.py
    - wave.py
  - graphic/
    - init.py
    - screen.py
    - render.py


- 디렉토리 : game,sound,graphic, 모듈: .py 파일



## 심화 개념

### 1. Decorator

- Python에서 함수는 **1급 객체**

- 기존 함수에 기능을 추가하거나 새로운 함수를 만드는 역할

- 공통적으로 사용하는 코드를 쉽게 관리, **재사용**할 수 있음

  - 예시코드 

  - `class Example:`

    ​	`def __init__(self, func):`

    ​		`print("Initializing Example")`

    ​		`self.func = func;`

    ​	`def __call__(self):`

    ​		`print("Start", self.func.__name__)`

    ​		`self.func();`

    ​		`print("End", self.func.__name__)`

    **`@Example`** <!--데코레이터-->

    `def my_function():`

    ​	`print("hello, world.")`

    `print (Program start)`

    `my_function();`

  - 출력내용 <!--Initialize Example / Program Start / Start my_function / hello, world. / End my_function-->

### 2. Iterator

- 반복가능한 Iterable 객체 중의 하나

- **next()** 메소드를 가지는 실행 가능한 객체

  - `a = [1, 2, 3, 4, 5]`

  - `b=iter(a)`

  - `for i in a:`

    ​	`print(i)`	# 1 2 3 4 5 차례로 출력

### 3. Generator

- **yield**문을 포함하는 함수

- 순환할때마다 필요한 값을 발생시킴``

  - `def num_generator(n):`

    ​	`print("Function Start")`

    ​	`while n<10:`

    ​		`yield n`

    ​		`n+=1`

    ​	`print("Function End")`

    `for i in num_generator(1):`

    ​	`print(i)`

  - <!--Function Start / 1부터 9까지 출력 / Function End-->