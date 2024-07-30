import tkinter as tk
from tkinter import messagebox


class ContactBook:
    def __init__(self, master):
        self.master = master
        master.title("Contact Book")

        self.name_label = tk.Label(master, text="Name:")
        self.name_entry = tk.Entry(master)

        self.phone_label = tk.Label(master, text="Phone:")
        self.phone_entry = tk.Entry(master)

        self.email_label = tk.Label(master, text="Email:")
        self.email_entry = tk.Entry(master)

        self.add_button = tk.Button(master, text="Add", command=self.add_contact)
        self.view_button = tk.Button(master, text="View", command=self.view_contacts)

        self.name_label.grid(row=0, column=0)
        self.name_entry.grid(row=0, column=1)
        self.phone_label.grid(row=1, column=0)
        self.phone_entry.grid(row=1, column=1)
        self.email_label.grid(row=2, column=0)
        self.email_entry.grid(row=2, column=1)
        self.add_button.grid(row=3, column=0)
        self.view_button.grid(row=3, column=1)

        self.contact_list = tk.Listbox(master)
        self.contact_list.grid(row=4, columnspan=2)

        self.contacts = []

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()

        if name and phone:
            self.contacts.append((name, phone, email))

            messagebox.showinfo("Success", "Contact added successfully!")
            self.clear_fields()

        else:
            messagebox.showerror("Error", "Please enter name and phone number.")

    def view_contacts(self):
        self.contact_list.delete(0, tk.END)
        for contact in self.contacts:
            self.contact_list.insert(tk.END, f"{contact[0]}-{contact[1]}")

    def clear_fields(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)


root = tk.Tk()
contact_book = ContactBook(root)
root.mainloop()
