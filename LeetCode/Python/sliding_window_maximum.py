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