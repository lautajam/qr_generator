import tkinter as tk

def qr_gen():
    print("QR generated.")

def save_path():
    print("The save path is...")

def extension():
    print("The image extension is...")

def exit_app():
    print("You left.")

# Creates the window
root = tk.Tk()
root.title("Qr Generator")
root.geometry("300x200")

# Title and subtitle
welcome_lbl = tk.Label(root, text="Welcome to Qr Generator!")
welcome_lbl.pack()

option_lbl = tk.Label(root, text="Select your option.")
option_lbl.pack()

# Buttons
qr_gen_btn = tk.Button(root, text="Qr generate", command=qr_gen)
qr_gen_btn.pack()

save_path_btn = tk.Button(root, text="Select the save path", command=save_path)
save_path_btn.pack()

extension_btn = tk.Button(root, text="Select the image extesion", command=extension)
extension_btn.pack()

exit_app_btn = tk.Button(root, text="Exit app", command=exit_app)
exit_app_btn.pack()

root.mainloop()