## 표준 라이브러리

* 운영체제 인터페이스 os
    * `from os import *`보단 `import os`를 사용하는 것이 좋다. 그래야 `os.open()`이 내장 `open()`을 가리키는 것을 피할 수 있다..
    * dir(), help() - 대화형 도우미
    * shutil 모듈 - 일상적인 파일과 디렉터리 관리 작업을 위한 사용하기 쉬운 인터페이스 제공
* 파일 와일드 카드 glob
    * glob 모듈은 디렉터리 와일드카드 검색으로 파일 목록을 만드는 함수를 제공한다.
* 명령행 인자
    * argparse 모듈은 명령행 인자를 처리하는 더 복잡한 메카니즘을 제공한다.
    * 하나 이상의 파일명과 보여주기 위한 선택적인 라인의 수를 추출하는 코드이다.
* 에러 출력 리디렉션과 프로그램 종료
    * sys 모듈은 stdin, stdout, stderr 어트리뷰트도 가지고 있다.
    * stderr는 stdout이 리디렉트 됬을 때도 볼 수 있는 경고와 에러메시지를 출력
* 문자열 패턴 매칭
    * re 모듈은 고급 문자열 처리를 위한 정규식 도구들을 제공.
    * 복잡한 매칭과 조작을 위해, 정규식은 간결하고 최적화된 솔루션을 제공
* 수학
    * math 모듈은 부동 소수점 연산을 위한 하부 C라이브러리 함수들에 대한 액세스를 제공
    * random 모듈은 무작위 선택을 할 수 있는 도구를 제공
    * statistics 모듈은 수치 데이터의 기본적인 통계적 특성들을 계산
* 인터넷 액세스
    * urllib.request - URL에서 데이터를 읽어오는 모듈
    * smtplib - 메일을 보내는 모듈
* 날짜와 시간
    * datetime - 날짜와 시간을 조작하는 클래스들을 제공
* 데이터 압축
    * zlib, gzip, bz2, lzma, zipfile, tarfile - 데이터 보관 및 압축 형식들을 직접 지원
* 성능 측정
    * timeit, profile, pstats
* 품질 관리
    * doctest, unittest
* 출력 포매팅
    * reprlib, pprint, textwrap, locale
* 템플릿
    * string
* 바이너리 데이터 레코드 배치 작업
    * struct
* 다중 스레딩 작업
    * threading
* 로깅
    * logging 모듈은 완전한 기능을 갖춘 유연한 로깅 시스템을 제공
* 약한 참조
    * weakref 모듈은 참조를 만들지 않고 객체를 추적할 수 있는 도구를 제공
* 리스트 작업 도구
    * array, collections
* 10진 부동 소수점 산술
    * decimal
