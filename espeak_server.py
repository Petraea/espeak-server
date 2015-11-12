from string import ascii_lowercase, digits
import subprocess
from twisted.internet import reactor, protocol

class Serve(protocol.Protocol):
    def dataReceived(self, data):
        bits=data.strip.split(';')
        words = bits.pop(-1)
        
        s = subprocess.Popen(['espeak','--stdin','-vnl+f4','-k20','-s150','-p60'],stdin=subprocess.PIPE)
        s.communicate(words)
def main():
    factory = protocol.ServerFactory()
    factory.protocol = Echo
    reactor.listenTCP(16016,factory)
    reactor.run()

if __name__ == '__main__':
    main()
