def rev_list_in_place(lst):
    # """Reverse list in place.
  for i, item in enumerate(lst):
    if i<=len(lst)//2:
        lst[i],lst[-1-i] =lst[-1-i], lst[i]

  return lst

    # You cannot do this with reversed(), .reverse(), or list slice
    # assignment!
    # """