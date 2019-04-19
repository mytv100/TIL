# Request
* Django REST 프레임워크의 Request 클래스는 표준 HttpRequest를 확장(상속X)하고, REST 프레임 워크의 유연한 request parsing 과 request authentication을 지원한다.
* request는 client로부터 들어오는 요청

## Request's property
* Request parsing
  * .data : body부분의 content를 담고있다.
  * .query_params : 장고의 표준 request.GET에 대해 보다 정확하게 명명되었다. request.GET 보다 requset.query_params 쓰는 것 추천
  * .parser : APIView 클래스나 @api_view 데코레이터는 이 property가 자동적으로 Parser 인스턴트의 리스트로 설정되는 것을 보증한다.
</br>
* Content negotiation
  * 다른 미디어 타입에 대해서 다른 직렬화 스키마를 선택할 수 있도록 해준다.
  * .accepted_renderer
  * .accepted_media_type
  </br>
* Authentication
  * APi의 다른 부분에 다른 인증 정책을 사용할 수 있다.
    ex) list는 IsAdminUser만 get은 IsAuthenticated만
  * .user : 인증한 사용자(django.contrib.models.User), 인증안하면 AnonymousUser
  * .auth : 추가적인 인증 contenxt (default value는 None)
  * .authenticators
  </br>
* Browser enhancements
  * .method : request의 HTTP method의 대문자로 되어있는 문자열 표현
  * .content_type : request의 body의 media type
  * .stream
