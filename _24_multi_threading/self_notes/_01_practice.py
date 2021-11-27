# Multithreading in Python

"""This article covers the basics of multithreading in Python programming language. Just
like multiprocessing, multithreading is a way of achieving multitasking. In
multithreading, the concept of threads is used.
Let us first understand the concept of thread in computer architecture.
"""

"""In computing, a process is an instance of a computer program that is being executed.
Any process has 3 basic components: 
An executable program.
The associated data needed by the program (variables, work space, buffers, etc.)
The execution context of the program (State of process)
"""

"""A thread is an entity within a process that can be scheduled for execution. Also, it is the
smallest unit of processing that can be performed in an OS (Operating System).
In simple words, a thread is a sequence of such instructions within a program that can
be executed independently of other code. For simplicity, you can assume that a thread
is simply a subset of a process!

A thread contains all this information in a Thread Control Block (TCB):

Thread Identifier: Unique id (TID) is assigned to every new thread

Stack pointer: Points to thread’s stack in the process. Stack contains the local
variables under thread’s scope.

Program counter: a register which stores the address of the instruction currently
being executed by thread.

Thread state: can be running, ready, waiting, start or done.
Thread’s register set: registers assigned to thread for computations.

Parent process Pointer: A pointer to the Process control block (PCB) of the
process that the thread lives on.
Consider the diagram below to understand the relation between process and its

thread:
Multithreading
Multiple threads can exist within one process where:"""

import threading

print("current thread:", threading.current_thread().getName())

if threading.current_thread() == threading.main_thread():
    print("The current thread is the main thread")
else:
    print("The current thread is not main thread")

name = threading.current_thread().getName()
print(name)


# 2. creating a thread and ue it to run

from threading import *

def movie():
    print("Movie running successfully in Theatres")

for i in range(5):
    m = Thread(target=movie())
    m.start()

# creating thread without using a class
from threading import *


def display(str):
    print(str)


for i in range(5):
    t = Thread(target=display('hello'), args='hello')
    t.start()

# Class Mythread(thread):
# t1 = mythread
# t1.join

# python program to create a thread by making our class as sub class to thread class

from threading import Thread


class Mythread(Thread):
    def run(self):
        for i in range(1, 6):
            print(i)

t1 = Mythread()
t1.start()
t1.join()


# program to create thread tha access the instance variables

'''


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age


    def get_details(self):
        print("get details:", self.name, self.age)

s = Student('raja', 26)
s2 = Student("super", 26)
s2.get_details()
s.get_details()
'''
from threading import *
from time import *
class Mythread:

    def prepareTea(self):
        self.task1()
        self.task2()
        self.task3()

    def task1(self):
        print("Boil milk and tea powder and wait for 5 minutes")
        sleep(5)
        print("done")

    def task2(self):
        print("Add sugar and wait for 3 minutes")
        sleep(3)
        print("done")
    def task3(self):
        print("filter it serve it === end")
        print("done")

obj = Mythread()
t = Thread(target=obj.prepareTea())

t.start()








