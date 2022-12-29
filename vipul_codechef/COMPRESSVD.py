# cook your dish here
def compress_video(l,k):
    j=0 
    while(j<len(l)-1):
        if l[j] == l[j+1]:
            l.remove(l[0])
        else:
            j+=1
    return len(l) 
    
for i in range(int(input())):
    k = int(input())
    l = [int(i) for i in input().split()]
    print(compress_video(l,k))