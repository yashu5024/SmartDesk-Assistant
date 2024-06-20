from tkinter import *
from PIL import Image, ImageTk
import speech_to_text
import action
import itertools

speech_to_text.listen_for_wake_word() #expecting to initialize the ui by saying "hello smart desk"
root = Tk()
root.title("SmartDesk Assistant")
root.geometry("540x625")
root.resizable(False, False)
root.config(bg="#6F8FAF")

# Gradient background function
def create_gradient(canvas, width, height, color1, color2):
    limit = width
    (r1, g1, b1) = canvas.winfo_rgb(color1)
    (r2, g2, b2) = canvas.winfo_rgb(color2)
    r_ratio = float(r2 - r1) / limit
    g_ratio = float(g2 - g1) / limit
    b_ratio = float(b2 - b1) / limit

    for i in range(limit):
        nr = int(r1 + (r_ratio * i))
        ng = int(g1 + (g_ratio * i))
        nb = int(b1 + (b_ratio * i))
        color = "#%4.4x%4.4x%4.4x" % (nr, ng, nb)
        canvas.create_line(i, 0, i, height, fill=color)

# Create a canvas for the gradient background
canvas = Canvas(root, width=540, height=625)
canvas.pack(fill='both', expand=True)
create_gradient(canvas, 540, 625, '#6F8FAF', '#1B3C59')

# Function to animate text insertion
def animate_text_insertion(text_widget, tag, text):
    for i, char in enumerate(text):
        text_widget.insert(END, char, tag)
        text_widget.update()
        text_widget.after(50)

# Ask function
def ask():
    user_val = speech_to_text.speech_to_text()
    animate_text_insertion(text, 'user', f"user --> {user_val}\n")
    bot_val = action.action(user_val)
    if bot_val != None:
        animate_text_insertion(text, 'SmartDesk', f"SmartDesk --> {str(bot_val)}\n")
    if bot_val == "ok sir":
        root.destroy()

# Send function
def send():
    sent = entry_box.get()
    animate_text_insertion(text, 'user', f"user --> {sent}\n")
    bot = action.action(sent)
    if bot != None:
        animate_text_insertion(text, 'SmartDesk', f"SmartDesk --> {str(bot)}\n")
    if bot == "ok sir":
        root.destroy()

# Delete function
def delete():
    text.delete("1.0", END)

# Animating text label
def animate_label(label, text):
    def update_text(index=0):
        label.config(text=text[:index])
        index += 1
        if index > len(text):
            index = 0
        label.after(150, update_text, index)
    update_text()

# Frame
frame = LabelFrame(root, padx=10, pady=10, bg="#6F8FAF", highlightthickness=0)
frame.place(relx=0.5, rely=0.1, anchor=CENTER)

# Text label
text_label = Label(frame, text="", font=("Arial", 18, "bold"), bg="#6F8FAF", fg="#FFFFFF")
text_label.pack(padx=20, pady=10)
animate_label(text_label, "SmartDesk Assistant")

# Add text widget
text = Text(root, font=("Arial", 12, "bold"), bg="#356696", fg="#FFFFFF")
text.place(x=10, y=125, width=350, height=300)

# Configure tags for alignment
text.tag_configure('user', justify='left')
text.tag_configure('bot', justify='right')

# Entry box
entry_box = Entry(root, justify=CENTER, font=("Arial", 12), bg="#FFFFFF", fg="#000000")
entry_box.place(x=120, y=480, width=300, height=65)

# Add image to the right of the text box
image = Image.open("C:\\Users\\yashu\\Desktop\\ai.jpg").resize((155, 300), Image.LANCZOS)
photo = ImageTk.PhotoImage(image)
image_label = Label(root, image=photo,bg="#6F8FAF")
image_label.place(x=365, y=125)

# Load button images
ask_image_normal = Image.open("C:\\Users\\yashu\\Desktop\\mic before.png").resize((60, 60), Image.LANCZOS)
ask_photo_normal = ImageTk.PhotoImage(ask_image_normal)

send_image_normal = Image.open("C:\\Users\\yashu\\Desktop\\send-button-concept-3d-illustration-GXA12G.jpg").resize((60, 60), Image.LANCZOS)
send_photo_normal = ImageTk.PhotoImage(send_image_normal)

delete_image_normal = Image.open("C:\\Users\\yashu\\Desktop\\delete.jpg").resize((60,60), Image.LANCZOS)
delete_photo_normal = ImageTk.PhotoImage(delete_image_normal)

# Buttons
button1 = Button(root, image=ask_photo_normal, bg="#356696", fg="#FFFFFF", pady=16, padx=30, borderwidth=3, relief=SOLID, command=ask)
button1.image = ask_photo_normal
button1.place(x=35, y=480)

button2 = Button(root, image=send_photo_normal, bg="#356696", fg="#FFFFFF", pady=16, padx=30, borderwidth=3, relief=SOLID, command=send)
button2.image = send_photo_normal
button2.place(x=435, y=480)

button3 = Button(root, image=delete_photo_normal, bg="#356696", fg="#FFFFFF", pady=16, padx=30, borderwidth=3, relief=SOLID, command=delete)
button3.image = delete_photo_normal
button3.place(x=225, y=555)

root.mainloop()