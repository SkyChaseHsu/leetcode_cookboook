import urllib.request
import random
import requests
import os
from lxml import etree

def get_user_agent():
	"""
	随机获取一个agent
	"""

	# agent池
	agent_pool = [
		"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
		"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36",
		"Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0"
		]

	# 从agent池中随机选出一个agent返回
	return agent_pool[random.randint(0, len(agent_pool)-1)]



def get_titles(target_url, rule):
	# agent池
	header = {'User-Agent':get_user_agent()}

	# 获取目标的html文件，etree解析
	req = requests.get(url=target_url, headers=header)
	req.encoding = req.apparent_encoding

	# etree解析内容
	etree = html.etree
	req_html = etree.HTML(req.content)

	# 解析出图片的链接
	content = req_html.xpath(rule)

	return content


if __name__ == "__main__":

	nums = get_titles("https://books.halfrost.com/leetcode/ChapterTwo/Array/", ".//article/table/tbody/tr/td[1]/text()")
	problems = get_titles("https://books.halfrost.com/leetcode/ChapterTwo/Array/", ".//article/table/tbody/tr/td[2]/text()")

	with open("array.txt", "w") as f:
		for num, problem in zip(nums, problems):
			f.write("{}/{}\n".format(num, problem))
