import re


cou = int(input())

for i in range(cou):
    card_id = input()
    if len(card_id) == 16 or len(card_id)==19:
        fir_num = re.match("^[456]+",card_id)
        if fir_num:
            lin = re.search("-",card_id)
            if lin:
                lin_num = re.findall("\-",card_id)
                if len(lin_num) == 3:
                    card = re.match("\d{4}\-\d{4}-\d{4}-\d{4}",card_id)
                    if card:
                        card_id_sub = re.sub("-", "", card_id)
                        for i in range(10):
                            n = str(i)
                            n = n*4
                            time = re.findall(n, card_id_sub)
                            if len(time) > 0:
                                print("Invalid")
                                break
                            elif i == 9:
                                print("Valid")
                            else:
                                continue
                    else:
                        print("Invalid")
                else:
                    print("Invalid")
            else:
                for i in range(10):
                    n = str(i)
                    n = n*4
                    time = re.findall(n,card_id)
                    if len(time) > 0:
                        print("Invalid")
                        break
                    elif i == 9:
                        print("Valid")
                    else:
                        continue
        else:
            print("Invalid")
    else:
        print("Invalid")
