# The Simple Pirate Pattern

A slightly modified demo of the Basic Reliable Queuing (Simple Pirate Pattern) with [ZeroMQ](http://zeromq.org/). See [Chapter Four](http://zguide.zeromq.org/py:chapter4) of the [zguide](http://zguide.zeromq.org/).

The Simple Pirate Pattern allows you to connect multiple clients and workers in a very simple but reliable request-reply fashion.

<pre>
+--------------+   +--------------+   +--------------+
|              |   |              |   |              |
|    client    |   |    client    |   |    client    |
|              |   |              |   |              |
+------+-------+   +------+-------+   +--------+-----+
       |                  |                    |
       +---------------------------------------+
                          |
                          |
                   +------+-------+
                   |              |
                   |     queue    |
                   |              |
                   +------+-------+
                          |
                          |
       +------------------+--------------------+
       |                                       |
+------+-------+   +--------------+   +--------+-----+
|              |   |              |   |              |
|    worker    |   |    worker    |   |    worker    |
|              |   |              |   |              |
+--------------+   +--------------+   +--------------+
</pre>

You can add or remove clients and workers as you like. If a client won't receive a reply from a worker, the client will retry its request until there is a response.


# Getting Started

I would strongly recommend to use [Virtual Environments](http://docs.python-guide.org/en/latest/dev/virtualenvs/).

## Installation

1. Creating a virtualenv: `virtualenv env`
2. Activate virtualenv: `. env/bin/activate`
3. Install dependencies: `pip install -r requirements.txt`

## Usage

You'll need at least three terminals with an activated virtualenv.

1. Start the queue: `python queue.py`
2. Start the worker: `python worker.py`
3. Start the client: `python client.py`
4. Start hacking and have fun! ;)
