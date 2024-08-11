from Jade_Calc import Jade_Calc
from Count_Days import Calc_Days, Calc_Weeks
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.button import MDRaisedButton

KV = '''
MainScreen:
    orientation: 'vertical'
    spacing: 20
    padding: 20
    
    # Dropdown 1
    MDRaisedButton:
        id: dropdown_btn_1
        text: "Select Option 1"
        on_release: app.menu_1.open()

    # Dropdown 2
    MDRaisedButton:
        id: dropdown_btn_2
        text: "Select Option 2"
        on_release: app.menu_2.open()

    # Dropdown 3
    MDRaisedButton:
        id: dropdown_btn_3
        text: "Select Option 3"
        on_release: app.menu_3.open()

    # Dropdown 4
    MDRaisedButton:
        id: dropdown_btn_4
        text: "Select Option 4"
        on_release: app.menu_4.open()
    
    # Submit Button
    MDRaisedButton:
        text: "Submit"
        on_release: app.on_button_press()

    # Label for displaying selected options
    MDLabel:
        id: result_label
        text: "Selected Options: None"
        halign: "center"
        size_hint_y: None
        height: self.texture_size[1]
'''

class MainScreen(MDBoxLayout):
    pass

class MyApp(MDApp):
    def build(self):
        # Load the KV string and set it as the root widget
        self.screen = Builder.load_string(KV)
        
        # Create dropdown menus
        menu_items_1 = [{"text": f"Option {i+1}", "viewclass": "OneLineListItem", "on_release": lambda x=f"Option {i+1}": self.set_item_1(x)} for i in range(5)]
        self.menu_1 = MDDropdownMenu(
            caller=self.screen.ids.dropdown_btn_1,
            items=menu_items_1,
            width_mult=4,
        )
        
        menu_items_2 = [{"text": f"Option {i+1}", "viewclass": "OneLineListItem", "on_release": lambda x=f"Option {i+1}": self.set_item_2(x)} for i in range(5)]
        self.menu_2 = MDDropdownMenu(
            caller=self.screen.ids.dropdown_btn_2,
            items=menu_items_2,
            width_mult=4,
        )

        menu_items_3 = [{"text": f"Option {i+1}", "viewclass": "OneLineListItem", "on_release": lambda x=f"Option {i+1}": self.set_item_3(x)} for i in range(5)]
        self.menu_3 = MDDropdownMenu(
            caller=self.screen.ids.dropdown_btn_3,
            items=menu_items_3,
            width_mult=4,
        )

        menu_items_4 = [{"text": f"Option {i+1}", "viewclass": "OneLineListItem", "on_release": lambda x=f"Option {i+1}": self.set_item_4(x)} for i in range(5)]
        self.menu_4 = MDDropdownMenu(
            caller=self.screen.ids.dropdown_btn_4,
            items=menu_items_4,
            width_mult=4,
        )
        
        return self.screen

    def set_item_1(self, text_item):
        self.screen.ids.dropdown_btn_1.text = text_item
        self.menu_1.dismiss()

    def set_item_2(self, text_item):
        self.screen.ids.dropdown_btn_2.text = text_item
        self.menu_2.dismiss()

    def set_item_3(self, text_item):
        self.screen.ids.dropdown_btn_3.text = text_item
        self.menu_3.dismiss()

    def set_item_4(self, text_item):
        self.screen.ids.dropdown_btn_4.text = text_item
        self.menu_4.dismiss()

    def on_button_press(self):
        selected_options = [
            self.screen.ids.dropdown_btn_1.text,
            self.screen.ids.dropdown_btn_2.text,
            self.screen.ids.dropdown_btn_3.text,
            self.screen.ids.dropdown_btn_4.text
        ]
        self.screen.ids.result_label.text = f"Selected Options: {', '.join(selected_options)}"

if __name__ == '__main__':
    MyApp().run()
