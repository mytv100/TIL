## 예외 처리 과정

* try/except/else/finally
* ex) 파일에서 수행할 작업 설명을 읽고 처리한 후 즉석에서 파일을 업데이트
  * try 블록 - 파일을 읽고 처리
  * except 블록 - try 블록에서 일어난 예외 처리
  * else 블록 - 파일을 즉석에서 업데이트하고 이와 관련된 예외 전달
  * finally 블록 - 파일 핸들을 정리
  
```
UNDEFINED = object()

def divide_json(path):
    handle = open(path, 'r+')    # IOError
    try:
        data = handle.read()     # UnicodeDecodeerror
        op = json.loads(data)    # ValueError
        value = (
            op['numerator']/
            op['denominator'])   # ZeroDivisionError
    except ZeroDivisionError as e:
        return UNDEFINED
    else:
        op['result'] = value
        result = json.dumps(op)
        handle.seek(0)
        handle.write(result)    # IOError
        return value
    finally:
        handle.close()          # 항상 실행
```
