

def allrow(mat,row):
    
    for i in range(len(mat[row])):
        if  mat[row][i]=='#':
            return False
    return True


def allcol(mat,col):
    
    for i in range(len(mat)):
        if  mat[i][col]=='#':
            return False
    return True


if __name__=="__main__":
    mat=[]
    with open("sample1_pavan.txt","r") as f:

        for line in f:
            l=line.strip()
            mat.append(list(l))
        # print(mat,len(mat),len(mat[0]))

    res=[]
    row=[]
    col=[]
    for i in range(len(mat)):
        if allrow(mat,i):
            row.append(i)
    for j in range(len(mat[0])):
        if allcol(mat,j):
            col.append(j)
    
    cur=[]

    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if mat[i][j]=='#':
                cur.append((i,j))

   # print(row,col,cur)
    ans=0
    for i,(r,c) in enumerate(cur):
        for j in range(i+1,len(cur)):
            r2,c2=cur[j]
           # print(r,c,r2,c2)
            dist=abs(r-r2)+abs(c-c2)
            for r1 in row:
                if min(r,r2)<=r1<=max(r,r2):
                    dist+=1
            
            for c1 in col:
                if min(c,c2)<=c1<=max(c,c2):
                    dist+=1
            # print(dist)
            ans+=dist 
    print(ans)

    
        

    




