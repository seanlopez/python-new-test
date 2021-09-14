import yaml

yaml.warnings({'YAMLLoadWarning': False})
f = open('../config.yaml', 'r', encoding="utf-8")
cfg = f.read()
d = yaml.load_all(cfg)

print(d)

for data in d:
    print(data)

f.close()

