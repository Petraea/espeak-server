
# Copyright (c) Twisted Matrix Laboratories.
# See LICENSE for details.

import subprocess

from twisted.internet import reactor, protocol


class Echo(protocol.Protocol):
    """This is just about the simplest possible protocol"""
    
    def dataReceived(self, data):
        "As soon as any data is received, write it back."
        s = subprocess.Popen(['espeak','--stdin','-vnl+f4','-k20','-s150','-p60'],stdin=subprocess.PIPE)
        s.communicate(data.strip())

def main():
    """This runs the protocol on port 8000"""
    factory = protocol.ServerFactory()
    factory.protocol = Echo
    reactor.listenTCP(16016,factory)
    reactor.run()

# this only runs if the module was *not* imported
if __name__ == '__main__':
    main()
