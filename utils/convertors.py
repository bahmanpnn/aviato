def grouped_list(list,size=4):
    my_list=[]
    for i in range(0,len(list),size):
        my_list.append(list[i:i+size])

    return my_list



