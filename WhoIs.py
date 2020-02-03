import whois

class Searcher:
    def Get():
        q = whois.query('Defendza.com')
        print(q.__dict__)
        
Searcher.Get()