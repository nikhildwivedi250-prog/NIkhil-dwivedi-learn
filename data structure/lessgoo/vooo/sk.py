views = [45, 12, 89, 23]

n = len(views)

for i in range(n):
    for j in range(n-i-1):
        if views[j] > views[j+1]:
            views[j], views[j+1] = views[j+1], views[j]



print("sorted views ; ", views)