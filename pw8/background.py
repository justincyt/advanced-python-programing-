import pickle 
import threading 

class BackgroudThread(threading.Thread): 
    def __init__(self,op,opp,pick_dum=None):
        threading.Thread.__init__(self)
        self.__op=op 
        self.__opp=opp
        self.__pick_dum=pick_dum

    def program(self):
        if self.__op == 'dump':
            if self.__pick_dum is not None:
                pickle.dump(self.__pick_dum,self.__opp)
            else:
                return 0 
        elif self.__op == 'load':
                loadfile=pickle.load(self.opp)
                return loadfile
    
def backgroudfuc(op,opp,pick_dum=None):
    back=BackgroudThread(op,opp,pick_dum)
    back.start()
    back.join()