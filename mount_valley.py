# Complete the countingValleys function below.
def countingValleys(n, s):
    valley_count=0
    starting_step=0
    ending_step=0

    for string in s:
        if string.upper()== "D":
            ending_step -=1
        
        if string.upper() == "U":
            ending_step +=1
        
        if (starting_step<0 and ending_step>=0):
            valley_count+=1
        
        starting_step= ending_step

    return valley_count