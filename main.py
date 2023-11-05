import customtkinter
import User
from zillowModel import ZillowModel
from zillowView import ZillowView
from controller import Controller
import requests

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue") # blue green and dark blue

root = customtkinter.CTk()
root.geometry("1920x1080")

zillowModel = ZillowModel()
zillowView = ZillowView(root)
controller = Controller(zillowModel, zillowView)

login_frame = customtkinter.CTkFrame(master=root)
login_frame.pack(pady=20, padx=60, fill="both", expand=True)

#TODO: implement secure login function
def login(username_input, password_input, error_label):
    login_url = "http://127.0.0.1:5000/login"
    PARAMS = {
         'username': username_input.get(),
         'password': password_input.get(),
    }
    res = requests.post(url=login_url, data=PARAMS)
    if  res.status_code == 200:
        for widget in login_frame.winfo_children():
            widget.destroy()
        login_frame.pack_forget()
        label = customtkinter.CTkLabel(root, text="Welcome to the Main Screen")
        label.pack()
    else:
        error_label.configure(text="Login failed. Please try again.")

def register(username_input, password_input, email_input):
    register_url = "http://127.0.0.1:5000/register"
    PARAMS = {
         'username': username_input.get(),
         'password': password_input.get(),
         'email': email_input.get()
    }
    res = requests.post(url=register_url, data=PARAMS)
    data = res.json()
    print(data)

def display_login_frame():
    welcome_label = customtkinter.CTkLabel(master=login_frame, text="Welcome, Please Login!")
    welcome_label.pack(pady=12, padx =10)
    username_input = customtkinter.CTkEntry(master=login_frame, placeholder_text="Username")
    username_input.pack(pady=12, padx=10)
    password_input = customtkinter.CTkEntry(master=login_frame, placeholder_text="Password", show="*")
    password_input.pack(pady=12, padx=10)
    error_label = customtkinter.CTkLabel(master=login_frame, text="", fg_color="red")
    error_label.pack()

    login_button = customtkinter.CTkButton(master=login_frame, text="Login", command=lambda: login(username_input, password_input, error_label))
    login_button.pack(pady=12, padx=10)

    login_register_button = customtkinter.CTkButton(master=login_frame, text="Register", command=display_register_frame)
    login_register_button.pack(pady=12, padx=10)

    checkbox = customtkinter.CTkCheckBox(master=login_frame, text="Remember Me")
    checkbox.pack(pady=15, padx=15)

def display_register_frame():
        for widget in login_frame.winfo_children():
            widget.destroy()
        register_welcome_label = customtkinter.CTkLabel(master=login_frame, text="Welcome, Please Register An Account :)")
        register_welcome_label.pack(pady=12, padx =10)
        register_username_input = customtkinter.CTkEntry(master=login_frame, placeholder_text="Username")
        register_username_input.pack(pady=12, padx=10)
        register_password_input = customtkinter.CTkEntry(master=login_frame, placeholder_text="Password", show="*")
        register_password_input.pack(pady=12, padx=10)
        register_email_input = customtkinter.CTkEntry(master=login_frame, placeholder_text="Email")
        register_email_input.pack(pady=12, padx=10)
        register_button = customtkinter.CTkButton(master=login_frame, text="Register", command=lambda: register(register_username_input, 
                                                                                                                register_password_input, 
                                                                                                                register_email_input))
        register_button.pack(pady=12, padx=10)

# program starts here (create state machine here)
display_login_frame()

#graph ZHVI data
# controller.get_ZHVI()
# zillowView.display_Unemployment_Widget()

root.mainloop()




