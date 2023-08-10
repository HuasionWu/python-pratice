from bs4 import BeautifulSoup

html_doc = """

<html><head><title>练习python</title></head>
<body>
<p class="title"><b>python3.8</b></p>

<p class="story">今天，程序员在上班
<a href="http://example.com/1" class="sister" id="link1">早上9点上班</a>,
<a href="http://example.com/2" class="sister" id="link2">下午6点下班</a> ,
你觉得这样的工作时长是否合理</p>

<p class="story">...</p>

"""

soup = BeautifulSoup(html_doc,'lxml')
print(soup.title.string)
#练习python
print(soup.p.string)
#python3.8
print(soup.title.parent.name)
#head
print(soup.a)
#<a class="sister" href="http://example.com/1" id="link1">早上9点上班</a>
print(soup.find_all('a'))
#[<a class="sister" href="http://example.com/1" id="link1">早上9点上班</a>, <a class="sister" href="http://example.com/2" id="link2">一个笑话短</a>]
print(soup.find(id="link2"))
#<a class="sister" href="http://example.com/2" id="link2">下午6点下班</a>
print(soup.get_text())
print(soup.select("title"))
print(soup.select("body a"))
print(soup.select("p > #link1"))