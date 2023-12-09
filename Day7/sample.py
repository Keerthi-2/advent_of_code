from collections import Counter
def strength(h):
    
    d=Counter(h)

    l=[i for i in d.values()]
    l.sort()
    l=l[::-1]
    
    if l  == [1,1,1,1,1]:
        return 0
    if l  == [2,1,1,1]:
        return 1
    if l  == [2,2,1]:
        return 2
    if l  == ([3,1,1]):
        return 3
    if l==[3,2]:
        return 4
    if l  == [4,1]:
        return 5
    if l  == [5]:
        return 6
    

    return -1
    
custom_order = 'AKQJT98765432'[::-1]
def custom_key(item):
    
    return [custom_order.index(char) for char in item]   

if __name__ == "__main__":
    h=[["32T3K",765],["T55J5",684],["KK677",28],["KTJJT",220],["QQQJA",483]]
    
    h = sorted(h, key=lambda x: (strength(x[0]),custom_key(x[0])))
    print(h)
    
    
    res=0
    for i in range(len(h)):
       # print(h[i][0],i+1)
        res+=(i+1)*(h[i][1])
    print(res)
    
