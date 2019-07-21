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
