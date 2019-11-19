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

#### 인수를 순회할 때는 방어적으로 하자
* 이미 소진한 이터레이터를 순회하더라더 오류가 발생하지 않는다.
  * 결과가 없는 이터레이터와 이미 소진한 이터레이터의 차이를 알 수 없음.
* 방어적으로 복사하는 방법
  * 입력 이터레이터를 명시적으로 소진
  * 전체 콘텐츠의 복사본을 리스트에 저장
* 문제점
  * 콘텐츠의 복사본이 크면 메모리가 고갈되어 멈출 수 있다.
* 해결 방법
  * 호출될 때마다 새 이터레이터를 반환하는 함수를 받게 만든다.

```
# 해결 방안 적용
def normalize_func(get_iter):
    total = sum(get_iter()) # 새 이터레이터
    result = []
    for value in get_iter(): # 새 이터레이터
        percent = 100 * value / total
        result.append(percent)
    return result

# 매번 새 이터레이터를 생성하는 람다 표현식을 넘겨줌
percentage = normalize_func(lambda: read_visit(path))  
```

* 더 좋은 해결 방법
    * 이터레이터 프로토콜을 구현한 새 컨테이너 클래스를 제공
        * 이터레이터 프로토콜은 파이썬의 for루프와 관련 표현식이 컨테이너 타입의 콘텐츠를 탐색하는 방법을 나타낸다.
            1. 파이썬에서 for x in foo -> iter(foo) 호출
            2. iter는 `foo __iter__` 호출
            3. `__iter__` 메서드는 이터레이터 객체를 반환(`__next__` 메서드를 구현하는)
            4. for 루프는 이터레이터 모두 소진할때까지 이터레이터 객체에 내장함수 next를 계속 호출
    * 여행자 데이터를 담은 파일을 읽는 iterable(순회 가능) 컨테이너 클래스
    ```
    def normalize(numbers):
        total = sum(numbers)
        result = []
        for value in numbers:
            percent = 100 * value / total
            result.append(percent)
        return result

    class ReadVisits(object):
        def __init__(self, data_path):
            self.data_path = data_path

        def __iter__(self):
            with open(self.data_path) as f:
                for line in f:
                    yield int(line)

    visits = ReadVisits(path)
    percentages = normalize(visits)
    print(percentages)
    ```
    * `normalize`의 `sum` 메서드가 `ReadVisits.__iter__`를 호출해서 새 이터레이터 객체 할당
    * `normalize`의 for 루프도 두 번째 이터레이터 객체를 할당할때 `__iter__`를 호출(숫자 정규화 부분)
    * 두 이터레이터가 독립적으로 작동한다. 입력 데이터를 여러 번 읽는다는 것이 단점이다.

    * 파라미터가 단순한 이터레이터가 아님을 보장하는 함수
    * 단순한 이터레이터는 거부하고, 이터레이터 프로토콜을 따르는 컨테이너면 기대한 대로 동작한다.
    ```
    def normalize_defensive(numbers):
        if iter(numbers) is iter(numbers):  # 이터레이터 거부
            raise TypeError('Must supply a container')
        total = sum(numbers)
        result = []
        for value in numbers:
            percent = 100 * value / total
            result.append(percent)
        return result
    ```
* 어떤 값에 iter를 두 번 호출했을 때 같은 결과가 나오고 내장 함수 next로 전진시킬 수 있다면
그 값은 컨테이너가 아닌 이터레이터다.

#### 가변 위치 인수
* 선택적인 위치 인수(관례적으로 `*args`, star args라고도 함) -> 함수 호출을 명확하게 함
* 마지막 위치 파라미터 이름 앞에 `*`를 붙여준다.


* 문제점
    1. 가변 인수가 함수에 전달되기에 앞서 항상 튜플로 변환된다.
    -> 함수를 호출하는 쪽에서 제너레이터에 * 연산자를 쓰면 메모리 많이 차지
    2. 추후에 호출 코드를 모두 변경하지 않고서는 새 위치 인수 추가 불가능

    
