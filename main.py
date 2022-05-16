# This is a sample Python script.
import tkinter as tk
from tkinter import *
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from tkinter import filedialog
from tkinter.filedialog import *
from tkinter import ttk
import matplotlib.pyplot as plt
import serial
import cv2
import pygame

from numpy import uint16, double
# import pyserial

# port_list = list(serial.tools.list_ports.comports())
# print(port_list)
# from serial import serial
import time
import os
import numpy as np

import serial.tools.list_ports

def init(chars, lines):
    global screen
    global myfont
    pygame.init()
    size = [12 * chars, 20 * lines]
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("hello")
    myfont = pygame.font.SysFont("monospace", 20)

def draw(args):
    i = 0;
    global screen
    global myfont
    screen.feel((0, 0, 0))
    while (i<len(args)):
        line = myfont.render(args[i], 2, (255, 255, 0))
        screen.blit(line, (0, 20 * i))
        i += 1
    pygame.display.flip()

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Bye, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def selectOutputDir():
    OutputDir = filedialog.askdirectory(parent=window)
    outputFile = OutputDir
    text0.insert(INSERT, outputFile)

def CreateDisplay():
    # text5.delete('1.0', END)
    nRaws = text1.get("1.0",END)
    nCols = text2.get("1.0",END)
    text5.insert(INSERT, nRaws)
    text5.insert(INSERT, nCols)


def prevScreen():
    text5.delete('1.0', END)
    text5.insert(INSERT, 'prevScreen')

def nextScreen():
    text5.delete('1.0', END)
    text5.insert(INSERT, 'nextScreen')

# speeds = ['1200','2400', '4800', '9600', '19200', '38400', '57600', '115200']

def saveScreen():
    text5.delete('1.0', END)
    text5.insert(INSERT, 'screen was saved')

def generateOutput():
    text5.delete('1.0', END)
    text5.insert(INSERT, 'files R ready')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # ser = serial.Serial(port='COM6', baudrate=1000000, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE,
    # bytesize=serial.EIGHTBITS, timeout=0.1)
    window = Tk()
    window.geometry('1200x500')
    window.title("Генератор INC файлов")

    # combobox = ttk.Combobox(window, values=connectedPorts)
    # print(dict(comboExample))
    # combobox.grid(column=0, row=1)
    # combobox.current(1)
    # print(comboExample.current(), comboExample.get())
    lbl0 = Label(window, text="Число строк")
    lbl0.grid(column=0, row=0)
    lbl1 = Label(window, text="Длина строки")
    lbl1.grid(column=1, row=0)
    lbl2 = Label(window, text="№ дисплея")
    lbl2.grid(column=2, row=0)
    lbl3 = Label(window, text="Статус")
    lbl3.grid(column=3, row=0)

    text0 = Text(width=20, height=1)# 4 outout dir
    text0.grid(column=0, row=1, sticky=(W))
    text0.insert(INSERT, 'outputDir')
    text1 = Text(width=20, height=1)# 4 nRwas
    text1.grid(column=1, row=1, sticky=(W))
    text1.insert(INSERT, 'nRwas')
    text2 = Text(width=20, height=1)# 4 nCols
    text2.grid(column=2, row=1, sticky=(W))
    text2.insert(INSERT, 'nCols')
    text3 = Text(width=20, height=1)# 4 n of cur screen
    text3.grid(column=3, row=1, sticky=(W))
    text3.insert(INSERT, 'curScreen')
    text4 = Text(width=20, height=1)# 4 screen content
    text4.grid(column=4, row=1, sticky=(W))
    text4.insert(INSERT, 'screenContent')
    text5 = Text(width=20, height=1)# 4 status
    text5.grid(column=5, row=1, sticky=(W))
    text5.insert(INSERT, 'Status')

    btn0 = Button(window, text="Путь к сохранённым файлам", command=selectOutputDir)
    btn0.grid(column=0, row=2)
    btn1 = Button(window, text="Создать дисплей", command=CreateDisplay)
    btn1.grid(column=1, row=2)
    btn2 = Button(window, text="Пред. дисплей", command=prevScreen)
    btn2.grid(column=2, row=2)
    btn3 = Button(window, text="След. дисплей", command=nextScreen)
    btn3.grid(column=3, row=2)
    btn4 = Button(window, text="Сохранить дисплей", command=saveScreen)
    btn4.grid(column=4, row=2)
    btn5 = Button(window, text="Сгенерировать файлы!", command=generateOutput)
    btn5.grid(column=5, row=2)
    init(5, 2)

    window.mainloop()
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

