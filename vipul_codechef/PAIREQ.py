# cook your dish here
def make_all_equal_using_pairs(l,k):
    max_element = max(l,key=l.count)
    count = l.count(max_element)
    r_l = k-count
    return r_l
for i in range(int(input())):
    k = int(int(input()))
    l = [int(i) for i in input().split()]
    print(make_all_equal_using_pairs(l,k))
    
    
    
            
