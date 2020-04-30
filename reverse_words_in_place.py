def reverse_wrd(word_lst):
  starting_i=0
  for i, ltr in enumerate(word_lst):
    if ltr==" ":
      ending_i=i-1
    if i==len(word_lst)-1:
      ending_i=i
    
      i_dif=(ending_i-starting_i)//2
      while starting_i<=i_dif:
        print(starting_i)
        word_lst[starting_i], word_lst[ending_i]= word_lst[ending_i], word_lst[starting_i]
        starting_i+=1
        ending_i-=1
      starting_i+=1
  return word_lst