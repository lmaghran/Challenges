def has_balenced_parens(parens_string):
  i=0
  for letter in parens_string:
    if i<0:
      return False
    elif letter=="(":
      i+=1
    elif letter==")":
      i-=1

  if i==0:
    return True
  else:
    return False