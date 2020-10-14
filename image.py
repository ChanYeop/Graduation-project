import cv2
import csv

arr1=[]
arr12=[]
j=1
k=1
c=1
for i in range(1,601):
    arr1.append('0619/'+str(j)+'_'+str(k)+'.jpg')
    k=k+1
    if(k%4 == 0):
        c=c+1
        k=1
    if(c%11==0):
        c=1
        k=1
        j=j+1
'''
j=1
k=0
for i in range(1,1081):
    arr1.append('0526/'+str(j)+'.'+str(k)+'.jpg')
    k=k+1
    if(k%30==0):
        k=0
        j=j+1
j=1
k=0
for i in range(1,1081):
    arr1.append('0410/'+str(j)+'.'+str(k)+'.jpg')
    k=k+1
    if(k%30==0):
        k=0
        j=j+1
j=1
k=0
for i in range(1,1081):
    arr1.append('0410/'+str(j)+'.'+str(k)+'.jpg')
    k=k+1
    if(k%30==0):
        k=0
        j=j+1
j=1
k=0
for i in range(1,1081):
    arr1.append('0410/'+str(j)+'.'+str(k)+'.jpg')
    k=k+1
    if(k%30==0):
        k=0
        j=j+1
j=1
k=0
for i in range(1,1081):
    arr12.append('0410/'+str(j)+'.'+str(k)+'.jpg')
    k=k+1
    if(k%30==0):
        k=0
        j=j+1
        
arr2=[]
arr22=[]
j=1
k=1
c=1
for i in range(1,601):
    arr2.append('06071/'+str(j)+'_'+str(k)+'.jpg')
    k=k+1
    if(k%4==0):
        c=c+1
        k=1
    if(c%11==0):
        c=1
        k=1
        j=j+1
        '''
'''
j=1
k=0
for i in range(1,1081):
    arr2.append('04101/'+str(j)+'.'+str(k)+'.jpg')
    k=k+1
    if(k%30==0):
        k=0
        j=j+1
j=1
k=0
for i in range(1,1081):
    arr2.append('04101/'+str(j)+'.'+str(k)+'.jpg')
    k=k+1
    if(k%30==0):
        k=0
        j=j+1
j=1
k=0
for i in range(1,1081):
    arr2.append('04101/'+str(j)+'.'+str(k)+'.jpg')
    k=k+1
    if(k%30==0):
        k=0
        j=j+1
j=1
k=0
for i in range(1,1081):
    arr2.append('04101/'+str(j)+'.'+str(k)+'.jpg')
    k=k+1
    if(k%30==0):
        k=0
        j=j+1
j=1
k=0
for i in range(1,1081):
    arr22.append('04101/'+str(j)+'.'+str(k)+'.jpg')
    k=k+1
    if(k%30==0):
        k=0
        j=j+1
'''
img=[]
i=0

'''
data = cv2.imread('final_project/'+arr1[2], cv2.IMREAD_COLOR)
res = cv2.cvtColor(data, cv2.COLOR_BGR2GRAY)
dst = cv2.resize(res, (40, 40))
cv2.imshow('ima',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''


for index,value in enumerate(arr1):
    data = cv2.imread('final_project/'+arr1[index], cv2.IMREAD_COLOR)
    res = cv2.cvtColor(data, cv2.COLOR_BGR2GRAY)
    dst = cv2.resize(res, (40, 40))
    dst_fl = list(dst.flatten())
    img.append(dst_fl)
    '''
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    '''
'''
img2 = []
for index2,value2 in enumerate(arr2):
    data2 = cv2.imread('final_project/'+arr2[index2], cv2.IMREAD_COLOR)
    res2 = cv2.cvtColor(data2, cv2.COLOR_BGR2GRAY)
    dst2 = cv2.resize(res2, (20, 40))
    dst_fl2 = list(dst2.flatten())
    img2.append(dst_fl2)

'''
f=open('test0619.csv','w', encoding='utf-8', newline="")
wr=csv.writer(f)

for i,v in enumerate(img):
    wr.writerow(img[i])

f.close()
