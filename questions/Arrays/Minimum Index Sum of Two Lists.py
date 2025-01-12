def brute(list1, list2):
    mini = float('inf')
    res = []

    for i in range(len(list1)):
        for j in range(len(list2)):
            if list1[i] == list2[j]:
                summ = i + j
                if summ < mini:
                    res = [list1[i]]
                    mini = summ
                elif summ == mini:
                    res.append(list1[i])
    return res

def optimal(list1, list2):


print(brute(["Shogun","Tapioca Express","Burger King","KFC"], ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]))