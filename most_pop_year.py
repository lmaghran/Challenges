# define most populated function
# most_pop_num=0
# most_pop_year= first_year
# loop through birth years for each tuple
# if birth year is in the range of another tuple, add one to the most_pop_num, change year to the most_pop_year
# if it is a tie, earliest year?

def most_populated(year_list):
  current_num=0
  most_pop_num=0
  most_pop_year= year_list[0][0]

  for i, yr_range in enumerate(year_list):
    birth_year= yr_range[0]
    while i<len(year_list):
      if birth_year>= year_list[i][0] and birth_year<=year_list[i][1]:
        current_num+=1
      i+=1

      most_pop_year= max(most_pop_year, birth_year)
  return most_pop_year