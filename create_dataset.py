import numpy as np
import cv2 as cv
from pathlib import Path

def create_data():
    letter = 'X'
    Path('dataset/'+letter).mkdir(parents=True, exist_ok=True)
    cap = cv.VideoCapture(0)
    i = 0    
    while True:
       
        ret, frame = cap.read()
        i+= 1
        if i % 5==0:
            cv.imwrite(f'dataset/{letter}/{str(i)}.png',frame)
        cv.imshow('frame', frame)
        if cv.waitKey(1) == ord('q') or i > 500:
            break
    cap.release()
    cv.destroyAllWindows()

if __name__ == "__main__":
   create_data()

#Faltan 3 letras que no sé como incluir aún (j, ñ, z)
  