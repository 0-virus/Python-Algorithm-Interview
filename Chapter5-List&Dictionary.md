리스트, 딕셔너리 (5장)
====================

## 리스트

### 리스트 주요 연산의 시간 복잡도

|연산|시간 복잡도|설명|
|:---|:---|:---|
|<span style="font-family:Consolas;">len(lst)</span>|$O(1)$||
|<span style="font-family:Consolas;">lst[i]</span>|$O(1)$||
|<span style="font-family:Consolas;">lst[i:j]</span>|$O(k)$|$k=j-i$||
|<span style="font-family:Consolas;">elem in lst</span>|$O(n)$||
|<span style="font-family:Consolas;">lst.count(elem)</span>|$O(n)$||
|<span style="font-family:Consolas;">lst.index(elem)</span>|$O(n)$||
|<span style="font-family:Consolas;">lst.append(elem)</span>|$O(1)$||
|<span style="font-family:Consolas;">lst.pop()</span>|$O(1)|리스트의 마지막 요소를 추출하여 리턴한다.|
|<span style="font-family:Consolas;">lst.pop(i)</span>|$O(n)|리스트의 $i$ 번째 요소를 추출하여 리턴한다. 데크(deque)를 이용하면 $O(n)$에 수행 가능하다.|
|<span style="font-family:Consolas;">del lst[i]</span>|$O(n)$|$i$ 의 값에 따라 달라지며, 최악의 경우 $O(n)$이다.|
|<span style="font-family:Consolas;">lst.sort()</span>|$O(n\log n)$|Timsort를 사용하며, 최선의 경우 $O(n)$에도 실행된다.|
|<span style="font-family:Consolas;">min(lst), max(lst)</span>|$O(n)|
|<span style="font-family:Consolas;">lst.reverse()</span>|$O(n)||

## 딕셔너리
### 딕셔너리의 주요 연산 시간 복잡도

|연산|시간 복잡도|설명|
|---|---|---|
|<span style="font-family:Consolas;">len(dic)</span>|$O(1)$||
|<span style="font-family:Consolas;">dic[key]</span>|$O(1)$||
|<span style="font-family:Consolas;">dic[key] = value</span>|$O(1)$|키, 값 삽입|
|<span style="font-family:Consolas;">key in dic</span>|$O(1)$||

### 딕셔너리 모듈
1. **defaultdict 객체**
   
   존재하지 않는 키를 조회하면 디폴트 값을 기준으로 아이템을 생성한다.
   ```python
   >>> a = collections.defaultdict(int)
   >>> a['A'] = 5
   >>> a['B'] = 4
   >>> a['C'] += 1 # 존재하지 않는 키이므로 디폴트 값인 0으로 value를 설정함
   >>> a
   defaultdict(<calss 'int'>, {'A': 5, 'B': 4, 'C': 1})
   ```

2. **Counter 객체**
   
   아이템의 개수를 딕셔너리로 리턴한다.
   ```python
   >>> a = [1, 2, 3, 4, 5, 5, 5, 6, 6]
   >>> b = collections.Counter(a)
   >>> b
   Counter({5: 3, 6: 2, 1: 1, 2: 1, 3: 1, 4: 1})
   ```