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
* 리스트를 가변 인수 함수를 호출할 때 사용하고 싶다면 `*` 연산자를 사용해서 `*리스트 이름` 형식으로 사용한다.
```
def func(*args):
    print(args)
```

* 문제점
    1. 가변 인수가 함수에 전달되기에 앞서 항상 튜플로 변환된다.
    -> 함수를 호출하는 쪽에서 제너레이터에 * 연산자를 쓰면 메모리 많이 차지
    2. 추후에 호출 코드를 모두 변경하지 않고서는 새 위치 인수 추가 불가능

#### 키워드 인수
* 위치 인수만으로는 이해하기 어려울 때 주로 사용
* 선택적인 키워드 인수는 항상 위치가 아닌 키워드로 넘겨야 한다.

```
def remainder(number, divisor):
    return number % divisor

# 동일한 호출
remainder(20,7)
remainder(20, divisor=7)
remainder(number=20, divisor=7)
remainder(divisor=7, number=20)

# 불가능한 호출
# 위치 인수는 키워드 인수 앞에 지정해야 한다.
remainder(number=20, 7)
>>> SyntaxError: non-keyword arg after keyword arg

# 각 인수는 한 번만 지정할 수 있다.
remainder(20, number=7)
>>> TypeError: remainder() got multiple values for argument 'number'
```

* 키워드 인수의 이점
1. 함수 호출을 더 명확하게 이해할 수 있다.
2. 함수를 정의할 때 기본값을 설정할 수 있다.
    `def remainder(number, divisor=7)` divisor의 default값은 7
3. 기존의 호출 코드와 호환성을 유지하면서 함수의 파라미터를 확장할 수 있는 강력한 수단

#### 동적 기본 인수, None & docstring
* 키워드 인수의 기본값으로 비정적(non-static) 타입을 사용해야 할 때
    * (ex) 이벤트 발생 시각까지 포함해 로깅 메시지 출력
    * datetime.now()가 함수를 정의할 때 딱 한번만 실행되므로 이 함수를 여러 번 호출하더라도 타임스탬프가 동일하게 출력된다.
    * `기본 인수의 값은 모듈이 로드될 때 한 번만 평가되며` 보통 프로그램이 시작할 때 일어난다.

    ```
    def log(message, when=datetime.now()):
        print('%s: %s' % (when, meesage))
    ```

    * 기본값을 None으로 설정하고 docstring(문서화 문자열)으로 실제 동작을 문서화하는 것이 관례다.

    ```
    def log(meesage, when=None):
        """Log a message with a stamp.

        Args:
            message: Message to print
            when: datetime of when the message occured.
                Defaults to the present time.
        """

        when = datetime.now() if when is None else when
        print('%s: %s' % (when, message))

    ```
    * 기본 인수 값으로 None을 사용하는 방법은 인수가 수정 가능(mutable)할 때 중요하다.
        * (ex) JSON 데이터로 인코드된 값을 로드, 데이터 디코딩이 실패하면 기본값으로 빈 딕셔너리 반환
        * 기본 인수 값은 딱 한 번만 평가되므로, 기본값으로 설정한 딕셔너리를 모든 decode 호출에서 공유
        ```
        def decode(data, default={}):
            try:
                return json.loads(data)
            except ValueError:
                return default
        ```
        * 키워드 인수의 기본값을 None으로 설정하고 함수의 docstring에 동작을 문서화해서 문제를 해결한다.
        ```
        def decode(data, default=None):
            """Load JSON data from a string.

            Args:
                data: JSON data to decode.
                default: Value to return if decoding fails.
                    Defaults to an empty dictionary.
            """
            if default is None:
                default = {}
            try:
                return json.loads(data)
            except ValueError:
                return default
        ```
#### 키워드 전용 인수, 명료성 강요
* 키워드 인수가 선택적인 동작이라서 함수를 호출하는 쪽에 키워드 인수로 의도를 명확하게 드러내라고 강요할 방법이 없다.
* 파이썬 3에서는 키워드 전용 인수(keyword-only-argument)로 함수를 정의해서 해결할 수 있다.
* 아래의 예시에서 인수 리스트에 있는 * 기호는 위치 인수의 끝과 키워드 전용 인수의 시작을 가리킨다.
```
def safe_division_c(number, divisor, *,
                    ignore_overflow=False, ignore_zero_division=False):
    # ...


safe_division_c(1, 10**500, True, False)
>>> TypeError: safe_division_c() takes 2 positional arguments but 4 were given
```

* 파이썬 2에는 키워드 전용 인수를 지정하는 명시적 문법이 없다.
* 인수 리스트에 ** 연산자를 사용해 올바르지 않은 함수 호출을 할 때 TypeError를 일으키는 방법으로 같은 동작을 만들 수 있다.

```
# 파이썬 2
def safe_division_d(number, divisor, **kwargs):
    ignore_overflow = kwargs.pop('ignore_overflow', False)
    ignore_zero_div = kwargs.pop('ignore_zero_division', False)
    if kwargs:
        raise TypeError('Unexpected **kwargs: %r' % kwargs)
        
```
