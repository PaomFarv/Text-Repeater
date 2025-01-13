import customtkinter as tk
tk.set_appearance_mode("System")
tk.set_default_color_theme("green")

root = tk.CTk()
root.title("Text Repeater")
root.geometry("400x500")

def generate_text():
    text = user_input.get()
    user_num = int(num.get())
    
    for i in range(user_num+1):
        label = tk.CTkLabel(master=main_frame,text=text,font=("Arial",30))
        label.pack(pady=10)

def clear():
    for text in main_frame.winfo_children():
        text.destroy()

user_input = tk.CTkEntry(master=root,placeholder_text="Enter your text  here",width=300,height=50,font=("Arial", 20))
user_input.pack(pady=20)

num = tk.CTkEntry(master=root,placeholder_text="Enter the quantity here",width=250,height=30,font=("Arial", 15))
num.pack()

inner_frame = tk.CTkFrame(master=root,fg_color="transparent")
inner_frame.pack(pady=10)

main_frame = tk.CTkScrollableFrame(master=root,border_width=2,orientation="vertical")
main_frame.pack(fill="both",expand=True,padx=30,pady=30)

generate_button = tk.CTkButton(master=inner_frame,text="Generate",command=generate_text,height=30,width=70,font=("Arial",17,"bold"))
generate_button.pack(side="left",padx=10,pady=10)

clear_button = tk.CTkButton(master=inner_frame,text="Clear",height=30,command=clear,width=70,font=("Arial",17,"bold"))
clear_button.pack(side="left",padx=10,pady=10)

root.mainloop()