# -*- coding: utf-8 -*-
"""
功能：第三方工具检测恶意域名服务器端
作者：吴晓宝
日期:2018-2-5
"""

from socket import socket,AF_INET, SOCK_STREAM
from detect_tools import detect_tools
import sys,getopt
reload(sys)
sys.setdefaultencoding('utf8')

def command_parse(argvs):
    tool_name= ''
    run_name = argvs[0]
    argv = argvs[1:]
    usage_tip = 'usage: '+run_name+' -t <tool_name>'
    try:
        opts, args = getopt.getopt(argv,"h:t:",["help","tool_name="])
    except getopt.GetoptError:
        print 'GetoptError,' + usage_tip
        print "+------------------------------------+"
        print "| detect tools selection:1/2/3/4/5/6 |"
        print "| tool-1 =>  sanliuling              |"
        print "| tool-2 =>  jinshan                 |"
        print "| tool-3 =>  tencentmanager          |"
        print "| tool-4 =>  baidudefender           |"
        print "| tool-5 =>  macfree                 |"
        print "| tool-6 =>  virustotal              |"
        print "+------------------------------------+"
        sys.exit(2)
    for opt, arg in opts:
        if opt in ('-h','--help'):
            print "+------------------------------------+"
            print "| detect tools selection:1/2/3/4/5/6 |"
            print "| tool-1 =>  sanliuling              |"
            print "| tool-2 =>  jinshan                 |"
            print "| tool-3 =>  tencentmanager          |"
            print "| tool-4 =>  baidudefender           |"
            print "| tool-5 =>  macfree                 |"
            print "| tool-6 =>  virustotal              |"
            print "+------------------------------------+"
            print usage_tip
            sys.exit()
        elif opt in ("-t","--tool_name"):
            tool_name = arg

    return tool_name

if __name__ == "__main__":
    tool_name = command_parse(sys.argv)
    if tool_name in ["sanliuling", "1"]:
        source_class = detect_tools.Sanliuling
        tool_name = "sanliuling"
    elif tool_name in ["jinshan", "2"]:
        source_class = detect_tools.Jinshan
        tool_name = "jinshan"
    elif tool_name in ["tencentmanager", "3"]:
        source_class = detect_tools.TencentManager
        tool_name = "tencentmanager"
    elif tool_name in ["baidudefender", "4"]:
        source_class = detect_tools.BaiduDefender
        tool_name = "baidudefender"
    elif tool_name in ["macfree", "5"]:
        source_class = detect_tools.Macfree
        tool_name = "macfree"
    elif tool_name in ["virustotal", "6"]:
        source_class = detect_tools.Virustotal
        tool_name = "virustotal"
    else:
        sys.exit(-1)
    print "[1]正在开启工具%s检测域名恶意性的服务器端..."%tool_name
    client_ip = '127.0.0.1'
    port = 10000
    server = socket(AF_INET, SOCK_STREAM)
    addr = (client_ip, port)
    server.bind(addr)
    server.listen(1)  # 每次等待处理一个连接
    print "服务器已开启"
    print "[2]建立与检测工具的连接..."
    if tool_name not in ["macfree", "virustotal"]:
        if tool_name == "baidu":
            dv = source_class.driver_homeweb()
        else:
            dv = source_class.driver_homeweb('qq.com')
    print "连接建立成功"
    count = 0
    while True:
        count+=1
        print "[%d]正在建立与客户端的连接..."%count
        client, addr_client = server.accept()
        print "已与客户端建立TCP连接"
        domain = client.recv(2048)
        print "[%d]正在检测域名%s的恶意性，请稍等..." % (count,domain)
        if tool_name not in ["macfree", "virustotal"]:
            dv, result = source_class.detect_malicious(domain, dv)
        else:
            result = source_class.detect_malicious(domain)
        print "[%d]检测结果为>>%s" % (count,result)
        client.sendall(result)
        client.close()