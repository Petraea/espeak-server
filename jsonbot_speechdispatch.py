# jsb/plugs/myplugs/speechnew.py
#
#
# New !speak implementation by The_Niz for remote festival

#jsb imports
from jsb.lib.examples import examples
from jsb.lib.commands import cmnds
from jsb.lib.persist import PlugPersist

user_settings = PlugPersist('espeak_setting')

#basic imports
import socket
import random
import logging

#host and port of speech (proxy) server
HOST = 'vinculum'
PORT = 16016

#defs
def conn_send(line):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    s.sendall(line+'\n')
    s.close()

def generate_settings(nick):
    voice=random.choice(['en+m3','en+m2','en+m1','en+','en+f1','en+f2','en+f3'])
    pitch=str(random.randint(0,99))
    speed=str(random.randint(100,300))
    if any(user_settings.data[x]['voice']==voice for x in user_settings.data) and any(user_settings.data[x]['pitch']==pitch for x in user_settings.data) and any(user_settings.data[x]['speed']==speed for x in user_settings.data):
        voice=random.choice(['en+m3','en+m2','en+m1','en+','en+f1','en+f2','en+f3'])
        pitch=str(random.randint(0,99))
        speed=str(random.randint(100,300))
    if nick not in user_settings.data:
        user_settings.data[nick]={}
    user_settings.data[nick]['voice']=voice
    user_settings.data[nick]['pitch']=pitch
    user_settings.data[nick]['speed']=speed
    user_settings.save()

def handle_settings(bot, event):
    if event.nick not in user_settings.data:
        generate_settings(event.nick)
    set = user_settings.data[event.nick]
    if not event.rest:
        event.reply(', '.join([a+'='+b for a,b in set.items()]))
        return
    type,setting = event.rest.strip().split('=')
    if type in ['voice','pitch','speed']:
        user_settings.data[event.nick][type]=setting
        user_settings.save()
        event.reply('Set '+type+' to '+setting)

def handle_speech(bot, event):
    if not event.rest:  event.missing("<text-to-speak>") ; return
    if event.nick not in user_settings.data:
        generate_settings(event.nick)
    v = user_settings.data[event.nick]['voice']
    s = user_settings.data[event.nick]['speed']
    p = user_settings.data[event.nick]['pitch']
    a = str(100)
    k = str(50)
    speechline = event.rest
    try:
        logging.warning(v+' '+s+' '+p+' '+a+' '+k+' '+speechline)
        conn_send(v+'\t'+s+'\t'+p+'\t'+a+'\t'+k+'\t'+event.nick+'\t'+speechline)
    except:
        event.reply("Cannot connect to host " + HOST + " on port " + str(PORT) )

def handle_spreek(bot, event):
    if not event.rest:  event.missing("<text-to-speak>") ; return
    if event.nick not in user_settings.data:
        generate_settings(event.nick)
    v = user_settings.data[event.nick]['voice']
    s = user_settings.data[event.nick]['speed']
    p = user_settings.data[event.nick]['pitch']
    a = str(100)
    k = str(50)
    if '+' in v:
        v = 'nl'+'+'+v.split('+')[-1]
    else:
        v = 'nl'
    speechline = event.rest
    try:
        logging.warning(v+' '+s+' '+p+' '+a+' '+k+' '+speechline)
        conn_send(v+'\t'+s+'\t'+p+'\t'+a+'\t'+k+'\t'+event.nick+'\t'+speechline)
    except:
        event.reply("Cannot connect to host " + HOST + " on port " + str(PORT) )

def handle_sprech(bot, event):
    if not event.rest:  event.missing("<text-to-speak>") ; return
    if event.nick not in user_settings.data:
        generate_settings(event.nick)
    v = user_settings.data[event.nick]['voice']
    s = user_settings.data[event.nick]['speed']
    p = user_settings.data[event.nick]['pitch']
    a = str(100)
    k = str(50)
    if '+' in v:
        v = 'de'+'+'+v.split('+')[-1]
    else:
        v = 'de'
    speechline = event.rest
    try:
        logging.warning(v+' '+s+' '+p+' '+a+' '+k+' '+speechline)
        conn_send(v+'\t'+s+'\t'+p+'\t'+a+'\t'+k+'\t'+event.nick+'\t'+speechline)
    except:
        event.reply("Cannot connect to host " + HOST + " on port " + str(PORT) )

def handle_dire(bot, event):
    if not event.rest:  event.missing("<text-to-speak>") ; return
    if event.nick not in user_settings.data:
        generate_settings(event.nick)
    v = user_settings.data[event.nick]['voice']
    s = user_settings.data[event.nick]['speed']
    p = user_settings.data[event.nick]['pitch']
    a = str(100)
    k = str(50)
    if '+' in v:
        v = 'fr'+'+'+v.split('+')[-1]
    else:
        v = 'fr'
    speechline = event.rest
    try:
        logging.warning(v+' '+s+' '+p+' '+a+' '+k+' '+speechline)
        conn_send(v+'\t'+s+'\t'+p+'\t'+a+'\t'+k+'\t'+event.nick+'\t'+speechline)
    except:
        event.reply("Cannot connect to host " + HOST + " on port " + str(PORT) )

cmnds.add("espeak", handle_speech, ["SPACE","SPEAK"])
examples.add("espeak", "use espeak to output sound!", "espeak I use espeak.") 
cmnds.add("espreek", handle_spreek, ["SPACE","SPEAK"])
examples.add("espreek", "gebruik espeak om te irritieren!", "espreek Ik gebruik espeak.") 
cmnds.add("esprech", handle_sprech, ["SPACE","SPEAK"])
examples.add("esprech", "benutzen espeak zur Ausgangrauschen!", "esprech Ich benutze espeak.") 
cmnds.add("edire", handle_dire, ["SPACE","SPEAK"])
examples.add("edire", "utilize espeak pour generer du son!", "esprech Je utilise espeak.") 
cmnds.add("espeak-settings", handle_settings, ["SPACE","SPEAK"])
examples.add("espeak-settings", "modify espeak settings", "espeak-settings voice=en+f3") 
