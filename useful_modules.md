<span style='font-family: Consolas'>

# Collections
## 딕셔너리 관련 객체
### defaultdict
&nbsp;존재하지 않는 키에 접근할 때, 디폴트 값을 기준으로 키를 생성한다.

  ```python
  >>> from collections import defaultdict
  >>> 
  >>> words = ['eat', 'tea', 'tan', 'ate']
  >>> anagrams = defaultdict(list)
  >>> for word in words:
  ...     tmp = ''.join(sorted(word))
  ...     anagrams[tmp].append(word)
  ... 
  >>> print(*anagrams.values())
  ['eat', 'tea', 'ate'] ['tan']
  ```

### Counter
&nbsp;아이템의 개수를 딕셔너리로 리턴한다.
   ```python
   >>> a = [1, 2, 3, 4, 5, 5, 5, 6, 6]
   >>> b = collections.Counter(a)
   >>> b
   Counter({5: 3, 6: 2, 1: 1, 2: 1, 3: 1, 4: 1})
   ```