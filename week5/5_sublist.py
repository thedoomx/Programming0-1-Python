def sublist(list1, list2):
    length_of_list = len(list1)
    temp_list = []
    index = 0
    sublist = False

    if len(list1) == 0:
        sublist = True
    else:
        while index < len(list2):
            temp_index = index
            if list2[index] == list1[0]:
                if (index + 2) >= len(list2):
                    sublist = False
                    break
                else:
                    while length_of_list > 0:
                        temp_list += [list2[temp_index]]
                        temp_index += 1
                        length_of_list -= 1
                    
                    if temp_list == list1:
                        sublist = True
                        break

            temp_list = []
            index += 1
            length_of_list = len(list1)

    return sublist
