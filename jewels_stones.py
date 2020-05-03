def numJewelsInStones(self, J: str, S: str) -> int:
    jewel_dict={}
    stone_dict={}
    jewel_sum=0
    for letter in J:
        jewel_dict[letter]= 1
        
    for letter2 in S:
        stone_dict[letter2]= stone_dict.get(letter2, 0)+1
        
    for letter in jewel_dict.keys():
        if letter in stone_dict:
            jewel_sum+=stone_dict[letter]
            
    return jewel_sum
            