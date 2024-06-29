import json
import sqlite3
class Phonebook:
    def __init__(self,):
        # self.phonebook = phonebook
        self.contacts = self.load_phonebook()


    def load_phonebook(self):
        try:
             with open('phonebook.json', 'r') as file:
                 data = json.load(file)
                 return data
        except FileNotFoundError:
            return {}

    def phonebook_save(self):
             with open("phonebook.json", 'w') as file:
                 json.dump(self.contacts, file, indent=2)

    def add(self, first_name, last_name, phone_number, email= None):
        cont = {"First Name": first_name, "Last Name": last_name, "Number": phone_number, "Email" : email, "Favorite": False}
        self.contacts.append(cont)
        self.phonebook_save()
        print(f'Contact {first_name} added in phonebook')

    def edit_cont(self,first_name, new_phone_number):
        if first_name in self.contacts:
            self.contacts[first_name] = new_phone_number
            self.phonebook_save()

    def delete(self, first_name):
        for contact in self.contacts:
            if contact["First Name"] == first_name:
                self.contacts.remove(contact)
        self.phonebook_save()

    def favorite(self, first_name):
       for contact in self.contacts:
           if contact["name"] == first_name:
               contact["Favorite"] = not contact["Favorite"]
               self.phonebook_save()
               return (f"{first_name}'s favorite status toggled")
    def view_contacts(self):
        return self.contacts

def db_init():
    conn = sqlite3.connect('phonebook.db')
    c = conn.cursor()
    c.execute('''
                CREATE TABLE IF NOT EXISTS contacts (
                id INTEGER PRIMARY KEY,
                first_name TEXT,
                last_name TEXT,
                phone_number TEXT,
                email TEXT,
                favorite INTEGER
               )
           ''')
    conn.commit()
    conn.close()


phonebook = Phonebook()
#phonebook.db_init()
phonebook.add("Alice", "Smith", "123-456-7890", "alice@example.com")
phonebook.add("Bob", "Brown", "987-654-3210", "bob@example.com")
print(phonebook.view_contacts())