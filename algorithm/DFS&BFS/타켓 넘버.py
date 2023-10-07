answer = 0

def solution(numbers, target):
    global answer 
    dfs(0,0,numbers,target)
    
    return answer

def dfs(index, sum, numbers, target):
    global answer
    
    length = len(numbers)
    
    if(index == length):
        if(target==sum):
            answer+=1
            
            return 1
        return 0
    
    dfs(index+1,sum+numbers[index],numbers,target)
    dfs(index+1,sum-numbers[index],numbers,target)