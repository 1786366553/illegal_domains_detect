# -*- coding: utf-8 -*-

from settings import DB
import MySQLdb as mdb

class DBOperate():

    @staticmethod
    def get_mysql_connect():

        conn = mdb.connect(
            host=DB['host'],
            user=DB['user'],
            passwd=DB['passwd'],
            port=DB['port'],
            db=DB['db'],
            charset=DB['charset']
        )
        cur = conn.cursor()

        return conn, cur

    @staticmethod
    def load_data(sql):

        conn, cur = DBOperate.get_mysql_connect()
        try:
            cur.execute(sql)
        except Exception:
            return []
        else:
            res = cur.fetchall()

        cur.close()
        conn.close()

        return res

    @staticmethod
    def replace_result(result_dict,table_name,conn,cur):
        keys,values = result_dict.keys(),tuple(result_dict.values())
        replace_sql = "replace into " + table_name + "(" + ','.join(keys) + ")values(" + ','.join(
            ['%s' for _ in range(len(keys))]) + ")"
        try:
            cur.execute(replace_sql, values)
        except Exception, e:
            print "replace error:", e
            conn.rollback()

        return conn,cur

    @staticmethod
    def close_connect(conn,cur):

        cur.close()
        conn.close()