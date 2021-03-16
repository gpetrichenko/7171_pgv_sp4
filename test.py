from multiprocessing import Process
from time import sleep
import numpy as np

class CustomProcess(Process):
   def __init__(self, limit):
       Process.__init__(self)
       self._limit = limit
   def run(self):
       for i in range(self._limit):
            matrix = np.arange(100).reshape(10,10)
            
            for val in range(matrix[i][0], matrix[i][-1]+1):
               if val > 1:
                   for n in range(2, val):
                       if (val % n) == 0:
                           break
                   else:
                       print(val, end=" ")
            sleep(0.5)

if __name__ == "__main__":
   print ("\nProgram #2\n")
   cpr = CustomProcess(10)
   cpr.start()