from tkinter import *
from tkinter import filedialog

root = Tk()
# tiltle name
root.title("Rj mp3 Player")
# size of player
root.geometry("700x500")
##create function to playlist to add one songs
def add_song():
	song = filedialog.askopenfilename()
#create function to playlist to add many songs
def add_many_songs():
	pass
# playlist box
playlist_box = Listbox(root, bg="black",fg="green", width=80, height=12)
playlist_box.pack(pady=20)

#Adding images to buttons
back_btn_img=PhotoImage(file='images/back.png')
forward_btn_img=PhotoImage(file='images/forward.png')
play_btn_img=PhotoImage(file='images/play.png')
pause_btn_img=PhotoImage(file='images/pause.png')
stop_btn_img=PhotoImage(file='images/stop.png')

# Creating Button frame
control_frame = Frame(root)
control_frame.pack(pady=20)

# Creating play/stop etc buttons
back_button=Button(control_frame, image=back_btn_img)
forward_button=Button(control_frame,image=forward_btn_img)
play_button=Button(control_frame, image=play_btn_img)
pause_button=Button(control_frame, image=pause_btn_img)
stop_button=Button(control_frame, image=stop_btn_img)

back_button.grid(row=0, column=0, padx=10)
forward_button.grid(row=0, column=1, padx=10)
play_button.grid(row=0, column=2, padx=10)
pause_button.grid(row=0, column=3, padx=10)
stop_button.grid(row=0, column=4, padx=10)

#Create Menu
my_menu = Menu(root)
root.config(menu=my_menu)

#create Add song menu dropdowns
add_song_menu = Menu(my_menu, tearoff=0)
my_menu.add_cascade(label="Add Songs",menu=add_song_menu)
#Add one song
add_song_menu.add_command(label="Add One Song To Playlist", command=add_song)
#Add many songs
add_song_menu.add_command(label="Add Many Song To Playlist", command=add_many_songs)


root.mainloop()