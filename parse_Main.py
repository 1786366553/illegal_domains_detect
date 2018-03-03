# -*- coding: utf-8 -*-

from detect_tool.detect_tools import detect_tools
from Write_Read import start_process
from DB_Operate import DBOperate

def parse_tool(tool):
    if len(str(tool)) == 1:
        no = int(tool)
        if no == 1:
            tool_name = "sanliuling"
        elif no == 2:
            tool_name = "jinshan"
        elif no == 3:
            tool_name = "tencentmanager"
        elif no == 4:
            tool_name = "baidudefender"
        elif no == 5:
            tool_name = "macfree"
        elif no == 6:
            tool_name = "virustotal"
        else:
            print "无此工具"
            print "+------------------------------------+"
            print "| detect tools selection:1/2/3/4/5/6 |"
            print "| tool-1 =>  sanliuling              |"
            print "| tool-2 =>  jinshan                 |"
            print "| tool-3 =>  tencentmanager          |"
            print "| tool-4 =>  baidudefender           |"
            print "| tool-5 =>  macfree                 |"
            print "| tool-6 =>  virustotal              |"
            print "+------------------------------------+"
            return None
    else:
        tool_name = tool
    if tool_name.strip().lower() == "sanliuling":
        source_class = detect_tools.Sanliuling
    elif tool_name == "jinshan":
        source_class = detect_tools.Jinshan
    elif tool_name == "tencent":
        source_class = detect_tools.TencentManager
    elif tool_name == "baidu":
        source_class = detect_tools.BaiduDefender
    elif tool_name == "macfree":
        source_class = detect_tools.Macfree
    elif tool_name == "virustotal":
        source_class = detect_tools.Virustotal
    else:
        print "无此工具"
        print "+------------------------------------+"
        print "| detect tools selection:1/2/3/4/5/6 |"
        print "| tool-1 =>  sanliuling              |"
        print "| tool-2 =>  jinshan                 |"
        print "| tool-3 =>  tencentmanager          |"
        print "| tool-4 =>  baidudefender           |"
        print "| tool-5 =>  macfree                 |"
        print "| tool-6 =>  virustotal              |"
        print "+------------------------------------+"
        return None

    return tool_name,source_class


def main(start_index,total,tool_name, source_class,process_num):
    process_num = int(process_num)
    sql = "select domain from "+tool_name+" where "+tool_name+"_result is NULL limit "+str(start_index)+","+str(total)
    res = DBOperate.load_data(sql)
    domains = [rs[0] for rs in res]
    print "load %d records"%len(domains)
    if len(domains)!=0:
        read_paras = (domains,source_class)
        write_paras = (tool_name,)
        start_process(read_paras,write_paras,process_num)


if __name__ == "__main__":
    from command_parse import command_parse
    import sys
    start_index,total,tool,process_num = command_parse(sys.argv)
    res = parse_tool(tool)

    if res is not None:
        tool_name, source_class = res
        main(start_index, total,tool_name, source_class,process_num)