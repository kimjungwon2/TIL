from collections import deque
import sys

input = sys.stdin.readline

N = int(input())
graph = [list(map(int,input().split())) for _ in range(N)]

size = 2
eat = 0

