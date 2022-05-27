import streamlit as st
from streamlit_webrtc import webrtc_streamer, VideoProcessorBase
import cv2 
import numpy as np 
from utils.img_process_predict import img_live
import pickle
import av
import threading
import os

separator = os.path.sep
path_act = os.path.dirname(os.path.abspath(__file__))
dir = separator.join(path_act.split(separator)[:-1])

with open(f'{dir}/model/SVC_model.pkl', 'rb') as f:
    svm = pickle.load(f)

st.title("Signals")
select = st.sidebar.selectbox("What do you want?",["Streaming", "Upload Image"])

if select == "Streaming":
    class VideoProcessor(VideoProcessorBase):
            def __init__(self):
                self.model_lock = threading.Lock()

            def recv(self, frame):
                img = frame.to_ndarray(format="bgr24")
                data = img_live(img)
                data = np.array(data)
                y_pred = svm.predict(data.reshape(-1,63))
                font = cv2.FONT_HERSHEY_SIMPLEX
                position = (50, 100)
                fontScale = 3
                color = (0, 0, 0)
                thickness = 5
                letter = str(y_pred[0])
                frame = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                frame = cv2.putText(frame, letter, position, font, 
                                fontScale, color, thickness, cv2.LINE_AA)

                return av.VideoFrame.from_ndarray(frame)

    webrtc_streamer(
            key="example",
            video_processor_factory=VideoProcessor,
            media_stream_constraints={
                "video": True,
                "audio": False
            }
        )
elif select == "Upload Image":
    st.subheader("Upload Image")
    frame = st.file_uploader("Upload Image", type=["jpg", "png"])
    if frame is not None:
        file_bytes = np.asarray(bytearray(frame.read())).astype(np.uint8)
        image = cv2.imdecode(file_bytes, 1)
        data = img_live(image)
        data = np.array(data)
        y_pred = svm.predict(data.reshape(-1,63))
        st.image(frame)
        st.subheader(f'The sign is a {y_pred[0]}')
    else:
        st.write("No Image Selected")

        
        
        
        

