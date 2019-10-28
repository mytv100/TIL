## 문자열

### python3
* bytes : raw 8 bit
* str : unicode


### python2
* str : raw 8 bit
* unicode : unicode

---

* 가장 일반적인 인코딩 `UTF-8`
* 파이썬3의 str인스턴스와 파이썬2의 unicode인스턴스는 연관된 바이너리 인코딩이 없다.


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
