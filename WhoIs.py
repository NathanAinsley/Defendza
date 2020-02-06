import whois
import socket

import Shodan

class Setup:
    def Domains(v):
        com = v + ".com"
        couk = v + ".co.uk"
        uk = v + ".uk"
        org = v + ".org"
        net = v + ".net"
        us = v + ".us"
        de = v + ".de"
        cn = v + ".cn"
        info = v + ".info"
        nl = v + ".nl"
        eu = v + ".eu"
        ru = v + ".ru"
        Domains = [com,couk,uk,org,net,us,de,cn,info,nl,eu,ru]
        return Domains

class Searcher:
    def GetDomainInfoByName(v):
        Domains = Setup.Domains(v)
        print(Domains)
        i = 0
        Records = []
        while i < len(Domains):
            try:
                q = whois.query(Domains[i])
                Servers = q.name_servers
                Name = q.name
                CreationDate = q.creation_date
                ExpireDate = q.expiration_date
                Update = q.last_updated
                Registrar = q.registrar
                record = [((Name),(CreationDate),(ExpireDate),(Update),(Registrar),(Servers))]
                Records = Records+(record)
                i+=1
            except:
                print("No Domain at: "+Domains[i])
                i+=1
           # Records = Records+(record)
        return Records
            
    def Reverse():
        return 0
        
    def SingleSocket(v):
        d = socket.gethostbyname(v)
        return d
        
        
    def Socket(v):
        Domains = Setup.Domains(v)
        i = 0
        while i < len(Domains):
            try:
                d = socket.gethostbyname(Domains[i])
                print(d)
            except:
                print("No Domain at: "+Domains[i])
            i+=1
            
    def printer(returned):
        for records in returned:
            for record in records:
                try:
                    if Searcher.SingleSocket(record[0]) != None: 
                        print(record)
                        try:
                            print("Domain Name: " + str(record[0]))
                        except:
                            print("No Domain Name Listed")
                        try:
                            print("Creation Date: " + str(record[1]))
                        except:
                            print("No Domain Name Listed")
                        try:
                            print("Expiration Date: " + str(record[2]))
                        except:
                            print("No Expiration Date Listed")
                        try:
                            print("Last Updated: " + str(record[3]))
                        except:
                            print("No Expiration Date Listed")
                        try:
                            print("Registrar name: " + str(record[4]))
                        except:
                            print("No Registrar Name listed")
                        try:
                            print("Servers: " + str(record[5]))
                        except:
                            print("No Servers Listed")
                        try:
                            print("IP Address: " + Searcher.SingleSocket(record[0]))
                            print(Shodan.Shodan.Shodan(Searcher.SingleSocket(record[0])))
                        except:
                            print("No IP Address linked")
                        print("\n \n \n")
                except:
                    pass
                    
        
returned = Searcher.GetDomainInfoByName('Defendza')
Searcher.printer(returned)