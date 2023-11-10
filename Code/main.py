from tkinter import *
from tkinter import filedialog

from data_processor import DataProcessor

data_processor = DataProcessor()


root = Tk()
root.title("METRICSTICS")

def open_file_dialog():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("CSV Files", "*.csv")])
    if file_path:
        path_textbox.delete(0, END)
        path_textbox.insert(0, file_path)

def calculate_metrics():
    data_processor.read_data(path_textbox.get())
    mean_value.set(data_processor.get_mean())
    median_value.set(data_processor.get_median())
    mode_value.set(data_processor.get_mode())
    min_value.set(data_processor.get_min_value())
    max_value.set(data_processor.get_max_value())
    std_value.set(data_processor.get_standard_deviation())
    mad_value.set(data_processor.get_mean_absolute_deviation())

def on_radio_button_click(value):
    if value == 2:
        data_processor.generate_random_data()
        path_textbox.delete(0, END)
        path_textbox.config(state="disabled")
        open_button.config(state="disabled")
    else:
        #data_processor.read_data(r"C:\Users\anant\OneDrive\Documents\MEngg\SOEN 6431 SCM\SOEN-6611-METRICSTICS\Code\list.txt")
        path_textbox.config(state="normal")
        open_button.config(state="normal")

mean_value = StringVar()
median_value = StringVar()
mode_value = StringVar()
min_value = StringVar()
max_value = StringVar()
std_value = StringVar()
mad_value = StringVar()

r = IntVar()
#Define Radio Button
radio1 = Radiobutton(root, text="Use custom data", variable=r, value=1, command=lambda: on_radio_button_click(1))
radio2 = Radiobutton(root, text="Generate randomized data", variable=r, value=2, command=lambda: on_radio_button_click(2))

# Radio positioning
radio1.grid(row=1, column= 0)
radio2.grid(row=1, column= 1)

# Define Input Textbox
path_textbox = Entry(root, width=35, borderwidth=5)
path_textbox.grid(row=2, column=1, columnspan=2, padx=10, pady=10)

# Define Labels
Label_mean = Label(root, textvariable = mean_value)
Label_title_mean = Label(root, text = "Mean:", anchor="e", justify="right")
Label_median = Label(root, textvariable = median_value)
Label_title_median = Label(root, text = "Median:", anchor="e", justify="right")
Label_mode = Label(root, textvariable = mode_value)
Label_title_mode = Label(root, text = "Mode:", anchor="e", justify="right")
Label_min = Label(root, textvariable = min_value)
Label_title_min = Label(root, text = "Minimum Value:", anchor="e", justify="right")
Label_max = Label(root, textvariable = max_value)
Label_title_max = Label(root, text = "Maximum Value:", anchor="e", justify="right")
Label_std = Label(root, textvariable = std_value)
Label_title_std = Label(root, text = "Standard Deviation:", anchor="e", justify="right")
Label_mad = Label(root, textvariable = mad_value)
Label_title_mad = Label(root, text = "Mean Absolute Deviation:", anchor="e", justify="right")

"""Label_filepath =  Label(root, text = "Enter file path", anchor="e", justify="right")"""

# Labels positioning
Label_title_mean.grid(row=4, column= 0, sticky="e")
Label_mean.grid(row=4, column= 1)
Label_title_median.grid(row=5, column= 0, sticky="e")
Label_median.grid(row=5, column= 1)
Label_title_mode.grid(row=6, column= 0, sticky="e")
Label_mode.grid(row=6, column= 1)
Label_title_min.grid(row=7, column= 0, sticky="e")
Label_min.grid(row=7, column= 1)
Label_title_max.grid(row=8, column= 0, sticky="e")
Label_max.grid(row=8, column= 1)
Label_title_std.grid(row=9, column= 0, sticky="e")
Label_std.grid(row=9, column= 1)
Label_title_mad.grid(row=10, column= 0, sticky="e")
Label_mad.grid(row=10, column= 1)

"""Label_filepath.grid(row=2, column=0, sticky="e")"""

# Define buttons

button_calculate= Button(root, text="Calculate Metrics", padx=30, pady=10, command= calculate_metrics)
open_button = Button(root, text="Open File", padx=10, pady=5, command=open_file_dialog)
# Button positioning

button_calculate.grid(row= 3, column=0, columnspan=2)
open_button.grid(row = 2, column = 0)

root.mainloop()