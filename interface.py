#INTERFACE CREATION

import tkinter as tk
from tkinter import ttk
import tkinter.font
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
import os


def import_file(root):
    filetypes = (('video files', '*.mp4'),('All files', '.'))
    root.filename = fd.askopenfilename(title='Open a file', initialdir='/', filetypes=filetypes)
    showinfo(title='Selected File', message=root.filename)


def convert_vp8(input_video):
    # Convert the input video into VP8 extension
    os.system("ffmpeg -i " + str(input_video) + " -c:v libvpx -crf 30 -b:v 1M -c:a libopus output_vp8.webm")


def convert_vp9(input_video):
    # Convert the input video into VP9 extension
    os.system("ffmpeg -i " + str(input_video) + " -c:v libvpx-vp9 -crf 30 -b:v 1M -c:a libopus output_vp9.webm")


def convert_h265(input_video):
    # Convert the input video into h265 extension
    os.system("ffmpeg -i " + str(input_video) + " -c:v libx265 -b:v 1M output_h265.mp4")


def convert_AV1(input_video):
    # Convert the input video into AV1 extension
    os.system("ffmpeg -i " + str(input_video) + " -c:v libaom-av1 -b:v 1M output_av1.mkv")


def main():

    # Root window, we set the size of the window and the title
    root = tk.Tk()
    root.geometry("800x400")
    root.title('Video converter program')
    root.configure(bg='PeachPuff3')
    root.resizable(0, 0)

    # Choose input video
    input_video = ttk.Label(root, text="CHOOSE A VIDEO FROM YOUR COMPUTER TO CONVERT IT TO ANY OF THESE EXTENSIONS:")
    input_video.place(x=40,y=25)

    # Button to import the input video file
    open_video_button = ttk.Button(root, text='Import', width=10, command=lambda: import_file(root))
    open_video_button.pack(expand=True)
    open_video_button.place(x=650, y=25)

    # Define font fo the buttons
    button_font = tkinter.font.Font(family='Helvetica', size=20, weight='bold')

    # Conversion to vp8
    conversion_vp8_button = tk.Button(root, text="CONVERT TO VP8", fg='black', bg='white',
                                      command=lambda: convert_vp8(root.filename))
    conversion_vp8_button.place(x=100, y=100)

    # apply font to the button label
    conversion_vp8_button['font'] = button_font

    # Conversion to vp9
    conversion_vp9_button = tk.Button(root, text="CONVERT TO VP9", fg='black', bg='white',
                                      command=lambda: convert_vp9('bbbVideo_480.mp4'))
    conversion_vp9_button.place(x=450, y=100)

    # apply font to the button label
    conversion_vp9_button['font'] = button_font

    # Conversion to h265
    conversion_h265_button = tk.Button(root, text="CONVERT TO h265", fg='black', bg='white',
                                       command=lambda: convert_h265('bbbVideo_480.mp4'))
    conversion_h265_button.place(x=100, y=200)

    # apply font to the button label
    conversion_h265_button['font'] = button_font

    # Conversion to AV1
    conversion_AV1_button = tk.Button(root, text="CONVERT TO AV1", fg='black', bg='white',
                                      command=lambda: convert_AV1('bbbVideo_480.mp4'))
    conversion_AV1_button.place(x=450, y=200)

    # apply font to the button label
    conversion_AV1_button['font'] = button_font

    # quit button
    quit_button = ttk.Button(root, text="Quit", command=root.destroy)
    quit_button.place(x=700, y=350)

    root.mainloop()


main()



