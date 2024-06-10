class TimeMap:

    def __init__(self):
        self.arr = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.arr[key].append([timestamp, value])
        

    def get(self, key: str, timestamp: int) -> str:
        tmp = self.arr[key]
        ind = bisect_right(tmp, [timestamp+1,])-1
        if ind==len(tmp) or ind<0:
            return ""
        return tmp[ind][1]
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)