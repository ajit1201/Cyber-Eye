
import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *
import os.path
import cv2
import mediapipe as mp
import pyautogui

_script = sys.argv[0]
_location = os.path.dirname(_script)
import unknown_support

_bgcolor = '#d9d9d9'
_fgcolor = '#000000'
_compcolor = 'gray40'
_ana1color = '#c3c3c3'
_ana2color = 'beige'
_tabfg1 = 'black' 
_tabfg2 = 'black' 
_tabbg1 = 'grey75' 
_tabbg2 = 'grey89' 
_bgmode = 'light' 

class Toplevel1:
    def __init__(self, top=None):

        top.geometry("600x454+468+138")
        top.minsize(120, 1)
        top.maxsize(1540, 845)
       #top.resizable(1,  1)
        top.title("CEBER EYE")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.top = top

        self.Frame1 = tk.Frame(self.top)
        self.Frame1.place(relx=0.0, rely=0.0, relheight=1.011, relwidth=0.525)
        self.Frame1.configure(relief='groove', borderwidth="2", background="#3374EE", highlightbackground="#d9d9d9", highlightcolor="black")

        self.Label1 = tk.Label(self.Frame1)
        self.Label1.place(relx=0.127, rely=0.198, height=50, width=260)
        self.Label1.configure(activebackground="#f9f9f9", anchor='w')
        self.Label1.configure(background="#3374EE", compound='left', disabledforeground="#a3a3a3", font="-family {Segoe UI} -size 24 -weight bold", foreground="#ffffff")
        self.Label1.configure(highlightbackground="#d9d9d9", highlightcolor="black", text='''Project Name''')

        self.Label2 = tk.Label(self.Frame1)
        self.Label2.place(relx=0.127, rely=0.307, height=21, width=270)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(anchor='w', background="#3374EE")
        self.Label2.configure(compound='left', disabledforeground="#a3a3a3")
        self.Label2.configure(font="-family {Segoe UI} -size 13", foreground="#ffffff")
        self.Label2.configure(highlightbackground="#d9d9d9", highlightcolor="black", text='''Software Engineering and''')

        self.Label3 = tk.Label(self.Frame1)
        self.Label3.place(relx=0.127, rely=0.375, height=31, width=104)
        self.Label3.configure(activebackground="#f9f9f9")
        self.Label3.configure(anchor='w', background="#3374EE", compound='left')
        self.Label3.configure(disabledforeground="#ffffff", font="-family {Segoe UI} -size 14", foreground="#ffffff")
        self.Label3.configure(highlightbackground="#d9d9d9", highlightcolor="black", text='''Testing''')

        self.Label3_1 = tk.Label(self.Frame1)
        self.Label3_1.place(relx=0.127, rely=0.44, height=21, width=280)
        self.Label3_1.configure(activebackground="#f9f9f9")
        self.Label3_1.configure(anchor='w', background="#3374EE")
        self.Label3_1.configure(compound='left', disabledforeground="#ffffff")
        self.Label3_1.configure(font="-family {Segoe UI} -size 13", foreground="#ffffff", highlightbackground="#d9d9d9", highlightcolor="black")
        self.Label3_1.configure(text='''Sohel Sheikh and Ajit Tiwari''')

        self.Label3_1_1 = tk.Label(self.Frame1)
        self.Label3_1_1.place(relx=0.127, rely=0.484, height=21, width=104)
        self.Label3_1_1.configure(activebackground="#f9f9f9",anchor='w')
        self.Label3_1_1.configure(background="#3374EE",compound='left',disabledforeground="#ffffff")
        self.Label3_1_1.configure(font="-family {Segoe UI} -size 13",foreground="#ffffff",highlightbackground="#d9d9d9", highlightcolor="black",text=''' ''')

        self.Button1 = tk.Button(self.top, command = hi)
        self.Button1.place(relx=0.667, rely=0.267, height=54, width=127)
        self.Button1.configure(activebackground="beige",activeforeground="black",background="#3374EE")
        self.Button1.configure(compound='left',disabledforeground="#a3a3a3",font="-family {Segoe UI} -size 24 -weight bold",foreground="#ffffff",highlightbackground="#d9d9d9",highlightcolor="black", pady="0", text='''START''')

        self.Button1_1 = tk.Button(self.top, command = shut_down)
        self.Button1_1.place(relx=0.667, rely=0.401, height=54, width=127)
        self.Button1_1.configure(activebackground="beige", activeforeground="black", background="#FD4746", compound='left', disabledforeground="#a3a3a3", font="-family {Segoe UI} -size 24 -weight bold", foreground="#ffffff", highlightbackground="#d9d9d9", highlightcolor="black", pady="0", text='''END''')

def start_up():
    unknown_support.main()


def hi():
    face_mesh =mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
    screen_w, screen_h = pyautogui.size()

    cam = cv2.VideoCapture(0)
    while True:
        _, frame = cam.read();
        frame = cv2.flip(frame, 1)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        output = face_mesh.process(rgb_frame)
        landmark_points = output.multi_face_landmarks
        frame_h, frame_w, _ = frame.shape
        if landmark_points:
            landmarks = landmark_points[0].landmark
            for id, landmark in enumerate(landmarks[474:478]):
                x = int(landmark.x * frame_w)
                y = int(landmark.y * frame_h)
                cv2.circle(frame, (x, y), 3, (0, 255, 0))
                if id == 1:
                    screen_x = (screen_w / frame_w * x)
                    screen_y = (screen_h / frame_h * y)
                    pyautogui.moveTo(screen_x, screen_y)
            left = [landmarks[145], landmarks[159]]

            for landmark in left:
                x = int(landmark.x * frame_w)
                y = int(landmark.y * frame_h)
                cv2.circle(frame, (x, y), 3, (0, 255, 255))
            if (left[0].y - left[1].y) < 0.004:
                pyautogui.click()
                pyautogui.sleep(1)

        cv2.imshow('Eye Controll Mouse', frame)
        cv2.waitKey(1)


def shut_down():
    exit()

if __name__ == '__main__':
    unknown_support.main()




