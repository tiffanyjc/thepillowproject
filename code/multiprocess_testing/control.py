import csv
import time
import sys
import os
import signal
from cmd import Cmd
import write_forever as wf
from multiprocessing import Process

mya = 1
myprocess = None

def do_printa():
    global mya
    mya = 2
    print(mya)

def do_increa():
    global mya
    mya = mya + 1
    print(mya)

def do_quit():
    print("Quitting.")
    raise SystemExit

def do_wf():
    global myprocess
    myprocess = Process(target=wf.writeToCSV)
    myprocess.start()
    print("process started")

def do_kill():
    global myprocess
    if myprocess != None:
        pid = myprocess.pid
        os.kill(pid, signal.CTRL_BREAK_EVENT)
        print("process terminated")
    else:
        print("process is null")

def repl():
    while True:
        raw_input = input("Prompt>")
        if raw_input == 'hello':
            print("hello")
        elif raw_input == 'nihao':
            print("nihao")
        elif raw_input == 'printa':
            do_printa()
        elif raw_input == 'increa':
            do_increa()
        elif raw_input == 'wf':
            do_wf()
        elif raw_input == 'kill':
            do_kill()
        elif raw_input == 'quit':
            do_quit()
        else:
            print("Error")

if __name__ == '__main__':
    repl()
