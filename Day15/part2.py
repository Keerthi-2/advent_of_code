def lens_library(lis):
    ans=0
    for l in lis:
        cur=l
        temp=0
        for i in range(len(cur)):
            temp+=(ord(cur[i])*17)
            
            temp=temp%256

        ans+=(temp)
        
    return ans%256

def lens_library1(cur):
   
    temp=0
    for i in range(len(cur)):
        temp+=(ord(cur[i]))
        
        temp=(temp*17)%256

    return temp

find_index = lambda lst, val: next((index for index, sublist in enumerate(lst) if sublist[0] == val), -1)
def lens_library_part2(cmds):
    ans=0
    box=[[] for i in range(0,256)]
    for cmd in cmds:
        if cmd[-1]=='-':
            #print(cmd,"-")
            name=cmd[:-1]
            ind=lens_library1(name)
            val=find_index(box[ind],name)
            if val!=-1:
                box[ind].pop(val)
            
        else:
            
            name,len_=cmd.split("=")
            ind=lens_library1(name)
            
           
            len_=int(len_)
           
            val=find_index(box[ind],name)
            if val!=-1:
                box[ind][val][1]=len_
            else:
                box[ind].append([name,len_])
    print(box[:4])
    for i in range(256):
        for j in range(len(box[i])):
            ans+=(i+1)*(j+1)*(int(box[i][j][1]))
            


    return ans


if __name__=="__main__":
    res=0
    cur=[]
    with open("input.txt","r") as f:
        for line in f:
            cur=line.strip().split(",")
            cur=[val.strip() for val in cur]
            res=lens_library_part2(cur)
    
    print(cur,res)

