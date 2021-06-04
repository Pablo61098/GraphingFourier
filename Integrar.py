from threading import Thread

class Integrar(Thread):

    def __init__(self,tipo,func,limits,periodo):

        Thread.__init__(self)
        self.tipo=tipo
        self.func=func
        self.limits=limits
        self.periodo=periodo

    def run(self):

        if(self.tipo=="a0"):
            pass
        elif (self.tipo == "an"):
            pass
        elif (self.tipo == "bn"):
            pass