def solution(data):
    left = 0
    right = len(data)-1
    ans =0
    left_max=0
    right_max=0
    while(left<right):
        if(data[left]<data[right]):
            if data[left]>=left_max:
                left_max = data[left]
            else:
                ans = ans+(left_max-data[left])
            left=left+1
        else:
            if data[right]>=right_max:
                right_max=data[right]
            else:
                ans = ans+right_max-data[right]

            right= right-1

    return ans

print(solution([0,1,0,2,1,0,1,3,2,1,2,1]))
