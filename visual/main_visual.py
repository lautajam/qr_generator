import tkinter as tk
from functions import *

# Creates the main window
root = tk.Tk()
root.title("Qr Generator")
root.geometry("700x200")

# Creates the main frame
main_frame = tk.Frame(root)

#--- FRAMES ---#


# Creates the QR_gen_frame frame
QR_gen_frame = tk.Frame(root)

QR_gen_frame_label = tk.Label(QR_gen_frame, text="This is the QR generator.")
QR_gen_frame_label.pack()

content_qr_label = tk.Label(QR_gen_frame, text="The link/text exceeds the limit, please write a link/text of less than 2953 characters.")
content_qr_label.pack()
content_qr_entry = tk.Entry(QR_gen_frame)
content_qr_entry.pack()

name_qr_label = tk.Label(QR_gen_frame, text="Type here your name that you want to named the QRcode:")
name_qr_label.pack()
name_qr_entry = tk.Entry(QR_gen_frame)
name_qr_entry.pack()

create_qr_bt = tk.Button(QR_gen_frame, text="Create Qr code", command=lambda: create(content_qr_entry.get(), name_qr_entry.get()))
create_qr_bt.pack()

QR_gen_frame_button = tk.Button(QR_gen_frame, text="Back", command=lambda: back_to_main_frame(QR_gen_frame, main_frame))
QR_gen_frame_button.pack()



# Creates the save path frame
save_path_frame = tk.Frame(root)

sp_title_label= tk.Label(save_path_frame, text="Your path now is:")
sp_title_label.pack()
sp_label1= tk.Label(save_path_frame, text="*PATH*")
sp_label1.pack()
sp_label2= tk.Label(save_path_frame, text="Please, type in the path to save the image")
sp_label2.pack()
sp_path_entry = tk.Entry(save_path_frame)
sp_path_entry.pack()
sp_path_bt = tk.Button(save_path_frame, text="Change save path", command=lambda: change_path(sp_path_entry.get()))
sp_path_bt.pack()

save_path_button = tk.Button(save_path_frame, text="Back", command=lambda: back_to_main_frame(save_path_frame, main_frame))
save_path_button.pack()



# Creates the extension frame
extension_frame = tk.Frame(root)

sp_title_label= tk.Label(extension_frame, text="Your extesion now is:")
sp_title_label.pack()
ext_label1= tk.Label(extension_frame, text="*EXTENSION*")
ext_label1.pack()
ext_label2= tk.Label(extension_frame, text="(Valid extensions: 'jpg', 'jpeg', 'png', 'gif', 'bmp', 'svg' and 'tiff')")
ext_label2.pack()
ext_label3= tk.Label(extension_frame, text="Please, type in the valid image extension.")
ext_label3.pack()
ext_path_entry = tk.Entry(extension_frame)
ext_path_entry.pack()
ext_path_bt = tk.Button(extension_frame, text="Change save path", command=lambda: change_extension(ext_path_entry.get()))
ext_path_bt.pack()

extension_button = tk.Button(extension_frame, text="Back", command=lambda: back_to_main_frame(extension_frame, main_frame))
extension_button.pack()



# Labels main frame
welcome_lbl = tk.Label(main_frame, text="Welcome to Qr Generator!")
welcome_lbl.pack()

option_lbl = tk.Label(main_frame, text="Select your option.")
option_lbl.pack()

# Buttons main frame
qr_gen_btn = tk.Button(main_frame, text="Qr generate", command=lambda: qr_gen(main_frame, QR_gen_frame))
qr_gen_btn.pack()

save_path_btn = tk.Button(main_frame, text="Select the save path", command=lambda: save_path(main_frame, save_path_frame))
save_path_btn.pack()

extension_btn = tk.Button(main_frame, text="Select the image extension",  command=lambda: extension(main_frame, extension_frame))
extension_btn.pack()

exit_app_btn = tk.Button(main_frame, text="Exit app", command=lambda: exit_app(root))
exit_app_btn.pack()



# Show main frame at start and start the app loop
main_frame.pack()

root.mainloop()