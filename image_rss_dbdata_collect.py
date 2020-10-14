# test BLE Scanning software
# jcs 6/8/2014
import cv2
import time
import blescan
import sys
import pymysql
import bluetooth._bluetooth as bluez

dev_id = 0
try:
    sock = bluez.hci_open_dev(dev_id)
        #print "ble thread started"

except:
    #print "error accessing bluetooth device..."
        sys.exit(1)

blescan.hci_le_set_scan_parameters(sock)
blescan.hci_enable_le_scan(sock)
uuid1='01aa00ccddeeffaabbccddeeffaabbcc'
uuid2='02aa00ccddeeffaabbccddeeffaabbcc'
uuid3='03aa00ccddeeffaabbccddeeffaabbcc'
uuid4='04aa00ccddeeffaabbccddeeffaabbcc'
uuid5='05aa00ccddeeffaabbccddeeffaabbcc'
cap=cv2.VideoCapture(0)
while True:
    ret, frame=cap.read()
    if ret:
        #frame = cv2.flip(frame,0)
        #frame = cv2.flip(frame,1)
        res=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        dst=cv2.resize(res,(40,40))
        dst_fl=dst.flatten()
        dst_fl1 = str(dst_fl[:800])
        dst_fl2 = str(dst_fl[800:])

        returnedList = blescan.parse_events(sock, 20)
        va1=0
        va2=0
        va3=0
        va4=0
        va5=0
        rss1=0
        rss2=0
        rss3=0
        rss4=0
        rss5=0
        for beacon in returnedList:
            uuid = beacon.split(',')[1]
            rssi = beacon.split(',')[5]
            if uuid == uuid1:
                if va1==0:
                    va1=1;
                    rss1=int(rssi);
                elif va1==1:
                    rss1=rss1*0.5+int(rssi)*0.5
            elif uuid == uuid2:
                if va2==0:
                    va2=1;
                    rss2=int(rssi);
                elif va2==1:
                    rss2=rss2*0.5+int(rssi)*0.5
            elif uuid == uuid3:
                if va3==0:
                    va3=1;
                    rss3=int(rssi);
                elif va3==1:
                    rss3=rss3*0.5+int(rssi)*0.5
            elif uuid == uuid4:
                if va4==0:
                    va4=1;
                    rss4=int(rssi);
                elif va4==1:
                    rss4=rss4*0.5+int(rssi)*0.5
            elif uuid == uuid5:
                if va5==0:
                    va5=1;
                    rss5=int(rssi);
                elif va5==1:
                    rss5=rss5*0.5+int(rssi)*0.5
        if va1==1 and va2==1 and va3==1 and va4==1 and va5==1:
            '''
            con=pymysql.connect(host='192.168.43.44', user='root', password='long', db='db', charset='utf8')
            curs=con.cursor()
            sq1="select replace(img, '\n','') from imagine"
            curs.execute(sq1)
            result=str(curs.fetchall())
            con.commit()
            con.close()
            '''
            print "success"
            conn = pymysql.connect(host='localhost', user='root', password='long', db='db', charset='utf8')
            curs = conn.cursor()
            sql1="delete from imagine"
            curs.execute(sql1)
            sql2="insert into imagine(img) values(%s)"
            curs.execute(sql2, dst_fl1+dst_fl2)

            sql4="delete from rss"
            curs.execute(sql4)
            sql3 = """insert into rss(rss1, rss2, rss3, rss4, rss5) values (%s, %s, %s, %s, %s)"""
            curs.execute(sql3, (rss1, rss2, rss3, rss4, rss5))
            conn.commit()
            conn.close()
            time.sleep(1)
