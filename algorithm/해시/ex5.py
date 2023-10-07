def solution(clothes):

    cloth_dict = dict()   # key: 종류, value: [의상 이름]
    for cloth in clothes:
        if cloth[1] in cloth_dict:   # 이미 있는 종류의 경우(리스트에 추가)
            cloth_dict[cloth[1]].append(cloth[0])
        else:   # 처음 추가하는 종류의 경우(리스트 생성)
            cloth_dict[cloth[1]] = [cloth[0]]
    # print(cloth_dict)

    cnt = []
    calc1 = 0
    for c_t in cloth_dict:
        calc1 += len(cloth_dict[c_t])   # 하나씩 착용하는 경우
        cnt.append(len(cloth_dict[c_t]))

    calc2 = 1
    if len(cloth_dict) > 1:
        for c_t in cloth_dict:
            calc2 *= (len(cloth_dict[c_t]) + 1)
        return calc2 - 1

    return calc1


solution([["yellow_hat", "headgear"], ["blue_sunglasses",
         "eyewear"], ["green_turban", "headgear"]])
