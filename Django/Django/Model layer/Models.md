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
  * ForeignKey 필드의 이름은 모델의 이름을 소문자로 쓰는 것을 추천(장려)한다. 필수 아님
* Many-to-Many relationships
* One-to-one relationships
