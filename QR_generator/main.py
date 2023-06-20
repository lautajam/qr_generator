from logic.data_management import search_data

text_qr, name_img, menu_var, go = "", "", "", True

folder, extension = search_data()

print("Hello! Welcome to link/text convert to QRcode")
print(folder, extension)