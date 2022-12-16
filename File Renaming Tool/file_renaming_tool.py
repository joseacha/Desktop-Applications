import os
import tkinter as tk
from tkinter import filedialog, ttk

# Function to rename files
def rename_files():
  # Get the directory containing the files
  directory = filedialog.askdirectory()

  # Get the new file name prefix
  new_name_prefix = entry.get()

  # Iterate through all files in the directory
  for i, filename in enumerate(os.listdir(directory)):
    # Split the file name and extension
    name, extension = os.path.splitext(filename)

    # Construct the new file name
    new_name = f"{new_name_prefix} {i}{extension}"

    # Rename the file
    os.rename(os.path.join(directory, filename), os.path.join(directory, new_name))

    # Update the progress bar and status label
    progress_bar["value"] = (i + 1) / len(os.listdir(directory)) * 100
    status_label.config(text=f"Renaming file {i + 1} of {len(os.listdir(directory))}: {filename}")
    root.update_idletasks()

  # Update the status label
  status_label.config(text="Finished renaming files")

# Create the main window
root = tk.Tk()
root.geometry("450x160")
root.title("Rename Files")

# Create a label and text entry for the new file name prefix
label = tk.Label(root, text="Enter new file name prefix:")
entry = tk.Entry(root)

# Create a progress bar
progress_bar = ttk.Progressbar(root, orient="horizontal", length=200, mode="determinate")

# Create a status label
status_label = tk.Label(root, text="")

# Create a button to initiate the file renaming
rename_button = tk.Button(root, text="Rename files", command=rename_files)


# Create a footer label with a description of the program
footer_label = tk.Label(root, text="\nThis program allows you to rename multiple files in a folder with a specified prefix.\n\ngithub/joseacha\n")

# Place the widgets in the window
label.pack()
entry.pack()
progress_bar.pack()
status_label.pack()
rename_button.pack()
footer_label.pack(side="bottom")

# Run the main loop
root.mainloop()
