## 문자열

### Python 3
* bytes : raw 8 bit
* str : unicode


### Python 2
* str : raw 8 bit
* unicode : unicode

---

* 가장 일반적인 인코딩 `UTF-8`
* 파이썬 3의 str인스턴스와 파이썬 2의 unicode인스턴스는 연관된 바이너리 인코딩이 없다.


* 유니코드 문자 -> 바이너리 데이터 : encode 메서드
* 바이너리 데이터 -> 유니코드 문자 : decode 메서드


* 핵심 부분에서는 유니코드 문자 타입을 사용

---

### 문자 타입이 분리되어 있어서 부딪히는 두 가지 상황
* UTF-8(혹은 다른 인코딩)로 인코드된 문자인 raw 8 bit 값을 처리하려는 상황
* 인코딩이 없는 유니코드 문자를 처리하려는 상황


* 위 두 경우에서는 헬퍼 함수 두 개 필요
  * python3
    * str이나 bytes를 입력받고 str을 반환하는 메서드
    * str이나 bytes를 입력받고 bytes를 반환하는 메서드
  * python2
    * str이나 unicode를 입력받고 unicode를 반환하는 메서드
    * str이나 unicode를 입력받고 str를 반환하는 메서드

#### 이슈
* 파이썬 2에서 str이 7비트 아스키 문자만 포함하고 있다면 unicode와 str 인스턴스가 같은 타입처럼 보인다.
  * str과 unicode를 + 연산자로 묶을 수 있다.
  * str과 unicode를 같음과 같지 않음 연산자로 비교할 수 있다.
  * `%s` 같은 포맷 문자열에 unicode 인스턴스를 사용할 수 있다.
  * <Strong> but, 파이썬 3에서는 bytes와 str인스턴스는 빈 문자열이라도 같지 않다.</strong>


* 내장 함수 open이 반환하는 파일 핸들을 사용하는 연산은 기본으로
  * 파이썬 3에서는 UTF-8 인코딩을 사용한다.
  * 파이썬 2에서는 바이너리 인코딩을 사용한다.
