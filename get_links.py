from lxml.html import etree

with open("./leetcode_all.html", "r", encoding='utf-8') as f:
	html_content = etree.HTML("".join(f.readlines()))
	target = html_content.xpath("//div[@class='question-title']/a/@href")
	print(target)

