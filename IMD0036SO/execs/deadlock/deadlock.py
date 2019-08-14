from threading import Thread

fileInUse = False
finished = False

def isBlanc():
    with open('test.txt', 'r') as arq:
        dat = arq.read()
        if len(dat) > 0:
            return False
        else :
            return True

    
def fus_ro_dah():
    with open('test.txt', 'a+') as dat:
        dat.write("Fus Ro Dah!!!!\n")
    return True


t1 = Thread(target= fus_ro_dah)
t2 = Thread(target= isBlanc )







    
    
    