# Show Qr_gen frame
def qr_gen(main_frame, QR_gen_frame):
    print("Now in the qr generator window.")
    main_frame.pack_forget()
    QR_gen_frame.pack()

# Show save_path frame
def save_path(main_frame, save_path_frame):
    print("Now in the save path window.")
    main_frame.pack_forget()
    save_path_frame.pack()

# Show extension frame
def extension(main_frame, extension_frame):
    print("Now in the extension window.")
    main_frame.pack_forget()
    extension_frame.pack()

# Quit app
def exit_app(root):
    print("You left.")
    root.quit()

# Hide the current frame and show main frame
def back_to_main_frame(frame, main_frame):
    frame.pack_forget()
    main_frame.pack()
    print("Back to main menu")

# Prints on console the content and the name of the qr entered.
def create(content_qr_entry, name_qr_entry):
    print("QR content:", content_qr_entry)
    print("QR name:", name_qr_entry)

# Prints on console the changed path
def change_path(sp_path_entry):
    print("The new save path is:", sp_path_entry)

# Prints on console the changed extension
def change_extension(ext_path_entry):
    print("The new extension is:", ext_path_entry)