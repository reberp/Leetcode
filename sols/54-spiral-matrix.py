class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        out=[]
        x=0
        amt=(len(matrix)*len(matrix[0]))
        while x<amt:        
            for x in matrix[0]:
                known.add(x)
                out.append(x)
            matrix=matrix[1:] #remove what I just ran through
            matrix=list(zip(*matrix))[::-1] #basically a left rotate. WIthout the ::-1 is a diagonal mirror
            x=len(out)
        return out