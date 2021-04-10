import os
import argparse
import configparser
from lxml.html import etree

class Config(object):
    """读取config类,单例模式
    """
    
    __instance = None
    def __new__(cls):
        if not cls.__instance:
            cls.__instance = object.__new__(cls)
        return cls.__instance
    
    def __init__(self):
        config = configparser.ConfigParser()
        config.read("conf/config.ini", encoding="UTF-8")
        self.section = config["default"]

    def __getitem__(self, key):
        """重构[],获取配置"""
        return self.section[key]


def get_problems_info(file):
    """解析leetcode problems列表的html文件,输出problems的信息

    参数:
        file (str):     html文件的路径
    
    返回:
        infos (dict):   problems的信息,格式如下
        {
            "no" : {
                "no": no,
                "cn_title": cn_title,
                "en_title": en_title,
                "href": href,
                "level": level
            }
        }
    """
    config = Config()
    file_path="{}/{}".format(config["html_dir"], file)
    with open(file_path, "r", encoding='utf-8') as f:
        html_content = etree.HTML("".join(f.readlines()))
        nos = html_content.xpath("///table/tbody[1]/tr[*]/td[2]/text()")
        hrefs = html_content.xpath("//div[@class='question-title']/a/@href")
        cn_titles = html_content.xpath("//div[@class='question-title']/a/text()")
        levels = html_content.xpath("///table/tbody[1]/tr[*]/td[6]/span/text()")

    infos = dict()
    for no, href, cn_title, level in zip(nos, hrefs, cn_titles, levels):
        infos[no] = {"no": no, "cn_title": cn_title, "en_title": href.split("/")[-1], "href": href, "level": level}

    return infos

    
def create_csv(infos, output="output.csv"):
    with open(output, "w") as f:
        f.write("no, cn_title, en_title, href, level\n")
        for _, v in infos.items():
            f.write(",".join(v.values()) + "\n")



if __name__ == "__main__":
    # 读取脚本参数
    parser = argparse.ArgumentParser()
    parser.add_argument("-html", help="html文件名")
    parser.add_argument("-o", "--output", help="输出的文件路径")
    args = parser.parse_args()

    file = args.html
    output_file = args.output


    problems_info = get_problems_info(file)
    create_csv(problems_info)