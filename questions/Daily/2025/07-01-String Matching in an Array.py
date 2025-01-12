def brute(words):
    res = []
    for i in words:
        for j in words:
            if i != j and i in j:
                res.append(i)
                break
    return res

