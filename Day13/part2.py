def point_of_incidence(mat):


    print(mat)
    r="row"
    c="col"
    ans=0
    R=len(mat)
    C=len(mat[0])
    
    for r in range(R-1):
        badness=0
        for dr in range(R):
            up=r-dr
            down=r+1+dr
            if 0<=up<down<R:
                for c in range(C):
                    if mat[up][c]!=mat[down][c]:
                        badness+=1
        if badness==1:
            print(f"row_wise is {r}")
            return (r+1),"row"



    for c in range(C-1):
        badness=0
        for dc in range(C):
            up=c-dc
            down=c+1+dc
            if 0<=up<down<C:
                for r in range(R):
                    if mat[r][up]!=mat[r][down]:
                        badness+=1
        if badness==1:
            print(f"col_wise is {c}")
            return (c+1),"col"
    


if __name__=="__main__":
    ans=0 
    with open("input.txt","r") as f:
        cur=[]

        for line in f:
            line=line.strip()
            if len(line)==0:
               # print(cur)
                count,flag=point_of_incidence(cur)
                print(count,flag)
                if flag=="col":
                    ans+=count
                else:
                    ans+=count*100
                cur=[]
            else:
                cur.append(list(line))
        count,flag=point_of_incidence(cur)
        print(count,flag)
        if flag=="col":
            ans+=count
        else:
            ans+=count*100

        print(ans)
