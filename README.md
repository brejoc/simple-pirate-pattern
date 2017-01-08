# The Simple Pirate Pattern

A slightly modified demo of the Basic Reliable Queuing (Simple Pirate Pattern) with [ZeroMQ](http://zeromq.org/). See [Chapter Four](http://zguide.zeromq.org/py:chapter4) of the [zguide](http://zguide.zeromq.org/).

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
