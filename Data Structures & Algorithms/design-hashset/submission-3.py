class MyHashSet:

    # def __init__(self):
    #     self.size = 10_000
    #     self.buckets = [[] for _ in range(self.size)]

    # def add(self, key: int) -> None:
    #     hash_value = key % self.size

    #     if key not in self.buckets[hash_value]:
    #         self.buckets[hash_value].append(key)
        
    # def remove(self, key: int) -> None:
    #     hash_value = key % self.size

    #     if key in self.buckets[hash_value]:
    #         self.buckets[hash_value].remove(key)

    # def contains(self, key: int) -> bool:
    #     hash_value = key % self.size

    #     return key in self.buckets[hash_value]

    def __init__(self):
        self.buckets = [0] * 1_000_001

    def add(self, key: int) -> None:
        self.buckets[key] = True
        
    def remove(self, key: int) -> None:
        self.buckets[key] = False

    def contains(self, key: int) -> bool:
        return self.buckets[key] == True


        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)