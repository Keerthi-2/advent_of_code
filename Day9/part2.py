
def mirage_maintenance(history):
    if(history.count(0) == len(history)):
        return 0
    
    diff = []

    i = 1

    while(i < len(history)):
        diff.append(history[i] -history[i-1])
        i += 1
    
    return history[0] - mirage_maintenance(diff)
       
    
    for i in range(len(res)-1):
        sum_last-=res[i][0]
    
    return sum_last







if __name__=="__main__":
    input=[]
    ans=0
    with open("input.txt","r") as f:
        for line in f:
            l=line.strip()
            input=list(map(int,l.split()))
            #ansinput[0]
            ans+=mirage_maintenance(input)
           

        print(ans)
