from jinja2 import Environment, FileSystemLoader
from lxml.html import etree
import os


def get_problems():
	problems = dict()
	with open("array.txt", "r") as f:
		for line in f.readlines():
			no, title = tuple(line.split("/"))
			problems[no.lstrip("0")] = title.strip()

	return problems


def get_finished(dirpath="./solutions"):
	finished = dict()
	for _, _dirs, _files in os.walk(dirpath):
		for _dir in _dirs:
			no, title = tuple(_dir.split("_"))
			finished[no] = title

	return finished


def get_links():
	with open("./leetcode_all.html", "r", encoding='utf-8') as f:
		html_content = etree.HTML("".join(f.readlines()))
		nos = html_content.xpath("///table/tbody[1]/tr[*]/td[2]/text()")
		hrefs = html_content.xpath("//div[@class='question-title']/a/@href")
		cn_titles = html_content.xpath("//div[@class='question-title']/a/text()")
		levels = html_content.xpath("///table/tbody[1]/tr[*]/td[6]/span/text()")

	links = dict()
	for no, href, cn_title, level in zip(nos, hrefs, cn_titles, levels):
		links[no] = {"no": no, "cn_title": cn_title, "en_title": href.split("/")[-1], "href": href, "level": level}

	return links


def get_tags():

	tags = dict()
	dirnames = os.listdir("./solutions")

	for dirname in dirnames:
		no = dirname.split("_")[0]
		try:
			with open("./solutions/{0}/{0}.py".format(dirname), "r", encoding="utf-8") as f:
				for line in f.readlines():
					if line[0] != "#":
						break
					tag = line.split(" ")[-1]
					tags[no] = tag
					break;
		except:
			pass

	return tags


def get_md():
	with open("array.md", "w", encoding="utf-8") as f:
		env = Environment(loader=FileSystemLoader("template"))
		md_template = env.get_template("array.md")
		context = md_template.render({"problems": get_problems(), "finished": get_finished(), "links": get_links(), "tags": get_tags()})
		f.write(context)


if __name__ == "__main__":
	get_md()