from tkinter import*


class LibraryManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Library Management System")
        self.root.geometry("1920x1080+0+0")      #width & height
    
        #To set title alignment and fonts
        lbltitle=Label(self.root,text= "LIBRARY MANAGEMENT SYSTEM",bg="White",fg="#427bff",bd=20,relief=RIDGE,font=("times new roman",50,"bold"),padx=2,pady=6)
        lbltitle.pack(side=TOP ,fill=X)

        #to create frame
        frame=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="white")
        frame.place(x=0,y=130,width=1530,height=400)



if __name__ == "__main__":
    root=Tk()
    obj=LibraryManagementSystem(root)
    root.mainloop()
