inner class `Meta` has variables `model` and `fields`            

`model` : 직렬화할 모델 클래스   
  `fields` : 포함할 필드 ["movie",] ,  `__all__`는 전체 필드 포함

  `read_only_fields` ['movie',] movie 는 읽기만 가능

  `exclude` ('movie',)  movie 만 제외, `__all__` 이랑 같이 쓸 수 없음
