def lastStoneWeight(self, stones: List[int]) -> int:
#find the first max - pop it
#find the second max -pop it 
#when the list is one number- return that number

while len(stones)>1:
    stones.sort()
    print(stones)
    largest_num= stones.pop()
    second_num = stones.pop()
    if largest_num != second_num:
        stones.append(largest_num-second_num)
    else:
        stones.append(0)

return stones[0]