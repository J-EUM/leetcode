class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # [100] -> 1
        # 1 이상 인용된거 1개 1<=1
        # 2 이상 인용된거 1개 2>1
        # [0,0,2] -> 1
        # 0 이상        3개 0<=3
        # 1 이상 인용된거 1개 1<=1
        # 2 이상        1개  2>1
        # [3,0,6,1,5] -> 3
        # 1이상        
        # 3이상 인용된거 3개
        # [1,3,1] -> 1
        # 1이상 인용된거 3개
        # [4,4,4,4,4,4,5] -> 4
        # 4이상 인용된거 7개 
        # 5이상 1개 
        # 앞에숫자가 h_index
        # [0 0]
        # 0이상 2개 -> 0
        # [0 0 1]
        # 0이상 3개
        # 1이상 1개
        # 0,1중에 큰거 1 -> 1

        # [6,5,3,1,0] -> 3
        # 6이상 1개      
        # 5이상 2개
        # 3이상 3개
        # 1이상 4개
        # a <= b 면 a

        # [0,0,2] -> 1
        #  0 1 2
        #  3 2 1
        #  

        # i = 0 h([0,0,0,0,9,9) = 2 max_h = 6 | first member is 0, try again
        # i = 1 h([0,0,0,9,9) = 2 max_h = 5 | first member is 0, try again
        # i = 2 h([0,0,9,9) = 2 max_h = 4 | first member is 0, try again
        # i = 3 h([0,9,9) = 2 max_h = 3 | first member is 0, try again
        # i = 4 h([9,9) = 2 max_h = 2 | first member is 9

        citations.sort()
        n = len(citations)
        for i, v in enumerate(citations):
            if n - i <= v:
                return n - i
        return 0
