from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.geometry("800x600")

Label(root, text="Trees", fg="black", font=("Courier", 15)).place(x=170, y=20)
Label(root, text="Ocean", fg="black", font=("Courier", 15)).place(x=570, y=20)
Label(root, text="Mountains", fg="black", font=("Courier", 15)).place(x=170, y=310)
Label(root, text="Sky", fg="black", font=("Courier", 15)).place(x=570, y=310)

img1 = Image.open("trees.jpeg")
resized_image1 = img1.resize((300, 200), Image.Resampling.LANCZOS)
new_image1 = ImageTk.PhotoImage(resized_image1)

canvas = Canvas(root, width=325, height=225)
canvas.create_image(15, 15, anchor=NW, image=new_image1)
canvas.place(x=50, y=50)

img2 = Image.open("ocean.jpg")
resized_image2 = img2.resize((300, 200), Image.Resampling.LANCZOS)
new_image2 = ImageTk.PhotoImage(resized_image2)

canvas2 = Canvas(root, width=325, height=225)
canvas2.create_image(15, 15, anchor=NW, image=new_image2)
canvas2.place(x=430, y=50)

root.mainloop()
