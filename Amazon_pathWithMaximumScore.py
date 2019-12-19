def findAll(data,i,j):
        if(i==len(data)-1):
            return data[i][len(data[i])-1-j:]
        else:
            return [data[i][len(data[i])-j-1]]+findAll(data,i+1,j)

print(findAll([[1,2,3],[4,5,1],[6,7,8],[1,2,3]],0,1))


def pathWithMaximumScore(data):

    for i in range(0,len(data)):
        x = data[0][:len(data[0])-i]+findAll(data[i:],0,i)
        print(x)

pathWithMaximumScore([[1,2,3],[4,5,1],[6,7,8],[1,2,3]])
   
