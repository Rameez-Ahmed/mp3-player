from tkinter import *

root = Tk()
# tiltle name
root.title("Rj mp3 Player")
# size of player
root.geometry("500x400")
# playlist box
playlist_box = Listbox(root, bg="black",fg="green", width=60)
playlist_box.pack(pady=20)






root.mainloop()