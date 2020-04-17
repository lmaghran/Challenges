def countElements(self, arr: List[int]) -> int:
    counter=0
    for item in arr:
        if item +1 in arr:
            counter+=1
    return counter