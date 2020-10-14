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
        print(dst_fl)
        conn = pymysql.connect(host='localhost', user="root", password='long', db='db', charset='utf8')
        curs=conn.cursor()
        sql="delete from imagine"
        curs.execute(sql)
        sql2="insert into imagine(img) values (%s)"
        curs.execute(sql2, (dst_fl))
        conn.commit()
        conn.close()
    time.sleep(10)

cap.rlelase()
cv2.destroyAllWindows()
