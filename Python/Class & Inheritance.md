# 클래스와 상속
----
#### 딕셔너리와 튜플보다는 헬퍼 클래스로 관리
* 내장 딕셔너리와 튜플 타입을 쓰면 내부 관리용으로 층층이 타입을 추가하는 게 쉽다.
* 하지만, 계층이 한 단계가 넘는 중첩은 피해야 한다.(딕셔너리를 담은 딕셔너리)


* (ex) 각 시험 별 비중을 다르게 해서 최종 성적을 구하는 클래스와 메서드

```
class WeightedGradebook(object):
    def report_grade(self, name, subject, score, weight):
        by_subject = self._grades[name]
        grade_list = by_subject.setdefault(subject, [])
        grade_list.append((score, weight))

    def average_grade(self, name):
        by_subject = self._grades[name]
        score_sum, score_count = 0, 0
        for subject, scores in by_subject.items():
            subject_avg, total_weight = 0, 0
            for score, weight in scores:
                score_sum = score_sum + score * weight
                score_count = score_count + 1
        return score_sum / score_count
```

* 클래스 리펙토링
    * 성적은 변하지 않으므로 튜플을 사용 (score, weight)
    * 일반 튜플은 위치에 의존 -> namedtuple 타입 사용 -> 작은 불변 데이터 클래스(immutable data class)를 쉽게 정의
    * namedtuple의 제약
        * namedtuple로 만들 클래스에 기본 인수 값을 설정할 수 없다. -> 데이터에 선택적인 속성이 많으면 다루기 힘들다.
        * namedtuple 인스턴스의 속성 값을 여전히 숫자로 된 인덱스와 순회 방법으로 접근할 수 있다. -> 외부 API로 노출한 경우 의도와 다르게 사용될 수 있다.
```
import collections

# namedtuple 성적
Grade = collections.namedtuple('Grade', ('score', 'weight'))

# 성적들을 담은 단일 과목 클래스
class Subject(object):
    def __init__(self):
        self._grades = []

    def report_grade(self, score, weight):
        self._grades.append(Grade(score, weight))

    def average_grade(self):
        total, total_weight = 0, 0
        for grade in self._grades:
            total += grade.score * grade.weight
            total_weight += grade.weight
        return total / total_weight

# 한 학생이 공부한 과목들을 표현하는 클래스
class Student(object):
    def __init__(self):
        self._subjects = {}

    def subject(self, name):
        if name not in self._subjects:
            self._subjects[name] = Subject()
        return self._subjects[name]

    def average_grade(self):
        total, count = 0, 0
        for subject in self._subjects.values():
            total += subject.average_grade()
            count += 1
        return total / count

# 학생의 이름을 키로 사용해 동적으로 모든 학생을 담는 컨테이너
class Gradebook(object):
    def __init__(self):
        self._students = {}

    def student(self, name):
        if name not in self._students:
            self._students[name] = Student()
        return self._students[name]


book = Gradebook()
albert = book.student('Albert Einstein')
math = albert.subject('Math')
math.report_grade(80, 0.10)
# ...
print(albert.average_grade())

>>>
81.5
```

#### 인터페이스가 간단하다면 클래스 대신 함수를 받자
* 후크(hook) : 함수를 넘겨서 동작을 사용자화하는 기능
    * 파이썬이 후크로 동작하는 이유 : 일급 함수
* defaultdict 클래스 : 찾을 수 없는 키에 접근할 때마다 호출될 함수를 받음.
* 기본값 후크를 defaultdict에 넘겨서 찾을 수 없는 키의 총 개수를 세는 방법
    1. 상태 보존 클로저

```
current = {'green' : 12, 'blue' : 3}
increments = [
    ('red', 5),
    ('blue', 17),
    ('orange', 9),
]

# 상태 보존 클로저를 기본값 후크로 사용하는 헬퍼 함수
def increment_with_report(current, increments):
    added_count = 0

    def missing():
        nonlocal added_count # 상태 보존 클로저
        added_count += 1
        return 0

    result = defaultdict(missing, current)
    for key, amount in increments:
        result[key] += amount

    return result, added_count

result, count = increment_with_report(current, increments)
assert count == 2
```

    2. 보존할 상태를 클래스화하는 작은 클래스를 정의

asd
    sd
