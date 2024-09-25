import tkinter as tk
from tkinter import messagebox, simpledialog

class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class ContactBookApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")

        self.contacts = []

        self.create_widgets()

    def create_widgets(self):
        # Frame for contact list
        self.contact_list_frame = tk.Frame(self.root)
        self.contact_list_frame.pack(pady=10)

        self.contact_listbox = tk.Listbox(self.contact_list_frame, width=50, height=15)
        self.contact_listbox.pack(side=tk.LEFT)

        self.scrollbar = tk.Scrollbar(self.contact_list_frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.contact_listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.contact_listbox.yview)

        # Frame for buttons
        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack(pady=2)

        self.add_button = tk.Button(self.button_frame, text="Add Contact", command=self.add_contact,bg="#0CCE6B")
        self.add_button.pack(side=tk.LEFT, padx=2)

        self.update_button = tk.Button(self.button_frame, text="Update Contact", command=self.update_contact,bg="#DCED31")
        self.update_button.pack(side=tk.LEFT, padx=2)

        self.delete_button = tk.Button(self.button_frame, text="Delete Contact", command=self.delete_contact,bg="#EF2D56")
        self.delete_button.pack(side=tk.LEFT, padx=2)

        self.search_button = tk.Button(self.button_frame, text="Search Contact", command=self.search_contact,bg="#A3BCF9")
        self.search_button.pack(side=tk.LEFT, padx=2)

    def add_contact(self):
        name = simpledialog.askstring("Input", "Enter Name:")
        if not name:
            return
        phone = simpledialog.askstring("Input", "Enter phone number:")
        email = simpledialog.askstring("Input", "Enter email:")
        address = simpledialog.askstring("Input", "Enter address:")
        contact = Contact(name, phone, email, address)
        self.contacts.append(contact)
        self.update_contact_listbox()

    def update_contact_listbox(self):
        self.contact_listbox.delete(0, tk.END)
        for contact in self.contacts:
            self.contact_listbox.insert(tk.END, f"{contact.name} - {contact.phone}")

    def update_contact(self):
        selected_index = self.contact_listbox.curselection()
        if not selected_index:
            messagebox.showwarning("Select Contact", "Please select a contact to update !!!")
            return

        contact = self.contacts[selected_index[0]]
        name = simpledialog.askstring("Input", "Enter new store name:", initialvalue=contact.name)
        phone = simpledialog.askstring("Input", "Enter new phone number:", initialvalue=contact.phone)
        email = simpledialog.askstring("Input", "Enter new email:", initialvalue=contact.email)
        address = simpledialog.askstring("Input", "Enter new address:", initialvalue=contact.address)

        contact.name = name
        contact.phone = phone
        contact.email = email
        contact.address = address
        self.update_contact_listbox()

    def delete_contact(self):
        selected_index = self.contact_listbox.curselection()
        if not selected_index:
            messagebox.showwarning("Select Contact", "Please select a contact to delete!!!")
            return

        confirm = messagebox.askyesno("Delete Confirmation", "Are you sure you want to delete this contact ?")
        if confirm:
            del self.contacts[selected_index[0]]
            self.update_contact_listbox()

    def search_contact(self):
        query = simpledialog.askstring("Search", "Enter name or phone number to search !!!")
        if not query:
            return

        results = [contact for contact in self.contacts if query.lower() in contact.name.lower() or query in contact.phone]
        if results:
            self.contact_listbox.delete(0, tk.END)
            for contact in results:
                self.contact_listbox.insert(tk.END, f"{contact.name} - {contact.phone}")
        else:
            messagebox.showinfo("No Results", "No contacts found !!!")

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBookApp(root)
    root.geometry("500x300")
    root.configure(background="#E3DAFF")
    root.mainloop()
