from datetime import datetime as dt

class Datalogger:
    def __init__(self, moduleName):
        self.f = open("loggerd"+moduleName+".txt", "w")

    def LOG(self, message):
        strConcat = "[LOG] " + str(dt.now()) + " - " + message
        self.f.write(strConcat+"\n")
        print(strConcat)