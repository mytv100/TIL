# Response
* Response 클래스를 사용하는 것은 content-negotiated Web API responses를 위한 더 나은 인터페이스를 제공한다  
* 다른 Response 클래스써도 상관없음

## Creating responses
### Response(data, status=None, template_name=None, headers=None, content_type=None)
* Arguments
  * data : response에 포함될 직렬화된 데이터
  * status : response에 포함될 상태 코드
  * template_name : template이 있을 경우, 여기에 넣어준다.
  * headers : response에 사용될 http 헤더
  * content_type : response의 content 타입 (json, xml, etc)

### Attributes
* 아래의 것들을 따로 설정해줄 수 있다.
* .data
* .status_code
* content
* .template_name
* .accept_renderer
* .accepted_media_type
* .renderer_context

## Standard HttpResponse attributes
* Response는 SimpleTemplateResponse를 상속받음 -> SimpleTemplateResponse의 attributes랑 methods 사용가능하다
* .render() : 이 메서드는 최종 response content에 직렬화된*serialized) 데이터를 나타낸다(render).
