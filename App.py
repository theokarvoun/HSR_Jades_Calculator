from Jade_Calc import Jade_Calc
from Count_Days import Calc_Days, Calc_Weeks
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel

# Define the layout of the app using KV language
KV = '''
MainScreen:
    orientation: 'vertical'
    spacing: 20
    padding: 20
    
    # Label and Dropdown 1
    MDLabel:
        text: "Equilibrium Level"  # Change this text to modify the label above the first dropdown
        halign: "center"
    MDRaisedButton:
        id: dropdown_btn_1
        text: "Select"  # Initial text for the first dropdown button
        size_hint_x: 1  # Take up the entire width
        on_release: app.menu_1.open()

    # Label and Dropdown 2
    MDLabel:
        text: "MOC Stages (Fully Cleared)"  # Change this text to modify the label above the second dropdown
        halign: "center"
    MDRaisedButton:
        id: dropdown_btn_2
        text: "Select"  # Initial text for the second dropdown button
        size_hint_x: 1  # Take up the entire width
        on_release: app.menu_2.open()

    # Label and Dropdown 3
    MDLabel:
        text: "Dropdown Menu 3"  # Change this text to modify the label above the third dropdown
        halign: "center"
    MDRaisedButton:
        id: dropdown_btn_3
        text: "Select Option 3"  # Initial text for the third dropdown button
        size_hint_x: 1  # Take up the entire width
        on_release: app.menu_3.open()

    # Label and Dropdown 4
    MDLabel:
        text: "Dropdown Menu 4"  # Change this text to modify the label above the fourth dropdown
        halign: "center"
    MDRaisedButton:
        id: dropdown_btn_4
        text: "Select Option 4"  # Initial text for the fourth dropdown button
        size_hint_x: 1  # Take up the entire width
        on_release: app.menu_4.open()
    
    # Submit Button
    MDRaisedButton:
        text: "Submit"  # Text on the submit button
        size_hint_x: 1  # Take up the entire width
        on_release: app.on_button_press()

    # Label for displaying selected options
    MDLabel:
        id: result_label
        text: "Selected Options: None"  # Initial text of the result label
        halign: "center"
        size_hint_y: None
        height: self.texture_size[1]
'''

# Define the main screen layout
class MainScreen(MDBoxLayout):
    pass

# Define the main application class
class MyApp(MDApp):
    def build(self):
        # Load the KV string and set it as the root widget
        self.screen = Builder.load_string(KV)
        
        # Menu items for each dropdown menu
        # Change the text in these dictionaries to modify the dropdown options
        menu_items_1 = [{"text": f"{i+1}", "viewclass": "OneLineListItem", "on_release": lambda x=f"{i+1}": self.set_item_1(x)} for i in range(6)]
        menu_items_2 = [{"text": f"{i+1}", "viewclass": "OneLineListItem", "on_release": lambda x=f"{i+1}": self.set_item_2(x)} for i in range(12)]
        menu_items_3 = [{"text": f"Option {i+1}", "viewclass": "OneLineListItem", "on_release": lambda x=f"Option {i+1}": self.set_item_3(x)} for i in range(5)]
        menu_items_4 = [{"text": f"Option {i+1}", "viewclass": "OneLineListItem", "on_release": lambda x=f"Option {i+1}": self.set_item_4(x)} for i in range(5)]

        # Create dropdown menus for each button
        # The `caller` argument connects the dropdown to the correct button
        self.menu_1 = MDDropdownMenu(
            caller=self.screen.ids.dropdown_btn_1,
            items=menu_items_1,  # The options for the first dropdown
            width_mult=4,  # Width multiplier for the dropdown menu
        )
        self.menu_2 = MDDropdownMenu(
            caller=self.screen.ids.dropdown_btn_2,
            items=menu_items_2,  # The options for the second dropdown
            width_mult=4,
        )
        self.menu_3 = MDDropdownMenu(
            caller=self.screen.ids.dropdown_btn_3,
            items=menu_items_3,  # The options for the third dropdown
            width_mult=4,
        )
        self.menu_4 = MDDropdownMenu(
            caller=self.screen.ids.dropdown_btn_4,
            items=menu_items_4,  # The options for the fourth dropdown
            width_mult=4,
        )
        
        return self.screen

    # Methods to set the selected item for each dropdown
    # These methods are called when an option is selected from the dropdown
    def set_item_1(self, text_item):
        self.screen.ids.dropdown_btn_1.text = text_item
        self.menu_1.dismiss()  # Close the dropdown menu after selection

    def set_item_2(self, text_item):
        self.screen.ids.dropdown_btn_2.text = text_item
        self.menu_2.dismiss()

    def set_item_3(self, text_item):
        self.screen.ids.dropdown_btn_3.text = text_item
        self.menu_3.dismiss()

    def set_item_4(self, text_item):
        self.screen.ids.dropdown_btn_4.text = text_item
        self.menu_4.dismiss()

    # Method to handle the Submit button press
    def on_button_press(self):
        # Get the selected options from all dropdowns
        selected_options = [
            self.screen.ids.dropdown_btn_1.text,
            self.screen.ids.dropdown_btn_2.text,
            self.screen.ids.dropdown_btn_3.text,
            self.screen.ids.dropdown_btn_4.text
        ]
        # Display the selected options in the result label
        self.screen.ids.result_label.text = f"Selected Options: {', '.join(selected_options)}"

# Run the app
if __name__ == '__main__':
    MyApp().run()
