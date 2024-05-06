import time

def dino():
    dinosaur = '''
                __  "rawr"
                / _) 
        .-^^^-/ /
    __/       /
    <__.|_|-|_|

    Dino, by 1113
    '''
    for dinosaurs in range (0, 10):
        print(dinosaur)
        time.sleep(3)

    #spawn dino forever!
    #while True:
    #    print(dinosaur)
    #    time.sleep(3)
dino()