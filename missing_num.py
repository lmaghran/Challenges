def missing_number(nums_list, max_num):
  max_set=set(range(max_num+1))
  missing_num= sum(max_set)-sum(nums_list)
  return missing_num