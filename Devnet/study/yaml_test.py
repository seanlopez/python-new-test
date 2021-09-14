import yaml

f = open("./ISE_Conf.yml", 'r', encoding="utf-8")
cont = f.read()
#print(cont)

x = yaml.load(cont)

#print(x["Application_Conf"])
#print(x["Basic_Conf"])
#print(x["Basic_Conf"][1]["Version"])

data = {
    "name": "Sean",
    "Social Media": {'Webex': "tianyuan@cisco.com",
                     'wechat': "walyk"},
    'Security_Team': ['ISE', 'Firepower', 'AMP']
}

print(yaml.dump(data, default_flow_style = False))

y = yaml.dump(data, default_flow_style = False)

f1 = open("load_write.yml", "w")
f1.write(y)
f1.close()



