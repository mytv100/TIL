# Model
* 웹 어플리케이션의 데이터를 구조화하고 조작하기 위해 Django가 제공하는 추상적인 계층
* 일반적으로, 각 모델은 하나의 데이터베이스 테이블에 매핑된다.
---
* 각 모델 쿨래스는 django.db.models.Model의 서브 클래스이다
* Django는 automatically-generated database-access API를 제공한다.
---
* database의 table 이름은 app_model의 형태로 생성된다. 오버라이딩 가능
* `id` 필드(<strong>PK</strong>)는 자동으로 생성된다. 오버라이딩 가능

* model 클래스를 사용하기 위해서는 설정 파일(settings.py)의 INSTALLED_APPS 안에 app 이름을 적어줘야한다. -> 이어서 migrate 명령어룰 사용해줘야 한다.
---
## Fields
* 모델 클래스의 각 속성은 데이터베이스 필드를 의미한다.
* 필요하다면, 커스텀 필드를 만들 수 있다.

### Field types
* 각 필드는 적절한 Field 클래스의 인스턴스여야 한다.
* Field의 타입은 데이터베이스에게 어떤 종류의 데이터가 저장될 것인지를 알려준다.

### Field options
* 각 필드는 특정한 인자(argument)를 갖는다.
  * (ex) CharField -> max_length
  * null = True or False
  * blank = True -> form에서 빈 값 입력받을 수 있음.
  * choices를 인자로 가지면 default form은 select box다.
    * keyword : choice, get_FOO_display in https://docs.djangoproject.com/en/2.2/topics/db/models/

### Verbose field name
* 필드에 대해 사람이 일기 좋게 붙이는 이름
* 지정해주지 않는다면, Django field명에서 _ 를 공백으로 변경해서 자동적으로 생성해준다.

### Relationships
* Many-to-one relationships
  * django.db.models.ForeignKey을 사용한다.
  * ForeignKey 필드의 이름은 관계 모델의 이름을 소문자로 쓰는 것을 추천(장려)한다. 필수 아님


* Many-to-Many relationships
  * ManyToManyField의 이름은 관계 모델의 이름을 소문자로 쓰는 것을 추천(장려)한다. 필수 아님.
  * 추가적인 필드가 필요할 경우, many-to-many 관계를 관리(연결)할 수 있는 모델을 생성하여 포함시킨다.
  * 또한 ManyToManyField의 through 인자를 사용하여 중간 모델(두 모델을 연결하는)을 나타낸다.
  * 예시

  ```
  class Person(models.Model):
      name = models.CharField(max_length=128)

      def __str__(self):
          return self.name

  class Group(models.Model):
      name = models.CharField(max_length=128)
      members = models.ManyToManyField(Person, through='Membership')

      def __str__(self):
          return self.name

  class Membership(models.Model):
      person = models.ForeignKey(Person, on_delete=models.CASCADE)
      group = models.ForeignKey(Group, on_delete=models.CASCADE)
      date_joined = models.DateField()
      invite_reason = models.CharField(max_length=64)
  ```

  * intermediate_model.other_model.remove(name3) -> intermediate_model에서 모든 name3이라는 이름을 가진 other_model을 제거함
  * intermediate_model.other_model.clear() -> intermediate_model와 관계된 모든 other_model을 제거함

  ```
  # Find all the groups with a member whose name starts with 'Paul'
  >>> Group.objects.filter(members__name__startswith='Paul')
  <QuerySet [<Group: The Beatles>]>

  # Find all the members of the Beatles that joined after 1 Jan 1961
  >>> Person.objects.filter(
  ...     group__name='The Beatles',
  ...     membership__date_joined__gt=date(1961,1,1))
  <QuerySet [<Person: Ringo Starr]>
  ```

* One-to-one relationships
  * OneToOneField를 사용한다.

### Field name restrictions
* field 이름으로 Python reserved word 사용 불가능
* 연속해서 '_'(underscore) 사용 불가능 -> Django의 쿼리 조회 문법이 작동하는 방식이라서
* 이름의 끝에 '_'(underscore) 사용 불가능 -> Django의 쿼리 조회 문법이 작동하는 방식이라서


## Meta
* inner 클래스로 Meta를 사용해서 모델에 metadata를 줄 수 있다.
* Meta 클래스와 metadata는 선택사항이다.
* metadata의 종류
  * ordering : 정렬
  * db_table : 데이터베이스 테이블 이름
  * verbose_name, verbose_name_plural : 사람이 읽기 좋은 단수, 복수 이름


## Model attributes
* 가장 중요한 attribute는 `Manager` 이다.
* custom `Manager`가 없다면, 기본 이름은 objects 이다.
* Manager는 모델 클래스로만 접근 가능하다.(모델 인스턴스로 접근 불가능)

## Model methods
* 거의 오버라이딩하는 메소드들
  * __str__() : 객체의 문자열 표현을 반환해주는 메소드
  * 
