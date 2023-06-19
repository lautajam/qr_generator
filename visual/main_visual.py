import tkinter as tk

# Show Qr_gen frame
def qr_gen():
    print("QR generated.")
    main_frame.pack_forget()
    QR_gen_frame.pack()

# Show save_path frame
def save_path():
    print("The save path is...")
    main_frame.pack_forget()
    save_path_frame.pack()

# Show extension frame
def extension():
    print("The image extension is...")
    main_frame.pack_forget()
    extension_frame.pack()

# Quit app
def exit_app():
    print("You left.")
    root.quit()

# Hidde the actual frame and show main frame
def back_to_main_frame(frame):
    frame.pack_forget()
    main_frame.pack()
    print("Back to main menu")

# Prints on console the content and the name of the qr entered.
def submit():
    content_qr = content_qr_entry.get()
    print("QR content:", content_qr)
    name_qr = name_qr_entry.get()
    print("QR name:", name_qr)

# Creates the main window
root = tk.Tk()
root.title("Qr Generator")
root.geometry("700x300")

# Creates the main frame
main_frame = tk.Frame(root)

# Labels main frame
welcome_lbl = tk.Label(main_frame, text="Welcome to Qr Generator!")
welcome_lbl.pack()

option_lbl = tk.Label(main_frame, text="Select your option.")
option_lbl.pack()

# Buttons main frame
qr_gen_btn = tk.Button(main_frame, text="Qr generate", command=qr_gen)
qr_gen_btn.pack()

save_path_btn = tk.Button(main_frame, text="Select the save path", command=save_path)
save_path_btn.pack()

extension_btn = tk.Button(main_frame, text="Select the image extension", command=extension)
extension_btn.pack()

exit_app_btn = tk.Button(main_frame, text="Exit app", command=exit_app)
exit_app_btn.pack()

# FRAMES
#
# 
# Creates the QR_gen_frame frame

QR_gen_frame = tk.Frame(root)

QR_gen_frame_label = tk.Label(QR_gen_frame, text="This is the QR_gen screen.")
QR_gen_frame_label.pack()

content_qr_label = tk.Label(QR_gen_frame, text="The link/text exceeds the limit, please write a link/text of less than 2953 characters.")
content_qr_label.pack()
content_qr_entry = tk.Entry(QR_gen_frame)
content_qr_entry.pack()

name_qr_label = tk.Label(QR_gen_frame, text="Type here your name that you want to named the QRcode:")
name_qr_label.pack()
name_qr_entry = tk.Entry(QR_gen_frame)
name_qr_entry.pack()

create_qr_bt = tk.Button(QR_gen_frame, text="Create Qr code", command=submit)
create_qr_bt.pack()

QR_gen_frame_button = tk.Button(QR_gen_frame, text="Back", command=lambda: back_to_main_frame(QR_gen_frame))
QR_gen_frame_button.pack()


# Creates the QR_gen_frame frame
save_path_frame = tk.Frame(root)

save_path_label= tk.Label(save_path_frame, text="This is the save_path screen.")
save_path_label.pack()

save_path_button = tk.Button(save_path_frame, text="Back", command=lambda: back_to_main_frame(save_path_frame))
save_path_button.pack()

# Creates the QR_gen_frame frame
extension_frame = tk.Frame(root)

extension_label= tk.Label(extension_frame, text="This is the extension screen.")
extension_label.pack()

extension_button = tk.Button(extension_frame, text="Back", command=lambda: back_to_main_frame(extension_frame))
extension_button.pack()

# Show main frame at start and start the app loop
main_frame.pack()

root.mainloop()