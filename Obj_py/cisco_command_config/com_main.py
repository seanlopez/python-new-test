import com_cls


creatvar = locals()

while True:
    print("1.Add command to system\n")
    print("2.Del command form system\n")
    print("** leave this system please input '0'  **\n")
    choise = input("please input your choise :  >>").strip()
    if len(choise) != 1 or  not choise.isdigit():
        print("your input is worry")
        continue
    elif choise == "0":
        exit()
    else:
        if choise == "1":
            var_name = input("please input your command's name:  >>")
            desc_ = input("please input your command's description:  >>")
            creatvar[var_name] = com_cls.com(var_name,desc_)
        elif choise == "2":
            var_name = input("please input your command's name:  >>")
            if var_name in creatvar:
                option_ = input("the command is already exsit, are your sure to del this?(Y):  >>").strip()
                if option_ == "Y" or option_ == "y":
                    del creatvar[var_name]
            else:
                print("your command is not exsit!")
