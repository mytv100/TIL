#### ViewSet
 * http method 를 drf ViewSet method 로 변형을 해줌
 ~~~
   get -> list or [ retrieve(read) : detail ]
   post -> create
   put -> update
   patch -> partial_update
   del -> delete
 ~~~


 ModelViewSet has class variables `queryset`, `serializer_class`, `permission_classes`

 `queryset` : queryset about model | `self.get_queryset`

 `serializer_class` : `self.get_serializer`
 `permission_classes` : ViewSet access permission check
