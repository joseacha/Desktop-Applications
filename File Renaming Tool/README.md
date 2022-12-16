# File Renaming Tool

This is a simple Python program that allows you to rename multiple files in a folder with a specified prefix. It has a graphical user interface (GUI) created with the `tkinter` library.

## Requirements

- Python 3
- `tkinter` library (should be installed by default with Python)

## Usage

To use the program, simply run it with Python:

'python file_renaming_tool.py'


A window will open with a text entry field and a button. Enter the desired prefix for the new file names in the text entry field, then click the "Rename files" button. A file browser will open, allowing you to select the folder containing the files you want to rename. The program will then rename all the files in the selected folder with the specified prefix.

## Notes

- The program will append the current file index and the original file extension to the prefix to create the new file names.
- The progress of the file renaming process is shown in a progress bar.

