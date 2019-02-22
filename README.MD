# PyAsynch

PyAsynch is a package to create distributed Python Services through RabbitMQ.

The services talk each other through a common RabbitMQ queue and expose the service also as HTTP Tornado Server

## How to use it

```
pip install pyasynch
```
or 
```
pip3 install pyasynch
```

or just clone the git repo.

Create your custom node
```

from pyasynch.node import Node

class MyNode(Node):

    def mymethod(self,arg1,arg2,**kwargs):
        return {'myproperty':'myvalue'}
        
    def mysecondmethod(self,myproperty,**kwargs):
        return {}   

```

Create the configuration file (e.g. myconfig.json)

```
{
  "endpoint": {
    "amqp": "amqp://guest:guest@127.0.0.1:5672/pyasynch",
    "id": "myendpoint",
    "threaded": false
  }
}
```

Create the routing file (e.g. myroutes.json)

```
{
 "routes": {
    "pyasynch://myendpoint/mynode/mymethod" : ["pyasynch://myendpoint/mynode/mysecondmethod"],
}    
```

Create the main (e.g. main.py) runner and register the node

```
# IMPORTS
from pyasynch.environment import Environment

env = Environment()
env.register_node('mynode',MyNode(env.endpoint))

try:
    env.run()
except KeyboardInterrupt:
    env.stop()

```

Everything is ready, now you can run the endpoint service (check if RabbitMQ is running properly)

python3 main.py -c myconfig.json -r myroutes.json -p 8081

You can replicate nodes and endpoint logic in a scalable way.
