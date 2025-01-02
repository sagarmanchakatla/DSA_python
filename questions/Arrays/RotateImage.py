from questions.Basics.sample import reverse

image = [[1, 2, 3],
         [4, 0, 6],
         [7, 8, 9]]

def brute():
    n = len(image)
    rotate = [[0 for i in range(n)] for i in range(n)]

    for i in range(n):
        for j in range(n):
            rotate[j][n-i-1] = image[i][j]

    print(rotate)


# brute()

def optimal():
    n = len(image)

    # transpose the image
    for i in range(n):
        for j in range(i+1, n):
            image[i][j], image[j][i] = image[j][i], image[i][j]

    # reverse the image
    for i in range(n):
        image[i].reverse()

optimal()
for i in image:
    print(i, end='\n')