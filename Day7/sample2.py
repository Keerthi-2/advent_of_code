from collections import Counter
def strength(h):
    d=Counter(h)
    if d['J']>0 and d['J']<5:
        
        max_val=0
        max_char=''
        f=d['J']
        for k,v in d.items():
            if k!='J' and v>max_val:
                max_val=v
                max_char=k
        d[max_char]+=f
        d.pop('J')
   

    l=[i for i in d.values()]
    l.sort()
    l=l[::-1]
    
    if l  == [1,1,1,1,1]:
        return 0
    if l  == [2,1,1,1]:
        return 1
    if l  == [2,2,1]:
        return 2
    if l  == [3,1,1]:
        return 3
    if l==[3,2]:
        return 4
    if l  == [4,1]:
        return 5
    if l  == [5]:
        return 6
    

    return -1
    
custom_order = 'AKQT98765432J'[::-1]
def custom_key(item):
    return [custom_order.index(char) for char in item]   

if __name__ == "__main__":
    h=[]
    with open("input2.txt","r") as f:
        while(True):
            l=f.readline()
            if len(l)==0:
                break
            val=l.strip().split()
            h.append([val[0],val[1]])

    
    for i in h:
        if i[0]=='JJJJJ':
            print(f"strength is:{i[0]}----{strength(i[0])+1}")

    h = sorted(h, key=lambda x: (strength(x[0])+1,custom_key(x[0])))
    
    
    res=0
    for i in range(len(h)):
       # print(h[i][0],i+1)
        res+=(i+1)*(int(h[i][1]))
    print(res)
    

