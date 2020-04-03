class Solution:
    def isHappy(self, n: int) -> bool:
        
        list_sum=[]
        while True:
            sum_n = 0
            for char in str(n): 
                sum_n +=int(char) ** 2 
 
            if sum_n in list_sum:
                return False
            else:
                list_sum.append(sum_n)
            
            if sum_n == 1:
                return True 
            n=sum_n