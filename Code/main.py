from tkinter import *
from tkinter import filedialog
from tkinter import ttk  # Import the themed button

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
path_textbox = ttk.Entry(root, width=35, font=('Arial', 10))
path_textbox.grid(row=2, column=1, columnspan=2, padx=10, pady=10, sticky="ew")

# Define Labels

labels = ["Mean:", "Median:", "Mode:", "Minimum Value:", "Maximum Value:", "Standard Deviation:", "Mean Absolute Deviation:"]
label_vars = [mean_value, median_value, mode_value, min_value, max_value, std_value, mad_value]

for i, label_text in enumerate(labels):
    label = ttk.Label(root, text=label_text)
    label.grid(row=i + 5, column=0, sticky="e", pady=5, padx=10)
    label_var = ttk.Label(root, textvariable=label_vars[i])
    label_var.grid(row=i + 5, column=1, sticky="w", pady=5, padx=10)

root.columnconfigure(1, weight=1)

"""Label_filepath =  Label(root, text = "Enter file path", anchor="e", justify="right")"""

# Labels positioning
# Label_title_mean.grid(row=5, column= 0, sticky="e")
# Label_mean.grid(row=5, column= 1)
# Label_title_median.grid(row=6, column= 0, sticky="e")
# Label_median.grid(row=6, column= 1)
# Label_title_mode.grid(row=7, column= 0, sticky="e")
# Label_mode.grid(row=7, column= 1)
# Label_title_min.grid(row=8, column= 0, sticky="e")
# Label_min.grid(row=8, column= 1)
# Label_title_max.grid(row=9, column= 0, sticky="e")
# Label_max.grid(row=9, column= 1)
# Label_title_std.grid(row=10, column= 0, sticky="e")
# Label_std.grid(row=10, column= 1)
# Label_title_mad.grid(row=11, column= 0, sticky="e")
# Label_mad.grid(row=11, column= 1)




"""Label_filepath.grid(row=2, column=0, sticky="e")"""


#define functions

def getMean():
     mean_value.set(data_processor.get_mean())


def getMinimum():
    min_value.set(data_processor.get_min_value())

def getMaximum():
    max_value.set(data_processor.get_max_value())

def getMode():
    mode_value.set(data_processor.get_mode())

def getMedian():
    median_value.set(data_processor.get_median())

def getMAD():
    mad_value.set(data_processor.get_mean_absolute_deviation())

def getStandardDev():
    std_value.set(data_processor.get_standard_deviation())

# Define buttons

style = ttk.Style()
style.configure('TButton', padding=5, relief="flat", font=('Arial', 10))
style.configure('TLabel', font=('Arial', 10))


button_calculate = ttk.Button(root, text="Calculate Metrics", command=calculate_metrics, style="TButton")
button_calculate.grid(row=4, column=0, padx=20, pady=20)

open_button = ttk.Button(root, text="Open File", command=open_file_dialog, style="TButton")
open_button.grid(row=2, column=0, padx=10, pady=15)

min_btn = ttk.Button(root, text="Calculate Minimum", command=getMinimum, style="TButton")
min_btn.grid(row=3, column=0, pady=20, padx=20)

max_btn = ttk.Button(root, text="Calculate Maximum", command=getMaximum, style="TButton")
max_btn.grid(row=3, column=1, pady=20, padx=20)

mode_btn = ttk.Button(root, text="Calculate Mode", command=getMode, style="TButton")
mode_btn.grid(row=3, column=2, pady=20, padx=20)

median_btn = ttk.Button(root, text="Calculate Median", command=getMedian, style="TButton")
median_btn.grid(row=3, column=3, pady=20, padx=20)

mean_btn = ttk.Button(root, text="Calculate Mean", command=getMean, style="TButton")
mean_btn.grid(row=3, column=4, pady=20, padx=20)

mad_btn = ttk.Button(root, text="Calculate MAD", command=getMAD, style="TButton")
mad_btn.grid(row=3, column=5, pady=20, padx=20)

standard_dev_btn = ttk.Button(root, text="Calculate Standard Deviation", command=getStandardDev, style="TButton")
standard_dev_btn.grid(row=3, column=6, pady=20, padx=20)


root.mainloop()