def segments(message):
    """Divides messages into 160 characters, returns the divided text as an array"""
    mess_segments=[]
    mess_len= len(list(message))
    segment_nums= math.ceil(mess_len/160)

    # If the length of the message is under 160 char, return it in array
    if mess_len<=160:
        mess_segments.append(message)
        return mess_segments

    # seperates the message into a list
    message=list(message)

    #Iterate through the number of segments, starting with 1 (1 of X)
    for i in range(1, segment_nums+1):
        # string formating for ex. (1/5)
        seg_txt= '({}/{})'.format(str(i), str(segment_nums))
        seg_len= len(seg_txt)

        #list slicing to create a 160 character message
        new_mess= message[:160-seg_len]
        mess_segments.append("".join(new_mess)+seg_txt)

        #slice the message to only include the unappended text
        message= message[160-seg_len:]

    # return the list with message segments
    return mess_segments
