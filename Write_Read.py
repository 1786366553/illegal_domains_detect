# -*- coding: utf-8 -*-

import time
from DB_Operate import DBOperate
from multiprocessing import Process,Queue,cpu_count,active_children
import sys
reload(sys)
sys.setdefaultencoding('utf8')

def write_data(q,table_name):

    print "===================start:store data===================="
    item = ''
    conn,cur = DBOperate.get_mysql_connect()
    count = 0
    while item!='quit':
        while not q.empty():
            item = q.get()
            if item!='quit':
                conn,cur = DBOperate.replace_result(item,table_name,conn,cur)
                count+=1
                if count%5==0:
                    print "commited %d records"%count
                    conn.commit()
            else:
                break
        time.sleep(10)
    conn.commit()
    DBOperate.close_connect(conn,cur)
    print "===================end:store data===================="

def read_data(i,q,items,source_class):

    print "===================process id %d=>%s:start====================" % (i,source_class.__name__)
    source_class.detect_domains(q,items)
    print "===================process id %d=>%s:end====================" % (i,source_class.__name__)

def start_process(read_paras,write_paras,process_num):

    print "=========================start=============================="
    process = []
    q = Queue()
    for i in range(1, process_num + 1):
        process.append(Process(target=read_data, args=(i,q)+read_paras))
    process.append(Process(target=write_data, args=(q,) + write_paras))
    for p in process:
        p.start()

    print("The number of CPU is:" + str(cpu_count()))
    for p in active_children():
        print("child   p.name:" + p.name + "\tp.id" + str(p.pid))
    print "===========================over============================="