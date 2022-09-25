from tkinter import *

root = Tk()
root.title('KeyPress TEST')
width, height = 1000, 300
root.geometry(f'{width}x{height}')

def onKeyPress(event):

    label_text = 'Key Char : ' + event.char + '\n' + \
        'Key Code : ' + str(event.keycode)

    label.config(text=label_text)


label = Label(root, bg='black', fg='white', font=('Noto Mono', 50), width=width, height=height)
label.config(text='KeyPress TEST')
label.pack()

root.bind('<KeyPress>', onKeyPress)


root.mainloop()