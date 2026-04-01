class MyHashMap:

    def __init__(self):
        # self.buckets = [[] for _ in range(1_000_001)]
        self.buckets = [-1] * 1000001
    def put(self, key: int, value: int) -> None:
        # if len(self.buckets[key]) > 0:
        #     self.buckets[key] = [value]
        # else:
        #     self.buckets[key].append(value)
        self.buckets[key] = value

    def get(self, key: int) -> int:
        # if len(self.buckets[key]) > 0:
        #     return self.buckets[key][0]
        # else:
        #     return -1
        return self.buckets[key]

    def remove(self, key: int) -> None:
        # self.buckets[key] = []
        self.buckets[key] = -1

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)