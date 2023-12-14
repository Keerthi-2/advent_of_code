def parabola_disc(mat):

    for i in range(1,len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j]=='O' and mat[i-1][j]=='.':
                rr=i-1
                while(rr>0 and mat[rr-1][j]=='.'):
                    rr=rr-1
                mat[rr][j],mat[i][j]='O','.'

    ans=0
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if mat[i][j]=='O':
                ans+=(len(mat)-i)


    return ans







if __name__=="__main__":
    mat=[]
    with open("input.txt","r") as f:

        for line in f:
            mat.append(list(line.strip()))
        print(mat)

        print(parabola_disc(mat))
