# 1. https://www.geeksforgeeks.org/dsa/two-pointers-technique/

arr =[10, 20, 35, 50]
n = len(arr)
t = 70
for i in range(n):
    for j in range (i+1, n):
        if (arr[i] + arr[j] == 70):
            print(arr[i], arr[j])
            break

# Output: 20 50

#2. https://www.geeksforgeeks.org/dsa/count-pairs-difference-equal-k/
arr = [1, 4, 1, 4, 5]
k = 3
c = 0
n = len(arr)
for i in range(n):
    for j in range (i+1, n):
    #     if (arr[i] - arr[j] == k or arr[j] - arr[i] == k):
    #         c+=1
        if (abs(arr[i] - arr[j]) == k):
            c+=1
print(c)
# Output: 4


#3. https://www.geeksforgeeks.org/find-triplet-sum-two-equals-third-element/
arr = [1, 2, 3, 4, 5]
n = len(arr)
found = False
# print(f"Array: {arr}")
for i in range(n):
    for j in range(i + 1, n):
        # print(f"Checking if {arr[i]} + {arr[i + 1]} == {arr[j]}")
        if (arr[i] + arr[i + 1] == arr[j]):
            found = True
            # print(f"{arr[i]} + {arr[i + 1]} == {arr[j]}")
    if found:
        break

# Output: True
