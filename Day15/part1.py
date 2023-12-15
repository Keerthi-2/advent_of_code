def lens_library(lis):
    ans=0
    for l in lis:
        cur=l
        temp=0
        for i in range(len(cur)):
            temp+=ord(cur[i])
            temp=temp*17
            temp=temp%256

        ans+=temp 

    return ans%256



if __name__=="__main__":
    res=0
    cur=[]
    with open("input.txt","r") as f:
        for line in f:
            cur=line.strip().split(",")
            cur=[val.strip() for val in cur]
            res=lens_library(cur)
    
    print(cur,res)

