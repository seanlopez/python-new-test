def minion_game(string):
    # your code goes here
    l = len(string)
    list_str = list(string)
    list_yuan = []
    list_fu = []

    for i in list_str:
        if i in ["A", "E", "I", "O", "U"]:
            list_yuan.append(i)
        else:
            list_fu.append(i)

    #print(list_yuan)
    #print(list_fu)

    idx_fu = []
    idx_yuan = []
    for fu in list_fu:
        idx_fu.append(list_str.index(fu))
        list_str.insert(list_str.index(fu),"o")
        list_str.remove(fu)

    list_str = list(string)
    for yuan in list_yuan:
        idx_yuan.append(list_str.index(yuan))
        list_str.insert(list_str.index(yuan),"o")
        list_str.remove(yuan)

    list_str = list(string)
    #print(idx_fu)
    #print(idx_yuan)

    l_len_str = l
    stuart_sc = 0
    kevin_sc = 0
    for fu_idx in idx_fu:
        for i in range(l):
            if l_len_str - i > fu_idx:
                if string[fu_idx:l_len_str-i]:
                    stuart_sc = stuart_sc+1

    for yuan_idx in idx_yuan:
        for i in range(l):
            if l_len_str-i > yuan_idx:
                if string[yuan_idx:l_len_str-i]:
                    kevin_sc = kevin_sc+1


    #print(kevin_sc)
    #print(stuart_sc)
    if kevin_sc > stuart_sc:
        print("Kevin "+str(kevin_sc))
    elif kevin_sc < stuart_sc:
        print("Stuart "+str(stuart_sc))
    else:
        print("Draw")

minion_game(s)
