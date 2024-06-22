import subprocess
import tkinter.messagebox
from tkinter import *
from tkinter import messagebox as mb, simpledialog
import time
import os


class FileService:
    def __init__(self, parent):
        self.__parent = parent

    def zip(self):
        item = ""
        zip_name = simpledialog.askstring("Archive", "Enter the archive name: ")
        if not zip_name:
            tkinter.messagebox.showwarning("Error", "You did not enter anything!")
            return
        if self.__parent.get_last_active_panel() == "l":
            item = self.__parent.get_left_panel().get(self.__parent.get_left_panel().curselection())
        elif self.__parent.__last_active_panel == "r":
            item = self.__parent.get_right_panel().get(self.__parent.get_right_panel().curselection())
        if zip_name.endswith(".tar.gz"):
            process = subprocess.Popen(["tar", "-cvf", zip_name, item], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            output, error = process.communicate()
            if error:
                tkinter.messagebox.showwarning("Archive Error", "An error occurred or you do not have enough permissions!")
                return
        else:
            tkinter.messagebox.showwarning("Error", "Only tar.gz archives are supported")
            return
        tkinter.messagebox.showinfo("Archive", "Archive created successfully!")
        if self.__parent.get_last_active_panel() == "l":
            self.__parent.update_left_panel()
        elif self.__parent.get_last_active_panel() == "r":
            self.__parent.update_right_panel()

    def unzip(self):
        zip_name = ""
        if self.__parent.get_last_active_panel() == "l":
            zip_name = self.__parent.get_left_panel().get(self.__parent.get_left_panel().curselection())
        elif self.__parent.get_last_active_panel() == "r":
            zip_name = self.__parent.get_right_panel().get(self.__parent.get_right_panel().curselection())
        process = subprocess.Popen(["tar", "-xvf", zip_name], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = process.communicate()
        if error:
            tkinter.messagebox.showwarning("Error", "Only tar.gz format is supported")
            return
        tkinter.messagebox.showinfo("Unzipping", "Archive successfully extracted!")
        if self.__parent.get_last_active_panel() == "l":
            self.__parent.update_left_panel()
        elif self.__parent.get_last_active_panel() == "r":
            self.__parent.update_right_panel()

    def forward(self):
        if not os.path.isdir(self.__parent.__path_field.get()):
            return
        if self.__parent.get_last_active_panel() == "l":
            self.__parent.set_left_panel_path(self.__parent.__path_field.get())
        elif self.__parent.get_last_active_panel() == "r":
            self.__parent.set_right_panel_path(self.__parent.__path_field.get())
        if self.__parent.get_last_active_panel() == "l":
            self.__parent.update_left_panel()
        elif self.__parent.get_last_active_panel() == "r":
            self.__parent.update_right_panel()

    def back(self):
        s_path = self.__parent.get_path_field().get().split("/")
        new_path = "/".join(s_path[:-2]) + "/"
        self.__parent.update_path_field(new_path)
        if self.__parent.get_last_active_panel() == "l":
            self.__parent.set_left_panel_path(new_path)
        elif self.__parent.get_last_active_panel() == "r":
            self.__parent.set_right_panel_path(new_path)
        if self.__parent.get_last_active_panel() == "l":
            self.__parent.update_left_panel()
        elif self.__parent.get_last_active_panel() == "r":
            self.__parent.update_right_panel()

    def find(self):
        current_dir = "/"
        item_to_find = self.__parent.get_path_field().get()
        if item_to_find == current_dir:
            return
        if self.__parent.get_last_active_panel() == "l":
            self.__parent.get_right_panel().delete(0, END)
        elif self.__parent.get_last_active_panel() == "r":
            self.__parent.get_left_panel().delete(0, END)
        is_found = False
        for address, directories, files in os.walk(current_dir):
            for file in files:
                if file == item_to_find:
                    if self.__parent.get_last_active_panel() == "l":
                        self.__parent.get_right_panel().insert(0, os.path.join(address, file))
                    elif self.__parent.get_last_active_panel() == "r":
                        self.__parent.get_left_panel().insert(0, os.path.join(address, file))
                    is_found = True
            for directory in directories:
                if directory == item_to_find:
                    if self.__parent.get_last_active_panel() == "l":
                        self.__parent.get_right_panel().insert(0, os.path.join(address, directory))
                    elif self.__parent.get_last_active_panel() == "r":
                        self.__parent.get_left_panel().insert(0, os.path.join(address, directory))
                    is_found = True
        if not is_found:
            tkinter.messagebox.showwarning("Warning", "No items named " + item_to_find + " found!\n")
            self.__parent.update_left_panel()
            self.__parent.update_right_panel()

    def copy(self):
        item_path = ""
        path_to_copy = simpledialog.askstring("Move", "Enter the path where you want to copy:")
        if not path_to_copy:
            tkinter.messagebox.showwarning("Error", "You did not enter anything")
            return
        if self.__parent.get_last_active_panel() == "l":
            item = self.__parent.get_left_panel().get(self.__parent.get_left_panel().curselection())
            item_path = self.__parent.get_left_panel_path() + item
        elif self.__parent.get_last_active_panel() == "r":
            item = self.__parent.get_right_panel().get(self.__parent.get_right_panel().curselection())
            item_path = self.__parent.get_right_panel_path() + item
        if mb.askyesno("Copying", "\nCopy from " + item_path + "\n To " + path_to_copy):
            if os.path.isdir(item_path):
                process = subprocess.Popen(["cp", "-R", item_path, path_to_copy])
            else:
                process = subprocess.Popen(["cp", item_path, path_to_copy],
                                        stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            output, error = process.communicate()
            if error:
                tkinter.messagebox.showwarning("Copying Problem", "An error occurred or you do not have enough permissions")
        self.__parent.update_left_panel()
        self.__parent.update_right_panel()

    def move(self):
        new_path = simpledialog.askstring("Move",
                                        "Enter the full path to the directory where you want to move:")
        if not os.path.isdir(new_path):
            tkinter.messagebox.showwarning("Error", "The path does not point to a directory!")
            return
        item_path = ""
        if self.__parent.get_last_active_panel() == "l":
            item = self.__parent.get_left_panel().get(self.__parent.get_left_panel().curselection())
            if not item:
                tkinter.messagebox.showwarning("Error", "You did not select an item to move")
                return
            item_path = self.__parent.get_left_panel_path() + item
        elif self.__parent.get_last_active_panel() == "r":
            item = self.__parent.get_right_panel_path().get(self.__parent.get_right_panel().curselection())
            if not item:
                tkinter.messagebox.showwarning("Error", "You did not select an item to move")
                return
            item_path = self.__parent.get_right_panel_path() + item
        process = subprocess.Popen(["mv", item_path, new_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = process.communicate()
        if error:
            tkinter.messagebox.showwarning("Moving Problem", "An error occurred or you do not have enough permissions!")
        self.__parent.update_left_panel()
        self.__parent.update_right_panel()

    def rename(self):
        new_name = simpledialog.askstring("Rename", "Enter the new name: ")
        if not new_name:
            tkinter.messagebox.showwarning("Error", "You did not enter anything!")
            return
        item_path = ""
        target_path = ""
        if self.__parent.get_last_active_panel() == "l":
            item = self.__parent.get_left_panel().get(self.__parent.get_left_panel().curselection())
            item_path = self.__parent.get_left_panel_path() + item
            target_path = self.__parent.get_left_panel_path() + new_name
        elif self.__parent.get_last_active_panel() == "r":
            item = self.__parent.get_right_panel().get(self.__parent.get_right_panel().curselection())
            item_path = self.__parent.get_right_panel_path() + item
            target_path = self.__parent.get_right_panel_path() + new_name
        process = subprocess.Popen(["mv", item_path, target_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = process.communicate()
        if error:
            tkinter.messagebox.showwarning("Renaming Problem", "An error occurred or you do not have enough permissions!")
        self.__parent.update_left_panel()
        self.__parent.update_right_panel()

    def mkdir(self):
        dir_name = simpledialog.askstring("Create Directory", "Enter the name of the new directory: ")
        if not dir_name:
            tkinter.messagebox.showwarning("Error", "You did not enter anything!")
            return
        path_to_create = ""
        if self.__parent.get_last_active_panel() == "l":
            self.__parent.update_path_field(self.__parent.get_left_panel_path())
            path_to_create = self.__parent.get_left_panel_path() + dir_name
        elif self.__parent.get_last_active_panel() == "r":
            self.__parent.update_path_field(self.__parent.get_right_panel_path())
            path_to_create = self.__parent.get_right_panel_path() + dir_name
        if os.path.isdir(path_to_create) or os.path.isfile(path_to_create):
            tkinter.messagebox.showwarning(title="Warning", message="An object at the selected path already exists!")
            return
        if mb.askyesno(title="Create Folder?", message=dir_name):
            os.makedirs(path_to_create)
        self.__parent.update_left_panel()
        self.__parent.update_right_panel()

    def create_file(self):
        file_name = simpledialog.askstring("Create File", "Enter the file name: ")
        if not file_name:
            tkinter.messagebox.showwarning("Error", "You did not enter anything!")
            return
        path_to_create = ""
        if self.__parent.get_last_active_panel() == "l":
            self.__parent.update_path_field(self.__parent.get_left_panel_path())
            path_to_create = self.__parent.get_left_panel_path() + file_name
        elif self.__parent.get_last_active_panel() == "r":
            self.__parent.update_path_field(self.__parent.get_right_panel_path())
            path_to_create = self.__parent.get_right_panel_path() + file_name
        if os.path.exists(path_to_create):
            tkinter.messagebox.showwarning(title="Warning", message="An object at the specified path already exists!")
            return
        if mb.askyesno(title="Create File?", message=path_to_create):
            process = subprocess.Popen(["touch", path_to_create], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            output, error = process.communicate()
            if error:
                tkinter.messagebox.showwarning("File Creation Problem", "An error occurred or you do not have enough permissions!")
            if self.__parent.get_last_active_panel() == "l":
                self.__parent.update_left_panel()
            elif self.__parent.get_last_active_panel() == "r":
                self.__parent.update_left_panel()

    def delete(self):
        full_path = ""
        if self.__parent.get_last_active_panel() == "l":
            full_path = self.__parent.get_path_field().get() + \
                        self.__parent.get_left_panel().get(self.__parent.get_left_panel().curselection())
        elif self.__parent.get_last_active_panel() == "r":
            full_path = self.__parent.get_path_field().get() + \
                        self.__parent.get_right_panel().get(self.__parent.get_right_panel().curselection())
        if mb.askyesno("Delete", "Are you sure you want to delete " + full_path + "?"):
            if os.path.isdir(full_path):
                process = subprocess.Popen(["rm", "-rf", full_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            else:
                process = subprocess.Popen(["rm", full_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            output, error = process.communicate()
            if error:
                tkinter.messagebox.showwarning("Deletion Problem", "An error occurred or you do not have enough permissions!")
        self.__parent.update_left_panel()
        self.__parent.update_right_panel()

    def info(self):
        item = ""
        if self.__parent.get_last_active_panel() == "l":
            item = self.__parent.get_left_panel().get(self.__parent.get_left_panel().curselection())
        elif self.__parent.get_last_active_panel() == "r":
            item = self.__parent.get_right_panel().get(self.__parent.get_right_panel().curselection())
        full_path = self.__parent.get_path_field().get() + item
        size = os.path.getsize(full_path)
        last_m_time = os.path.getmtime(full_path)
        c_time = os.path.getctime(full_path)
        message = f"Size: {size} bytes\n" + f"Last modified: {time.ctime(last_m_time)}\n" \
                + f"Creation date: {time.ctime(c_time)}"
        tkinter.messagebox.showinfo("Information", message)

    def make_soft_link(self):
        link_name = simpledialog.askstring("Create Link", "Enter the link name:")
        if not link_name:
            tkinter.messagebox.showwarning("Error", "You did not enter anything")
            return
        item = ""
        if self.__parent.get_last_active_panel() == "l":
            item = self.__parent.get_left_panel().get(self.__parent.get_left_panel().curselection())
        elif self.__parent.get_last_active_panel() == "r":
            item = self.__parent.get_right_panel().get(self.__parent.get_right_panel().curselection())
        full_path = self.__parent.get_path_field().get() + item
        process = subprocess.Popen(["ln", "-s", full_path, link_name])
        output, error = process.communicate()
        if error:
            tkinter.messagebox.showwarning("Error", "An error occurred while creating the link!")
            return
        self.__parent.update_left_panel()
        self.__parent.update_right_panel()

    def make_hard_link(self):
        link_name = simpledialog.askstring("Create Link", "Enter the link name:")
        if not link_name:
            tkinter.messagebox.showwarning("Error", "You did not enter anything")
            return
        item = ""
        if self.__parent.get_last_active_panel() == "l":
            item = self.__parent.get_left_panel().get(self.__parent.get_left_panel().curselection())
        elif self.__parent.get_last_active_panel() == "r":
            item = self.__parent.get_right_panel().get(self.__parent.get_right_panel().curselection())
        full_path = self.__parent.get_path_field().get() + item
        process = subprocess.Popen(["ln", full_path, link_name])
        output, error = process.communicate()
        if error:
            tkinter.messagebox.showwarning("Error", "An error occurred while creating the link!")
            return
        self.__parent.update_left_panel()
        self.__parent.update_right_panel()
