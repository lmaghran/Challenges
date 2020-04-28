def array_mut(n,a):
    b_list=[]
    for i, num in enumerate(a):
        if i==0:
            new_num= num+a[1]
        elif i==n-1:
            new_num=a[i-1]+num
            
        else:
            new_num= a[i-1]+num + a[i+1]
        
        b_list.append(new_num)
    return b_list