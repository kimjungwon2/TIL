import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
M = int(input())
target_list = list(map(int, input().split()))

nums.sort()


def binary_search(start, end, target):
    if (start >= end):
        if (nums[start] == target):
            print(1)
            return 1
        else:
            print(0)
            return 0

    mid = (start+end)//2

    if (nums[mid] < target):
        binary_search(mid+1, end, target)
    else:
        binary_search(start, mid, target)


for each_target in target_list:
    binary_search(0, N-1, each_target)
