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

*
