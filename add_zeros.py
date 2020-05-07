    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        i=0
        og_length= len(arr)
        while i<og_length:
            if arr[i]==0:
                arr.insert(i,0)
                i+=2
                
            else:
                i+=1
                
        while len(arr)> og_length:
            arr.pop()