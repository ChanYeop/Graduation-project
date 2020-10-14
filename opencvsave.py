import cv2
import time
import pymysql

cap = cv2.VideoCapture(0)

while True:
    ret, frame=cap.read()

    if ret:
        res=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        dst = cv2.resize(res,(20,40))
        dst_fl=str(dst.flatten())

        conn = pymysql.connect(host='192.168.43.220',user='root', password='long', db='db', charset='utf8')
        curs=conn.cursor()
        sq1 = "select replace(img, '\r\n','') from imagine"
        curs.execute(sq1)
        result = str(curs.fetchall())
        print(result[0])
        im = []
        '''
        for i in result:
            if(i=='\n'):
                continue
            else:
                im.append(i)
        print(im)
        '''

        conn.close()
        conn = pymysql.connect(host='localhost',user='root',password='long', db='db', charset='utf8')
        curs=conn.cursor()
        sql="delete from imagine"
        curs.execute(sql)
        sql2="insert into imagine(img) values (%s)"
        curs.execute(sql2, (result+dst_fl))
        conn.commit()
        conn.close()
    time.sleep(10)
