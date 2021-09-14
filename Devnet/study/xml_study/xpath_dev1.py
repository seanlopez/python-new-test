from lxml import etree

bookstore = '''
<bookstore>
<book category = "Cookie">
    <title>book1</title>
    <author>Gilbert</author>
    <year>2005</year>
    <price>10000</price>
</book>

<book category = "WEB">
    <title>book2</title>
    <author>JK</author>
    <year>2006</year>
    <price>20000</price>
</book>

<book category = "CHILDREN">
    <title>book3</title>
    <author>Peter</author>
    <year>2007</year>
    <price>30000</price>
</book>

</bookstore>
'''

s = etree.HTML(bookstore)
print(s.xpath("//bookstore"))

print(s.xpath("//book[position()<3]"))

print(s.xpath("//@category"))

print(s.xpath("//book[@category='WEB']"))

print(s.xpath("//book[price>10000]"))

print(s.xpath("//bookstore/*"))
print(s.xpath("//bookstore//*"))

print(s.xpath("//book[@*]/price/text()"))

for i in s.xpath("//*"):
    #print(i)
    print(i.tag)

