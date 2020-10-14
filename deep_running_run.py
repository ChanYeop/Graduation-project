import numpy as np
import tensorflow as tf
import random
import pymysql
import time
import serial
port="/dev/ttyUSB0"
serialFromArduino = serial.Serial(port, 9600)
serialFromArduino.flushInput()

locax=[0,8.25,8.25,6.75,6.75,5.25,5.25,3.75,3.75,2.25,2.25,0.75,0.75,0.75,2.25,0.75,2.25,0.75,2.25,0.75,2.25]
locay=[0,0.75,2.25,0.75,2.25,0.75,2.25,0.75,2.25,0.75,2.25,0.75,2.25,3.75,3.75,5.25,5.25,6.75,6.75,8.25,8.25]
def MinMaxScaler(data):
    numerator = data + 100
    denominator = 80
    # noise term prevents the zero division
    return numerator / (denominator + 1e-5)

def MinMaxScaler2(data):
    numerator = data
    denominator = 255
    # noise term prevents the zero division
    return numerator / (denominator + 1e-5)

inputs_A = tf.keras.Input(shape=(40,40,1))
inputs_B = tf.keras.Input(shape=[5])

layer1 = tf.keras.layers.Conv2D(kernel_size=(4,4),padding='SAME', filters=8)(inputs_A)
layer2 = tf.keras.layers.MaxPool2D(pool_size=(2,2), strides=(2,2))(layer1)
layer3 = tf.keras.layers.Conv2D(kernel_size=(4,4),padding='SAME', filters=16)(layer2)
layer4 = tf.keras.layers.MaxPool2D(pool_size=(2,2), strides=(2,2))(layer3)
layer5 = tf.keras.layers.Flatten()(layer4)
layer6 = tf.keras.layers.Dense(units=10, activation="selu", kernel_initializer="lecun_normal")(layer5)
layer7 = tf.keras.layers.concatenate([layer6, inputs_B])
layer8 = tf.keras.layers.Dense(15, activation="selu", kernel_initializer="lecun_normal")(layer7)
layer9 = tf.keras.layers.Dense(12, activation="selu", kernel_initializer="lecun_normal")(layer8)
layer10 = tf.keras.layers.Dense(9, activation="selu", kernel_initializer="lecun_normal")(layer9)
layer11 = tf.keras.layers.Dense(6, activation="selu", kernel_initializer="lecun_normal")(layer10)
layer12 = tf.keras.layers.Dense(4, activation="selu", kernel_initializer="lecun_normal")(layer11)
outputs = tf.keras.layers.Dense(2, activation=tf.identity)(layer12)
model = tf.keras.Model(inputs=[inputs_A, inputs_B], outputs=outputs)
model.compile(optimizer=tf.keras.optimizers.Adam(lr=0.001, beta_1=0.9, beta_2=0.999), loss='mse')
#model.compile(optimizer=tf.keras.optimizers.SGD(lr=0.001, momentum=0.9, nesterov=True), loss='mse')

#model.load_weights('./0615_weight_basic/my_model')
model.load_weights('./0627_weight2/my_model')

print("end")
print("insert : ")

loca=int(input())
chacha=0
final_v=1
final_count=0

while True:
    """
    conn = pymysql.connect(host='192.168.43.78', port=3306, user='root', password='long', db='db', charset='utf8')
    cur=conn.cursor()
    sql = 'select * from rss'
    cur.execute(sql)
    rss_rows=cur.fetchall()
    rss=list(rss_rows)

    
    sql2= "select replace(img, '\n', '')  from imagine"
    cur.execute(sql2)
#conn.commit()
    image_rows=cur.fetchall()
    ima=str(image_rows)
    #print(ima)
    imag=[]
    s="1"
    for i in ima:
        if(i=='u' or i=='"' or i=='(' or i==")" or i=='\n' or i=='[' or i==']' or i==',' or i==' ' or i=="'"):
            if s!="":
                imag.append(int(s))
                s=""
        else:
            s=s+i
    
    conn.commit()
    conn.close()

    vaxyz = (elem for elem in rss)
    vaxy = list(vaxyz)
    vaa=np.array(vaxy)
    print(vaa)
    vaxyz2 = (elem2 for elem2 in imag)
    vaxy2 = list(vaxyz2)
    vab=np.array(vaxy2)

    aaaa = MinMaxScaler(vaa)
    bbbb = vaa[0,-4:]
    cccc = MinMaxScaler2(vab[1:])

    #aaaa = vaa
    #bbbb = vaa[0,-4:]
    #cccc = vab[1:]
    
    x_now=aaaa
    y_now=bbbb
    c_now=cccc

    xx_now=x_now.reshape(1,5,order='C')
    yy_now=y_now.reshape(1,4,order='C')
    cc_now=tf.reshape(c_now,[-1,40,40,1])

    loca_now=loca_now=model.predict((cc_now, xx_now),steps=1)
    #print(loca_now)
    vax=loca_now[0][0]
    vay=loca_now[0][1]
    #vaz=loca_now[0][2]
    #vava=loca_now[0][3]
    vamin=99999
    va=0
    
    for i in range(1,21):
        vavamin=((vax-locax[i])**2+(vay-locay[i])**2)**0.5
        if(vamin>vavamin):
            vamin=vavamin
            va=i


    if(va>loca-2 and va<loca+2):
        print("finish!!")
        serialFromArduino.write(b"d")
        break
    elif(va<loca):
        #print(va)
        if(va>10):
            serialFromArduino.write(b"a")
            time.sleep(1.4)
            print("a")
        elif(va<7):
            serialFromArduino.write(b"a")
            time.sleep(1.4)
            print("a")
        else:
            serialFromArduino.write(b"c")
            print("c")
            time.sleep(1)
            #serialFromArduino.write(b"a")
            #print("c")    
