# reverse string  as same position without using builtin function

#input ----> python programming

# output ---->  nohtyp gnimmargorp


def split(a):
    last_index = len(a)-1
    start_index = 0
    mid_space_index = 0
    a_list = []

    if a.count(" ")>0:
        for index,value in enumerate(a):
            if index==last_index:
                new_string = a[mid_space_index+1:last_index+1]
                a_list.append(new_string)
            if ord(value)==32:
                mid_space_index = index
                a_list.append(a[start_index:mid_space_index])
                start_index = mid_space_index+1

        final_string =""
        for i in a_list:
            length_of_i = len(i)
            append_list = []
            for j in range(length_of_i-1,-1,-1):
                append_list.append(i[j])
            append_list.append(" ")
            final_string+=''.join(append_list)
       
        return final_string
    else:
        final_string = []
        for i in range(len(a),0,-1):
            final_string.append(a[i-1])
        return final_string


split("amar singh")