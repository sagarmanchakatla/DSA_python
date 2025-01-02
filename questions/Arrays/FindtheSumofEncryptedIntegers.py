def sumOfEncryptedInt(nums):
        def encrypt(x):
            n = len(str(x))
            lar = -1
            res = ''
            while x > 0:
                k = x % 10
                lar = max(lar, k)
                x = x // 10
            res += str(lar)*n
            print(int(res))
        encrypt(nums[0])

sumOfEncryptedInt([191,2,3,4,5])

