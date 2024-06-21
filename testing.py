import tkinter as tk

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Menu Example")
        self.geometry("400x300")

        # Create container to hold all frames
        self.container = tk.Frame(self)
        self.container.pack(fill="both", expand=True)

        # Dictionary to hold references to all frames
        self.frames = {}

        # Initialize frames
        for F in (MenuScreen, StartScreen):
            page_name = F.__name__
            frame = F(parent=self.container, controller=self)
            self.frames[page_name] = frame

            # Put all frames in the same location
            frame.grid(row=0, column=0, sticky="nsew")

        # Show the initial frame
        self.show_frame("MenuScreen")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

class MenuScreen(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        label = tk.Label(self, text="This is the menu screen")
        label.pack(side="top", fill="x", pady=10)

        start_button = tk.Button(self, text="Start",
                                 command=lambda: controller.show_frame("StartScreen"))
        start_button.pack()

class StartScreen(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        label = tk.Label(self, text="This is the start screen")
        label.pack(side="top", fill="x", pady=10)

        menu_button = tk.Button(self, text="Back to Menu",
                                command=lambda: controller.show_frame("MenuScreen"))
        menu_button.pack()

if __name__ == "__main__":
    app = Application()
    app.mainloop()
