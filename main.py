import tkinter as tk

from Labelling.backend.images import ImagePaths

from Labelling.backend.backend import Backend
from Labelling.graphics.bottomtoolbar.bottomtoolbar import BottomToolBar
from Labelling.graphics.menubar.menubar import MenuBar
from Labelling.graphics.toolbar.toolbar import ToolBar
from Labelling.graphics.workspace.workspace import WorkSpace

from Labelling.graphics.file.image_paths import tk_open_dir, tk_open_files
from Labelling.graphics.popup import popup

class App:
    def __init__(self):
        # Graphics
        self.root = tk.Tk()
        self.root.title("Computer Vision Labeller")
        self.root.geometry("500x500")   # Makes window size 500x500

        # Backend
        self.backend: Backend = Backend(self)

        self.menu_bar: MenuBar = MenuBar(self)
        self.tool_bar: ToolBar = ToolBar(self)
        self.workspace: WorkSpace = WorkSpace(self)
        self.bottom_tool_bar: BottomToolBar = BottomToolBar(self)

    def add_img_dir(self):
        self.backend.image_paths.load_dir(tk_open_dir())
        self.workspace.display_image(self.backend.image_paths.next_image())

    def add_img_files(self):
        self.backend.image_paths.load_files(tk_open_files())
        self.workspace.display_image(self.backend.image_paths.next_image())

    def next_image(self, event=None):
        self.workspace.save()   # Automatically save workspace -- may be unintuitive
        self.workspace.reset_workspace()
        self.workspace.display_image(self.backend.image_paths.next_image())
        print(f"Image: {self.backend.image_paths.get_image_path()}")

    def prev_image(self, event=None):
        self.workspace.save()   # Automatically save workspace -- may be unintuitive
        self.workspace.reset_workspace()
        self.workspace.display_image(self.backend.image_paths.prev_image())
        print(f"Image: {self.backend.image_paths.get_image_path()}")


if __name__ == '__main__':
    app = App()
    app.bottom_tool_bar.line_width.set(1)
    app.root.mainloop()
