## linear search:

for each item in the list:
if item == target:
return index
return -1 (indicating that the target is not in the list)

## binary search :

1. Set low = 0, high = n-1 (where n is the number of elements in the list)
2. Repeat until low <= high:
   a. Set mid = (low + high) // 2
   b. If arr[mid] == target, return mid
   c. If arr[mid] < target, set low = mid + 1
   d. If arr[mid] > target, set high = mid - 1
3. If low > high, target is not in the list

## interpolation search:

1. Set low = 0, high = n-1
2. Repeat until low <= high:
   a. Calculate pos using the interpolation formula
   b. If arr[pos] == target, return pos
   c. If arr[pos] < target, set low = pos + 1
   d. If arr[pos] > target, set high = pos - 1
3. If low > high, target is not in the list

## jump search:

1. Set step = sqrt(n) where n is the number of elements
2. Repeat until arr[min(step, n)-1] < target:
   a. Increase the step index
3. Perform a linear search in the current block to find the target
   hashing

## exponential search:

1. Set i = 1
2. Repeat until arr[i] >= target:
   a. Double i
3. Perform binary search in the range (i/2) to min(i, n-1)

## Fibonacci search:

1. Find the smallest Fibonacci number greater than or equal to n (the number of elements)
2. Initialize two Fibonacci numbers a and b based on the found Fibonacci number
3. Repeat until a > 1:
   a. Calculate the new position: pos = min(start + a - 1, n-1)
   b. If arr[pos] == target, return pos
   c. If arr[pos] < target, set (start, a, b) = (pos + 1, b - a, a)
   d. If arr[pos] > target, set (a, b) = (a - b, a)

## ternary search:

1. Set left = 0, right = n-1
2. Repeat until left <= right:
   a. Calculate mid1 = left + (right - left) / 3
   b. Calculate mid2 = right - (right - left) / 3
   c. If arr[mid1] == target, return mid1
   d. If arr[mid2] == target, return mid2
   e. If arr[mid1] > target, set right = mid1 - 1
   f. If arr[mid2] < target, set left = mid2 + 1
   g. If target is not found, repeat the process with the new range (left, right)
