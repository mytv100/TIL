# Class-based Views
* drf는 Django의 View클래스를 상속받은 APIView클래스를 제공한다.
  * 핸들러 메소드를 통과하는 Request들은 Django의 `httpResponse` instance가 아닌 drf의 `Request` instance가 된다.
  * Response도 마찬가지다.

## Dispatch methods
* view의 .dispatch() 메소드에 의해 직접 호출되는 메소드들
* 이 메소드들은  `.get()`, `.post()`, `.put()`, `.delete()` 와 같은 핸들러 메소드들을 호출하기 전이나 후에 수행해야하는 모든 작업을 수행한다.
  * .initial() : 사용 권한 및 제한 적용, content negotiation 수행
  * .handle_exception() : error response 커스터마이징할 때
  * .initialize_request()
  * .finalize_response()

# Function Based Views
