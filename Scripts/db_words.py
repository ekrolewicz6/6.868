import MySQLdb as mdb
import sys
import os.path
import time
import urllib2

import re

def main(argv=None):
    
    if argv is None:
        argv = sys.argv

    if len(argv) == 1 :
        print "Did not enter enough args. Usage: python db_words.py <words_file_path>"
        sys.exit()

    path = argv[1]
    # if not os.path.lexists(path) or path[path.rfind(".")+1:] != "txt" :
    #     print "Path you entered does not contain a text file."
    #     sys.exit()
    
    con = None

    try:
        con = mdb.connect('sql.mit.edu', 'tchwella', 
            '12345678', 'tchwella+6868')

        f = open(path)
        lines = f.readlines()
        cur = con.cursor()
        i = 1
        
        for line in lines:
            line = line.replace("\n", "").replace("'", "*")
            print str(i) + "/" + str(len(lines)) + " " + line
            # print "SELECT * FROM words WHERE words.word = '" + line + "'"
            # cur.execute("SELECT * FROM words WHERE words.word = '" + line + "'")
            # if cur.fetchone() == None:
                # cur.execute("INSERT INTO words (word, rank) VALUES('" + line + "', 0) ")
            data = get_dictionary_page(line)
            types = get_speech_part(data)
            for t in types:
                cur.execute("START TRANSACTION;")
                cur.execute("BEGIN;")
                cur.execute("SELECT * FROM types WHERE types.type = \"" + t + "\";")
                if cur.fetchone() == None:
                    print t
                    cur.execute("INSERT INTO types (type) VALUES(\"" + t + "\");")
                cur.execute("INSERT INTO pos (wordid, typeid) VALUES((SELECT ID FROM words WHERE words.word = \"" + line + "\"), (SELECT ID FROM types WHERE types.type = \"" + t + "\"));")
                cur.execute("COMMIT;")
            try:
                syns = get_synonyms(data)[0][1].replace(" ", "").replace(".", "").split(",")
                for s in syns:
                    s.replace("'", "*")
                    cur.execute("START TRANSACTION;")
                    cur.execute("BEGIN;")
                    cur.execute("SELECT * FROM words WHERE words.word = \"" + s + "\";")
                    if cur.fetchone() == None:
                        print s
                        cur.execute("INSERT INTO words (word) VALUES(\"" + s + "\");")
                    cur.execute("INSERT INTO synonyms (word1id, word2id) VALUES((SELECT ID FROM words WHERE words.word = \"" + line + "\"), (SELECT ID FROM words WHERE words.word = \"" + s + "\"));")
                    cur.execute("COMMIT;")
                print "Added Syns for " + line
            except Exception, e:
                # print e
                pass


            
            i+=1
        
    except mdb.Error, e:
      
        print "Error %d: %s" % (e.args[0], e.args[1])
        sys.exit(1)

    finally:
        
        if con:
            con.close()

def parse_page_contents(data, exp):
    matches = re.findall(exp,data)
    #"(?<=10-YEAR).*[NOTE].*>(\d+-\d+-\d+)<.*>(\w+)<"
    return matches

def get_page(url):
    # proxy_support = urllib2.ProxyHandler({"http":""})
    # urllib2.install_opener(urllib2.build_opener(proxy_support))
    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:12.0) Gecko/20100101 Firefox/12.0' }
    opener = urllib2.Request(url, None, headers)
    return urllib2.urlopen(opener).read()

def get_dictionary_page(word):
    _word = word.replace(" ", "%20").replace("*", "'")
    return get_page("http://dictionary.reference.com/browse/" + _word)

def get_speech_part(data):
    types = parse_page_contents(data, """<span class="pg">([a-zA-Z]+).*</span>""")
    return types

def get_synonyms(data):    
    synonyms = parse_page_contents(data, """<div><span class="sectionLabel">Synonyms</span>.*(<span>1. </span></span>([a-zA-Z ,.]*).?).*</div><br/>""")
    return synonyms

# def yolo(text):
#     words = text.split(" ")
#     print words
#     for word in range(len(words)):
#         print word
#         if words[word] == 'said':
#             print words[word]
#             words[word+1] = "YOLO"
#     return "".join(words)

if __name__ == "__main__":
    sys.exit(main())