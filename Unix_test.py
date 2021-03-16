import os
import pty
from time import sleep
import numpy as np

def communication(child_writes):

    # файловые дескрипторы r, w для чтения и записи

    r, w = os.pipe()

      

    # Создание дочернего процесса с использованием fork

    processid = os.fork()

    if processid:

        # Это родительский процесс

        # Закрывает дескриптор файла w

        os.close(w)

        r = os.fdopen(r)

        print ("Parent reading")

        str = r.read()

        print( "Parent reads =", str)

    else:

        # Это дочерний процесс

        os.close(r)

        w = os.fdopen(w, 'w')

        print ("Child writing")

        w.write(child_writes)

        print("Child writes = ",child_writes)

        w.close()

          
# Код драйвера

child_writes = "Hello geeks"

communication(child_writes)
