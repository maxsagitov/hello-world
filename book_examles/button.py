import sys
from tkinter import Button, mainloop   # Tkinter в Python 2.6
x = Button(
text ='Press me',
command=(lambda:sys.stdout.write('Spam\n')))
x.pack()
mainloop()
