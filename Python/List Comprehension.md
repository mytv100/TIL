## List Comprehension(리스트 함축 표현식)

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
