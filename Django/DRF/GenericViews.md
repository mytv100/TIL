# Generic views
* 일반적으로 사용되는 패턴을 제공하는 사전에 정의된 views
```
class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdminUser,)

    def list(self, request)
        # get_queryset() 사용함 self.queryset 대신에
        queryset = self.get_queryset()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)
```
## GenericAPIView
* REST framework's APIView 클래스 + standard list and detail views
### Attributes
* Basic settings
  * queryset : 뷰에서 객체를 반환하는데 사용해야하는 쿼리셋
  * serializer_class : 입력에 대한 validating 과 deserializing, 출력에 대한 serializing 할 때 사용된다.
  * lookup_field : 각 모델의 객체들에 대한 조회에 사용되는 model field다. default는 `pk`다.
    * hyperlinked APIs를 사용하고
    * 커스텀 value를 사용할 필요가 있다면
    * API views와 serializer_class 둘 다 lookup_field를 지정해줘야 한다.
  * lookup_url_kwarg : 객체 조회에 사용되는 URL kward argument
    * URL conf 이 값에 대응하는 keyword argument를 가지고 있어야 한다.
    * 설정안하면 default는 lookup_field의 값이다.

* Pagination
  * list views랑 사용될 때 pagination을 control하기 위해서 사용된다.
  * pagination_class : list의 결과들을 paginating할 때 사용된다.
    * default는 DEFAULT_PAGINATION_CLASS setting과 같은 값을 가진다.
    * `pagination_class=None` 뷰에서 pagination을 비활성화한다.
* Filtering
  * filter_backends : queryset을 filtering하기위해 사용되는 filter backend classes의 리스트
    * default는 DEFAULT_FILTER_BACKENDS setting과 같은 값을 가진다.
### Methods
* Base methods:
  * get_queryset(self)
    * list views에서 사용될 queryset 반환
    * detail views에서 조회를 위한 base로 사용됨
    * default는 queryset attribute 값 반환
    * `self.queryset`은 한 번만 evaludate되기 때문에, 이 메소드를 사용함
    ```
    def get_queryset(self):
        user = self.request.user
        return user.accounts.all()
    ```
  * get_object(self)
    * detail views에 사용되는 object instance를 반환한다.
    * default는 기본 쿼리셋을 lookup_field parameter를 이용해서 필터링한다.
    * 한개 이상의 URL kwarg에 기반한 객체 조회와 같은 복잡한 동작을 제공하기위해 오버라이딩할 수 있음
    ```
    def get_object(self):
      queryset = self.get_queryset()
      filter = {}
      for field in multiple_lookup_fields:
        filter[field] = self.kwargs[field]

      obj = get_object_or_404(queryset, **filter)
      self.check_object_permissions(self.request, obj)
      return obj
    ```
    * object level permission이 없으면 check_object_permissions 제외해도 된다.

  * filter_queryset(self, queryset)
    * 쿼리셋이 주어지면, 사용중인 모든 filter backends로 필터링하여 새로운 쿼리셋을 반환한다.
    ```
    def filter_queryset(self, queryset):
      filter_backends = (CateogryFilter,)

      if 'geo_route' in self.request.query_params:
        filter_backends = (GeoRouteFilter, CateogryFilter)
      elif 'geo_point' in self.request.query_params:
        filter_backends = (GeoPointFilter, CateogryFilter)

      for backend in list(filter_backends):
        queryset = backend().filter_queryset(self.request, queryset, view=self)

      return queryset
    ```
  * get_serializer_class(self)
    * serializer 클래스 반환
    * default는 serializer_class attribute 값을 반환한다.
    * read와 write에 다른 serializer사용하거나 다른 타입의 유저들에게 다른 serializer 제공할 수 있다.
    ```
    def get_serializer_class(self):
        if self.request.user.is_staff:
            return FullAccountSerializer
        return BasicAccountSerializer
    ```
* Save and deleion hooks
  * mixin class들에 의해 제공된다.
  * perform_create(self, serializer) - 새로운 object instance를 저장할 때 CreateModelMixin에 의해 호출됨
  * perform_update(self, serializer) - 존재하는 object instance를 저장할 때 UpdateModelMixin에 의해 호출됨
  * perform_destroy(self, instance) - object instance를 삭제할 때 DestroyModelMixin에 의해 호출됨
  * 이러한 훅 메소드들은 request에 내포되어 있지만 request data의 일부가 아닌 속성을 설정하는 데 유용하다.
  * (ex) request user를 기준 or URL 키워드 인수를 기반으로 object에 attribute를 설정할 수 있다.
  ```
  # object를 저장하기 전이나 후에 동작 정의 가능(logging 등)
  def perform_update(self, serializer):
      instance = serializer.save()
      send_email_confirmation(user=self.request.user, modified=instance)

  # database 저장 시점에서 validation이 필요할 때 사용 가능
  def perform_create(self, serializer):
      queryset = SignupRequest.objects.filter(user=self.request.user)
      if queryset.exists():
          raise ValidationError('You have already signed up')
      serializer.save(user.request.user)
  ```
* Other methods
  * GenericAPIView 사용해서 custom views 만들 때 오버라이딩 해야할 수 도있다.
  * get_serializer_context(self)
    * serializer에 공급될 추가적인 context를 포함한 dictionary를 반환한다.
    * default는 'request', 'view', 'format' keys를 포함한다.
  * get_serializer(self, instance=None, data=None, many=False, partial=False)
    * serializer instance를 반환한다.
  * get_paginated_response(self, data)
    * Response 객체의 paginated style을 반환한다.
  * paginate_queryset(self, queryset)
    * 필요하다면 queryset을 paginate한다.
    * pagination이 구성되지 않았으면 page object나 None을 반환한다.
  * filter_queryset(self, queryset)

## Mixins
* mixin 클래스들은 기본 view behavior를 제공하는 데 사용되는 action을 제공한다.
* ListModelMixin : list() - listing a queryset
* CreateModelMixin : create() - 새로운 모델 instance를 저장하고 생성한다.
* RetrieveModelMixin : retrieve() - 이미 있는 모델 instance 반환
* UpdateModelMixin
    * update() - 이미 있는 모델 instance update
    * partial_update() - PATCH, 부분 업데이트
* DestroyModelMixin : destroy() - 이미 있는 모델 instance 삭제

## Concrete View Classes
* CreateAPIView
* ListAPIView
* RetrieveAPIView
* DestroyAPIView
* UpdateAPIView
* ListCreateAPIView
* RetrieveUpdateAPIView
* RetrieveDestroyAPIView
* RetrieveUpdateDestroyAPIView

## Customizing the generic views
### Creating custom mixins
* URL conf에서 multiple fileds를 기반으로한 objects 조회가 필요하다면
```
class MultipleFieldLookupMixin(object):
    """
    Apply this mixin to any view or viewset to get multiple field filtering
    based on a `lookup_fields` attribute, instead of the default single field filtering.
    """

    def get_object(self):
        queryset = self.get_queryset()             # Get the base queryset
        queryset = self.filter_queryset(queryset)  # Apply any filter backends
        filter = {}
        for field in self.lookup_fields:
            if self.kwargs[field]: # Ignore empty fields.
                filter[field] = self.kwargs[field]
        obj = get_object_or_404(queryset, **filter)  # Lookup the object
        self.check_object_permissions(self.request, obj)
        return obj

class RetrieveUserView(MultipleFieldLookupMixin, generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_fields = ('account', 'username')
```

### Creating custom base classes
* 자신만의 base views 집합을 만들고 싶을 때,  
```
class BaseRetrieveView(MultipleFieldLookupMixin,
                       generics.RetrieveAPIView):
    pass

class BaseRetrieveUpdateDestroyView(MultipleFieldLookupMixin,
                                    generics.RetrieveUpdateDestroyAPIView):
    pass
```

## Third party packages
* 추가적인 generic view 제공
* Django REST Framework bulk
* Django Rest Multiple Modles
