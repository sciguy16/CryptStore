import gi
import sys
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class MyWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title='This Encryption Method is stupid')

        self.box = Gtk.Box(spacing=6)
        self.add(self.box)

        self.button = Gtk.Button(label="Open Entry Form")
        self.button.connect("clicked", self.on_button_clicked)
        self.box.pack_start(self.button, True, True, 0)

        self.button1 = Gtk.Button(label="Generate a Key1")
        self.button1.connect("clicked", self.on_button1_clicked)
        self.box.pack_start(self.button1, True, True, 0)

    def on_button_clicked(self, widget):
        print("Trying to Open Entry  Form")
        entryForm.show_all()

    def on_button1_clicked(self, widget):
        print("Fuck you dave")


class EntryWindow(Gtk.Window):
    def __init__(self):
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

        self.entryFile = Gtk.Button(label="Choose a File")
        self.entryFile.connect("clicked", self.on_file_clicked)
        vbox.pack_start(self.entryFile, True, True, 0)

        self.entryEncrypt = Gtk.Button(label="Encrypt")
        self.entryEncrypt.connect("clicked", self.on_encrypt_clicked)
        vbox.pack_start(self.entryEncrypt, True, True, 0)


        self.entryCancel = Gtk.Button(label="Cancel")
        self.entryCancel.connect("clicked", self.on_cancel_clicked)
        vbox.pack_start(self.entryCancel, True, True, 0)

        self.entryPath   = Gtk.Button(label="Cancel")
        self.entryCancel.connect("clicked", self.on_cancel_clicked)
        vbox.pack_start(self.entryCancel, True, True, 0)

    def on_encrypt_clicked(self, button):
        print("We're now encrypting")
        print("Name = ", self.entryName.get_text())
        print("Age = ", self.entryAge.get_text())
        print("Address = ", self.entryAddress.get_text())
        print("Phone Number = ", self.entryNum.get_text())
        print("Password = Do you think i'd be this stupid ;) ")
        print("Path = ", absolutely_path)
    def on_file_clicked(self, button):
        files.show_all()
    def on_cancel_clicked(self, button):
        print("Bye Bye")
        self.hide()

class FileChooserWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="FileChooser Example")

        box = Gtk.Box(spacing=6)
        self.add(box)

        button1 = Gtk.Button("Choose File")
        button1.connect("clicked", self.on_file_clicked)
        box.add(button1)

        button2 = Gtk.Button("Choose Folder")
        button2.connect("clicked", self.on_folder_clicked)
        box.add(button2)

    def on_file_clicked(self, widget):
        global absolutely_path
        dialog = Gtk.FileChooserDialog("Please choose a file", self,
            Gtk.FileChooserAction.OPEN,
            (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
             Gtk.STOCK_OPEN, Gtk.ResponseType.OK))

        self.add_filters(dialog)

        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            print("Open clicked")
            print("File selected: " + dialog.get_filename())
            absolutely_path = dialog.get_filename()
            self.hide()
            print(absolutely_path)
        elif response == Gtk.ResponseType.CANCEL:
            print("Cancel clicked")
            self.hide()

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

    def on_folder_clicked(self, widget):
        global absolutely_path
        dialog = Gtk.FileChooserDialog("Please choose a folder", self,
            Gtk.FileChooserAction.SELECT_FOLDER,
            (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
             "Select", Gtk.ResponseType.OK))
        dialog.set_default_size(800, 400)

        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            print("Select clicked")
            print("Folder selected: " + dialog.get_filename())
            absolutely_path = dialog.get_filename()
            self.hide()
            print(absolutely_path)
        elif response == Gtk.ResponseType.CANCEL:
            print("Cancel clicked")
            self.hide()
        dialog.destroy()


absolutely_path = None
print(sys.version)
entryForm = EntryWindow()
entryForm.connect("delete-event", Gtk.main_quit)
files = FileChooserWindow()
files.connect("delete-event", Gtk.main_quit)
win = MyWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()