import gi
import sys

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class MyWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title='This Encryption Method is stupid')
        self.set_border_width(10)

        self.box = Gtk.Box(spacing=6)
        self.add(self.box)

        self.button = Gtk.Button(label="Encrypt Files/Folders")
        self.button.connect("clicked", self.on_button_clicked)
        self.box.pack_start(self.button, True, True, 0)

        self.button1 = Gtk.Button(label="Decrypt Files/Folders")
        self.button1.connect("clicked", self.on_button1_clicked)
        self.box.pack_start(self.button1, True, True, 0)
        link = Gtk.LinkButton("https://www.sucss.org/sucss2bu", "OnlineHelp")
        self.box.pack_start(link, True, True, 0)
    def on_button_clicked(self, widget):
        print("Trying to Open Entry  Form")
        entryForm.show_all()

    def on_button1_clicked(self, widget):
        decryptWindow.show_all()


class EntryWindow(Gtk.Window):
    def __init__(self):
        self.set_border_width(10)
        Gtk.Window.__init__(self, title="Entry Demo")
        self.set_size_request(200, 100)

        self.timeout_id = None

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(vbox)

        self.entryName = Gtk.Entry()
        self.entryName.set_text("Name")
        vbox.pack_start(self.entryName, True, True, 0)

        self.entryAge = Gtk.Entry()
        self.entryAge.set_text("Age")
        vbox.pack_start(self.entryAge, True, True, 0)

        self.entryAddress = Gtk.Entry()
        self.entryAddress.set_text("Address")
        vbox.pack_start(self.entryAddress, True, True, 0)

        self.entryNum = Gtk.Entry()
        self.entryNum.set_text("Phone Number")
        vbox.pack_start(self.entryNum, True, True, 0)

        self.entryPassword = Gtk.Entry()
        self.entryPassword.set_text("Password")
        vbox.pack_start(self.entryPassword, True, True, 0)

        self.entryPassword1 = Gtk.Entry()
        self.entryPassword1.set_text("Confirm Password")
        vbox.pack_start(self.entryPassword1, True, True, 0)

        self.entryConfirm = Gtk.Button(label="Scrub")
        self.entryConfirm.connect("clicked", self.on_password_check)
        vbox.pack_start(self.entryConfirm, True, True, 0)

        self.entryFile = Gtk.Button(label="Choose a File")
        self.entryFile.connect("clicked", self.on_file_clicked)
        vbox.pack_start(self.entryFile, True, True, 0)

        self.entryEncrypt = Gtk.Button(label="Encrypt")
        self.entryEncrypt.connect("clicked", self.on_encrypt_clicked)
        vbox.pack_start(self.entryEncrypt, True, True, 0)


        self.entryCancel = Gtk.Button(label="Cancel")
        self.entryCancel.connect("clicked", self.on_cancel_clicked)
        vbox.pack_start(self.entryCancel, True, True, 0)

    def on_password_check(self,button):
        string1 = self.entryPassword.get_text()
        string2 = self.entryPassword1.get_text()
        print(string1, string2)
        if(len(string1)< 16):
            print("please make your password longer")

        if((string1==string2)):
            print("They're the same")

        else:
            print("They're not the same")
            dialog = PasswordToShort(self)
            response = dialog.run()
            if response == Gtk.ResponseType.OK:
                print("The OK button was clicked")
            elif response == Gtk.ResponseType.CANCEL:
                print("The Cancel button was clicked")
            dialog.destroy()


    def on_encrypt_clicked(self, button):
        print("We're now encrypting")
        print("Name = ", self.entryName.get_text())
        print("Age = ", self.entryAge.get_text())
        print("Address = ", self.entryAddress.get_text())
        print("Phone Number = ", self.entryNum.get_text())
        print("Password = Do you think i'd be this stupid ;) ")
        print("Confirm password = i'm really not that stupid, we're at a cyber security event.")
        print("Path = ", absolutely_path)
        string1 = self.entryPassword.get_text()
        string2 = self.entryPassword1.get_text()
        print(string1, string2)
        if (len(string1) < 16):
            print("Please Make Your Password Longer")

        if ((string1 == string2)):
            print("They're the same")
        else:
            print("They're not the same")
    def on_file_clicked(self, widget):
        global absolutely_path
        dialog = Gtk.FileChooserDialog("Please choose a file or folder", self,
            Gtk.FileChooserAction.OPEN,
            (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
             Gtk.STOCK_OPEN, Gtk.ResponseType.OK))

        self.add_filters(dialog)

        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            print("Open clicked")
            print("File/Folder selected: " + dialog.get_filename())
            absolutely_path = dialog.get_filename()

            print(absolutely_path)
        elif response == Gtk.ResponseType.CANCEL:
            print("Cancel clicked")


        dialog.destroy()

    def add_filters(self, dialog):
        filter_text = Gtk.FileFilter()
        filter_text.set_name("Text files")
        filter_text.add_mime_type("text/plain")
        dialog.add_filter(filter_text)

        filter_py = Gtk.FileFilter()
        filter_py.set_name("Python files")
        filter_py.add_mime_type("text/x-python")
        dialog.add_filter(filter_py)

        filter_any = Gtk.FileFilter()
        filter_any.set_name("Any files")
        filter_any.add_pattern("*")
        dialog.add_filter(filter_any)

    def on_cancel_clicked(self, button):
        print("Bye Bye")
        self.hide()
        absolutely_path = None

class Decrypt(Gtk.Window):
    def __init__(self):
        self.set_border_width(10)
        Gtk.Window.__init__(self, title="Entry Demo")
        self.set_size_request(200, 100)

        self.timeout_id = None

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(vbox)


        self.entryPassword = Gtk.Entry()
        self.entryPassword.set_text("Password")
        vbox.pack_start(self.entryPassword, True, True, 0)

        self.entryFile = Gtk.Button(label="Choose a File")
        self.entryFile.connect("clicked", self.on_file_clicked)
        vbox.pack_start(self.entryFile, True, True, 0)

        self.entryEncrypt = Gtk.Button(label="Decrypt")
        self.entryEncrypt.connect("clicked", self.on_decrypt_clicked)
        vbox.pack_start(self.entryEncrypt, True, True, 0)


        self.entryCancel = Gtk.Button(label="Close")
        self.entryCancel.connect("clicked", self.on_cancel_clicked)
        vbox.pack_start(self.entryCancel, True, True, 0)

    def on_cancel_clicked(self, button):
        print("Bye Bye")
        self.hide()
        absolutely_path = None
    def on_decrypt_clicked(self,button):
        print("We're now decrypting")
        print("Password = ", self.entryPassword.get_text())

    def on_file_clicked(self, widget):
        global absolutely_path
        dialog = Gtk.FileChooserDialog("Please choose a file or folder", self,
                                       Gtk.FileChooserAction.OPEN,
                                       (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
                                        Gtk.STOCK_OPEN, Gtk.ResponseType.OK))

        self.add_filters(dialog)

        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            print("Open clicked")
            print("File/Folder selected: " + dialog.get_filename())
            absolutely_path = dialog.get_filename()

            print(absolutely_path)
        elif response == Gtk.ResponseType.CANCEL:
            print("Cancel clicked")

        dialog.destroy()

    def add_filters(self, dialog):
        filter_text = Gtk.FileFilter()
        filter_text.set_name("Text files")
        filter_text.add_mime_type("text/plain")
        dialog.add_filter(filter_text)

        filter_py = Gtk.FileFilter()
        filter_py.set_name("Python files")
        filter_py.add_mime_type("text/x-python")
        dialog.add_filter(filter_py)

        filter_any = Gtk.FileFilter()
        filter_any.set_name("Any files")
        filter_any.add_pattern("*")
        dialog.add_filter(filter_any)
class PasswordToShort(Gtk.Dialog):

    def __init__(self, parent):
        Gtk.Dialog.__init__(self, "Password Check Failed", parent, 0,
            (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
             Gtk.STOCK_OK, Gtk.ResponseType.OK))

        self.set_default_size(150, 100)

        label = Gtk.Label("Please ensure your passwords are the same")

        box = self.get_content_area()
        box.add(label)
        self.show_all()



absolutely_path = None
print(sys.version)
entryForm = EntryWindow()
entryForm.connect("delete-event", Gtk.main_quit)
decryptWindow = Decrypt()
decryptWindow.connect("delete-event", Gtk.main_quit)
#files = FileChooserWindow()
#files.connect("delete-event", Gtk.main_quit)
win = MyWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()

