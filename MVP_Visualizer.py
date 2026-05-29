
# This is core code of this Transfer Function Visualizer
# Desgined and implemented by Qijun Zhou, May 2026
# Function : 
# input : Transfer Function/Filter type
# output: Bode plot/ciruit design and implementation
# copy right belongs to Qijun Zhou


import numpy as np # type: ignore
import matplotlib.pyplot as plt 

import tkinter as tk # 制作UI界面


# ----------------------------------
# Bode Plot Generator
# ----------------------------------

# Low pass
def lowpassamp_plot(cut_off):
    plt.figure()

    w =[ 1, cut_off, cut_off*10]
    mag =[0,0,-20*np.log10(cut_off*10)]
    plt.semilogx(w, mag)
    plt.xlabel("Angular Frequency")
    plt.ylabel("Amplitude(dB)")
    plt.title("Amplitude Bode Plot")


def lowpassphase_plot(cut_off):
    plt.figure()
    w =[ 1, cut_off/10, cut_off*10, cut_off*100]
    mag =[0,0,-90, -90]
    plt.semilogx(w, mag)
    plt.xlabel("Angular Frequency")
    plt.ylabel("Degree")
    plt.title("Amplitude Phase Plot")


# High pass
def highpassamp_plot(cut_off):
    plt.figure()


    w =[ 1, cut_off, cut_off*10]
    mag =[0,0,20*np.log10(cut_off*10)]
    plt.semilogx(w, mag)
    plt.xlabel("Angular Frequency")
    plt.ylabel("Amplitude(dB)")
    plt.title("Amplitude Bode Plot")


def highpassphase_plot(cut_off):
    plt.figure()

    w =[ 1, cut_off/10, cut_off*10, cut_off*100]
    mag =[0,0,90, 90]
    plt.semilogx(w, mag)
    plt.xlabel("Angular Frequency")
    plt.ylabel("Degree")
    plt.title("Amplitude Phase Plot")


# Band pass
def bandpassamp_plot(cut_off):
    plt.figure()

def bandpassphase_plot(cut_off):
    plt.figure()


# ----------------------------------
# Transfer Function Generator
# ----------------------------------
# Low pass
def lowpass_tf(cut_off):
    ap = cut_off
    return f"H(s) = {ap} / (s + {ap})"


# High pass
def highpass_tf(cut_off):
    return None



# Band pass
def bandpass_tf(cut_off):
    return None

# ----------------------------------
# 将用户输入filter 类型转化为二进制码
# ----------------------------------
def filtertype_describer(filter_signal):
    if(filter_signal == "lowpass"):
        return 00
    elif filter_signal == "highpass":
        return int("01")
    elif filter_signal == "bandpass":
        return 10
    else:
        return 11
    



# ------------------------------------------

# 让用户通过UI选择filter type
root = tk.Tk()
root.title("Transfer Function Visualizer")
root.geometry("400x300")

# 标题行
label = tk.Label(root, text="Choose your filter type")

# 选择行
filter_type = tk.StringVar()
filter_type.set(None)

menu = tk.OptionMenu(root, filter_type, "lowpass","highpass","bandpass")



# 输入cutoff frequency 行
entry =tk.Entry(root)



# generate button
def generate():
    selected = filter_type.get() # This is the filter type
    Cutoff_frequency = float(entry.get())
    code = filtertype_describer(selected)
    if(code == 00):
        lowpassamp_plot(Cutoff_frequency)
        lowpassphase_plot(Cutoff_frequency)
        plt.show()
        Transfer = lowpass_tf(Cutoff_frequency)
        print(Transfer)
    elif code == int("01"):
        highpassamp_plot(Cutoff_frequency)
        highpassphase_plot(Cutoff_frequency)
        plt.show()
        Transfer = highpass_tf(Cutoff_frequency)
        print(Transfer)
    elif code == 10:
        bandpassamp_plot(Cutoff_frequency)
        bandpassphase_plot(Cutoff_frequency)
        plt.show()
        Transfer = bandpass_tf(Cutoff_frequency)
        print(Transfer)
    else:
        print("Error, please choose a filter type to continue")



    
button = tk.Button(root, text="generate", command = generate)

# deploy

label.pack()

menu.pack()

entry.pack()

button.pack()

root.mainloop()

