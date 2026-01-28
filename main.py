import sys
import Tkinter as tk
from tkFileDialog import askopenfilename, asksaveasfilename


class App(tk.Tk):

    """
    A simple demo of the basic Tkinter widgets. This can be used as a skeleton for a simple GUI applications.
    Unfortunately, on my system (Ubuntu) it looks like shit.
    """

    def __init__(self):
        tk.Tk.__init__(self)


        self.create_widget_frame()

        button_box = tk.Frame(self)
        tk.Button(button_box, text='OK', command=self.on_ok_clicked).grid(pady=15)
        button_box.pack()

        self.create_menu()
        self.set_keybindings()
        App.center_on_screen(self)


    @staticmethod
    def center_on_screen(toplevel):
        toplevel.update_idletasks()
        w = toplevel.winfo_screenwidth()
        h = toplevel.winfo_screenheight()
        size = tuple(int(_) for _ in toplevel.geometry().split('+')[0].split('x'))
        x = w/2 - size[0]/2
        y = h/2 - size[1]/2
        toplevel.geometry('%dx%d+%d+%d' % (size + (x, y)))


    def create_widget_frame(self):

        label_config = {'sticky': tk.E, 'column': 0, 'padx': 5, 'pady': 5}
        widget_config = {'sticky': tk.W, 'column': 1, 'padx': 5, 'pady': 5}

        widget_frame = tk.Frame(self)
        current_row = 0

        tk.Label(widget_frame, text='Entry (text): ').grid(label_config, row=current_row)
        self.entry = tk.Entry(widget_frame)
        self.entry.grid(row=current_row, column=1, sticky=tk.E)
        current_row += 1

        tk.Label(widget_frame, text='Scale (number): ').grid(label_config, row=current_row)
        self.scale = tk.Scale(widget_frame, from_=0, to=10, resolution=0.1, orient=tk.HORIZONTAL)
        self.scale.grid(widget_config, row=current_row)
        current_row += 1

        tk.Label(widget_frame, text='Checkbox (boolean): ').grid(label_config, row=current_row)
        self.checkbox_val = tk.IntVar()
        self.checkbox = tk.Checkbutton(widget_frame, variable=self.checkbox_val)
        self.checkbox.grid(widget_config, row=current_row)
        current_row += 1

        tk.Label(widget_frame, text='Spinbox (number): ').grid(label_config, row=current_row)
        self.spinbox = tk.Spinbox(widget_frame, from_=0, to=10)
        self.spinbox.grid(widget_config, row=current_row)
        current_row += 1

        self.enum_val = tk.StringVar(widget_frame)
        self.enum_val.set('one') # default value
        tk.Label(widget_frame, text='OptionMenu (enum): ').grid(label_config, row=current_row)
        self.combobox = tk.OptionMenu(widget_frame, self.enum_val, 'one', 'two', 'three')
        self.combobox.grid(widget_config, row=current_row)
        current_row += 1

        widget_frame.pack()


    def set_keybindings(self):
        self.bind_all('<Control-o>', lambda event: self.open_file())
        self.bind_all('<Control-s>', lambda event: self.save_file())
        self.bind_all('<Control-q>', self.quit_app)
        self.bind_all('<Control-h>', lambda event: self.show_help())
        self.bind_all('<Return>', lambda event: self.on_ok_clicked())


    def on_ok_clicked(self):
        print 'Entry text: %s' % self.entry.get()
        print 'Scale value: %.1f' % self.scale.get()
        print 'Checkbutton value: %i' % self.checkbox_val.get()
        print 'Spinbox value: %i' % int(self.spinbox.get())
        print 'OptionMenu value: %s' % self.enum_val.get()


    def create_menu(self):
        menubar = tk.Menu(self)
        
        fileMenu = tk.Menu(menubar, tearoff=False)
        menubar.add_cascade(label="File", underline=0, menu=fileMenu)
        fileMenu.add_command(label="Open", underline=1, command=self.open_file, accelerator="Ctrl+O")
        fileMenu.add_command(label="Save", underline=1, command=self.save_file, accelerator="Ctrl+S")
        fileMenu.add_command(label="Quit", underline=1, command=self.quit_app, accelerator="Ctrl+Q")
        
        helpMenu = tk.Menu(menubar, tearoff=False)
        menubar.add_cascade(label="Help", underline=0, menu=helpMenu)
        helpMenu.add_command(label="Help", underline=1, command=self.show_help, accelerator="Ctrl+H")
        helpMenu.add_command(label="About", underline=1, command=self.about_app)
        
        self.config(menu=menubar)


    def open_file(self):
        """Options are explained here: http://tkinter.unpythonic.net/wiki/tkFileDialog"""
        filename = askopenfilename(title='Open a file')
        if filename:
            print 'Open and do something with %s' % filename


    def save_file(self):
        """Options are explained here: http://tkinter.unpythonic.net/wiki/tkFileDialog"""
        filename = asksaveasfilename()
        if filename:
            print 'Save something to %s' % filename


    def quit_app(self, event):
        sys.exit(0)


    def show_help(self):
        print 'Open a link to online help/wiki here'


    def about_app(self):
        # FIXME: pressing return correctly closes dialog, but also incorrectly fires the main window's 'on_click' method
        about_text = """
        Put info about the application here, e.g., name, author(s), version,
        license, etc. This text will appear in the \"about\" dialog."""
        about_dialog = tk.Toplevel(self)
        about_dialog.title('About App')
        about_dialog.bind('<Escape>', lambda event: about_dialog.destroy())
        about_dialog.bind('<Return>', lambda event: about_dialog.destroy())
        App.center_on_screen(about_dialog)
        tk.Message(about_dialog, text=about_text).pack()
        button = tk.Button(about_dialog, text='Close', command=about_dialog.destroy).pack()



if __name__ == "__main__":
    app = App()
    app.mainloop()