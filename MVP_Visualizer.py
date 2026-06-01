
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
    mag =[-20*np.log10(cut_off),-20*np.log10(cut_off),-20*np.log10(cut_off*10)]
    plt.semilogx(w, mag)
    plt.xlabel("Angular Frequency")
    plt.ylabel("Amplitude(dB)")
    plt.title("Amplitude Bode Plot")
    plt.grid(True, which="both")


def lowpassphase_plot(cut_off):
    plt.figure()
    w =[ 1, cut_off/10, cut_off*10, cut_off*100]
    mag =[0,0,-90, -90]
    plt.semilogx(w, mag)
    plt.xlabel("Angular Frequency")
    plt.ylabel("Degree")
    plt.title("Amplitude Phase Plot")
    plt.grid(True, which="both")

# High pass
def highpassamp_plot(cut_off):
    plt.figure()


    w =[ 1, cut_off, cut_off*10]
    mag =[20*np.log10(cut_off),20*np.log10(cut_off),20*np.log10(cut_off*10)]
    plt.semilogx(w, mag)
    plt.xlabel("Angular Frequency")
    plt.ylabel("Amplitude(dB)")
    plt.title("Amplitude Bode Plot")
    plt.grid(True, which="both")


def highpassphase_plot(cut_off):
    plt.figure()

    w =[ 1, cut_off/10, cut_off*10, cut_off*100]
    mag =[0,0,90, 90]
    plt.semilogx(w, mag)
    plt.xlabel("Angular Frequency")
    plt.ylabel("Degree")
    plt.title("Amplitude Phase Plot")
    plt.grid(True, which="both")


# Band pass
def bandpassamp_plot(wL, wH, wT, K):
    plt.figure()

    if wL>= wH:
        print("Error, lower cutoff frequency must be smaller than higher cutoff frequency")
        return
    if wL <=0 or wH <=0 or wT<=0:
        print("Error,cutoff frequency and termination frequency should larger than zero")
        return
    
    if wT <= wH: 
        print("Error, termiantion frequency should larger than higher cutoff frequency")
        return
    
    if K<=0:
        print("Error, K must be positive")
        return

    w_start = wL / 10

    mid_gain_db = 20 * np.log10(K / wH)

    w = [w_start, wL , wH, wT]

    mag = [mid_gain_db-20,
           mid_gain_db,
           mid_gain_db,
           mid_gain_db-20*np.log10(wT/wH)]
    
    plt.semilogx(w, mag)
    plt.xlabel("Angular Frequency")
    plt.ylabel("Amplitude(dB)")
    plt.title("Amplitude Bode Plot")
    plt.grid(True, which="both")




def bandpassphase_plot(wL, wH, wT, K):
    plt.figure()

    if wL>= wH:
        print("Error, lower cutoff frequency must be smaller than higher cutoff frequency")
        return
    if wL <=0 or wH <=0 or wT<=0:
        print("Error,cutoff frequency and termination frequency should larger than zero")
        return
    
    if wT <= wH: 
        print("Error, termiantion frequency should larger than higher cutoff frequency")
        return
    
    if K<=0:
        print("Error, K must be positive")
        return
    

    w_start = wL / 10

    if wH < 10 * wL:
        w = np.logspace(np.log10(wL/10), np.log10(wT), 500)
        phase = 90 - np.degrees(np.arctan(w / wL)) - np.degrees(np.arctan(w / wH))
        plt.semilogx(w, phase)
        plt.title("Precise Bode Phase Plot")
    else:
        w = [wL/10, wL, wL*10, wH/10, wH*10, wT]
        phase = [90, 45, 0, -45, -90, -90]
        plt.semilogx(w, phase)
        w = [wL/10, wL, wL*10, wH/10, wH*10, wT]
        plt.title("Approximate Bode Phase Plot")

  
    plt.xlabel("Angular Frequency")
    plt.ylabel("Degree")

    plt.grid(True, which="both")

# -------------------------------------------------
# Transfer Function Generator
# ------------------------------------------------
# Low pass
def lowpass_tf(cut_off):
    ap = cut_off
    return f"H(s) = {ap} / (s + {ap})"


# High pass
def highpass_tf(cut_off):
    az = cut_off
    return f"H(s) = s+{az}"


# Band pass
def bandpass_tf(wL,wH,K):
    return f"H(s)={K}s / (s+{wL})(s+{wH})"

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
# UI 界面
# ------------------------------------------

# 让用户通过UI选择filter type


root = tk.Tk()
root.title("Transfer Function Visualizer")
root.geometry("600x500")

# 标题行
label = tk.Label(root, text="Choose your filter type")

label.pack()
# 选择行
filter_type = tk.StringVar()
filter_type.set(None)

input_frame = tk.Frame(root)
input_frame.pack()

entries ={}


def input_updates(*args):
    global  entries

    for widget in input_frame.winfo_children():
        widget.destroy()
    
    entries = {}

    selected = filter_type.get()  # filtertype

    if selected == "bandpass":
        labels = ["wL", "wH", "wT", "K"]
        
        for name in labels:
            tk.Label(input_frame, text=name).pack()
            entries[name]=tk.Entry(input_frame)
            entries[name].pack()

    elif selected == "lowpass" or selected == "highpass":
        tk.Label(input_frame, text = "cutoff frequency").pack()
        entries["cutoff"]=tk.Entry(input_frame)
        entries["cutoff"].pack()



menu = tk.OptionMenu(root, filter_type, "lowpass","highpass","bandpass", command = input_updates)
menu.pack()

input_updates()

# generate button
def generate():
    selected = filter_type.get() # This is the filter type
  
    code = filtertype_describer(selected)
    if(code == 00):
        Cutoff_frequency = float(entries["cutoff"].get())
        lowpassamp_plot(Cutoff_frequency)
        lowpassphase_plot(Cutoff_frequency)
        plt.show()
        Transfer = lowpass_tf(Cutoff_frequency)
        print(Transfer)
    elif code == int("01"):
        Cutoff_frequency = float(entries["cutoff"].get())
        highpassamp_plot(Cutoff_frequency)
        highpassphase_plot(Cutoff_frequency)
        plt.show()
        Transfer = highpass_tf(Cutoff_frequency)
        print(Transfer)
    elif code == 10:
        wl = float(entries["wL"].get())
        wh = float(entries["wH"].get())
        wt = float(entries["wT"].get())
        k = float(entries["K"].get())

        bandpassamp_plot(wl,wh,wt,k)
        bandpassphase_plot(wl,wh,wt,k)
        plt.show()

        Transfer = bandpass_tf(wl,wh,k)

        print(Transfer)
    else:
        print("Error, please choose a filter type to continue")



button = tk.Button(root, text="generate", command = generate)


button.pack()


root.mainloop()

