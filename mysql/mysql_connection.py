import pymysql

conn = pymysql.connect(host="192.168.223.22", port=3306, user="tianqi", passwd="Tq19950822.", db="Test")

cursor = conn.cursor() #创建游标


effect_row = cursor.execute("select * from student")    #打印收到影响的行数
print(effect_row)

print(cursor.fetchone())
print(cursor.fetchone())
'''

data = [
    ("test_name1", 20),
    ("test_name2", 33)
]

effect_row = cursor.executemany("insert into student(name, age) values (%s, %s)", data)
conn.commit()
'''


