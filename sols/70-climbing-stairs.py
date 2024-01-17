class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        count=0
        current_stair=0
        known={}
        known[n]=1
        known[n-1]=1
        def start(n,current_stair):
            count=0
            if current_stair in known:
                #print("Skip calculating from {}".format(current_stair))
                return known[current_stair]
            else:
                #print("adding {}".format(current_stair))
                known[current_stair] = start(n,current_stair+1) + start(n,current_stair+2)
                return known[current_stair] 
        #print(known)
        #print(start(n,current_stair))
        return start(n,current_stair)