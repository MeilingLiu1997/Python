This project addressbook.py is used to add, display, search, modify, and delete contacts in electronic way. In the whole program, it is divided into 7 parts (functions).
===============================================================================
In the first part, under the menu() function, it mainly lists 6 choices to users: add new contacts, display address book, search for a contact, modify contact, delete contact, and exit the program.

In the second part, under the addNew() function, it asks users to add new contact’s information: name, address, phone number, and email address. At the meantime, updating those data into the new list(a 2-dimensional list) and the a file contacts.txt.

In the third part,  under the display() function, it open a contacts.txt file and read each line of the context in the file, and then, printing them to the user.

In the forth part, under the search() function, it asks users to enter name of the contact that they want to search for. Next, I create a new namelist and open the contact.txt file. In the namelist, it only include a part of the whole list. For example, list = [[0,1],[4,5]] and in the namelist=[0,1], or namelist = [4,5]. Based on if statement, if what the user search for is in the file, print the whole information of that individual. For example, when the user enter ‘4’ as a name, the program will print [4,5] at the end, which is in the namelist.

In the fifth part, under the modify() function, it opens the contacts.txt and new.txt files at first. It has the same process with search() function at the beginning, and then, ask user to enter what aspect they want to change, and enter the new item. After that, in the list, the ‘old’ name will be removed and insert the ‘new’ name at the same place with the ‘old’ name. At the same time, the old contacts.txt will be removed, and write what in the list on separate lines in the new.txt file. At last, rename ‘new.file’ into ‘contacts.file’.

In the sixth part, under the delete() function, it similar with modify() function. After opening two files: ‘new.file’ and ‘contacts.file’, ask a user whose information needs to be deleted. And then, find the name in the namelist, remove the whole contact of that individual, and erase the whole old contact.txt file. At the end, rewrite what in the list on separate lines in the new file. Finally, rename ‘new.file’ into ‘contacts.file’.

In the last part, under the exit() function, it only contain a quit() function, which means to end the whole program.