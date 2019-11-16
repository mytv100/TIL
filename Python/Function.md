### Function - 함수에 대한 것들
* 함수 반환 값 리스트 -> 제너레이터(generator) 사용
  * 제너레이터는 yield 표현식을 사용하는 함수다.
  * 제너레이터 함수는 호출되면 실제로 실행하지 않고 바로 이터레이터(iterator)를 반환한다.
  * 내장 함수 next를 호출할 때마다 이터레이터는 제네레이터가 다음 yield 표현식으로 진행하게 한다.
  * 제너레이터에서 yield에 전달한 값을 이터레이터가 호출하는 쪽에 반환한다.

```
# 1. 리스트 반환 함수
def index_words(text):
    result = []
    if text:
        result.append(0)
    for index, letter in enumerate(text):
        if letter == ' ':
            result.append(index+1)
    return result

address = 'Four score and seven years ago...'
result = idnex_words(address)
print(result[:3])

>>>
[0, 5, 11]

# 2. 제네레이터 함수
def index_words_iter(text):
    if text:
        yield 0
    for index, letter in enumerate(text):
        if index == ' ':
            yield index + 1

result = list(index_words_iter(address))

```

* 1. index_words 함수의 단점
  1. 코드가 복잡하고 깔끔하지 않다.
  2. 반환하기 전에 모든 결과를 리스트에 저장해야 한다.
    * 입력이 매우 많다면 프로그램 실행 중에 메모리가 고갈되어 동작을 멈출 수 있다.


* <strong>이터레이터에 상태가 있고 재사용할 수 없다.</strong>
