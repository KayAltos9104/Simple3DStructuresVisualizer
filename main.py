import visualizer
from tkinter import *
from tkinter import ttk
from tkinter import filedialog


def open_file():
    filepath = filedialog.askopenfilename()
    if filepath != "":
        visualizer.read_structure(filepath)
    entry_x_cut.delete(0, END)
    entry_y_cut.delete(0, END)
    entry_z_cut.delete(0, END)
    entry_x_cut.insert(0, visualizer.x_cut)
    entry_y_cut.insert(0, visualizer.y_cut)
    entry_z_cut.insert(0, visualizer.z_cut)

def visualize():
    global x_cut, y_cut, z_cut
    visualizer.x_cut = int(entry_x_cut.get()) if int(entry_x_cut.get()) >= 0 else 0
    visualizer.y_cut = int(entry_y_cut.get()) if int(entry_y_cut.get()) >= 0 else 0
    visualizer.z_cut = int(entry_z_cut.get()) if int(entry_z_cut.get()) >= 0 else 0
    visualizer.visualize()


root = Tk()
root.title("3DVisualizer v.1.0")
root.geometry("300x250")

btn_open = ttk.Button(text="Open file", command=open_file)
btn_open.pack(anchor=NW, padx=6, pady=6)

btn_visual = ttk.Button(text="Visualize", command=visualize)
btn_visual.pack(anchor=NW, padx=6, pady=6)

entry_x_cut = ttk.Entry()
entry_x_cut.pack(anchor=NW, padx=6, pady=6)
#entry_x_cut.insert(0,'0')

entry_y_cut = ttk.Entry()
entry_y_cut.pack(anchor=NW, padx=6, pady=6)
#entry_y_cut.insert(0,'0')

entry_z_cut = ttk.Entry()
entry_z_cut.pack(anchor=NW, padx=6, pady=6)
#entry_z_cut.insert(0,'0')

root.mainloop()
