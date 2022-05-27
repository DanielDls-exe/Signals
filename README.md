# Signals

Signals is a sign language alphabet recognition project using Python, Mediapipe, OpenCV, Machine Learning (Sklearn) and Streamlit. In essence it is a program that recognizes which alphabet sign we are doing in real time or through images. 

![gif](https://i.makeagif.com/media/5-27-2022/4Kp0UY.gif)
![gif](https://i.makeagif.com/media/5-27-2022/iJ7bUh.gif)

## How to use?

1. Clone the repository with git clone

```bash
  git clone https://github.com/DanielDls-exe/Signals-.git
```
2. Let's install the requirements

```bash
  pip install -r requirements.txt
```

3. If we want to create our own sign dataset, we must execute the script "create_dataset.py". Otherwise we can skip to step number 6 "Run Streamlit".

```bash
  python create_dataset.py
```
The program will ask us which sign we want to add to the dataset, then it will open the web cam for a few seconds, here we must show the camera the sign we want to add. What this process is doing is taking several pictures, exactly 100 pictures with a small time interval between each one of them.

This program also creates a folder called "dataset" and inside it, it will save the 100 photos in folders with the name of the signal that we have written.

4. We must extract the landmark of all the images of each sign, and save them in a .csv, for this we will execute the program "create_csv.py".

```bash
  python create_csv.py
```
Now we have our .csv created as "dataset.csv". 

5. Let's train! For this, we are going to execute all the lines of code of the "train_SVC.ipynb". Once the training is finished we will have the model saved in the file as "SVC_model.pkl".

6. Run Streamlit. 
To do this, inside the streamlit_webRTC folder, execute the following command:

```bash
  streamlit run main.py
```
In the "Streaming" section we can show the signs through the webcam and it will recognize them live, in the "Upload image" section we can upload an image of our hand and it will show through the web what sign we are doing.
