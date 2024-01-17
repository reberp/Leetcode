class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        path_res=[] #{index of path: [path values]} the return value
        def dfs (this_path,candidates,target):
            # calculate next row down
            #print("---------")
            #print(candidates)
            next_set=[]
            temp=[]
            for i,c in enumerate(candidates):
                #print("--")
                next_path = [*this_path,c]
                #print("Next path {}".format(next_path))
                #print("{}".format(c))
                if (target-c)==0:
                    #print("Found answer: {}".format(next_path))
                    path_res.append(next_path)
                elif (target-c)<0:
                    pass
                else:
                    #print("Calling DFS: {},{},{}".format(next_path,candidates[i:],target-c))
                    dfs(next_path,candidates[i:],target-c)
            return path_res

        
        return dfs([],candidates,target)
        #print(dfs([],candidates,target))        