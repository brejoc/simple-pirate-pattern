#!/usr/bin/env python

#
#  Lazy Pirate client
#  Use zmq_poll to do a safe request-reply
#  To run, start lpserver and then randomly kill/restart it
#

from __future__ import print_function

import zmq

from time import sleep

REQUEST_TIMEOUT = 2500
SERVER_ENDPOINT = "tcp://localhost:5555"

context = zmq.Context(1)

print("I: Connecting to server...")
client = context.socket(zmq.REQ)
client.connect(SERVER_ENDPOINT)

poll = zmq.Poller()
poll.register(client, zmq.POLLIN)

sequence = 0
while True:
    sequence += 1
    request = str(sequence).encode()
    print("I: Sending (%s)" % request)
    client.send(request)

    expect_reply = True
    while expect_reply:
        socks = dict(poll.poll(REQUEST_TIMEOUT))
        if socks.get(client) == zmq.POLLIN:
            reply = client.recv()
            if not reply:
                break
            if int(reply) == sequence:
                print("I: Server replied OK (%s)" % reply)
                expect_reply = False
            else:
                print("E: Malformed reply from server: %s" % reply)

        else:
            print("W: No response from server, retrying...")
            # Socket is confused. Close and remove it.
            client.setsockopt(zmq.LINGER, 0)
            client.close()
            poll.unregister(client)
            print("I: Reconnecting and resending (%s)" % request)
            # Create new connection
            client = context.socket(zmq.REQ)
            client.connect(SERVER_ENDPOINT)
            poll.register(client, zmq.POLLIN)
            client.send(request)

context.term()
