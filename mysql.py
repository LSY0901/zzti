# -*- coding:utf-8 -*-
"""
----------------------------------------------
  File Name:   testmysql
  Description: 
  Author:       Mr.Liu
  date:         2018/8/25
-----------------------------------------------
   Change Activity:
                2018/8/25:
-----------------------------------------------
"""
_author_ = 'Mr.Liu'
import pymysql

if __name__ == '__main__':
    try:
            con = pymysql.connect(host='127.0.0.1', user='root',
                                  password='', db='zzti', port=3306)
            cursor = con.cursor()

            sql = 'insert into zyglist (title,dateinfo) VALUES (%s,%s)'
            cursor.execute(sql, ('awsedfg', '2018-08-26'))
            con.commit()

            cursor.close()
            con.close()
            print('操作成功')
    except BaseException as e:
        print('异常：', e)
