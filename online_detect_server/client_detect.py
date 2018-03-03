# -*- coding: utf-8 -*-
"""
功能：第三方工具检测恶意域名客户端
作者：吴晓宝
日期:2018-2-5
"""

from socket import socket,AF_INET, SOCK_STREAM,error
import sys
reload(sys)
sys.setdefaultencoding('utf8')

def get_detect_result(domain,server_ip,port):

    try:
        client = socket(AF_INET, SOCK_STREAM)
    except error, e:
        print e
        return "连接异常"
    else:
        addr = (server_ip, port)
        try:
            client.connect(addr)
        except error, e:
            print e
            return "连接异常"
        else:
            result = ''
            while True:
                try:
                    client.sendall(domain)
                    buf = client.recv(2048)
                    result += buf
                except error, e:
                    print e
                    return "连接异常"
                else:
                    if not buf:
                        break
        client.close()
    return result

if __name__ == "__main__":
    server_ip, port = '127.0.0.1',10000
    while True:
        domain = raw_input("输入域名/quit>>")
        if domain == "quit":
            print "检测测试结束"
            break
        else:
            print "开始测试检测..."
            result = get_detect_result(domain, server_ip, port)
            print "检测结果为%s"%result