## enumerate

* 내장 함수 range는 정수 집합을 순회하는 루프를 실행할 때 유용
* 문자열 리스트 같은 순회할 자료 구조가 있을 때 직접 루프 실행 가능

* 리스트를 순회하거나 리스트의 현재 아이템의 인덱스를 알고 싶은 경우

```
for i in range(len(flavor_lsit)):
  flavor = flavor_lsit[i]
  print('%d: %s' % (i + 1, flavor))

for i, flavor in enumerate(flavor_lsit):
# 두 번째 파라미터로 세기 시작할 숫자 지정 가능(default = 0)
  print('%d: %s' % (i + 1, flavor))
```

## zip
* 이터레이터를 병렬 처리할 때 사용
* 소스 리스트와 파생 리스트 병렬 처리시, 소스 리스트의 길이만큼 순회

```
names = ['Cecilia', 'Lise', 'Marie']
letters = [len(n) for n in names]

longest_name = None
max_letters = 0

# range
for i in range(len(names)):
  count = letters[i]
  if count > max_letters:
    longest_name = names[i]
    max_letters = count

# enumerate
for i, name in enumerate(names):
  count = letters[i]
  if count > max_letters:
    longest_name = names
    max_letters = count

# zip
for name, count in zip(names, lettes):
  if count > max_letters:
    longest_name = names
    max_letters = count

```

* 문제점
1. 파이썬 2에서 제공하는 zip이 제너레이터가 아니다.
  * 이터레이터를 완전히 순회해서 zip으로 생성한 모든 튜플을 반환한다
  * -> 메모리를 많이 사용한다

2. 입력 이터레이터들의 길이가 다르면 zip이 이상하게 동작한다.
  * 결과를 조용히 잘라낸다. -> 경고 없음
