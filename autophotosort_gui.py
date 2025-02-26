import tkinter as tk
from tkinter import filedialog
import os
import webbrowser
from src.sorter import split_photos_by_date

def main():
    root = tk.Tk()
    root.title("Auto Photo Sorter")

    # Set app icon
    try:
        icon_image = tk.PhotoImage(file="src/AutoPhotoSortLogo.png")
        root.iconphoto(False, icon_image)
    except tk.TclError:
        print("Icon file not found or not supported.")

    root.geometry("650x420")
    root.resizable(False, False)

    # Load the logo image and display it
    logo_image = tk.PhotoImage(file="src/AutoPhotoSortLogo.png")
    logo_label = tk.Label(root, image=logo_image)
    logo_label.image = logo_image
    logo_label.pack(pady=10)

    input_folder = tk.StringVar()
    output_folder = tk.StringVar()

    default_input_dir = os.path.join(os.getcwd(), "data", "input")
    default_output_dir = os.path.join(os.getcwd(), "data", "output")
    input_folder.set(default_input_dir)
    output_folder.set(default_output_dir)

    def open_input_folder_dialog():
        """Opens a dialog to select the input folder."""
        default_input_dir = os.path.join(os.getcwd(), "data", "input")
        input_folder.set(default_input_dir)
        if os.path.exists(default_input_dir):
            os.startfile(default_input_dir)
        else:
            folder_selected = filedialog.askdirectory()
            if folder_selected:
                input_folder.set(folder_selected)

    def open_output_folder_dialog():
        """Opens a dialog to select the output folder."""
        default_output_dir = os.path.join(os.getcwd(), "data", "output")
        output_folder.set(default_output_dir)
        if os.path.exists(default_output_dir):
            os.startfile(default_output_dir)
        else:
            folder_selected = filedialog.askdirectory()
            if folder_selected:
                output_folder.set(folder_selected)

    def start_sorting():
        """Initiates the photo sorting process."""
        in_dir = input_folder.get()
        out_dir = output_folder.get()
        # Checks if input and output directories are valid
        if in_dir and out_dir:
            split_photos_by_date(in_dir, out_dir) # Sort photos using the function from sorter.py
            tk.messagebox.showinfo("Info", "Sorting complete!")
        else:
            tk.messagebox.showerror("Error", "Please select both input and output folders.")

    title_label = tk.Label(root, text="Auto Photo Sorter", font=("Helvetica", 16))
    title_label.pack(pady=5)

    description_label = tk.Label(root, text="is a simple Python tool designed to automatically organize your photos \ninto folders based on the year and month they are taken. ")
    description_label.pack(pady=5)

    input_frame = tk.Frame(root)
    input_frame.pack(pady=5)
    input_button = tk.Button(input_frame, text="Open Input Folder", command=open_input_folder_dialog, width=15, height=2)
    input_button.pack(side=tk.LEFT, padx=5)
    input_entry = tk.Entry(input_frame, textvariable=input_folder, width=70, state='disabled')
    input_entry.pack(side=tk.LEFT)

    output_frame = tk.Frame(root)
    output_frame.pack(pady=5)
    output_button = tk.Button(output_frame, text="Open Output Folder", command=open_output_folder_dialog, width=15, height=2)
    output_button.pack(side=tk.LEFT, padx=5)
    output_entry = tk.Entry(output_frame, textvariable=output_folder, width=70, state='disabled')
    output_entry.pack(side=tk.LEFT)

    start_button = tk.Button(root, text="Start Sorting", command=start_sorting)
    start_button.pack(pady=20)

    github_link = tk.Label(root, text="by cv0x[GitHub]", fg="blue", cursor="hand2")
    github_link.pack(anchor='se', padx=10, pady=10)
    github_link.bind("<Button-1>", lambda e: webbrowser.open("https://github.com/cv0x"))

    root.mainloop()

if __name__ == "__main__":
    main()
