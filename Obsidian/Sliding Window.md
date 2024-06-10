https://leetcode.com/problems/frequency-of-the-most-frequent-element/description/

```python
# so agar mai sort kar dun to let say sabhi chote in a window ko bade in window 
# mai convert karna hoga and it should not exceed k

nums.sort()
l = ans = 0
tot = 0
for r in range(len(nums)):
	tot+=nums[r]
	while (nums[r]*(r-l+1)-tot)>k:
		tot-=nums[l]
		l+=1
	ans = max(ans,(r-l+1))
	
return ans
```

https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/description/

```python
l = ans = 0
tot = 0
for r in range(len(nums)):
	tot+=nums[r]
	while ((r-l+1)-tot)>1:
		tot-=nums[l]
		l+=1
	ans = max(ans,(r-l)) # why r-l and not r-l+1 because we need to remove 1 elemen

return ans
```

https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

```python
l = ans = 0
d = defaultdict(int)
for r in range(len(nums)):
	d[nums[r]]+=1
	while d[nums[r]]>1:
		d[nums[l]]-=1
		l+=1
	ans = max(ans,(r-l+1))
return ans
	
```

https://leetcode.com/problems/subarray-product-less-than-k/description/

```python
l = ans = 0
tot = 1
for r in range(len(nums)):
	tot *= nums[r]
	while l<=r and tot>=k:
		tot//=nums[l]
		l+=1
	ans += (r-l+1)
return ans

```

https://leetcode.com/problems/minimum-window-substring/

```python
d_t = Counter(t)
res = [-1,-1]
length = float('inf')
l = ans = 0
d_s = defaultdict(int)
tot = 0
for r in range(len(s)):
	d_s[s[r]]+=1
	if d_s[s[r]]==d_t[s[r]]:
		tot+=1
	while tot==len(d_t):
		if length>(r-l+1):
			length = r-l+1
			res = [l,r]
		d_s[s[l]]-=1
		if d_s[s[l]]<d_t[s[l]]:
			tot -= 1
		l+=1
l, r = res
return s[l:r+1] if l!=-1 else ""

```

https://leetcode.com/problems/minimum-size-subarray-sum/

```python
l = ans = 0
ans = float('inf')
tot = 0
for r in range(len(nums)):
	tot += nums[r]
	while l<=r and tot>=target:
		ans = min(ans,(r-l+1))
		tot-=nums[l]
		l+=1
return ans if ans!=float('inf') else 0
```

https://leetcode.com/problems/longest-repeating-character-replacement/description/

```python
l = ans = 0
d = defaultdict(int)
tot = 0
for r in range(len(nums)):
	d[nums[r]]+=1
	tot = max(tot,d[nums[r]])
	while (r-l+1)-tot>k:
		d[nums[l]]-=1
		l+=1
	ans = max(ans,r-l+1)
return ans
        
```

https://leetcode.com/problems/max-consecutive-ones-iii/description/

```python
l = ans = 0
tot = 0
for r in range(len(nums)):
	tot += nums[r]
	while (r-l+1)-tot>k:
		tot -= nums[l]
		l+=1
	ans = max(ans,r-l+1)
return ans
        
```

https://leetcode.com/problems/get-equal-substrings-within-budget/description/

```python
l = ans = 0
tot =0
for r in range(len(s)):
	tot += abs(ord(s[r])-ord(t[r]))
	while tot>maxCost:
		tot -= abs(ord(s[l])-ord(t[l]))
		l+=1
	ans = max(ans,(r-l+1))
return ans

```

https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/description/

```python
# think ulta bich mai i want a big subarray which has tot equals sum(nums)-x. Also
# sum(nums)<x we can't remove it so, we should handle it separately.
tot = sum(nums)
if tot<x:
	return -1
target = tot - x
l = ans = 0
tot = 0
flg = 1
for r in range(len(nums)):
	tot += nums[r]
	while tot>target:
		tot -= nums[l]
		l+=1
	if tot==target:
		flg = 0
		ans = max(ans,r-l+1)
if flg:
	return -1
return len(nums)-ans

```

https://leetcode.com/problems/maximum-erasure-value/description/

```python
l = ans = 0
d = defaultdict(int)
tot = 0
for r in range(len(nums)):
	d[nums[r]]+=1
	tot += nums[r]
	while d[nums[r]]>1:
		d[nums[l]]-=1
		tot -= nums[l]
		l+=1
	ans = max(ans, tot)
return ans

```

https://www.lintcode.com/problem/883/

```python
# consecutive ones if i flip only one 0
l = ans = 0
tot = 0
for r in range(len(nums)):
	tot += nums[r]
	while (r-l+1)-tot>1:
		tot -= nums[l]
		l+=1
	ans = max(ans,r-l+1)
return ans

```

```python
# consecutive subarray can be done on max subarray

@cache
def h(i=0, isFlipped=False):
	if i == len(nums):
		return 0
	if nums[i]:
		return 1 + h(i + 1, isFlipped)
	else:
		if not isFlipped:
			return 1 + h(i + 1, True)
		else:
			return 0

max_consecutive = 0
for start in range(len(nums)):
	max_consecutive = max(max_consecutive, h(start, False))

return max_consecutive

```

https://www.lintcode.com/problem/41/ 
maximum subarray
```python
@cache
def h(i=0):
	if i == len(nums):
		return -float('inf')
	return max(nums[i], nums[i] + h(i + 1))

max_consecutive = -float('inf')
for start in range(len(nums)):
	max_consecutive = max(max_consecutive, h(start))

return max_consecutive
```

https://www.lintcode.com/problem/928/
Longest Substring with At Most Two Distinct Characters
```python
l = ans = 0
d = defaultdict(int)
for r in range(len(s)):
	d[s[r]]+=1
	while len(d)>2:
		d[s[l]]-=1
		if d[s[l]]==0:
			del d[s[l]]
		l+=1
	ans = max(ans,r-l+1)
return ans

```

https://www.lintcode.com/problem/386
Longest Substring with At Most K Distinct Characters
```python
l = ans = 0
d = defaultdict(int)
for r in range(len(s)):
	d[s[r]]+=1
	while len(d)>k:
		d[s[l]]-=1
		if d[s[l]]==0:
			del d[s[l]]
		l+=1
	ans = max(ans,r-l+1)
return ans

```

https://leetcode.com/problems/sliding-window-maximum/description/
```python
q = deque()
res = []
for i,v in enumerate(nums):
    while len(q)>0 and nums[q[-1]]<v:
        q.pop()
    q.append(i)
    while len(q)>1 and q[-1]-q[0]+1>k:
        q.popleft()
    if i>=k-1:
        res.append(nums[q[0]])
return res

```

https://leetcode.com/problems/find-the-longest-semi-repetitive-substring/description/

```python
l = ans = 0
tot = 0

for r in range(1,len(s)):
	if s[r]==s[r-1]:
		tot += 1
	while tot>1:
		if s[l]==s[l+1]:
			tot-=1
		l+=1
	ans = max(ans,r-l+1)
return max(1,ans)
```

https://leetcode.com/problems/minimum-number-of-operations-to-make-array-continuous/
```python
N = len(nums)
nums = sorted(set(nums))
l = ans = 0
for r in range(len(nums)):
	while nums[r]-nums[l]>N-1:
		l+=1
	ans = max(ans,r-l+1)
return N-ans

```

https://leetcode.com/problems/binary-subarrays-with-sum/description/
```python
def h(goal):
	l = ans = 0
	tot = 0
	for r in range(len(nums)):
		tot += nums[r]
		while l<=r and tot>goal:
			tot-=nums[l]
			l+=1
		ans += (r-l+1)
	return ans

return h(goal) - h(goal-1)

```

https://leetcode.com/problems/subarrays-with-k-different-integers/description/
```python
def h(k):
	l = ans = 0
	d = defaultdict(int)
	for r in range(len(nums)):
		d[nums[r]]+=1
		while len(d)>k:
			d[nums[l]]-=1
			if d[nums[l]]==0:
				del d[nums[l]]
			l+=1
		ans += (r-l+1)
		
	return ans

return h(k)-h(k-1)

```

https://leetcode.com/problems/count-number-of-nice-subarrays/description/
```python
def h(k):
	l = ans = 0
	tot = 0
	for r in range(len(nums)):
		tot += (nums[r]&1)
		while tot>k:
			tot -= (nums[l]&1)
			l+=1
		ans += (r-l+1)
	return ans

return h(k)-h(k-1)

```

https://leetcode.com/problems/count-vowel-substrings-of-a-string/description/
```python
def h(goal):
	l = ans = 0
	d = defaultdict(int)
	for r in range(len(word)):
		if word[r] not in "aeiou":
			l = r+1
			d = defaultdict(int)
			continue
		d[word[r]]+=1
		while l<=r and len(d)>goal:
			d[word[l]]-=1
			if d[word[l]]==0:
				del d[word[l]]
			l+=1
		ans += r-l+1
	return ans


return h(5)-h(4)
```

https://leetcode.com/problems/find-all-anagrams-in-a-string/
```python
dp = Counter(p)
l = 0
d = defaultdict(int)
tot = 0
res = []
for r in range(len(s)):
	d[s[r]]+=1
	if d[s[r]]==dp[s[r]]:
		tot+=1
	while r-l+1>len(p):
		if d[s[l]]==dp[s[l]]:
			tot-=1
		d[s[l]]-=1
		if d[s[l]]==0:
			del d[s[l]]
		l+=1

	
	if tot==len(dp) and r-l+1==len(p):
		res.append(l)

return res
```

https://github.com/lzl124631x/LeetCode/tree/master/leetcode/1176
```python
if len(s)<k:
	return 0
l = ans = 0
tot = 0
for r in range(len(s)):
	tot += s[r]
	while r-l+1>k:
		tot -= s[l]
		l+=1
	if r-l+1==k:
		# print(l,r,tot)
		if tot<lower:
			ans -= 1
		elif tot>upper:
			ans += 1
return ans

```

https://github.com/lzl124631x/LeetCode/tree/master/leetcode/1100
```python
if len(s)<k:
	return 0
l = ans = 0
d = defaultdict(int)
tot = 0
for r in range(len(s)):
	d[s[r]]+=1
	if d[s[r]]==1:
		tot += 1
	while r-l+1>k:
		if d[s[l]]==1:
			tot-=1
		d[s[l]]-=1
		if d[s[l]]==0:
			del d[s[l]]
		l+=1
	if tot==k:
		ans+=1
return ans

```

https://leetcode.com/problems/permutation-in-string/description/
```python
l = ans = 0
dp = Counter(s1)
d = defaultdict(int)
tot = 0
for r in range(len(s2)):
	d[s2[r]]+=1
	if d[s2[r]] == dp[s2[r]]:
		tot+=1
	while r-l+1>len(s1):
		if d[s2[l]]==dp[s2[l]]:
			tot-=1
		d[s2[l]]-=1
		if d[s2[l]]==0:
			del d[s2[l]]

		l+=1
	if tot == len(dp):
		return True
return False

```

https://leetcode.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k/description/
```python
d = set()
for i in range(len(s)-k+1):
	d.add(s[i:i+k])
return len(d)==(2**k)
```