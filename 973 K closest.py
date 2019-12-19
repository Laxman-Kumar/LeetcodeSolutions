def kClosest(points,k):
        temp = []
        for x in points:
            temp.append((x[0]-0)**2+(x[1]-0)**2)
        data = list(zip(temp,points))
        print(min(data))
        temp=[]
        while(k>0):
            x  = min(data)
            temp.append(x)
            del data[data.index(x)]
            k-=1
            print(data)
        return [x[1] for x in temp]

print(kClosest([[1,3],[-2,2],[2,-2]],2))
