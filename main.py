import customtkinter
import User #not sure if i need a class for this just because the data is so small
from zillowModel import ZillowModel
from zillowView import ZillowView
from controller import Controller
import requests
from widgets.navbar import Navbar

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue") # blue green and dark blue

root = customtkinter.CTk()
root.geometry("1920x1080")

zillowModel = ZillowModel()
zillowView = ZillowView(root)
controller = Controller(zillowModel, zillowView)

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)
state = 'login'

#TODO: implement a more secure login function
# and URLs will update when officially uploaded
def login(username_input, password_input, error_label):
    login_url = "http://127.0.0.1:5000/login"
    PARAMS = {
         'username': username_input.get(),
         'password': password_input.get(),
    }
    res = requests.post(url=login_url, data=PARAMS)
    if  res.status_code == 200:
        update_frame('homepage')
    else:
        error_label.configure(text="Login failed. Please try again.")

def register(username_input, password_input, email_input, error_label):
    register_url = "http://127.0.0.1:5000/register"
    PARAMS = {
         'username': username_input.get(),
         'password': password_input.get(),
         'email': email_input.get()
    }
    res = requests.post(url=register_url, data=PARAMS)
    if res.status_code == 200:
        update_frame('login')
    else:
        error_label.configure(text="Register failed. Please try again.")

def display_login_frame():
    welcome_label = customtkinter.CTkLabel(master=frame, text="Welcome, Please Login!")
    welcome_label.pack(pady=12, padx =10)
    username_input = customtkinter.CTkEntry(master=frame, placeholder_text="Username")
    username_input.pack(pady=12, padx=10)
    password_input = customtkinter.CTkEntry(master=frame, placeholder_text="Password", show="*")
    password_input.pack(pady=12, padx=10)
    error_label = customtkinter.CTkLabel(master=frame, text="", fg_color="red")
    error_label.pack()

    login_button = customtkinter.CTkButton(master=frame, text="Login", command=lambda: login(username_input, password_input, error_label))
    login_button.pack(pady=12, padx=10)

    login_register_button = customtkinter.CTkButton(master=frame, text="Register", command=lambda: update_frame('register'))
    login_register_button.pack(pady=12, padx=10)

    checkbox = customtkinter.CTkCheckBox(master=frame, text="Remember Me")
    checkbox.pack(pady=15, padx=15)

def display_register_frame():
    register_welcome_label = customtkinter.CTkLabel(master=frame, text="Welcome, Please Register An Account :)")
    register_welcome_label.pack(pady=12, padx =10)
    register_username_input = customtkinter.CTkEntry(master=frame, placeholder_text="Username")
    register_username_input.pack(pady=12, padx=10)
    register_password_input = customtkinter.CTkEntry(master=frame, placeholder_text="Password", show="*")
    register_password_input.pack(pady=12, padx=10)
    register_email_input = customtkinter.CTkEntry(master=frame, placeholder_text="Email")
    register_email_input.pack(pady=12, padx=10)
    register_button = customtkinter.CTkButton(master=frame, text="Register", command=lambda: register(register_username_input, 
                                                                                                            register_password_input, 
                                                                                                            register_email_input,
                                                                                                            error_label))
    register_button.pack(pady=12, padx=10)

    error_label = customtkinter.CTkLabel(master=frame, text="", fg_color="red")
    error_label.pack()

def display_homepage():
    navbar = Navbar(frame)
    navbar.display()
    label = customtkinter.CTkLabel(root, text="Welcome to the Main Screen", fg_color="red")
    label.pack(pady=12, padx=10)
    print('hello')

def update_frame(state_change=None):
    global state
    if state_change != None:
        state = state_change
    for widget in frame.winfo_children():
        widget.destroy()
    if (state == 'login'):
        display_login_frame()
    elif (state == 'register'):
         display_register_frame()
    elif (state == 'homepage'):
        display_homepage()

# program starts here (create state machine here)
def main():
    update_frame('homepage')
    root.mainloop()

if __name__ == "__main__":
    main()

# graph ZHVI data
# controller.get_ZHVI()
# zillowView.display_Unemployment_Widget()




