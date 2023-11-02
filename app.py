import tkinter as tk 
import customtkinter as ctk

import torch 
import numpy as np
import cv2 
from PIL import Image, ImageTk
import random
import pygame

# Pygame mixer 초기화
pygame.mixer.init()

app = tk.Tk()
app.geometry("600x600")
app.title("Drowsy Detection")
ctk.set_appearance_mode("dark")

vidFrame = tk.Frame(height=480, width=600)
vidFrame.pack()
vid = ctk.CTkLabel(vidFrame)
vid.pack()

counter = 0
counterLabel = ctk.CTkLabel(text=counter, height=40, width=120, text_color="white", master=app)
counterLabel.pack()

def reset_counter():
    global counter
    counter = 0
    counterLabel.configure(text=str(counter))  # 카운터 라벨 업데이트

resetButton = ctk.CTkButton(text="Reset Counter", height=40, width=120, text_color="white", command=reset_counter, master=app)
resetButton.pack()

model = torch.hub.load("ultralytics/yolov5", "custom", path="last.pt", force_reload=True)
cap = cv2.VideoCapture(0)

def detect():
    global counter
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        return
    
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = model(frame)
    img = np.squeeze(results.render())

    if len(results.xywh[0]) > 0:
        dconf = results.xywh[0][0][4]
        dclass = results.xywh[0][0][5]
        print(f"Detected: conf={dconf}, class={dclass}")  # 감지된 객체의 신뢰도와 클래스를 출력

        if dconf.item() > 0.75 and dclass.item() == 15.0:
            filechoice = random.choice(["/Users/kimminyoung/minyoungxi/캡스톤/audio/drone-9708.mp3", 
                                        "/Users/kimminyoung/minyoungxi/캡스톤/audio/happy-birthday-to-you-lullaby-94102.mp3", 
                                        "/Users/kimminyoung/minyoungxi/캡스톤/audio/happy-birthday-to-you-ska-94111.mp3"])
            pygame.mixer.music.load(filechoice)
            pygame.mixer.music.play()
            counter += 1
            counterLabel.configure(text=str(counter))  # 카운터 라벨 업데이트
    
    imgarr = Image.fromarray(frame)
    imgtk = ImageTk.PhotoImage(imgarr)
    vid.imgtk = imgtk
    vid.configure(image=imgtk)
    vid.after(10, detect)

detect()
app.mainloop()
