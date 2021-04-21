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
    """将爬取的infos写入csv"""
    with open(output, "w") as f:
        for _, v in infos.items():
            f.write(",".join(v.values()) + "\n")


def make_solution_dir(no, en_title):
    """创建solution文件夹和文件
    
    参数:
        no (str):       题目编号
        en_title (str): 题目的英文标题
    """

    config = Config()
    solutions_dir = config["solutions_dir"]
    solution_dir = "{}_{}".format(no, en_title)
    solution_py_filename = "{}_{}.py".format(no, en_title)
    solution_js_filename = "{}_{}.js".format(no, en_title)

    try:
        os.mkdir("{}/{}".format(solutions_dir, solution_dir))
        with open("{}/{}/{}".format(solutions_dir, solution_dir, solution_py_filename), "w") as f:
            pass
        with open("{}/{}/{}".format(solutions_dir, solution_dir, solution_js_filename), "w") as f:
            pass
    except Exception:
        # 存在创建失败的情况(文件夹已存在),不管
        pass


def read_csv(csv_file):
    """读取csv文件的problems infos

    参数:
        csv_file (str): csv文件名
    
    返回值:
        infos (dict):   csv文件中problems的信息
    """
    config =Config()
    data_dir = config["data_dir"]

    infos = dict()
    with open("{}/{}".format(data_dir, csv_file), "r") as f:
        for line in f.readlines():
            no, cn_title, en_title, href, level = tuple(line.split(","))
            infos[no] = {
                "no": no,
                "cn_title": cn_title,
                "en_title": en_title,
                "href": href,
                "level": level
            }
    
    return infos


if __name__ == "__main__":
    # # 读取脚本参数
    # parser = argparse.ArgumentParser()
    # parser.add_argument("-html", help="html文件名")
    # parser.add_argument("-o", "--output", help="输出的文件路径")
    # args = parser.parse_args()

    # file = args.html
    # output_file = args.output

    # problems_info = get_problems_info(file)
    # create_csv(problems_info)

    # 根据csv文件创建solution文件夹
    problem_infos = read_csv("problemset_backtracking.csv")
    for k, v in problem_infos.items():
        no = v["no"]
        en_title = v["en_title"]
        print(no, en_title)
        make_solution_dir(no, en_title)