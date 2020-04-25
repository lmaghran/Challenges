# Complete the hourglassSum function below.
def hourglassSum(arr):
    array_sums=[]
    final_sums=[]
    hour_mid=[]

    for i, nums in enumerate(arr):
        for i, second_array in enumerate(arr[1:-1]):
            for j, num in enumerate(second_array[1:-1]):
                num

    for i, second_array in enumerate(arr):
        for j, num in enumerate(second_array):
            if j<len(second_array)-2:
                first_sum= num+second_array[j+1]+ second_array[j+2]
                array_sums.append(first_sum)
                
            if j>0 and i>0 and j<len(second_array)-1 and i<len(arr)-1:
                hour_mid.append(num)
                
    for x, num in enumerate(array_sums):
        if hour_mid:
            hour_middle= hour_mid.pop(0)
        if x<len(array_sums)-8:
            first_last_sum= num+ array_sums[x+8]+hour_middle
            final_sums.append(first_last_sum)
    
    return max(final_sums)