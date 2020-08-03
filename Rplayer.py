from tkinter import *

root = Tk()
# tiltle name
root.title("Rj mp3 Player")
# size of player
root.geometry("500x400")
# playlist box
playlist_box = Listbox(root, bg="black",fg="green", width=60)
playlist_box.pack(pady=20)

# Creating Button frame
control_frame = Frame(root)
control_frame.pack(pady=20)

# Creating play/stop etc buttons 
back_button = button(control_frame, text="Back")
forward_button = button(control_frame, text="Forward")
play_button = button(control_frame, text="Play")
pause_button = button(control_frame, text="Pause")
stop_button = button(control_frame, text="Stop")

back_button.grid(row=0, column=0)
forward_button.grid(row=0, column=1)
play_button.grid(row=0, column=2)
pause_button.grid(row=0, column=3)
stop_button.grid(row=0, column=4)



root.mainloop()