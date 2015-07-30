
def po(n):
    lst=[[1,1],[1,0]]

    if n == 0:
        return 0
    for i in range(2,n):
       lst = mul(lst)
    return lst[0][0]
def mul(lst):
    lst1=[[1,1],[1,0]]

    x=lst[0][0] * lst1[0][0]+ lst[0][1] * lst1[1][0]
    y=lst[0][0] * lst1[0][1]+ lst[0][1] * lst1[1][1]
    z=lst[1][0] * lst1[0][0]+ lst[1][1] * lst1[1][0]
    d=lst[1][0] * lst1[0][1]+ lst[1][1] * lst1[1][1]

    lst1[0][0]=x;lst1[0][1]=y;lst1[1][0]=z;lst1[1][1]
    return lst1

print po(input("enter re baba:"))
    

       
