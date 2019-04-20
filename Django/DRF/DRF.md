# Django REST Framework

* [Django REST Framework](https://www.django-rest-framework.org/) 는 Django를 기반으로 [RESTful](rest link) 웹 APIs 를 생성하는 효과적인 도구이다.

## DRF architecture
![drf_architecture](/assets/drf_architecture.jpg)

* drf 는 Serializer, ViewSet, Router 로 구성되어있음

  * Serializer : Django model 에 의해 정의되고 database 에 저장되어 있는 정보를 API를 통해 보다 쉽게 전송할 수 있는 형식으로 변환한다.

  * ViewSet : API를 통해 이용할 수 있는 함수(read, create, update, delete)를 정의한다.

  * Router : 각 viewset에 대한 접근을 제공할 URLs를 정의한다.

#### 실행 순서.
 1. ViewSet에서 Serializer를 통해서 request의 형태를 만들어 준다
 2. urls.py에서 Router가 ViewSet의 view들을 url과 매칭시켜준다.
 3. API를 통해 request가 들어옴
 4. urls.py에서 request의 url에 맞는 view로 request를 넘겨준다.
 5. ViewSet에서 request를 수행하고, serializer를 통해서 response의 형태를 만들어준다.
 6. ViewSet은 response를 반환해줌
