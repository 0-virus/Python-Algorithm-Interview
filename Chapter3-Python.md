파이썬(3장)
==========

## 파이썬 문법

> ## 인덴트
> - 공백 4칸을 원칙으로 한다.
> - 첫 번째 줄에 파라미터가 있으면, 파라미터가 시작되는 부분에 맞춘다.
> ```python
> total = sum(var_one, var_two,
>             var_three, var_four)
> ```
> - 파라미터가 첫 번째 줄에 있지 않으면, 4칸 인덴트를 한 번 더 추가하여 다른 행과 구분되게 한다.
> ```python
> def long_function_name(
>         var_one, var_two, var_three,
>         var_four):
>     print(var_one)
> ```
> - 여러 줄로 나누어 쓸 경우, 다음 행과 구분하기 위해 인덴트를 추가한다.
> ```python
> total = sum(
>     var_one, var_two,
>     var_three, var_four)
> ```

<br/>

> ## 네이밍 컨벤션
> - 스네이크 케이스를 따른다.
>
> > ### 스네이크 케이스
> > 1. 각 단어를 언더스코어(_)로 구분
> > 1. 일반적으로 모두 소문자 표기
> > 1. 경우에 따라 대문자로 표기(클래스 등)

<br/>

> ## 타입 힌트
> - 파이썬은 동적 언어이지만, 타입 힌트를 통해 자료형을 지정할 수 있다.
> ```python
> a: str = "1"
> b: int = 1
> 
> def fn(x: int, y: float) -> bool:
>     return x == y
> ```
> - mypy를 사용하면 타입 힌트 오류 여부를 확인할 수 있다.

<br/>

> ## 리스트 컴프리헨션
> - 기존 리스트를 기반으로 새로운 리스트를 만들어내는 구문을 의미한다.
> - 코드를 한 줄로 간결하게 쓸 수 있어 가독성이 좋아진다.
> ```python
> lst = [n * 2 for n in range(1, 10 + 1) if n % 2 == 1]
> ```
> - 리스트 외에 딕셔너리에도 사용 가능하다.
> ```python
> # 컴프리헨션 미적용
> a = {}
> for key, value in original.items():
>     a[key] = value
>
> # 컴프리헨션 적용
> a = {key: value for key, value in original.items()}
> ```

<br/>

> ## 제너레이터
> - 루프의 반복 동작을 제어할 수 있는 루틴이다.
>
> ### 예시
> ```python
> >>> def get_natural_number():
> ...    n = 0
> ...    while True:
> ...        n += 1
> ...        yield n
> ...
> 
> >>> get_natural_number()
> <generator object get_natural_number at 0x10d3139d0>
> ```
> ```yield```: ```return```과 달리 제너레이터가 지금까지 실행중이던 값을 내보냄
> <br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-> 제너레이터의 동작이 종료되지 않음
>
> 다음 값을 생성하려면 ```next()```를 이용하면 된다.
> ```python
> >>> g = get_natural_number()
> >>> for _ in range(0, 100):
> ...     print(next(g))
> ...
> 1
> 2
> 3
> ...
> 98
> 99
> 100
> ```

<br/>

> ## range
> - 제너레이터 방식의 함수
> - **리스트**는 <span style="color:red">**이미 생성된 값**</span>이 저장되어 있는 반면, **range** 데이터는 <span style="color:red">**생성해야 한다는 조건**</span>만 저장되어 있다. 따라서 메모리 점유율에서 크게 차이가 난다.
> ```python
> import sys
> 
> >>> a = [n for n in range(1000000)]
> >>> b = range(1000000)
> >>> len(a), len(b)
> 1000000, 1000000
>
> >>> sys.getsizeof(a)
> 8448728
> >>> sys.getsizeof(b)
> 48
> ```

<br/>

> ## enumerate
> - list, set, tuple 등의 자료형을 인덱스를 포함한 enumerate 객체로 반환한다.
> ```python
> lst = ['a1', 'b2', 'c3']
> for i, v in enumerate(lst):
>     print(i, v)
> ```

<br/>

> ## locals
> - 로컬에 선언된 모든 변수를 조회할 수 있다.
> - 디버깅에 매우 유용하다.
> ```python
> ...
> import pprint
> pprint.pprint(locals())
> ...
> 
> {'nums': [1, 2, 3, 4, 4],
>  'pprint': <module 'pprint' from 'C:\\...\\pprint.py'>,
>  'target': 9}

<br/>

## 코딩 스타일