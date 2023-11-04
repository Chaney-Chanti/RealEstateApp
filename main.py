import customtkinter
from zillowModel import ZillowModel
from zillowView import ZillowView
from controller import Controller


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue") # blue green and dark blue

root = customtkinter.CTk()
root.geometry("1920x1080")

zillowModel = ZillowModel()
zillowView = ZillowView(root)
controller = Controller(zillowModel, zillowView)

#TODO: implement secure login function
def login():
    username = username_input.get()
    password = password_input.get()
    if username == "user" and password == "pass":
        for widget in login_frame.winfo_children():
            widget.destroy()
        login_frame.pack_forget()
        label = customtkinter.CTkLabel(root, text="Welcome to the Main Screen")
        label.pack()
    else:
        error_label.configure(text="Login failed. Please try again.")


#program starts here
login_frame = customtkinter.CTkFrame(master=root)
login_frame.pack(pady=20, padx=60, fill="both", expand=True)

# login_frame = customtkinter.CTkFrame(master=root)
# login_frame.pack()

welcome_label = customtkinter.CTkLabel(master=login_frame, text="Welcome!")
welcome_label.pack(pady=12, padx =10)

username_input = customtkinter.CTkEntry(master=login_frame, placeholder_text="Username")
username_input.pack(pady=12, padx=10)
password_input = customtkinter.CTkEntry(master=login_frame, placeholder_text="Password", show="*")
password_input.pack(pady=12, padx=10)

button = customtkinter.CTkButton(master=login_frame, text="Login", command=login)
button.pack(pady=12, padx=10)

checkbox = customtkinter.CTkCheckBox(master=login_frame, text="Remember Me")
button.pack(pady=15, padx=15)

error_label = customtkinter.CTkLabel(master=login_frame, text="", fg_color="red")
error_label.pack()


#graph ZHVI data
# controller.get_ZHVI()
# zillowView.display_Unemployment_Widget()

root.mainloop()




