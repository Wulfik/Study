import os
from tkinter import *
from tkinter import ttk
from DataBase import *

class Interface():
    def __init__(self, title):
        self.root = Tk()
        self.root.title(title)

        self.label_show_goods = Label(self.root, text='Categories', font=('Times', 14))
        self.label_show_goods.grid(row = 0, column = 0, columnspan=3)

        self.icon_add = PhotoImage(file="add.png")
        self.label_add_category = Label(self.root, image=self.icon_add)
        self.label_add_category.grid(row=1, column=1, sticky='W')

        self.icon_delete = PhotoImage(file="delete.png")
        self.label_delete_category = Label(self.root, image=self.icon_delete)
        self.label_delete_category.grid(row=1, column=1, sticky='E')

        self.combobox_category_list = ttk.Combobox(self.root, font=('Times',14), state='readonly')
        self.combobox_category_list.set('Choose category')
        self.combobox_category_list.grid(row=1,column=1)

        self.label_add_goods = Label(self.root, image=self.icon_add)
        self.label_add_goods.grid(row=3, column=1, sticky='W')

        self.label_delete_goods = Label(self.root, image=self.icon_delete)
        self.label_delete_goods.grid(row=3, column=1, sticky='E')

        self.label_goods = Label(self.root, text='Goods', font=('Times',14))
        self.label_goods.grid(row=3,column=1,sticky='N')

        self.list_box = ttk.Treeview(self.root, columns=("Id", "Name", "Price"), show='headings')
        self.list_box.heading('Id', text='Id')
        self.list_box.column('Id',anchor=CENTER)
        self.list_box.heading('Name', text='Name')
        self.list_box.column('Name', anchor=CENTER)
        self.list_box.heading('Price', text='Price')
        self.list_box.column('Price', anchor=CENTER)

        self.list_box.grid(row=2,column=0,columnspan=3)

        self.menubar = Menu(self.root)
        self.root.config(menu=self.menubar)

        self.file_menu = Menu(self.menubar)

        self.file_menu.add_command(
            label='Delete all',
        )

        self.file_menu.add_command(
            label='Exit',
            command=exit
        )

        # add the File menu to the menubar
        self.menubar.add_cascade(
            label="File",
            menu=self.file_menu
        )

    def run(self):
        self.root.mainloop()


class Edit_Window():
    def __init__(self):
        self.root = Toplevel()
        self.root.title('Change goods')
        self.root.grab_set()

        self.label_change_goods = Label(self.root, text = 'Enter new goods information', font=('Times', 14))
        self.label_change_goods.grid(row = 0, column=0, columnspan=2)

        self.var_name = IntVar()
        self.checkbutton_name = Checkbutton(self.root, text='Name', variable=self.var_name, font=('Times', 14))
        self.checkbutton_name.grid(row = 1, column=0, columnspan=1)

        self.entry_name = Entry(self.root, state=DISABLED, font=('Times', 14))
        self.entry_name.grid(row = 1, column=1, columnspan=1)

        self.var_price = IntVar()
        self.checkbutton_price = Checkbutton(self.root, text='Price', variable=self.var_price, font=('Times', 14))
        self.checkbutton_price.grid(row = 2, column=0, columnspan=1)

        self.entry_price = Entry(self.root, state=DISABLED, font=('Times', 14))
        self.entry_price.grid(row = 2, column=1, columnspan=1)

        self.button_change = Button(self.root, text = 'Change', font=('Times', 14))
        self.button_change.grid(row = 3, column=0, columnspan=2)

    def run(self):
        self.root.mainloop()

    def exit(self):
        self.root.destroy()