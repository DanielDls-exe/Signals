import streamlit as st
from streamlit_webrtc import webrtc_streamer, VideoProcessorBase, RTCConfiguration
import cv2 
import numpy as np 
from img_process_predict import img_live
import pickle
import av
import threading

with open('SVC_model.pkl', 'rb') as f:
    svm = pickle.load(f)

st.title("Signals")


webrtc_streamer(key="example")

        
        
        
        

