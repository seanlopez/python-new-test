f = open("ME-D6-MLK.log", "r", encoding="utf-8")

doc_list = f.readlines()
tag_list = []
f.close()
End_config_row = 0
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

pattern = rf'echo\s\"(.+?)\"'

for i in range(len(tag_list_odd_index)):
    section_tag_between = section_tag_sep[i]
    tag_row = section_tag_between[0] + 1
    title_row = doc_list[tag_row]
    tmp = re.findall(pattern, title_row, re.S)
    split_title = tmp[0] + ".txt"
    split_file_path = "C:\python-new-code\SP_auto_separate\configure_separate\configure_sep\\" + split_title
    f = open(split_file_path, "w", encoding="utf-8")
    print(End_config_row)
    if i == len(tag_list_odd_index) - 1:
        for row in range(section_tag_between[0], End_config_row):
            f.write(doc_list[row])
    else:
        for row in range(section_tag_between[0], section_tag_sep[i+1][0]):
            f.write(doc_list[row])
    f.close()