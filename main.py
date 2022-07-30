############################ Modules ############################
from tkinter import *
from tkinter import ttk, filedialog
from tkinter.colorchooser import askcolor
from PIL import Image, ImageDraw, ImageFont
import cv2

############################ Variables ############################
root = Tk()
ui_theme = IntVar()
global font_size
font_size = IntVar()
rotation_angle = IntVar()

############################ Functions ############################
def browse_input():
    global input_path
    with open("./bin/input_extensions.txt",mode = "r") as ip:
        input_extension_file = ip.read()
    input_path = filedialog.askopenfilename(filetypes=[("Picture files", input_extension_file)])
    input_path_entry.delete(0, "")
    input_path_entry.insert(0, input_path)

def browse_output():
    global output_path
    output_path = filedialog.askdirectory()+"/"
    output_path_entry.delete(0, "")
    output_path_entry.insert(0, output_path)

def browse_names():
    global names_path
    names_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    names_path_entry.delete(0, "")
    names_path_entry.insert(0, names_path)
    with open(names_path,mode = "r") as fo:
        global names
        names = fo.read().splitlines()
    name_quantity_number_lable.configure(text=len(names))

def browse_font():
    global font_path
    font_path = filedialog.askopenfilename(filetypes=[("Font files", "*.ttf")])
    font_entry.delete(0, "")
    font_entry.insert(0, font_path)

def build_pictures():
    font = ImageFont.truetype(font_path, font_size.get())
    for x in range(len(names)):
        img = Image.open(input_path)
        I1 = ImageDraw.Draw(img)
        I1.text((x_cord, y_cord), names[x], fill =(colors[0]), font=font)
        img.save(output_path+names[x]+"-"+collection_entry.get()+file_extension.get())

def build_pictures_test():
    font = ImageFont.truetype(font_path, font_size.get())
    test_img = Image.open(input_path)
    I1 = ImageDraw.Draw(test_img)
    I1.text((x_cord, y_cord), "LukasFischer", fill =(colors[0]), font=font)
    test_img.show()

def ui_theme_func():
    if ui_theme.get():
        root.tk.call("set_theme", "light")
    else:
        root.tk.call("set_theme", "dark")

def pick_color():
    global colors
    colors = askcolor(title="Color Chooser")
    rgb_code_lable.configure(text=colors[0])

def driver_event():
    global img
    img = cv2.imread(input_path, 1)
    cv2.imshow('image', img)
    cv2.setMouseCallback('image', click_event)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def click_event(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        global x_cord, y_cord
        x_cord = x
        y_cord = y
        x_cord_data_lable.configure(text=x_cord)
        y_cord_data_lable.configure(text=y_cord)
        cv2.destroyAllWindows()

def validate(P):                                                   # max length for entry widget
    if len(P) <= 0:
        # empty Entry is ok
        return True
    elif len(P) <= 3 and P.isdigit():
        # Entry with 3 digit is ok
        return True
    else:
        # Anything else, reject it
        return False

vcmd = (root.register(validate), '%P')

def output_file():
    with open("./bin/output_extensions.txt",mode = "r") as ip:
        global output_extension_file
        output_extension_file = ip.read()
    

############################ Window settings ############################
root.title("Image GUI")
root.iconbitmap("./bin/icon.ico")
root.geometry("885x670")
root.resizable(width=False, height=False)

############################ Frame ############################
check_frame = ttk.LabelFrame(root, text="Input/Output Settings", padding=(20, 10))
check_frame.grid(row=0, column=0, padx=(20, 5), pady=(10, 5), sticky="nsew")

general_frame = ttk.LabelFrame(text="General settings", padding=(20, 10))
general_frame.grid(row=1, column=0, padx=(20, 5), pady=(5, 5), sticky="nsew")

color_frame = ttk.LabelFrame(general_frame, text="Font Color", padding=(20, 10))
color_frame.grid(row=0, column=0, columnspan=2, padx=(5, 5), pady=(5, 5), sticky="nsew")

cords_frame = ttk.LabelFrame(general_frame, text="Cords", padding=(20, 10))
cords_frame.grid(row=0, column=2, columnspan=2, padx=(5, 5), pady=(5, 5), sticky="nsew")

rotation_frame = ttk.LabelFrame(general_frame, text="Rotation", padding=(20, 10))
rotation_frame.grid(row=0, column=4, padx=(5, 5), pady=(5, 5), sticky="nsew")

collection_frame = ttk.LabelFrame(general_frame, text="Collection name", padding=(20, 10))
collection_frame.grid(row=1, column=0, columnspan=2, padx=(5, 5), pady=(5, 5), sticky="nsew")

names_frame = ttk.LabelFrame(general_frame, text="Names Quantity", padding=(20, 10))
names_frame.grid(row=1, column=2, padx=(5, 5), pady=(5, 5), sticky="nsew")

size_frame = ttk.LabelFrame(general_frame, text="Font size", padding=(20, 10))
size_frame.grid(row=2, column=2, padx=(5, 5), pady=(5, 5), sticky="nsew")

extension_frame = ttk.LabelFrame(general_frame, text="Output extension", padding=(20, 10))
extension_frame.grid(row=2, column=3, padx=(5, 5), pady=(5, 5), sticky="nsew")

theme_frame = ttk.LabelFrame(general_frame, text="UI Theme", padding=(20, 10))
theme_frame.grid(row=1, column=3, padx=(5, 5), pady=(5, 5), sticky="nsew")

############################ Label ############################
input_lable = Label(check_frame, text="Input file")
input_lable.grid(row=0, column=0, padx=5, pady=10, sticky="nsew")

name_lable = Label(check_frame, text="Name List\n (.txt file)")
name_lable.grid(row=1, column=0, padx=5, pady=10, sticky="nsew")

font_lable = Label(check_frame, text="Choose a font\n (.ttf file)")
font_lable.grid(row=2, column=0, padx=5, pady=10, sticky="nsew")

output_lable = Label(check_frame, text="Output Path")
output_lable.grid(row=3, column=0, padx=5, pady=10, sticky="nsew")

rgb_lable = Label(color_frame, text="RGB Value")
rgb_lable.grid(row=0, column=0, padx=5, pady=10, sticky="nsew")

rgb_code_lable = Label(color_frame, text="0, 0, 0", width= 9)
rgb_code_lable.grid(row=0, column=1, padx=5, pady=10, sticky="nsew")

x_cord_lable = Label(cords_frame, text="X Cord")
x_cord_lable.grid(row=0, column=0, padx=5, pady=10, sticky="nsew")

y_cord_lable = Label(cords_frame, text="Y Cord")
y_cord_lable.grid(row=1, column=0, padx=5, pady=10, sticky="nsew")

x_cord_data_lable = Label(cords_frame, text="---")
x_cord_data_lable.grid(row=0, column=1, padx=5, pady=10, sticky="nsew")

y_cord_data_lable = Label(cords_frame, text="---")
y_cord_data_lable.grid(row=1, column=1, padx=5, pady=10, sticky="nsew")

rotation_lable = Label(rotation_frame, text="Angle")
rotation_lable.grid(row=0, column=0, padx=5, pady=10, sticky="nsew")

name_quantity_lable = Label(names_frame, text="Names")
name_quantity_lable.grid(row=0, column=0, padx=5, pady=10, sticky="nsew")

name_quantity_number_lable = Label(names_frame, text="0")
name_quantity_number_lable.grid(row=0, column=1, padx=5, pady=10, sticky="nsew")

collection_lable = Label(collection_frame, text="(output: name-collection_name.png)")
collection_lable.grid(row=3, column=0, padx=0, pady=0, sticky="nsew")

############################ Entrys ############################
input_path_entry = ttk.Entry(check_frame, width=97)
input_path_entry.insert(0, "")
input_path_entry.grid(row=0, column=1, padx=5, pady=10, sticky="nsew")

names_path_entry = ttk.Entry(check_frame, width=97)
names_path_entry.insert(0, "")
names_path_entry.grid(row=1, column=1, padx=5, pady=10, sticky="nsew")

font_entry = ttk.Entry(check_frame, width=97)
font_entry.insert(0, "")
font_entry.grid(row=2, column=1, padx=5, pady=10, sticky="nsew")

output_path_entry = ttk.Entry(check_frame, width=97)
output_path_entry.insert(0, "")
output_path_entry.grid(row=3, column=1, padx=5, pady=10, sticky="nsew")

collection_entry = ttk.Entry(collection_frame, width=40)
collection_entry.insert(0, "")
collection_entry.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")

############################ Buttons ############################
browse_pic_button = ttk.Button(check_frame, text="Browse", command=browse_input)
browse_pic_button.grid(row=0, column=2, padx=5, pady=10, sticky="nsew")

browse_names_button = ttk.Button(check_frame, text="Browse", command=browse_names)
browse_names_button.grid(row=1, column=2, padx=5, pady=10, sticky="nsew")

browse_font_button = ttk.Button(check_frame, text="Browse", command=browse_font)
browse_font_button.grid(row=2, column=2, padx=5, pady=10, sticky="nsew")

browse_output_button = ttk.Button(check_frame, text="Browse", command=browse_output)
browse_output_button.grid(row=3, column=2, padx=5, pady=10, sticky="nsew")

test_build_button = ttk.Button(general_frame, text="Show an example Picture", command=build_pictures_test, width=25)
test_build_button.grid(row=1, column=4, padx=5, pady=10, sticky="nsew")

build_button = ttk.Button(general_frame, text="Build", command=build_pictures, style="Accent.TButton", width=25)
build_button.grid(row=2, column=4, padx=5, pady=10, sticky="nsew")

pick_color_button = ttk.Button(color_frame, text="Pick color", command=pick_color)
pick_color_button.grid(row=0, column=2, padx=5, pady=10, sticky="nsew")

cord_button = ttk.Button(cords_frame, text="Choose cord", command=driver_event)
cord_button.grid(row=0, column=2, rowspan=2, padx=5, pady=10, sticky="nsew")

#test_button = ttk.Button(text="Print size", command=driver_event)
#test_button.grid(row=3, column=0, padx=5, pady=10, sticky="nsew")

############################ Spinbox ############################

font_size_box = ttk.Spinbox(size_frame, from_=0, to=500, increment=0.5, textvariable=font_size, width=10)
font_size_box.insert(0, "1")
font_size_box.grid(row=0, column=0, padx=5, pady=10, sticky="nsew")

rotation_box = ttk.Spinbox(rotation_frame, from_=0, to=360, increment=0.5, textvariable=rotation_angle, width=10, validate="key", validatecommand=vcmd)
rotation_box.insert(0, "")
rotation_box.grid(row=0, column=1, padx=5, pady=10, sticky="nsew")

############################ Combobox ############################
file_extension = ttk.Combobox(extension_frame, width=10, values= output_extension_file )
file_extension.grid(row=0, column=0, padx=5, pady=10, sticky="nsew")
file_extension.current(0)

############################ Switch ############################
theme_switch = ttk.Checkbutton(theme_frame, style="Switch.TCheckbutton", onvalue=0, offvalue=1, variable=ui_theme, command=ui_theme_func)
theme_switch.grid(row=0, column=0, padx=5, pady=10, sticky="nsew")

############################ Theme ############################
root.call("source", "./bin/azure.tcl")
root.tk.call("set_theme", "dark")

############################ GUI Start ############################
if __name__ == "__main__" :
    root.mainloop()
    output_file