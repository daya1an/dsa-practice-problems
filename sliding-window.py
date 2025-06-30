#Sliding Window main loop formula: array_length - window_size + 1
#sub array = array[i:i+k]

#1
#https://www.geeksforgeeks.org/first-negative-integer-every-window-size-k

arr = [12, -1, -7, 8, -15, 30, 16, 28]
n = len(arr)
k = 3
result = []

for i in range(n-k+1):
     for j in range (i, i+k):
          if(arr[j] < 0):
               result.append(arr[j])
               break
          if(arr[j] > 0 and j == i+k-1):
               result.append(0)
               break

print("Final Result = ", result)
# output = [-1, -1, -7, -15, -15, 0]

#2
# https://www.geeksforgeeks.org/sum-of-all-subarrays-of-size-k

arr = [1, 2, 3, 4, 5, 6]
n = len(arr)
result = []
k = 3

for i in range(n-k+1):
     result.append(sum(arr[i:i+k]))

print("Final Result = ", result)
# op: 6 9 12 15 

#3
#https://www.geeksforgeeks.org/maximum-mex-from-all-subarrays-of-length-k

arr = [6, 1, 3, 2, 4]
n = len(arr)
k = 3
result = []
for i in range(n-k+1):
     print(arr[:i] + arr[i+k:])
     result.append(min(arr[:i] + arr[i+k:]))

print("Final Result = ",max(result))


#4
#https://www.geeksforgeeks.org/maximum-mex-from-all-subarrays-of-length-k

arr = [6, 1, 3, 2, 4]
n = len(arr)
k = 3
result = []
for i in range(n-k+1):
     print(arr[:i] + arr[i+k:])
     result.append(min(arr[:i] + arr[i+k:]))

print("Final Result = ",max(result))
