import customtkinter as tk
import pyperclip

tk.set_appearance_mode("System")
tk.set_default_color_theme("dark-blue")

root = tk.CTk()
root.title("Text Repeater")
root.geometry("400x600")

vault = ""
def generate_text():
    text = user_input.get()
    user_num = int(num.get())
    global vault
    vault = "\n".join([text]*user_num)
    label.configure(text=vault,font=("Arial",30))

def generate_text_paragraph():
    text = user_input.get()
    user_num = int(num.get())
    global label
    paragrpah_text = text * user_num
    label.configure(text=paragrpah_text,font=("Arial",30),wraplength=280)

def popup_disable():
    label1.configure(text="")

def copy_text():
    try:
        text = label.cget("text")
        pyperclip.copy(text)
        label1.configure(text="Text copied to clipboard!",font=("Arial",15))
        root.after(3000,popup_disable)
    except NameError:
        global vault
        pyperclip.copy(vault)
        label1.configure(text="Text copied to clipboard!",font=("Arial",15))
        root.after(3000,popup_disable)

def main():
    if checkbox_var.get():
        generate_text()
    else:
        generate_text_paragraph()

def clear():
    global vault
    vault = ""
    label.configure(text="")

user_input = tk.CTkEntry(master=root,placeholder_text="Enter your text  here",width=300,height=50,font=("Arial", 20))
user_input.pack(pady=20)

num = tk.CTkEntry(master=root,placeholder_text="Enter the quantity here",width=250,height=30,font=("Arial", 15))
num.pack()

inner_frame = tk.CTkFrame(master=root,fg_color="transparent")
inner_frame.pack(pady=10)

main_frame = tk.CTkScrollableFrame(master=root,border_width=2,orientation="vertical")
main_frame.pack(fill="both",expand=True,padx=30,pady=30)

label = tk.CTkLabel(master=main_frame,text="",font=("Arial",30),wraplength=280)
label.pack()

generate_button = tk.CTkButton(master=inner_frame,text="Generate",command=main,height=30,width=70,font=("Arial",17,"bold"))
generate_button.pack(side="left",padx=10,pady=10)

clear_button = tk.CTkButton(master=inner_frame,text="Clear",height=30,command=clear,width=70,font=("Arial",17,"bold"))
clear_button.pack(side="left",padx=10,pady=10)

checkbox_var = tk.BooleanVar()
new_line_cbox = tk.CTkCheckBox(master=inner_frame,text="Enable New Line",height=30,width=70,font=("Arial",17,"bold"),variable=checkbox_var)
new_line_cbox.pack(side="bottom",pady=10)

label1 = tk.CTkLabel(master=root,text="",font=("Arial",10))
label1.pack()

copy_button = tk.CTkButton(master=root,text="Copy Text",height=30,width=70,font=("Arial",17,"bold"),command=copy_text)
copy_button.pack(pady=40)

root.mainloop()