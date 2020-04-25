# Complete the repeatedString function below.
def repeatedString(s, n):
    count_a=0
    letter_dict={}
    for i, letter in enumerate(s):
        if letter=="a":
            count_a+=1
        letter_dict[i+1]= count_a
    
    repeat_str= n//len(s)
    remain= n%len(s)
    low_num= count_a* repeat_str
    if remain==0:
        return low_num
    else:
        total= low_num + letter_dict[remain]
        return total