import sys 


def merge(list):
    mid=len(list)//2
    left,right=list[:mid],list[mid:]
    l_len,r_len=len(left),len(right)

    if l_len>1: merge(left)
    if r_len>1: merge(right)

    lw,rw,k=0

    while lw<l_len and rw<r_len:

        if right[rw]<left[lw]:
            list[k]=left[lw]
            lw+=1
           
        else:
            list[k]=right[rw]
            rw+=1
        k+=1
    while lw<l_len:
        list[k]=left[lw]
        lw+=1
        k=+1
    while rw<l_len:
        list[k]=right[rw]
        rw+=1
        k+=1


