* Compile time - 소스 코드를 기계어로 변환하는 과정
  * Compile error - 구문 에러(Syntax error)
* Run time - 어떤 프로그램이 실행되는 동안의 시간
  * Runtime error
    * ZeroDivisionError
    * IndexError
    * NameError

---

* 런타임 환경(인터프리터의 구현)

1. CPython
  * C로 작성된 파이썬 구현의 리퍼런스
  * 파이썬 코드를 가상 머신에 의해 해석되는 중간 바이트코드로 컴파일한다.
  * 파이썬 패키지와 C언어의 확장 모듈간에 최고 레벨의 호환성을 제공

2. Jython
  * 파이썬 코드를 자바 바이트코드로 만들어 JVM(자바 가상 머신)에서 실행시키는 파이썬 구현
  * 자바 클래스를 파이썬 모듈처럼 불러와서 사용할 수 있다.

3. IronPython
  * 닷넷 프레임워크를 위한 파이썬 구현이다.
  * 파이썬과 닷넷 프레임워크 라이브러리 둘다 사용할 수 있다.
  * 파이썬 코드를 닷넷 프레임워크의 다른 언어로 바꿀 수 있다.

4. PyPy
  * 파이썬 언어의 정적 타입으로만 구현된 파이썬 인터프리터로서 통칭 RPython이라 불린다.
  * just-in-time 컴파일러와 복수의 백엔드(C, CLI, JVM)를 지원한다.
  * 벤치마크에서 CPython보다 5배나 빠르게 나왔다.
