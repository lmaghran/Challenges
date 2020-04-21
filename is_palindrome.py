def funWithAnagrams(text):
    ana_list=[]
    word_list=[]
    
    for word in text:
        word_dict={}

        for letter in word:
            if letter in word_dict:
                word_dict[letter]+=1
            else:
                word_dict[letter]=1

        if word_dict not in ana_list:
          word_list.append(word)
          ana_list.append(word_dict)

    word_list.sort()
    return word_list