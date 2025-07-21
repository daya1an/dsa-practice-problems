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

#3. https://www.geeksforgeeks.org/dsa/find-a-triplet-that-sum-to-a-given-value/

arr = [1, 4, 45, 6, 10, 8]
t = 13
n = len(arr)
cnt = 0
arr.sort() # [1,4,6,8,10,45]

for i in range(n-2):
    l = i+1
    r = n-1
    reqSum = t - arr[i]
    while l < r:
        if arr[l] + arr[r] == reqSum:
            print("True")
        if arr[l] + arr[r] < reqSum:
            l = l+1
        else:
            r = r-1
            
# Output: True

# https://www.geeksforgeeks.org/dsa/find-the-longest-substring-with-k-unique-characters-in-a-given-string/

# sample input:output
# mlg ; 1 : 1
# aaaa ; 2 : -1

s = "aabacbebebe" 
k = 3
hs = set()
cnt = -1

for i in range(len(s)):
    hs.clear()
    for j in range(i,len(s)):
        hs.add(s[j])
        if len(hs) == k:
            cnt = max(cnt, j-i+1)
        
        if len(hs) > k:
            break
print("Output: ",cnt)
