#User function Template for python3

class Solution:
    def gcd(self,a,b):
        while b:
            a,b = b, (a%b)
        return a
        
    def lcmAndGcd(self, a , b):
        lcm = abs(a*b) // self.gcd(a,b)
        gCd = self.gcd(a,b)
        
        return lcm,gCd


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        A, B = map(int, input().split())

        ob = Solution()
        ptr = ob.lcmAndGcd(A, B)

        print(ptr[0], ptr[1])
        print("~")

# } Driver Code Ends