# Exercise 8: Print the following pattern
# 1 
# 2 2 
# 3 3 3 
# 4 4 4 4 
# 5 5 5 5 5

k = 5
n= 1
while n <=k:
    for i in range(n):
        print(n, end=' ')

    print()
    n= n+1