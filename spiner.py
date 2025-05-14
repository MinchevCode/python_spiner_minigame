# from tkinter import*
#
# def btnclick(numbers):   #define the button(btn)click function
#     global operator
#     operator=operator + str(numbers)
#     text_Input.set(operator)
#
# def btnClearDisplay():   # define the clear function
#     global operator
#     operator=""
#     text_Input.set("")
#
# def btnEqualsInput():     #define the Equal to function
#     global operator
#     sumup=str(eval(operator))
#     text_Input.set(sumup)
#     operators=""
#
# cal = Tk()
# cal.title("Calculator")       # name the app, i choose a "Calculator" because it's random
# operator = ""
# text_Input = StringVar()
#
# txtDisplay = Entry(cal,font=('arial', 20,'bold'), textvariable=text_Input, bd=30, insertwidth=4,
#                    bg="powder blue", justify='right').grid(columnspan=4)
#
# btnclear=Button(cal,padx=16,pady=16,bd=8, fg="black",font=('arial', 20,'bold'),
#             text="C",bg="powder blue",command=btnClearDisplay).grid(row=1,column="0")
#
# BtnM=Button(cal,padx=16,pady=16,bd=8, fg="black",font=('arial', 20,'bold'),
#             text="M",bg="powder blue",).grid(row=1,column="1")
#
# Btnbraket1=Button(cal,padx=16,pady=16,bd=8, fg="black",font=('arial', 20,'bold'),
#             text="(",bg="powder blue",command=lambda:btnclick("(")).grid(row=1,column="2")
#
# Btnbracket2=Button(cal,padx=16,pady=16,bd=8, fg="black",font=('arial', 20,'bold'),
#             text=")",bg="powder blue",command=lambda:btnclick(")")).grid(row=1,column="3")
# #=======================================================================================================================
#
# btn7=Button(cal,padx=16,pady=16,bd=8, fg="black",font=('arial', 20,'bold'),
#             text="7",bg="powder blue",command=lambda:btnclick(7)).grid(row=2,column="0")
#
# btn8=Button(cal,padx=16,pady=16,bd=8, fg="black",font=('arial', 20,'bold'),
#             text="8", bg="powder blue",command=lambda:btnclick(8)).grid(row=2,column="1")
#
# btn9=Button(cal,padx=16,pady=16,bd=8, fg="black",font=('arial', 20,'bold'),
#             text="9", bg="powder blue",command=lambda:btnclick(9)).grid(row=2,column="2")
#
# Division=Button(cal,padx=16,pady=16,bd=8, fg="black",font=('arial', 20,'bold'),
#             text="/",bg="powder blue",command=lambda:btnclick("/")).grid(row=2,column="3")
# #===========================================================================================================================
#
# btn6=Button(cal,padx=16,pady=16,bd=8, fg="black",font=('arial', 20,'bold'),
#             text="6",bg="powder blue",command=lambda:btnclick(6)).grid(row=3,column="0")
#
# btn5=Button(cal,padx=16,pady=16,bd=8, fg="black",font=('arial', 20,'bold'),
#             text="5",bg="powder blue",command=lambda:btnclick(5)).grid(row=3,column="1")
#
# btn4=Button(cal,padx=16,pady=16,bd=8, fg="black",font=('arial', 20,'bold'),
#             text="4",bg="powder blue",command=lambda:btnclick(4)).grid(row=3,column="2")
#
# subtraction=Button(cal,padx=16,pady=16,bd=8, fg="black",font=('arial', 20,'bold'),
#             text="-",bg="powder blue",command=lambda:btnclick("-")).grid(row=3,column="3")
# #===============================================================================================================================
#
# btn3=Button(cal,padx=16,pady=16,bd=8, fg="black",font=('arial', 20,'bold'),
#             text="3",bg="powder blue",command=lambda:btnclick(3)).grid(row=4,column="0")
#
# btn2=Button(cal,padx=16,pady=16,bd=8, fg="black",font=('arial', 20,'bold'),
#             text="2",bg="powder blue",command=lambda:btnclick(2)).grid(row=4,column="1")
#
# btn1=Button(cal,padx=16,pady=16,bd=8, fg="black",font=('arial', 20,'bold'),
#             text="1",bg="powder blue",command=lambda:btnclick(1)).grid(row=4,column="2")
#
# Multiplication=Button(cal,padx=16,pady=16,bd=8, fg="black",font=('arial', 20,'bold'),
#             text="*",bg="powder blue",command=lambda:btnclick("*")).grid(row=4,column="3")
# #==================================================================================================================================
#
# Btn0=Button(cal,padx=16,pady=16,bd=8, fg="black",font=('arial', 20,'bold'),
#             text="0",bg="powder blue",command=lambda:btnclick(0)).grid(row=5,column="0")
#
# Dot=Button(cal,padx=16,pady=16,bd=8, fg="black",font=('arial', 20,'bold'),
#             text=".",bg="powder blue",command=lambda:btnclick(".")).grid(row=5,column="1")
#
# Equal=Button(cal,padx=16,pady=16,bd=8, fg="black",font=('arial', 20,'bold'),
#             text="=",bg="powder blue",command=btnEqualsInput).grid(row=5,column="2")
#
# Addition=Button(cal,padx=16,pady=16,bd=8, fg="black",font=('arial', 20,'bold'),
#             text="+",bg="powder blue",command=lambda:btnclick("+")).grid(row=5,column="3")
#
#
#
# cal.mainloop()


# import pygame
# import tkinter as tkr
# from tkinter.filedialog import askdirectory
# import os
#
# music_player = tkr.Tk()
# music_player.title("My Music Player")
# music_player.geometry("450x350")
# directory = askdirectory()
# os.chdir(directory)
# song_list = os.listdir()
#
# play_list = tkr.Listbox(music_player, font="Helvetica 12 bold", bg='yellow', selectmode=tkr.SINGLE)
# for item in song_list:
#     pos = 0
#     play_list.insert(pos, item)
#     pos += 1
# pygame.init()
# pygame.mixer.init()
#
# def play():
#     pygame.mixer.music.load(play_list.get(tkr.ACTIVE))
#     var.set(play_list.get(tkr.ACTIVE))
#     pygame.mixer.music.play()
# def stop():
#     pygame.mixer.music.stop()
# def pause():
#     pygame.mixer.music.pause()
# def unpause():
#     pygame.mixer.music.unpause()
# Button1 = tkr.Button(music_player, width=5, height=3, font="Helvetica 12 bold", text="PLAY", command=play, bg="blue", fg="white")
# Button2 = tkr.Button(music_player, width=5, height=3, font="Helvetica 12 bold", text="STOP", command=stop, bg="red", fg="white")
# Button3 = tkr.Button(music_player, width=5, height=3, font="Helvetica 12 bold", text="PAUSE", command=pause, bg="purple", fg="white")
# Button4 = tkr.Button(music_player, width=5, height=3, font="Helvetica 12 bold", text="UNPAUSE", command=unpause, bg="orange", fg="white")
#
# var = tkr.StringVar()
# song_title = tkr.Label(music_player, font="Helvetica 12 bold", textvariable=var)
#
# song_title.pack()
# Button1.pack(fill="x")
# Button2.pack(fill="x")
# Button3.pack(fill="x")
# Button4.pack(fill="x")
# play_list.pack(fill="both", expand="yes")
# music_player.mainloop()


from turtle import *
state = {'turn': 0}
def spinner():
    clear()
    angle = state['turn']/10
    right(angle)
    forward(100)
    dot(120, 'yellow')
    back(100)
    right(120)
    forward(100)
    dot(120, 'green')
    back(100)
    right(120)
    forward(100)
    dot(120, 'red')
    back(100)
    right(120)
    update()
def animate():
    if state['turn']>0:
        state['turn']-=1

    spinner()
    ontimer(animate, 20)
def flick():
    state['turn']+=10

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
width(20)
onkey(flick, 'space')
listen()
animate()
done()