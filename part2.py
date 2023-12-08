from math import gcd

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

def array_lcm(numbers):
    result = 1
    for num in numbers:
        result = lcm(result, num)
    return result

def source_to_dest(source,graph,instructions):
    
    ans=[]
    dest=[]  
    for s in source:
        steps=0
        curr=s
        while(curr[-1]!='Z'):
            for i in instructions:
                if i=='L':
                    curr=graph[curr][0]
                else:
                    curr=graph[curr][1]
                steps+=1
                if curr[-1]=='Z':
                    dest.append(curr)
                    
            

        ans.append(steps)
             
    print(source,dest)        
    print(ans)
    res=1
    l=len(instructions)
    for i in ans:    
        res=res*(i)

   
    return array_lcm(ans)

if __name__=="__main__":
    graph={}
    string=""
    with open("input1.txt","r") as f:
        source=[]
        
        for line in f:
            
            if line=="":
                continue
            if len(line)>4 and line[4]=='=':    
                node,dest=line.strip().split("=")
                node=node.strip()
                dest=dest.strip()
                if node[-1]=='A':
                    source.append(node)
                part1,part2=tuple(dest[1:-1].split(","))
                graph[node]=(part1.strip(),part2.strip())
            else:
                string+=line.strip()
        

        print(graph,string)
        print(source_to_dest(source,graph,string))


            


