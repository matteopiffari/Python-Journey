import threading


def printCube(num):
    print("Cube: {} from thread {}".format(num * num * num, threading.current_thread().name))


def printSquare(num):
    print("Square: {} from thread {}".format(num * num, threading.current_thread().name))


if __name__ =="__main__":
    t1 = threading.Thread(target=printSquare, args=(15,))
    t2 = threading.Thread(target=printCube, args=(15,))

    t1.start()
    t2.start()

    # Timeline
    
    # main:     [-----  IDLE  ---]
    # t1:             [----]
    # t2:             [------]

    t1.join()
    t2.join()

    print("All the threads have finished!")