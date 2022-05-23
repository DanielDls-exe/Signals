import cv2 
import streamlit as st
import numpy as np 
from img_process_predict import img_live
import pickle

# load model
with open('SVC_model.pkl', 'rb') as f:
    svm = pickle.load(f)


st.title("Signals")
run = st.checkbox('Predict Vocals')
FRAME_WINDOW = st.image([])
cam = cv2.VideoCapture(0)

while run:
    ret, frame = cam.read()
    print(len(frame))
    data = img_live(frame)
    data = np.array(data)
    y_pred = svm.predict(data.reshape(-1,63))
    font = cv2.FONT_HERSHEY_SIMPLEX
    position = (50, 100)
    fontScale = 3
    color = (0, 0, 0)
    thickness = 5
    letter = str(y_pred[0])
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame = cv2.putText(frame, letter, position, font, 
                    fontScale, color, thickness, cv2.LINE_AA)
    FRAME_WINDOW.image(frame)
else: 
    st.write("You have exited the app")
    cam.release()
    cv2.destroyAllWindows()
    




    



