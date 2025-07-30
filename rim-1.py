import random
import time 

def make_noodles(length = 50, strands = 10):
    noodle_shapes = ['~','~','-','^','=']   
    for _ in range(strands):
        noodle = ""
        for _ in range(length):
            noodle += random.choice(noodle_shapes)
        print(noodle)
        time.sleep(0.5)

print("cooking your noodles...")
make_noodles
print("noodles are ready!enjoy")
make_noodles()