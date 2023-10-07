def palindromic(str):
    length= len(str)

    first = 0
    last = length - 1 
    mid = length//2
    s = ''

    if(length%2==0):
        while(first< length):
            if(str[first]==str[last]):
                s += str[first]

            first+=1 
            last-=1
    else:
        while (first <length):
            if(first==mid):
                s+=str[first]
            elif(str[first]==str[last]):
                s += str[first]

            first+=1 
            last-=1

    return s


print(palindromic("babad"))
print(palindromic("cbbd"))
