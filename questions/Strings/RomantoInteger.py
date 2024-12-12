def romanToInt(s):
    h = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    sum = 0
    for i in len(s):
        if s[i] == 'I' and s[i+1] =='V':
            sum += 4
        sum += h[i]  
        print(h[i])      
    return sum

print(romanToInt("MCMXCIV"))