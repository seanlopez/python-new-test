def count_substring(string, sub_string):
    cou = int(0)
    sub_len = len(sub_string)
    for i in range(len(string)):
        my_str = string[i:i+sub_len]
        print(my_str)
        if my_str == sub_string:
            cou = cou + 1
        if i+3 == len(string):
            break
    return cou

print(count_substring("ThIsisCoNfUsInG","is"))
