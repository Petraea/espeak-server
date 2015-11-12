from string import ascii_lowercase, digits
ALLOWCHARS=ascii_lowercase+digits+'-+'
import subprocess
from twisted.internet import reactor, protocol

class Serve(protocol.Protocol):
    def dataReceived(self, data):
        voice='en'
        kaps='20'
        spd='150'
        pitch='60'
        amp='10'
        bits=data.strip().split(';')
        try:
            words=bits.pop()
            voice=''.join(x for x in (bits.pop(0) or voice) if x in ALLOWCHARS)
            spd=str(min(max(int(bits.pop(0) or spd),0),400))
            pitch=str(min(max(int(bits.pop(0) or pitch),0),99))
            amp=str(min(max(int(bits.pop(0) or amp),0),20))
            kaps=str(min(max(int(bits.pop(0) or kaps),0),99))
        except Exception as e:
            print (e)
        s = subprocess.Popen(['espeak','--stdin','-v'+voice,'-k'+kaps,'-s'+spd,'-p'+pitch,'-a'+amp],stdin=subprocess.PIPE,stderr=subprocess.PIPE)
        s.communicate(words)
def main():
    factory = protocol.ServerFactory()
    factory.protocol = Serve
    reactor.listenTCP(16016,factory)
    reactor.run()

if __name__ == '__main__':
    main()
