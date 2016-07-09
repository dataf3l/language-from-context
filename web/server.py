import cherrypy
import MySQLdb


class WebUI(object):
 
    def make_words(self, word_list):
        conn = MySQLdb.connect(host="127.0.0.1",
                               user="root",
                               passwd="",
                               db="lfc")
        x = conn.cursor()
        # remove from wordlist existing:
        d = "SELECT id, word FROM word where word in ('" + ("','".join(word_list)) + "')"
        print(d)
        x.execute(d)
        existing = x.fetchall()
        ids = []
        new_words = {}
        for w in word_list:
            new_words[w] = w

        for (e_id, e_word) in existing:
            print "Found " + str(e_id)
            ids.append(e_id)
            del(new_words[e_word])

        # add new terms:
        for word in new_words:
            q = "INSERT INTO word (word) VALUES ('"+word+"') "
            print(q)
            ids.append(conn.insert_id())
            try:
                x.execute(q)
                conn.commit()
            except:
                print("Insert Failed...")
                conn.rollback()

        # add new terms:
        for word_id in ids:
            q = "INSERT INTO knowledge(word_id,date_learned) VALUES ('"+str(word_id)+"', now()) "
            print(q)
            try:
                x.execute(q)
                conn.commit()
            except:
                print("Insert Failed...")
                conn.rollback()

        conn.close()
        
    @cherrypy.expose
    def save_knowledge(self, knowledge):
        return self.make_words(knowledge.split(" "))
        #return "ok:" + knowledge

    def get_template(self, template_name):
        f = open("template/" + template_name+".html")
        s = f.read()
        f.close()
        return s

    @cherrypy.expose
    def index(self):
        return self.get_template("index")

    @cherrypy.expose
    def register_knowledge(self):
        return self.get_template("register_knowledge_form")

if __name__ == '__main__':
    cherrypy.quickstart(WebUI())
