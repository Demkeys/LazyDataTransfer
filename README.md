# LazyDataTransfer
Lazy script to send/recv upto 64kb of data over the network using UDP. This is script doesn't have any validation logic so make sure you are providing the arguments properly, otherwise the behaviour is undefined. This is a very lazy method and should only be used if you're ok with UDP's unreliability. And it's mainly meant for small pieces of data.

In 'send' mode ip address must be address of target machine. In 'recv' mode the ip address must be address of host machine.

## Usage:
* Arg 1: mode (send/recv)
* Arg 2: file name
* Arg 3: address (ip address:port)

## Example: 
```python data_transfer.py send text01.txt 192.168.8.103:9510```
