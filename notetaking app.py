from tkinter import *


def enter(*args):


    if len(position) == 0:
        position.append(40)

        notes.append(Notes(displaycan, entrybox.get(), 30, position[-1]))

        entrybox.delete(0, END)

        print(position)


    else:
        position.append(position[-1]+80)
        notes.append(Notes(displaycan, entrybox.get(), 30, position[-1]))


        entrybox.delete(0, END)


        print(position)


root = Tk()

root.geometry("500x580")
root.title("Note Taking app")
root.config(background="#ededd1")

root.resizable(FALSE, FALSE)


Label(root, text="Developed by Saadh Zahid", bg='#ededd1', fg="grey").place(x=20, y=400)

position = []
notes = []


displaycan = Canvas(root, bg="white", width=460 , height=460)
displaycan.place(x=19, y=20)


entrybox = Entry(root, width=40, borderwidth=1, font=('Helvetica', 15))

entrybox.place(x=30, y=500)


entrybox.bind("<Return>", enter)




class Notes:
    def __init__(self, master, note, notex, notey):
        
        def xbutton():
            self.click.destroy()
            self.display.destroy()
            position.remove(self.notey)
            print(position)
            print(self.notey)

        self.note =  note
        self.notex = notex
        self.notey = notey


        self.click = Button(displaycan, text="delete", command=xbutton, relief=FLAT, fg="red", bg="white", font=('Times New Roman', 10))
        self.click.place(x=notex+180, y=notey+5)

        self.display = Label(displaycan, text=self.note, bg='white', font=('Times New Roman', 20))
        self.display.place(x=notex, y=notey)



root.mainloop()