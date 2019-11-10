## 클로저(closure)
* 클로저 - 자신이 정의된 스코프에 있는 변수를 참조하는 함수
* 파이썬에서 함수는 일급 객체다.
  * 일급 객체(first-class object) - 함수를 직접 참조, 변수에 할당, 다른 함수의 인수로 전달, 표현식과 if문 등에서 비교 가능
* 파이썬에서는 튜플을 비교할때 인덱스 0, 1, 2 순서로 비교한다.

```
numbers = [8, 3, 1, 2, 5, 4, 7, 6]
group = {2, 3, 5, 7}

def sort_priority(numbers, group):
    found = False
    def helper(x):
        if x in group:
            found = True
            return (0, x)
        return (1, x)
    number.sort(key=helper)
    return found

found = sort_priority(numbers, group)

>>>
found = False    # True로 예상했지만 False로 나옴
numbers = [2, 3, 5, 7, 1, 4, 6, 8]
```

---

### 스코프(scope) - 유효범위
* 표현식에서 변수를 참조할 때
  1. 현재 함수의 스코프
  2. 감싸고 있는 스코프(현재 스코프를 담고 있는 다른 함수 같은)
  3. 코드를 포함하고 있는 모듈의 스코프(전역 스코프)
  4. 내장 스코프(len이나 str같은 함수를 담고 있는)  
* 해당사항 없으면 NameError 발생


* 변수에 값을 할당할 때
  * 변수가 이미 현재 스코프에 정의되어 있다면 새로운 값을 얻는다(할당).
  * 변수가 현재 스코프에 존재하지 않으면 변수 정의로 취급한다.
  * 새로 정의되는 변수의 스코프는 그 할당을 포함하고 있는 함수가 된다.


* 파이썬 3에는 클로저에서 데이터를 얻어오는 nonlocal문이 있다.
* nonlocal문 특정 변수 이름에 할당할 때 -> 스코프 탐색이 일어나야 함을 나타낸다.
* 모듈 수준 스코프까지는 탐색할 수 없다.(전역 변수의 오염을 피하려고)

```
def sort_priority(numbers, group):
    found = False
    def helper(x):
        nonlocal found    
        if x in group:
            found = True
            return (0, x)
        return (1, x)
    numbers.sort(key=helper)
    return found

>>>
found = True
```
