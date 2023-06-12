def specific_sum(lst,result):
    sum_var=0
    start=0
    for i in range (0,len(lst)):
        if sum_var ==result:
            print((start+1),(i))
            break
        elif sum_var<result:
            sum_var=sum_var+lst[i]
        elif sum_var>result:
            sum_var=sum_var-lst[start]
            start=start+1
