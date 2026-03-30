class MyHashMap:

    # def __init__(self):
    #     self.buckets = [-1] * 1_000_001

    # def put(self, key: int, value: int) -> None:
    #     self.buckets[key] = value

    # def get(self, key: int) -> int:
    #     return self.buckets[key]

    # def remove(self, key: int) -> None:
    #     self.buckets[key] = -1

    def __init__(self):
        self.size = 10_000
        self.buckets = [[] for _ in range(self.size)]

    def put(self, key: int, value: int) -> None:
        hash_value = key % self.size
        for pair in self.buckets[hash_value]:
            if pair[0] == key:
                pair[1] = value
                return    
        self.buckets[hash_value].append([key, value])
        

    def get(self, key: int) -> int:
        hash_value = key % self.size
        for pair in self.buckets[hash_value]:
            if pair[0] == key:
                return pair[1]
        return -1

    def remove(self, key: int) -> None:
        hash_value = key % self.size

        for pair in self.buckets[hash_value]:
            if pair[0] == key:
                self.buckets[hash_value].remove(pair)

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)