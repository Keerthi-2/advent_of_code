

def extra_val(input):
    
    sum_last=0
    while(input.count(0)!=len(input)):
        cur=[]
        for i in range(0,len(input)-1):
            cur.append(input[i+1]-input[i])
        input=cur[::]
        if input[-1]!=0:
            sum_last+=input[-1]
       
    
    # for i in range(len(res)-1):
    #     sum_last+=res[i][-1]
  
    return sum_last







if __name__=="__main__":
    input=[]
    ans=0
    with open("input.txt","r") as f:
        for line in f:
            l=line.strip()
            input=list(map(int,l.split()))
            ans+=input[-1]
            ans+=extra_val(input)

        print(ans)
