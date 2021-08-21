#import libraries
from tkinter import*
from PIL import ImageTk,Image
from custom_button import TkinterCustomButton

#creat window
root=Tk()
root.title("Grocery store")
root.iconbitmap("image\logo.ico")


#to  get fit on screen 
window_width=root.winfo_screenwidth()
window_height=root.winfo_screenheight()
root.geometry("{}x{}+0+0".format(window_width,window_height))

#============variable===================
user=StringVar()
passd=StringVar()


# #==========Backgroundimage=============
bg_image=Image.open("image\girl.jpg")
bg_image=bg_image.resize((window_width,window_height),Image.ANTIALIAS)
bg_image=ImageTk.PhotoImage(bg_image)

#place on the window
Label(root,image=bg_image).place(relx=0,rely=0)

#add admin photo
logo1=ImageTk.PhotoImage((Image.open("image\employe.png").resize((200,200))))
button=Button(root,image=logo1,borderwidth=3,bg="white",relief=RIDGE)
button.place(relx=0.4,rely=0.1,width=200,height=190)



#add new window
new_window=Toplevel(root)
new_window.title("Login")
new_window.geometry("{}x{}+{}+{}".format(window_width//4, window_height//3,
                        int(window_width/3), window_height//3))
new_window.iconbitmap("image\logoo.ico")

#login logo
login_logo=ImageTk.PhotoImage(Image.open("image\log.png").resize((35,35)))
Label(new_window,image=login_logo).place(relx=0.1,rely=0.25)
Label(new_window,text='Username', font="-family {Poppins} -size 15" ).place(relx=0.1, rely=0.1)


# login entry
entry1 =Entry(new_window)
entry1.place(relx=0.25, rely=0.28, relwidth=0.7, relheight=0.10)
entry1.configure(font="-family {Poppins} -size 10")
entry1.configure(relief="flat")
entry1.configure(textvariable=user) 

#pass logo
passlog=ImageTk.PhotoImage(Image.open("image\password.png").resize((35,35)))
Label(new_window,image=passlog).place(relx=0.1,rely=0.57)
Label(new_window,text='Password', font="-family {Poppins} -size 15" ).place(relx=0.1, rely=0.42)


# pass entry
entry1 =Entry(new_window)
entry1.place(relx=0.25, rely=0.6, relwidth=0.7, relheight=0.10)
entry1.configure(font="-family {Poppins} -size 10")
entry1.configure(relief="flat")
entry1.configure(textvariable=passd) 

#login_button
but=TkinterCustomButton(master=new_window, corner_radius=20,text="LOGIN")
but.place(relx=0.5, rely=0.85,  anchor=CENTER)




root.mainloop()