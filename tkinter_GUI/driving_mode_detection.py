from tkinter import *

root = Tk()
root.title('Driving Mode Detection')
width, height = 1000, 300
root.geometry(f'{width}x{height}')

def onKeyPress(event):

    key_char_upper = event.char.upper()

    if key_char_upper == ' ': # Space key
        label.config(bg='red', text='Brakes!!', font=('Noto Mono', 80))
    elif key_char_upper == 'W': # Up arrow key
        label.config(bg='green', text='Move Forward ↑', font=('Noto Mono', 60))
    elif key_char_upper == 'S': # Down arrow key
        label.config(bg='magenta', text='Move Backward ↓', font=('Noto Mono', 60))
    elif key_char_upper == 'A': # Left arrow key
        label.config(bg='orange', text='Turn Left ←', font=('Noto Mono', 60))
    elif key_char_upper == 'D': # Right arrow key
        label.config(bg='blue', text='Turn Right →', font=('Noto Mono', 60))
    else:
        label.config(bg='black', text='Command does not exist !!', font=('Noto Mono', 40))

label = Label(root, bg='black', fg='white', font=('Noto Mono', 26), width=width, height=height)
label.config(text='Remote Driving Control through SOME/IP')
label.pack()

root.bind('<KeyPress>', onKeyPress)


root.mainloop()