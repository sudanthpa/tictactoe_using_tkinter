from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
from itertools import permutations

current_player = "O"
list1 = []
list2 = []
list3 = []


class Login:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1200x650")
        self.root.resizable(False, False)
        self.bg = ImageTk.PhotoImage(file="pic.jpg")
        self.bg_image = Label(self.root, image=self.bg).place(
            x=0, y=0, relwidth=1, relheight=1)
        self.root.title("Login Page")
        Login_Frame = Frame(self.root, bg="white").place(
            x=333, y=150, height=340, width=500)
        title_of_frame = Label(Login_Frame, text="Sign Up", font=(
            "Helvetica", 30, "bold"), fg="chocolate3", bg="white").place(x=375, y=180)
        username = Label(Login_Frame, text="Username", font=(
            "Helvetica", 12, "bold"), fg="chocolate3", bg="white").place(x=400, y=250)
        self.username_box = Entry(Login_Frame, font=(
            "times new roman", 15), bg="lightgray")
        self.username_box.place(x=400, y=270)
        password = Label(Login_Frame, text="Password", font=(
            "Helvetica", 12, "bold"), fg="chocolate3", bg="white").place(x=400, y=300)
        self.password_box = Entry(Login_Frame, font=(
            "times new roman", 15), bg="lightgray")
        self.password_box.place(x=400, y=320)
        forget_password = Button(Login_Frame, text="Forget Password?", bd=0, cursor="hand2", font=(
            "times new roman", 11), bg="white", fg="chocolate3", command=self.reset_password).place(x=400, y=350)
        Login_but = Button(self.root, command=self.login_check, text="Login", cursor="hand2", font=(
            "times new roman", 20), bg="white", fg="chocolate3").place(x=400, y=400)

    def reset_password(self):
        resetwindow = Toplevel(self.root)
        resetwindow.geometry("300x200")
        resetwindow.title("RESET PW PAGE")
        pass_message = Label(resetwindow, text="Instruction\n1.Change your password\nmanually in the code.", font=(
            "Helvetica", 10), fg="Red", bd=0).place(x=20, y=30)

    def login_check(self):
        if self.username_box.get() == "" or self.password_box.get() == "":
            messagebox.showerror("ERROR", "All fields must be filled!", parent=self.root)
        elif self.username_box.get() != 'sudan' or self.password_box.get() != '123':
            messagebox.showerror("ERROR", "Invalid username/password", parent=self.root)
        else:
            messagebox.showinfo("Welcome", "You have been logged in", parent=self.root)
            next_page_but = Button(self.root, cursor="hand2", font=(
                "times new roman", 13), text="Go-to next page", bd=0, bg="white", fg="black",
                                   command=self.createNewWindow).place(x=1070, y=10)
            next_page_but.pack()

    def createNewWindow(self):
        newWindow = Toplevel(self.root)
        newWindow.geometry("600x600")
        newWindow.resizable(False, False)
        newWindow.title("TIC-TAC-TOE")

        def current_player(number):
            global list1, list2, list3
            global current_player
            if current_player == "X":
                list2.append(number)
                list3.append(number)
                current_player = 'O'
                return current_player
            if current_player == "O":
                list1.append(number)
                list3.append(number)
                current_player = 'X'
                return current_player

        def check_for_win():
            global list1, list2, list3
            set1 = permutations([1, 2, 3])
            set2 = permutations([4, 5, 6])
            set3 = permutations([7, 8, 9])
            set4 = permutations([1, 4, 7])
            set5 = permutations([2, 5, 8])
            set6 = permutations([3, 6, 9])
            set7 = permutations([1, 5, 9])
            set8 = permutations([3, 5, 7])

            for i in set1, set2, set3, set4, set5, set6, set7, set8:
                for j in list(i):
                    plyr_1 = all(elem in list1 for elem in j)
                    plyr_2 = all(elem in list2 for elem in j)
                    if plyr_1 == True:
                        messagebox.showinfo("Game Result", "Player1(X) is the winner", parent=newWindow)
                        newWindow.destroy()
                        self.root.destroy()
                    elif plyr_2 == True:
                        messagebox.showinfo("Game Result", "Player2(O) is the winner", parent=newWindow)
                        newWindow.destroy()
                        self.root.destroy()
                    if len(list3) == 9:
                        messagebox.showinfo("Game Result", "Tie!", parent=newWindow)
                        newWindow.destroy()
                        self.root.destroy()

        def check_button(button):
            if button['state'] == NORMAL:
                button['state'] = DISABLED
            else:
                button['state'] = NORMAL

        def define_player(number, button):
            button.config(text=current_player(number))
            check_button(button)
            check_for_win()

        l1 = Label(newWindow, text="Player1 = 'X'")
        l1.grid(row=0, column=1)

        l2 = Label(newWindow, text="Player2 = 'O'")
        l2.grid(row=0, column=2)

        b1 = Button(newWindow, width=20, height=10, command=lambda: define_player(1, b1))
        b1.grid(row=1, column=1)

        b2 = Button(newWindow, width=20, height=10, command=lambda: define_player(2, b2))
        b2.grid(row=1, column=2)

        b3 = Button(newWindow, width=20, height=10, command=lambda: define_player(3, b3))
        b3.grid(row=1, column=3)

        b4 = Button(newWindow, width=20, height=10, command=lambda: define_player(4, b4))
        b4.grid(row=4, column=1)

        b5 = Button(newWindow, width=20, height=10, command=lambda: define_player(5, b5))
        b5.grid(row=4, column=2)

        b6 = Button(newWindow, width=20, height=10, command=lambda: define_player(6, b6))
        b6.grid(row=4, column=3)

        b7 = Button(newWindow, width=20, height=10, command=lambda: define_player(7, b7))
        b7.grid(row=8, column=1)

        b8 = Button(newWindow, width=20, height=10, command=lambda: define_player(8, b8))
        b8.grid(row=8, column=2)

        b9 = Button(newWindow, width=20, height=10, command=lambda: define_player(9, b9))
        b9.grid(row=8, column=3)


root = Tk()
obj = Login(root)
root.mainloop()