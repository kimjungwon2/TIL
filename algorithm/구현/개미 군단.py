def solution(hp):
    answer = 0

    count = hp//5

    hp -= count*5

    count2 = hp//3
    hp -= count2*3

    count3 = 0

    while (hp > 0):
        hp -= 1
        count3 += 1

    return count+count2+count3
