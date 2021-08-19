from tkinter import *
from tkinter import ttk
from tkinter.font import BOLD
from PIL import Image,ImageTk

root=Tk()
class login_window:
    def __init__(self,root):
        
        self.root=root
        self.root.title("Library Management System")
        self.root.geometry("1920x1080+0+0")      #width & height"

        

       

        #Adding background image
        self.bg=PhotoImage(file=r"C:\Users\91932\Desktop\Last year Project\Background.png")
        
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)        #to place image alignment right whenever window changes

        lbltitle=Label(self.root,text= "LIBRARY",fg="#427bff",bd=20,font=("Arial",35,"bold"))
        lbltitle.place(x=230,y=210)

        lbltitle=Label(self.root,text= "MANAGEMENT",fg="#427bff",bd=20,font=("Arial",35,"bold"))
        lbltitle.place(x=230,y=310)

        lbltitle=Label(self.root,text= "SYSTEM",fg="#427bff",bd=20,font=("Arial",35,"bold"))
        lbltitle.place(x=230,y=410)

        #to create frame on login page
        frame=Frame(self.root,bg="black")
        frame.place(x=880,y=170,width=340,height=450)
        
        #Icon
        img1=Image.open(r"C:\Users\91932\Desktop\Last year Project\Images\Icon.png")
        img1=img1.resize((100,100),Image.ANTIALIAS)         #antlialias convert high level image into low level image
        self.photoimage1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.photoimage1,bg="black",borderwidth=0)          #borderwidth cut extra borders
        lblimg1.place(x=990,y=175,width=100,height=100)


        get_str=Label(frame,text="Login Credentials",font=("times new roman",18,"bold"),fg="white",bg="black",relief=RIDGE)
        get_str.place(x=75,y=115)

        #label
        username=lbl=Label(frame,text="Username",font=("Courier",18,"bold"),fg="white",bg="black")
        username.place(x=70,y=165)

        self.txtuser=ttk.Entry(frame,font=("Arial",15))
        # self.txtuser.insert(10,'Username or Phonenumber')
        self.txtuser.place(x=50,y=200,width=270)

        password=lbl=Label(frame,text="Password",font=("Courier",18,"bold"),fg="white",bg="black")
        password.place(x=70,y=235)

        self.txtpass=ttk.Entry(frame,font=("Arial",15))
        # self.txtpass.insert(10,'Username or Phonenumber')
        self.txtpass.place(x=50,y=270,width=270)


        # Icon images
        img2=Image.open(r"C:\Users\91932\Desktop\Last year Project\Images\username.png")
        img2=img2.resize((27,27),Image.ANTIALIAS)         #antlialias convert high level image into low level image
        self.photoimage2=ImageTk.PhotoImage(img2)
        lblimg2=Label(image=self.photoimage2,bg="black",borderwidth=0)          #borderwidth cut extra borders
        lblimg2.place(x=928,y=340,width=25,height=25)

        img3=Image.open(r"C:\Users\91932\Desktop\Last year Project\Images\password.png")
        img3=img3.resize((27,27),Image.ANTIALIAS)         #antlialias convert high level image into low level image
        self.photoimage3img3=ImageTk.PhotoImage(img3)
        lblimg3=Label(image=self.photoimage3img3,bg="black",borderwidth=0)          #borderwidth cut extra borders
        lblimg3.place(x=928,y=410,width=25,height=25)

        #Loginbutton 
        loginbtn=Button(frame,text="Login",font=("Courier",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="#427bff",activeforeground="white",activebackground="#427bff")
        loginbtn.place(x=110,y=320,width=120,height=35)
        
        # registerbutton
        registrationbtn=Button(frame,text="New User Registration",font=("Courier",10,"bold"),borderwidth=0, relief=RIDGE,fg="white",bg="black",activeforeground="white",activebackground="black")
        registrationbtn.place(x=15,y=370,width=180)


        #forgetbutton
        Forgetbtn=Button(frame,text="Forget Password",font=("Courier",10,"bold"),borderwidth=0,relief=RIDGE,fg="white",bg="black",activeforeground="white",activebackground="black")
        Forgetbtn.place(x=20,y=390,width=120)

    

app=login_window(root)
root.mainloop()