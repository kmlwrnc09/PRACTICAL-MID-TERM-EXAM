import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("Song Artist Inforamtion")
window.geometry("500x500")

def add_artist():
    artist = artist_entry.get()
    age = age_entry.get()
    genre  = genre_entry.get()

    if artist == "" or age  == "" or genre == "":
        messagebox,showing ("Please enter all information. ")
        return
    output.insert(tk.END,f"Artist Name: {artist}\n")
    output.insert(tk.END,f"Age:{age}\n")
    output.insert(tk.END,f"Genre:{genre}\n")
    output.insert(tk.END,f"-----------\n")

def update_artist():
    output.delete("1.0", tk.END)
    add_artist()

def delete_artist():
    output.delete("1.0", tk.END)

def clear_entries():
    artist_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    genre_entry.delete(0, tk.END)

def exit_program():
    window.destroy()

tk.Label(window, text="Name:").pack(pady=5)
artist_entry = tk.Entry(window, width=40)
artist_entry.pack()

tk.Label(window, text="Age:").pack(pady=5)
age_entry = tk.Entry(window, width=40)
age_entry.pack()

tk.Label(window, text="Genre:").pack(pady=5)
genre_entry = tk.Entry(window, width=40)
genre_entry.pack()


button_frame = tk.Frame(window)
button_frame.pack(pady=15)

tk.Button(button_frame, text="Add", width=10,
          command=add_artist).grid(row=0, column=1, padx=5)

tk.Button(button_frame, text="Update", width=10,
          command=update_artist).grid(row=0, column=2, padx=5)

tk.Button(button_frame, text="Delete", width=10,
          command=delete_artist).grid(row=0, column=3, padx=5)

tk.Button(button_frame, text="Clear", width=10,
          command=clear_entries).grid(row=0, column=4, padx=5, pady=10)

tk.Button(button_frame, text="Exit", width=10,
          command=exit_program).grid(row=0, column=5, padx=5, pady=10)



tk.Label(window, text=" Song Artist Information").pack(pady=5)

output = tk.Text(window, width=40, height=10)
output.pack(pady=5)


window.mainloop()


