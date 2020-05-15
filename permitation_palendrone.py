def per_palindrome(string):
  letter_dictionary={}
  odd_num_counter=0
  for letter in string:
    letter_dictionary[letter]= letter_dictionary.get(letter,0)+1

  for key in letter_dictionary.keys():
    if letter_dictionary[key]%2!=0:
      odd_num_counter+=1
    if odd_num_counter>1:
      return False
  return True
print(per_palindrome('civil'))
