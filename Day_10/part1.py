def symbol_Coordinate(symbol,i,j):
    if symbol=='-':
        return [(i,j-1),(i,j+1)]
    if symbol=='|':
        return [(i+1,j),(i-1,j)]
    if symbol=='L':
        return [(i-1,j),(i,j+1)] 
    if symbol=='7':
        return [(i,j-1),(i+1,j)]
    if symbol=='F':
        return [(i,j+1),(i+1,j)]
    if symbol=='J':
        return [(i,j-1),(i-1,j)]
    
    return []

def dfs(mat,i,j,dist,ans,visited,flag):
    print(dist,mat[i][j])
    if mat[i][j]=='S':
        flag=True
    if i<len(mat) and j<len(mat[i]) and mat[i][j]!=('.' or 'S'):
        l=symbol_Coordinate(mat[i][j],i,j)
        for cur in l:
            x1,y1=cur
            if (x1,y1) not in visited:
                visited.add((x1,y1))
                ans=max(ans,dist+1)
                dfs(mat,x1,y1,dist+1,ans,visited,flag)
            
    
    return dist
    
def pipe_maze(mat,u,v):
    r=len(mat)
    c=len(mat[0])
    ans=0
    visited=set()
   # print(u,v)
    if u+1<r and v<c and mat[u+1][v]!='.':
        visited.add((u+1,v))
        flag=False
        ans=dfs(mat,u+1,v,1,ans,visited,flag)
        if flag:
            ans=ans//2
     #   print(f"first-dfs{ans}")
    if u<r and v+1<c and mat[u][v+1]!='.':
        visited.clear()
        visited.add((u,v+1))
        flag=False
        ans=dfs(mat,u,v+1,1,ans,visited,flag)
        if flag:
            ans=ans//2
      #  print(f"second-dfs{ans}")
    if u-1>=0 and v<c and mat[u-1][v]!='.':
        visited.clear()
        visited.add((u-1,v))
        flag=False
        ans=dfs(mat,u-1,v,1,ans,visited,flag)
        if flag:
            ans=ans//2
      #  print(f"third-dfs{ans}")
    if u<r and v-1>=0 and mat[u][v-1]!='.':
        visited.clear()
        visited.add((u,v-1))
        flag=False
        ans=dfs(mat,u,v-1,1,ans,visited,flag)
        if flag:
            ans=ans//2
     #   print(f"fourth-dfs{ans}")
    
    return ans




if __name__=="__main__":
    mat=[]
    with open("sample.txt","r") as f:
        for line in f:
            l=line.strip()
            
            mat.append(list(l))
    print(mat)
    start_i=0
    start_j=0
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if mat[i][j]=='S':
                start_i=i
                start_j=j
                break
    print(pipe_maze(mat,start_i,start_j))
    