import MySQLdb as db

#sudo mysql -uremote -p -h 192.168.1.105

class Database:
    def __init__(self):
        self.HOST = "novawebapp.ddns.net"
        self.PORT = 555
        self.USER = "remote"
        self.PASSWORD = "password"
        self.DB = "edp"
        self.connect()

    def connect(self):
        try:
            self.connection = db.Connection(host=self.HOST, port=self.PORT, user=self.USER, passwd=self.PASSWORD, db=self.DB)
            print('connected')
            self.dbhandler = self.connection.cursor()
        except Exception as e:
            print("Can't connect")
            raise e

    def connectionClose(self):
        self.connection.close()
    
    def getName(self,user_id):
        self.connect()
        self.dbhandler.execute("SELECT first_name from auth_user WHERE id = "+str(user_id))
        result = self.dbhandler.fetchall()
        self.connectionClose()
        return result[0][0]

    
    
    def getProjects(self, user_id):
        self.connect()

        project_entries = []
        self.dbhandler.execute("SELECT id,title,description,code from main_personalproject WHERE user_id = "+str(user_id))
        result = self.dbhandler.fetchall()
        for item in result:
            print(item)
            project_entries.append(item)
        self.connectionClose()
        return project_entries

    def getSingleProject(self, id):
        self.connect()
        self.dbhandler.execute("SELECT id,title,description,code from main_personalproject WHERE id = "+str(id))
        result = self.dbhandler.fetchall()
        self.connectionClose()
        return result[0]

    def getTutorials(self, user_id):
        self.connect()
        tutorial_entries = []
        tutorial_steps = {}

        self.dbhandler.execute("SELECT code,project_id,step from main_structuredprojectcode WHERE user_id = "+str(user_id))
        result = self.dbhandler.fetchall()
        for item in result:
            if item[1] not in tutorial_steps:
                tutorial_steps[item[1]] = []
            tutorial_steps[item[1]].append(item)
        print(tutorial_steps) 
        self.dbhandler.execute("SELECT id,title,description,slug from main_structuredproject WHERE id IN ({})".format(str(tutorial_steps.keys()).strip('dict_keys([])')))
        result = self.dbhandler.fetchall()
        for item in result:
            tutorial_entries.append(item)
        self.connectionClose()
        print(tutorial_entries)
        return tutorial_entries, tutorial_steps


    def getTutorialSteps(self, user_id, project_id):
        self.connect()
        single_tutorial_steps = []
        self.dbhandler.execute("SELECT code,project_id,step from main_structuredprojectcode WHERE user_id = {} AND project_id = {}".format(str(user_id), str(project_id)))
        result = self.dbhandler.fetchall()
        for item in result:
            single_tutorial_steps.append(item)
        print(single_tutorial_steps) 
        self.connectionClose()
        return single_tutorial_steps

    def getSingleTutorialStep(self, user_id, project_id, step):
        self.connect()
        single_tutorial_step = []
        self.dbhandler.execute("SELECT code,project_id,step from main_structuredprojectcode WHERE user_id = {} AND project_id = {} AND step = {}".format(str(user_id), str(project_id), str(step)))
        result = self.dbhandler.fetchall()
        for item in result:
            single_tutorial_step.append(item)
        print(single_tutorial_step) 
        self.connectionClose()
        return single_tutorial_step
        

test = Database()
test.getTutorials(3)
