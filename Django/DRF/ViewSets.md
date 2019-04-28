# ViewSets
* 한 클래스에 관계된 view들의 집합과 logic을 결합한 것
* 다른 framework의 Resources나 Controllers와 비슷하다.
* get()이나 post()와 같은 메소드 핸들러 제공 X, 대신 list()와 create()같은 action 제공하는 CBV
* 메소드 핸들러는 .as_view() method 사용할 때 해당하는 action과 bound된다.
* URL conf에서 router에 ViewSet을 등록하면, 자동적으로 url이 생성된다.
* View class보다 ViewSet클래스를 사용함에 있어서 이점
  * 반복되는 로직을 한 클래스안에 결합시켜놓을 수 있다.
  * router를 사용해서 URL conf의 wiring up(url과 view를 연동시키는 작업)을 직접 다루지 않아도 된다.

## ViewSet actions
* REST Framewokr에 포함된 default router는 create/retrieve/update/destroy의 표준 집합에 대한 경로를 제공한다.

## Inspecting ViewSet actions
* basename : 생성되는 URL name들의 base로 사용됨
* action : 현재 action의 이름(list, create)
* detail : 현재 action이 list인지 detail인지에 대한 지시자, boolean
* suffix : viewset 타입에 대한 display 접미사 - detail attribute를 미러링한다. --> ? 잘모르겠음 써봐야 할 듯
* name : viewset을 위한 display 이름, suffix와 상호 배타적(동시에 적용되지 않는다?)임
* description : viewset의 개별 view에 대한 display 설명

## Marking extra actions for routing
* @action decorator를 사용해서 추가적인 action들에 대해 marking 해준다.
* detail 인자를 True -> single object, False -> entire collection
* router는 URL patterns을 detail 인자에 따라 구성한다. e.g., DefaultRouter는 URL patterns에 detail action들을 pk를 포함해서 구성한다.
```
@action(detail=True, methods=['post','delete'], permission_classes=[IsAdminOrIsSelf])
```

## Routing additional HTTP methods for extra actions
* 추가적인 mapping은 인자를 사용하지 않는다.
```
@action(detail=True, methods=['put'], name='Change Password')
def password(self, request, pk=None):
    """Update the user's password."""
    ...

@password.mapping.delete
def delete_password(self, request, pk=None):
    """Delete the user's password."""
    ...
```

## Reversing action URLs
* .reverse_action() - action으로부터 URL을 구한다.
* basename은 ViewSet을 등록하는 동안 router에 의해서 제공된다.
* 따라서, router를 사용하지 않으면 .as_view() method에 basename을 argument로 줘야한다.


# API Reference
* ViewSet
  * APIView 상속 -> permission_classes, authentication_classes와 같은 표준 attributes 사용 가능
  * actions의 구현을 제공하지 않음
* GenericViewSet
  * GenericAPIView 상속 -> get_object, get_queryset methods 와 다른 generic view base behavior의 default 집합 제공
  * mixin 클래스가 필요하거나 action의 구현을 명시적으로 정의해야 한다.
* ModelViewSet
  * GenericAPIView 상속하고 다양한 mixin class 사용
  * 제공되는 action - list(), retrieve(), create(), update(), partial_update(), destroy()
  * 최소한 queryset과 serializer_class attributes 설정해줘야 한다.
  * queryset을 제거하고 get_queryset()을 설정해주면 router에서 model의 basename을 인식하지 못하므로 basename을 kwarg로 명시해줘야 한다.
* ReadOnlyModelViewSet
  * GenericAPIView 상속
  * ModelViewSet과 마찬가지로 여러가지 다양한 action의 구현을 포함하나, read-only action들만 제공함, list(), retrieve()

# Custom ViewSet base classes
* ModelViewSet의 모든 action을 사용할 필요가 없을 때나 다른 방법으로 커스터마이징 하고싶을 때 사용
```
class CreateListRetrieveViewSet(mixins.CreateModelMixin,
                                mixins.ListModelMixin,
                                mixins.RetrieveModelMixin,
                                viewsets.GenericViewSet):
    """
    A viewset that provides `retrieve`, `create`, and `list` actions.

    viewsets.GenericViewSet
    To use it, override the class and set the `.queryset` and
    `.serializer_class` attributes.
    """
    pass
```
 
