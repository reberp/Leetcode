class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        matches = {
            "(":")",
            "[":"]",
            "{":"}",
        }
        if not s:
            #print("Empty")
            return False
        arr=[str(s[0])]
        #print(len(s))
        for x in range(1,len(s)):
            next_char=str(s[x])
            #print(next_char)
            if (len(s)-x)<len(arr):
                return False
            #if arr and ( ((ord(next_char)-1) == ord(arr[-1])) or ((ord(next_char)-2) == ord(arr[-1])) ):
            if arr and arr[-1] in matches and (matches[arr[-1]]==next_char):
                #print("match")
                arr.pop()
                #print("Len now: "+str(len(arr)))
            else:
                if next_char in [")","}","]"]:
                    return False
                arr.append(str(s[x]))
           # print(arr)
        if len(arr)>0:
            return False
        else:
            return True