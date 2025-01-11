# 합이 0
import sys

input = sys.stdin.readline
N = int(input())
students = list(map(int,input().split()))
students.sort()

result = 0

for i in range(N-2):
    left, right = i+1, N-1
    while left < right:
        sum_ = students[left] + students[right] + students[i]
        if sum_==0:
            if students[left] == students[right]:
                result += (right-left)
                left += 1
            else:
                j, k = left, right
                while students[j] == students[left] and j < right:
                    j += 1
                while students[k] == students[right] and k > left:
                    k -= 1
                result += (j-left)*(right-k)
                left, right = j, k
        elif sum_ > 0:
            right -= 1
        else:
            left += 1

print(result)