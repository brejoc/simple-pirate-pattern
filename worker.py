#!/usr/bin/env python

#
#  Simple Pirate worker
#  Connects REQ socket to tcp://*:5556
#  Implements worker part of LRU queueing
#

from random import randint
import time
import zmq

LRU_READY = "\x01"

context = zmq.Context(1)
worker = context.socket(zmq.REQ)

identity = "%04X-%04X" % (randint(0, 0x10000), randint(0, 0x10000))
worker.setsockopt(zmq.IDENTITY, identity)
worker.connect("tcp://localhost:5556")

print("I: (%s) worker ready" % identity)
worker.send(LRU_READY)

cycles = 0
while True:
    msg = worker.recv_multipart()
    if not msg:
        print("I: (%s) no response. Stopping!!!" % identity)
        break
    print("I: (%s) normal reply" % identity)
    time.sleep(1) # Do some heavy work
    worker.send_multipart(msg)
