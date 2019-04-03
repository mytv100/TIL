---
Serializer : Django model 에 의해 정의되고 database 에 저장되어 있는 정보를 API를 통해 보다 쉽게 전송할 수 있는 형식으로 변환한다.
* converts the information stored in the database and defined by the Django models into a format which is more easily transmitted via an API

ViewSet : API를 통해 이용할 수 있는 함수(read, create, update, delete)를 정의한다.
* defines the functions (read, create, update, delete) which will be available via the API

Router : 각 viewset에 대한 접근을 제공할 URLs를 정의한다.
* defines the URLs which will provide access to each viewset
#### 시작 전
1. model class에 의해서 database 생성됨


---
#### 실행 순서
 1. API로 request가 들어옴 (http://ip:port/appName/modelName 형식으로)
 2. Project의 urls.py -> App의 urls.py -> Router -> views.py ->ViewSet
 3. ViewSet에서 Serializer 호출해서 형태를 만들어줌
 4. response 를 반환해줌
---
#### Serializer
 * 보여주는 형식을 정의함, 틀
---
#### ViewSet
 * http method 를 drf ViewSet method 로 변형을 해줌
 ~~~
   get -> list or [ retrieve(read) : detail ]
   post -> create
   put -> update
   patch -> partial_update
   del -> delete
 ~~~
---
 Serializer - ModelSerializer
----
inner class `Meta` has variables `model` and `fields`            

`model` : 직렬화할 모델 클래스   
  `fields` : 포함할 필드 ["movie",] ,  `__all__`는 전체 필드 포함
  
  `read_only_fields` ['movie',] movie 는 읽기만 가능
  
  `exclude` ('movie',)  movie 만 제외, `__all__` 이랑 같이 쓸 수 없음
  ---
#### overriding
```python
def create(self, validated_data):
```  

 ---
 #### ViewSet - ModelViewSet

ModelViewSet has class variables `queryset`, `serializer_class`, `permission_classes`

`queryset` : queryset about model | `self.get_queryset`

`serializer_class` : `self.get_serializer`
`permission_classes` : ViewSet access permission check
---
#### overriding
```python
def create*self, request, *args, **kwargs): 
    ...
    ...
    
    self.perform_create(serializer) # -> serializer.save()
    

```