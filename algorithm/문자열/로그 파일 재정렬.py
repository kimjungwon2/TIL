def sor(list):
    letter, digit = [], []
    for a in list:
        if a.split()[1].isdigit():
            digit.append(a)
        else:
            letter.append(a)

    letter.sort(key=lambda x: (x.split()[1:], x.split()[0]))

    return letter+digit


print(sor(["dig1 8 1 5 1", "let1 art can", "dig2 3 6",
      "let2 own kit dig", "let3 art zero"]))
