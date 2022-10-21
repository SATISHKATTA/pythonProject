'''
find the sum of all the list elements
input : list
'''
'''list1 = [45,67,23,67,23,56,32]
sum = 0
for i in list1:
    sum += i
print('list1 = ', list1)
print('Sum of all List elements = ', sum)'''

from threading import *
import time
def welcome():
    time.sleep(1)
    for i in range(4):
        print('sasikanth')

def melcow():
    time.sleep(1)
    for i in range(4):
        print('bhavya')

initial=time.time()
ob1=Thread(target=welcome)
ob2=Thread(target=melcow)
ob1.start()
time.sleep(0.2)
ob2.start()
ob1.join()

ob2.join()
print(f'time out:{round(time.time()-initial)}')









