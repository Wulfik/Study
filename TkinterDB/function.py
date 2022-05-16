import os

from Interface import *
from DataBase import DataBase
from tkinter import messagebox
from tkinter import simpledialog
interface = Interface('DataBase')

def add_category(event):
    new_name = simpledialog.askstring('New name','Enter new category name')
    print(new_name)
    if DataBase.check_unique_category(new_name) == False and new_name != '' and new_name != None:
        DataBase.add_category(new_name)
        messagebox.showinfo('Add new category', f'New category `{new_name}` successfully added')
        interface.combobox_category_list.config(values=DataBase.get_category())
        interface.combobox_category_list.set(DataBase.get_category()[-1])
        for item in interface.list_box.get_children():
            interface.list_box.delete(item)
    elif new_name == '':
        messagebox.showerror('Add new category', 'Please,write new category name`')
        add_category()
    elif DataBase.check_unique_category(new_name) == True:
        messagebox.showerror('Add new category',f'You already have category with name `{new_name}`')
        add_category()

def delete_category(event):
    if interface.combobox_category_list.get() != 'Choose category' and messagebox.askyesno('Delete category', f'Are you sure you want to delete the category `{interface.combobox_category_list.get()}`?') == True:
        DataBase.delete_category(interface.combobox_category_list.get())
        interface.combobox_category_list.config(values=DataBase.get_category())
        interface.combobox_category_list.set('Choose category')
        for item in interface.list_box.get_children():
            interface.list_box.delete(item)
        messagebox.showinfo('Delete category', 'Category successfully deleted')

def add_goods(event):
    category = interface.combobox_category_list.get()
    if category == 'Choose category':
        messagebox.showerror('Add goods', 'Please,select category')
        return
    name = simpledialog.askstring('Name','Enter new name')
    if category != 'Choose category' and name != None and name != '' and DataBase.check_unique_goods(category,name) == False:
        price = simpledialog.askinteger('Price', 'Enter new price')
        DataBase.add_goods(name,category, price)
        goods_list = DataBase.get_goods(interface.combobox_category_list.get())
        for item in interface.list_box.get_children():
            interface.list_box.delete(item)
        for goods in goods_list:
            goods = list(goods)
            goods.pop(2)
            interface.list_box.insert('', index='end', values=(goods))
    elif name == '':
        messagebox.showerror('Add new goods', 'Please,write new goods name`')
        add_goods()
    elif DataBase.check_unique_category(name) == True:
        messagebox.showerror('New goods','You alreade have this goods name in category')
        add_goods()
def delete_goods(event):
    if interface.list_box.focus() != '' and messagebox.askyesno('Delete note', 'Are you sure you want to delete the note?') == True:
        name = interface.list_box.item(interface.list_box.focus())['values'][1]
        DataBase.delete_goods(name, interface.combobox_category_list.get())
        item = interface.list_box.focus()
        interface.list_box.delete(item)
        messagebox.showinfo('Notes', 'Note successfully deleted')

def delete_goods_key(event):
    if event.char == '=':
        print(DataBase.show())
        print(interface.list_box.focus())
    if event.keysym == 'Delete':
        if interface.list_box.focus() != '' and messagebox.askyesno('Delete note', 'Are you sure you want to delete the note?') == True:
            name = interface.list_box.item(interface.list_box.focus())['values'][1]
            DataBase.delete_goods(name, interface.combobox_category_list.get())
            item = interface.list_box.focus()
            interface.list_box.delete(item)
            messagebox.showinfo('Notes', 'Note successfully deleted')

def fill_listbox(event):
    goods_list = DataBase.get_goods(interface.combobox_category_list.get())
    for item in interface.list_box.get_children():
        interface.list_box.delete(item)
    for goods in goods_list:
        goods = list(goods)
        goods.pop(2)
        interface.list_box.insert('', index='end', values=(goods))

def fill_tree():
    goods_list = DataBase.get_goods(interface.combobox_category_list.get())
    for item in interface.list_box.get_children():
        interface.list_box.delete(item)
    for goods in goods_list:
        goods = list(goods)
        goods.pop(2)
        interface.list_box.insert('', index='end', values=(goods))

def change_goods(event):
    last_item = interface.list_box.item(interface.list_box.focus())
    def change_entry_state():
        if change_window.var_name.get() == 1:
            change_window.entry_name['state'] = NORMAL
        else:
            change_window.entry_name.config(state=DISABLED)
        if change_window.var_price.get() == 1:
            change_window.entry_price.config(state=NORMAL)
        else:
            change_window.entry_price.config(state=DISABLED)

    def get_new_param():
        if change_window.var_name.get() == 1 and change_window.entry_name.get() != '':
            new_name = change_window.entry_name.get()
            if DataBase.check_unique_goods(interface.combobox_category_list.get(),new_name) == False:
                id = last_item['values'][0]
                DataBase.update_name(new_name,id)
                fill_tree()
            else:
                messagebox.showerror('Change name', f'You already have `{new_name}` goods name in this category')
        if change_window.var_price.get() == 1:
            new_price = change_window.entry_price.get()
            try:
                id = last_item['values'][0]
                DataBase.update_price(int(new_price),id)
                fill_tree()
            except:
                messagebox.showerror('Price', 'Please, entry numbers, not letter')
        if change_window.var_name.get() == 0 and change_window.var_price.get() == 0:
            messagebox.showerror('Change information', 'Please, entry new name or price')
        if change_window.var_name.get() == 1 and change_window.entry_name.get() == '':
            messagebox.showerror('Change information', 'Please, entry name')
    if interface.list_box.focus() != '':
        change_window = Edit_Window()
        change_window.checkbutton_name.configure(command=change_entry_state)
        change_window.checkbutton_price.configure(command=change_entry_state)
        change_window.button_change.configure(command=get_new_param)
        change_window.run()

def delete_db():
    os.remove('DB.db')
    DataBase.create_table()
    interface.combobox_category_list.set('Choose category')
    interface.combobox_category_list.config(values=DataBase.get_category())
    for item in interface.list_box.get_children():
        interface.list_box.delete(item)


def start():
    DataBase.create_table()
    interface.combobox_category_list.config(values=DataBase.get_category())
    interface.combobox_category_list.bind("<<ComboboxSelected>>", fill_listbox)
    interface.list_box.bind("<Double-1>", change_goods)
    interface.list_box.bind("<Key>", delete_goods_key)
    interface.label_add_category.bind('<Button-1>', add_category)
    interface.label_delete_category.bind('<Button-1>', delete_category)
    interface.label_add_goods.bind('<Button-1>', add_goods)
    interface.label_delete_goods.bind('<Button-1>', delete_goods)
    interface.file_menu.entryconfig(1, command = delete_db)
    interface.run()