def source_to_dest(graph,instructions):

    steps=0
    curr='AAA'
    length=len(instructions)
  
    
    j=0
    while(curr!='ZZZ'):
        for i in instructions:
           
            if i=='L':
                curr=graph[curr][0]
            else:
                curr=graph[curr][1]
            steps+=1
            if curr=='ZZZ':
                
                return steps

        


    return steps

if __name__=="__main__":
    graph={}
    string=""
    with open("input.txt","r") as f:
      
        for line in f:
            
            if line=="":
                continue
            if len(line)>4 and line[4]=='=':    
                node,dest=line.strip().split("=")
                dest=dest.strip()
                part1,part2=tuple(dest[1:-1].split(","))
                graph[node.strip()]=(part1.strip(),part2.strip())
            else:
                string+=line.strip()
        

        print(graph,string)
        print(source_to_dest(graph,string))


            


