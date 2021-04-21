import json
from lxml import etree


def get_uri_para(html_file):
    f = open(html_file, "r", encoding="UTF-8").read()
    html = etree.HTML(f)
    
    # 表格的数量
    tables_cnt = len(html.xpath("//h4[starts-with(text(), 'URI')]/../div[@class='tablenoborder']//caption/text()"))

    tables = []
    for table_i in range(1, tables_cnt + 1):
        table = dict()
        
        # 获得表格的caption
        caption = html.xpath(f"//h4[starts-with(text(), 'URI')]/../div[@class='tablenoborder'][{table_i}]//caption/text()")[0]
        table["caption"] = caption
        
        # 获得表格的head
        head = html.xpath(f"//h4[starts-with(text(), 'URI')]/../div[@class='tablenoborder'][{table_i}]//thead/tr/th/p/text()")
        table["head"] = head
        
        # 获得表格的参数
        table["para"] = []
        row_cnt = len(html.xpath(f"//h4[starts-with(text(), 'URI')]/../div[@class='tablenoborder'][{table_i}]//tbody/tr"))
        for row_i in range(1, row_cnt + 1):
            # 获得每一行的参数
            row = html.xpath(f"//h4[starts-with(text(), 'URI')]/../div[@class='tablenoborder'][{table_i}]//tbody/tr[{row_i}]/td/p/text()")
            
            para_dict = dict()
            for head_k, row_k in zip(head, row):
                para_dict[head_k] = row_k
            table["para"].append(para_dict)
            
        # 加入tables
        tables.append(table)
    
    return tables


def get_req_para(html_file):
    f = open(html_file, "r", encoding="UTF-8").read()
    html = etree.HTML(f)
    
    # 表格的数量
    tables_cnt = len(html.xpath("//h4[starts-with(text(), '请求消息')]/../div[@class='tablenoborder']//caption/text()"))

    tables = []
    for table_i in range(1, tables_cnt + 1):
        table = dict()
        
        # 获得表格的caption
        caption = html.xpath(f"//h4[starts-with(text(), '请求消息')]/../div[@class='tablenoborder'][{table_i}]//caption/text()")[0]
        table["caption"] = caption
        
        # 获得表格的head
        head = html.xpath(f"//h4[starts-with(text(), '请求消息')]/../div[@class='tablenoborder'][{table_i}]//thead/tr/th/p/text()")
        table["head"] = head
        
        # 获得表格的参数
        table["para"] = []
        row_cnt = len(html.xpath(f"//h4[starts-with(text(), '请求消息')]/../div[@class='tablenoborder'][{table_i}]//tbody/tr"))
        for row_i in range(1, row_cnt + 1):
            # 获得每一行的参数
            row = html.xpath(f"//h4[starts-with(text(), '请求消息')]/../div[@class='tablenoborder'][{table_i}]//tbody/tr[{row_i}]/td/p/text()")
            
            para_dict = dict()
            for head_k, row_k in zip(head, row):
                para_dict[head_k] = row_k
            table["para"].append(para_dict)
            
        # 加入tables
        tables.append(table)
    
    return tables


def get_req_para2(html_file):
    f = open(html_file, "r", encoding="UTF-8").read()
    html = etree.HTML(f)
    
    # 表格的数量
    tables_cnt = len(html.xpath("//h4[starts-with(text(), '请求参数')]/../div[@class='tablenoborder']//caption/text()"))

    tables = []
    for table_i in range(1, tables_cnt + 1):
        table = dict()
        
        # 获得表格的caption
        caption = html.xpath(f"//h4[starts-with(text(), '请求参数')]/../div[@class='tablenoborder'][{table_i}]//caption/text()")[0]
        table["caption"] = caption
        
        # 获得表格的head
        head = html.xpath(f"//h4[starts-with(text(), '请求参数')]/../div[@class='tablenoborder'][{table_i}]//thead/tr/th/p/text()")
        table["head"] = head
        
        # 获得表格的参数
        table["para"] = []
        row_cnt = len(html.xpath(f"//h4[starts-with(text(), '请求参数')]/../div[@class='tablenoborder'][{table_i}]//tbody/tr"))
        for row_i in range(1, row_cnt + 1):
            # 获得每一行的参数
            row = html.xpath(f"//h4[starts-with(text(), '请求参数')]/../div[@class='tablenoborder'][{table_i}]//tbody/tr[{row_i}]/td/p/text()")
            
            para_dict = dict()
            for head_k, row_k in zip(head, row):
                para_dict[head_k] = row_k
            table["para"].append(para_dict)
            
        # 加入tables
        tables.append(table)
    
    return tables


def get_resp_para(html_file):
    f = open(html_file, "r", encoding="UTF-8").read()
    html = etree.HTML(f)
    
    # 表格的数量
    tables_cnt = len(html.xpath("//h4[starts-with(text(), '响应消息')]/../div[@class='tablenoborder']//caption/text()"))

    tables = []
    for table_i in range(1, tables_cnt + 1):
        table = dict()
        
        # 获得表格的caption
        caption = html.xpath(f"//h4[starts-with(text(), '响应消息')]/../div[@class='tablenoborder'][{table_i}]//caption/text()")[0]
        table["caption"] = caption
        
        # 获得表格的head
        head = html.xpath(f"//h4[starts-with(text(), '响应消息')]/../div[@class='tablenoborder'][{table_i}]//thead/tr/th/p/text()")
        table["head"] = head
        
        # 获得表格的参数
        table["para"] = []
        row_cnt = len(html.xpath(f"//h4[starts-with(text(), '响应消息')]/../div[@class='tablenoborder'][{table_i}]//tbody/tr"))
        for row_i in range(1, row_cnt + 1):
            # 获得每一行的参数
            row = html.xpath(f"//h4[starts-with(text(), '响应消息')]/../div[@class='tablenoborder'][{table_i}]//tbody/tr[{row_i}]/td/p/text()")
            
            para_dict = dict()
            for head_k, row_k in zip(head, row):
                para_dict[head_k] = row_k
            table["para"].append(para_dict)
            
        # 加入tables
        tables.append(table)
    
    return tables


def get_resp_para2(html_file):
    f = open(html_file, "r", encoding="UTF-8").read()
    html = etree.HTML(f)
    
    # 表格的数量
    tables_cnt = len(html.xpath("//h4[starts-with(text(), '响应参数')]/../div[@class='tablenoborder']//caption/text()"))

    tables = []
    for table_i in range(1, tables_cnt + 1):
        table = dict()
        
        # 获得表格的caption
        caption = html.xpath(f"//h4[starts-with(text(), '响应参数')]/../div[@class='tablenoborder'][{table_i}]//caption/text()")[0]
        table["caption"] = caption
        
        # 获得表格的head
        head = html.xpath(f"//h4[starts-with(text(), '响应参数')]/../div[@class='tablenoborder'][{table_i}]//thead/tr/th/p/text()")
        table["head"] = head
        
        # 获得表格的参数
        table["para"] = []
        row_cnt = len(html.xpath(f"//h4[starts-with(text(), '响应参数')]/../div[@class='tablenoborder'][{table_i}]//tbody/tr"))
        for row_i in range(1, row_cnt + 1):
            # 获得每一行的参数
            row = html.xpath(f"//h4[starts-with(text(), '响应参数')]/../div[@class='tablenoborder'][{table_i}]//tbody/tr[{row_i}]/td/p/text()")
            
            para_dict = dict()
            for head_k, row_k in zip(head, row):
                para_dict[head_k] = row_k
            table["para"].append(para_dict)
            
        # 加入tables
        tables.append(table)
    
    return tables


def get_json_from_html(html_file="test.html"):
    f = open(html_file, "r", encoding="UTF-8").read()
    html = etree.HTML(f)
    
    res = dict()
    # 功能介绍
    introd = html.xpath("//h4[starts-with(text(), '功能介绍')]/../p/text()")[0]
    res["功能介绍"] = introd
    
    # URI
    uri = html.xpath("//h4[starts-with(text(), 'URI')]/../p/text()")[0]
    res["URI"] = uri
    
    # URI参数
    uri_para = get_uri_para(html_file)
    res["URI参数"] = uri_para
    
    # 请求参数
    req_para = get_req_para(html_file)
    if not req_para:
        req_para = get_req_para2(html_file)
    res["请求参数"] = req_para

    # 请求样例
    req_eg = html.xpath("//h4[starts-with(text(), '请求消息')]/../div[@class='pre-box']//pre/text()")
    if not req_eg:
        req_eg = html.xpath("//h4[starts-with(text(), '请求示例')]/../div[@class='pre-box']//pre/text()")
    res["请求样例"] = req_eg
    
    # 响应参数
    resp_para = get_resp_para(html_file)
    if not resp_para:
        resp_para = get_resp_para2(html_file)
    res["响应参数"] = resp_para
    
    # 响应样例
    resp_eg = html.xpath("//h4[starts-with(text(), '响应消息')]/../div[@class='pre-box']//pre/text()")
    if not resp_eg:
        resp_eg = html.xpath("//h4[starts-with(text(), '响应示例')]/../div[@class='pre-box']//pre/text()")
    res["响应样例"] = resp_eg
    
    # 错误码
    error_code = html.xpath("//h4[starts-with(text(), '错误码')]/../p/text()")[0]
    res["错误码"] = error_code + "错误码"
    
    return res


if __name__ == "__main__":
    res = get_json_from_html()
    json_file = open("ief_apis.json", "w", encoding="UTF-8")
    json_file.write(json.dumps(res, ensure_ascii=False))
    json_file.close()