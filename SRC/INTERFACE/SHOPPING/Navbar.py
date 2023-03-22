"""
Nabar.py

Configure MarcoNeo's navbar on its shopping menu.
"""

#-------------------------------------------------------------------#

from SRC.INTERFACE.gui_utils import Frame, Label, AppButton

#-------------------------------------------------------------------#

class Navbar(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        
        self.configure(bg="black")
        self.setup_images()
        self.setup_label()
        self.setup_buttons()
        
    def setup_images(self):
        """
        Defines the images used in the menu.
        """
        return
    
    def setup_label(self):
        """
        Defines the labels used in the menu.
        """
        Label(self, text="Navbar").grid(row=0, column=0, padx=10, pady=10)
    
    def setup_buttons(self):
        """
        Defines the buttons used in the menu.
        """
        shopping_menus = self.master.gui.app.config['Shopping']
        row = 1
        for menu in shopping_menus:
            button = AppButton(self, text=menu, command=lambda menu=menu: self.toggle(menu))
            setattr(self, f"{menu.lower()}_btn", button)
            button.grid(row=row, column=0, padx=10, pady=10)
            row += 1
            
        back_btn = AppButton(self, text="Back", command=lambda: self.master.gui.change_menu(self.master.gui.main_menu))
        setattr(self, "back_btn", back_btn)
        back_btn.grid(row=row, column=0, padx=10, pady=10)

    def toggle(self, toggle):
        """
        Changes the current toggle of the navbar.
        """
        self.navbar_current_toggle = toggle
        self.master.body.update_body(toggle)
    