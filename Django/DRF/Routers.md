# Routers
* REST Framework는 Django를 위한 자동적인 URL routing 제공
* URLs의 집합에 view logic을 wiring하는 단순하고, 빠르고, 일관된 방법을 제공한다.
## Usage
```
router = routers.SimpleRouter()
router.register(r'users', UserViewSet)
router.register(r'accounts', AccountViewSet)
urlpatterns = router.urls
```
* register method에 반드시 필요한 인자
  * prefix : 경로들의 집합을 위해 사용하기 위한 URL prefix(접두사)
  * viewset : ViewSet 클래스
* 선택적으로 사용하는 인자
  * basename : URL name에 사용되는 base, 설정 안되어있으면 viewset의 queryset 속성으로부터 자동적으로 생성된다.
* URL patterns example
  * ^users/$ : 'user-list'
  * ^users/{pk}/$ : 'user-detail'
  * ^accounts/$ : 'account-list'
  * ^accounts/{pk}/$ : 'account-detail'
  * basename -> user or account 이 부분

### Using `include` with routers
```
# 기본
router = routers.SimpleRouter()
router.register(r'users', UserViewSet)
router.register(r'accounts', AccountViewSet)

urlpatterns = [
    url(r'^forgot-password/$', ForgotPasswordFormView.as_view()),
]

urlpatterns += router.urls

# 대안
urlpatterns = [
    url(r'^forgot-password/$', ForgotPasswordFormView.as_view()),
    url(r'^', include(router.urls)),
]

# namespace
urlpatterns = [
    url(r'^forgot-password/$', ForgotPasswordFormView.as_view()),
    url(r'^api/', include((router.urls, 'app_name'))),
]

# namespace + app_name
urlpatterns = [
    url(r'^forgot-password/$', ForgotPasswordFormView.as_view()),
    url(r'^api/', include((router.urls, 'app_name'), namespace='instance_name')),
]
```
* hyperlinked serializer와 함께 namespacing을 사용한다면 serializer에 `view_name` 매개변수를 올바르게 반영하는지 확인해야 한다.
* view_name = 'app_name:user-detail'와 같은 매개변수를 포함해야 한다.
* 자동 view_name 생성은 %(model_name)-detail과 같은 패턴을 사용한다.
* hyperlinked serializer를 사용할 때 모델명이 실제로 충돌하지 않는다면 DRF view의 namespace를 사용하지 않는 것이 좋다.

### Routing for extra actions
```
class UserViewSet(ModelViewSet):
    ...

    @action(methods=['post'], detail=True, permission_classes=[IsAdminOrIsSelf])
    def set_password(self, request, pk=None):
        ...
```
* URL pattern : ^users/{pk}/set_password/$
* URL name : 'user-set-password'
* default URL pattern은 method name을 바탕으로 한다.
* default URL name은 hyphenated(하이픈을 넣은) method와 ViewSet.name의 결합으로 구성된다.
* default 변경하려면 아래와 같이 url_path, url_name을 지정해주면 된다.
```
@action(methods=['post'], detail=True, permission_classes=[IsAdminOrIsSelf],
           url_path='change-password', url_name='change_password')
   def set_password(self, request, pk=None):

# URL path: ^users/{pk}/change-password/$
# URL name: 'user-change_password'
```
# API Guide
## SimpleRouter
* list, create, retrieve, update, partial_update, destroy action을 위한 경로 제공

|URL style|HTTP Method|Action|URL Name|
|---|---|---|---|
|{prefix}/|GET|list|{basename}-list|
|{prefix}/|POST|create|{basename}-list|
|{prefix}/{url_path}/|GET, or as specified by `methods` argument|`@action(detail=False)` decorated method|{basename}-{url_name}|
|{prefix}/{lookup}/|GET|retrieve|{basename}-detail|
|{prefix}/{lookup}/|PUT|update|{basename}-detail|
|{prefix}/{lookup}/|PATCH|partial_update|{basename}-detail|
|{prefix}/{lookup}/|DELETE|destroy|{basename}-detail|
|{prefix}/{lookup}/{url_path}/|GET, or as specified by `methods` argument|`@action(detail=True)` decorated method|{basename}-{url_name}|

```
# trailing_slash 옵션
router = SimpleRouter(trailing_slash=False)
```

```
# lookup pattern 설정
class MyModelViewSet(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    lookup_field = 'my_model_id'
    lookup_value_regex = '[0-9a-f]{32}'
```

## DefaultRouter

|URL style|HTTP Method|Action|URL Name|
|---|---|---|---|
|[.format]|GET|automatically generated root view|{api-root|
|{prefix}/[.format]|GET|list|{basename}-list|
|{prefix}/[.format]|POST|create|{basename}-list|
|{prefix}/{url_path}/[.format]|GET, or as specified by `methods` argument|`@action(detail=False)` decorated method|{basename}-{url_name}|
|{prefix}/{lookup}/[.format]|GET|retrieve|{basename}-detail|
|{prefix}/{lookup}/[.format]|PUT|update|{basename}-detail|
|{prefix}/{lookup}/[.format]|PATCH|partial_update|{basename}-detail|
|{prefix}/{lookup}/[.format]|DELETE|destroy|{basename}-detail|
|{prefix}/{lookup}/{url_path}/[.format]|GET, or as specified by `methods` argument|`@action(detail=True)` decorated method|{basename}-{url_name}|

* trailing_slash는 SimpleRouter와 동일하게 설정한다.

## Custom Routers
* 이미 존재하는 router classes 중 하나 상속
* .routes attribute는 각 viewset에 매핑될 URL 패턴들을 template하는데 사용된다.
* .routes attribute는 Route named tuples의 리스트이다.   
* The arguments to the Route named tuple
  * url : A string representing the URL to be routed
    * format strings
      * {prefix} - The URL prefix to use for this set of routes.
      * {lookup} - The lookup field used to match against a single instance.
      * {trailing_slash} - Either a '/' or an empty string, depending on the trailing_slash argument.
  * mapping: A mapping of HTTP method names to the view methods
  * name: The name of the URL as used in reverse calls.
    * format string
      * {basename} - The base to use for the URL names that are created.
  * initkwargs: view를 인스턴스화 할 때 전달되어야 하는 추가적인 인수 dictionary
    * detail, basename, suffix는 viewset introspection에서 예약되 있다(내부적으로 사용된다는 의미인 듯)
    * browsable API에서 view 이름과 탐색 경로 링크(breadcrumb link)를 생성하는데 사용된다.

## Customizing dynamic routes
* 어떻게 @action 데코레이터가 routed되는지 커스터마이징 할 수 있다.
* the arguments to DynamicRoute
  * url: A string representing the URL to be routed.
    * format strings : Route의 format strings + {url_path}
  * name: The name of the URL as used in reverse calls.
    * format strings
      * {basename} - The base to use for the URL names that are created.
      * {url_name} - The url_name provided to the @action.
  * initkwargs:  view를 인스턴스화 할 때 전달되어야 하는 추가적인 인수 dictionary

## Example
* list랑 retrieve action만 route
```
# router
class CustomReadOnlyRouter(SimpleRouter):
    """
    A router for read-only APIs, which doesn't use trailing slashes.
    """
    routes = [
        Route(
            url=r'^{prefix}$',
            mapping={'get': 'list'},
            name='{basename}-list',
            detail=False,
            initkwargs={'suffix': 'List'}
        ),
        Route(
            url=r'^{prefix}/{lookup}$',
            mapping={'get': 'retrieve'},
            name='{basename}-detail',
            detail=True,
            initkwargs={'suffix': 'Detail'}
        ),
        DynamicRoute(
            url=r'^{prefix}/{lookup}/{url_path}$',
            name='{basename}-{url_name}',
            detail=True,
            initkwargs={}
        )
    ]

# views.py
class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A viewset that provides the standard actions
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'username'

    @action(detail=True)
    def group_names(self, request, pk=None):
        """
        Returns a list of all the group names that the given
        user belongs to.
        """
        user = self.get_object()
        groups = user.groups.all()
        return Response([group.name for group in groups])    

# urls.py
router = CustomReadOnlyRouter()
router.register('users', UserViewSet)
urlpatterns = router.urls        
```

|URL|HTTP Method|Action|URL Name|
|---|---|---|---|
|/users]|GET|list|user-list|
|/users/{username}|GET|retrieve|user-detail|
|/users/{username}/group_names|GET|group_names|user-group-names|
* url_path = group_names, url_name = group-names
## Advanced custom routers
* 완전히 커스텀한 behavior를 제공하길 원하면, `BaseRouter`와 `get_urls(self)`method를 오버라이드 해야 한다.
* method는 등록된 viewsets과 URL patterns의 리스트를 확인해야 한다.
* self.registry attribute에 접근함으로써 등록된 prefix, viewset, basename tuple들이 확인된다.
* get_default_basename(self, viewset)도 있다.

# Third Party Packages
* DRF Nested Routers
* ModelRouter(wq.db.rest)
* DRF-extensions
