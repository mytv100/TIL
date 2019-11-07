## List Comprehension(리스트 함축 표현식)
* 한 리스트에서 다른 리스트를 만들어내는 간견한 문법
* 내장 함수 map과 filter 대신 list comprehension을 사용
  * filter와 map을 사용한 식이 더 복잡해 보인다.
* 딕셔너리와 세트도 컴프리헨션 표현식을 지원한다.

```
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares = [x**2 for x in a]
# squares = map(lambda x: x ** 2, a)
print(squares)

>>> [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```
```
even_squares = [x**2 for x in a if x % 2 == 0]
# even_squares = map(lambda x: x**2, filter(lambda x: x % 2 == 0, a))
print(even_squares)

>>> [4, 16, 36, 64, 100]

```

---
* 리스트 컴프리헨션에서 표현식을 2개 넘게 쓰지 말자
  * 중첩되다 보면 이해하기 어려워짐
* 같은 루프 레벨에 여러 조건이 있으면 암시적인 and 표현이 된다.
```
b = [x for x in a if x > 4 if x % 2 == 0]
                           and
```
---
* 문제점 : 입력 시퀀스에 있는 각 값별로 아이템을 하나씩 담은 새 리스트를 통째로 생성
  * 입력이 클 때는 메모리를 많이 소모
  * ex) 파일을 읽고 각 줄에 있는 문자의 개수 반환 -> 파일에 오류가 있거나 끊김이 없는 네트워크 소켓일 경우 문제 발생


* 위 문제를 해결하기 위해서 제너레이터 표현식(generator expression)을 제공
* 제너레이터 표현식은 리스트 컴프리헨션과 제너레이터를 일반화한 것
* 실행될 때 출력 시퀀스를 모두 구체화하지 않는다.(메모리 로딩 X)
* 대신 이터레이터(iterator, 한 번에 한 아이템을 내줌)로 평가된다.


* 제너레이터 표현식은 다른 제너레이터 표현식과 함께 사용할 수 있다.

```
it = (len(x) for x in open('/tmp/my_file.txt'))
print(it)
>>> <generator object <genexpr> at 0x101b81480>

roots = ((x, x**0.5) for x in it)
print(next(roots))
>>> (15, 3.813491)

이터레이터 it가 이터레이터 roots의 입력으로 사용된다.
```

* 이터레이터는 상태가 있으므로 한 번 넘게 사용하지 않도록 주의!
