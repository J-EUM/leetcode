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

        answer = 0
        for i in range(min(max(citations)+1, len(citations)+1)):
            cnt = sum(1 for x in citations if x >= i)
            if i <= cnt:
                answer = i
            else:
                break
        return answer
