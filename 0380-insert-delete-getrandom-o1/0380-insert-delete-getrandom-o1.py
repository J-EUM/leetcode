# https://leetcode.com/problems/insert-delete-getrandom-o1/solutions/455253/python-super-efficient-detailed-explanation

class RandomizedSet:

    def __init__(self):
        self.data = []
        self.data_map = {}  # data의 요소:인덱스 저장
        
    # val이 set안에 없으면 insert, True리턴. 아니면False
    def insert(self, val: int) -> bool:
        if val in self.data_map:
            return False

        self.data_map[val] = len(self.data)
        self.data.append(val)
        return True
        
    # val이 존재하면 삭제, True리턴, 아니면 False
    def remove(self, val: int) -> bool:
        if val not in self.data_map:
            return False
        
        last_elem_in_list = self.data[-1]
        index_of_elem_to_remove = self.data_map[val]

        self.data_map[last_elem_in_list] = index_of_elem_to_remove
        self.data[index_of_elem_to_remove] = last_elem_in_list

        self.data.pop()
        self.data_map.pop(val)
        return True

    def getRandom(self) -> int:
        return random.choice(self.data)
        

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()