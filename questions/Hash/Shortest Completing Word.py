from collections import Counter

def brute(licensePlate, words):
    lh = Counter(c.lower() for c in licensePlate if c.isalpha())

    words.sort(key=len)

    for word in words:
        wordCount = Counter(word)
        for char, val in lh.items():
            if val >= wordCount[char]:
                return word


brute("1s3 PSt", ["step","steps","stripe","stepple"])