import re

def config_split(file_handler):
    doc_list = file_handler.readlines()
    tag_list = []
    file_handler.close()
    End_config_row = doc_list.index("exit all\n")
    for i in range(len(doc_list)):
        if doc_list[i] == "#--------------------------------------------------\n":
            tag_list.append(i)
        elif doc_list[i] == "exit all\n":
            End_config_row = i

    tag_list_odd_index = []
    tag_list_none_odd_index = []
    for i in range(len(tag_list)):
        if i % 2 == 1:
            tag_list_odd_index.append(i)
        else:
            tag_list_none_odd_index.append(i)

    section_tag_sep = {}

    for i in range(len(tag_list_odd_index)):
        temp_list = []
        temp_list.append(tag_list[tag_list_none_odd_index[i]])
        temp_list.append(tag_list[tag_list_odd_index[i]])
        section_tag_sep[i] = temp_list

    out_put_dic = {}
    pattern = rf'echo\s\"(.+?)\"'
    for i in range(len(tag_list_odd_index)):
        section_tag_between = section_tag_sep[i]
        tag_row = section_tag_between[0] + 1
        title_row = doc_list[tag_row]
        tmp = re.findall(pattern, title_row, re.S)
        split_title = tmp[0]
        section_contend = ""
        if i == len(tag_list_odd_index) - 1:
            for row in range(section_tag_between[1]+1, End_config_row):
                section_contend = section_contend + doc_list[row]
            if split_title in out_put_dic.keys():
                out_put_dic[split_title] = out_put_dic[split_title] + section_contend
            else:
                out_put_dic[split_title] = section_contend
        else:
            for row in range(section_tag_between[1]+1, section_tag_sep[i + 1][0]):
                section_contend = section_contend + doc_list[row]
            if split_title in out_put_dic.keys():
                out_put_dic[split_title] = out_put_dic[split_title] + section_contend
            else:
                out_put_dic[split_title] = section_contend
    return out_put_dic

if __name__ == "__main__":
    f = open("ME-D6-MLK.log", "r", encoding="utf-8")
    print(config_split(f))
