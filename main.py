from Jade_Calc import Jade_Calc
from Count_Days import Calc_Days, Calc_Weeks
from Files import FileReader as reader
from WebScraper import Scraper
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel
from kivymd.uix.selectioncontrol import MDSwitch

# Define the layout of the app using KV language
KV = '''
MainScreen:
    orientation: 'vertical'
    spacing: 20
    padding: 20

    # Label and Dropdown for the new menu
    MDLabel:
        text: "Select Upcoming Version"  # Change this text to modify the label above the new dropdown
        halign: "center"
    MDRaisedButton:
        id: dropdown_btn_new
        text: "Select"  # Initial text for the new dropdown button
        size_hint_x: 1  # Take up the entire width
        on_release: app.menu_new.open()

    # Existing Label and Dropdown 1
    MDLabel:
        text: "Equilibrium Level"  # Change this text to modify the label above the first dropdown
        halign: "center"
    MDRaisedButton:
        id: dropdown_btn_1
        text: "Select"  # Initial text for the first dropdown button
        size_hint_x: 1  # Take up the entire width
        on_release: app.menu_1.open()

    # Label and Selector for Dropdown 2
    MDLabel:
        text: "Memory Of Chaos"  # Change this text to modify the label above the second dropdown
        halign: "center"

    # GridLayout for Switch and Labels
    GridLayout:
        cols: 3
        size_hint_x: 0.6  # Adjust width of the entire layout
        pos_hint: {"center_x": 0.475}  # Center horizontally
        spacing: 20
        
        MDLabel:
            text: "Stages"
            halign: "left"
            size_hint_x: 0.2  # Adjust the size_hint_x to make labels and switch align better
        
        MDSwitch:
            id: option_switch
            on_active: app.update_menu_2(self.active)
            size_hint_x: 0.2  # Reduce the size of the switch (less wide)
            size_hint: None, None  # Disable size hints to allow setting custom width
            width: 40  # Set the width of the switch explicitly
            height: dp(48)  # Set the height of the switch explicitly to maintain aspect ratio
        
        MDLabel:
            text: "Stars"
            halign: "right"
            size_hint_x: 0.2  # Adjust the size_hint_x to make labels and switch align better

    # Dropdown 2 (Options controlled by switch)
    MDRaisedButton:
        id: dropdown_btn_2
        text: "Select"  # Initial text for the second dropdown button
        size_hint_x: 1  # Take up the entire width
        on_release: app.menu_2.open()

    # Label and Dropdown 3
    MDLabel:
        text: "Pure Fiction (Stars)"  # Change this text to modify the label above the third dropdown
        halign: "center"
    MDRaisedButton:
        id: dropdown_btn_3
        text: "Select"  # Initial text for the third dropdown button
        size_hint_x: 1  # Take up the entire width
        on_release: app.menu_3.open()

    # Label and Dropdown 4
    MDLabel:
        text: "Apocalyptic Shadow (Stars)"  # Change this text to modify the label above the fourth dropdown
        halign: "center"
    MDRaisedButton:
        id: dropdown_btn_4
        text: "Select"  # Initial text for the fourth dropdown button
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
    list1 = list
    list2 = list
    def build(self):

        url1 = "https://docs.google.com/spreadsheets/d/12SYPRGPIVJ2-bY01ksF4aqdinZDbyD-LN2ipeB5i6T0/export?format=csv&gid=0"
        url2 = "https://docs.google.com/spreadsheets/d/140MawDp6uzxSR6lgICO4USXKe7QektrSHRstomDdsVs/export?format=csv&gid=0"
        Scraper.scrapeToFile(data=Scraper.convert_to_string(Scraper.scrape(url1)),name='Data',extension='.txt')
        Scraper.scrapeToFile(data=Scraper.convert_to_string(Scraper.scrape(url2)),name='Data2',extension='.txt')
        self.list1 = reader.extractDates(reader.readFileAsList(name='Data',extension='.txt'))
        self.list2 = reader.extractDates(reader.readFileAsList(name='Data2',extension='.txt'))
        text = reader.extractText(reader.readFileAsList(name='Data2',extension='.txt'))
        # Load the KV string and set it as the root widget
        self.screen = Builder.load_string(KV)

        # Initial menu items for dropdowns
        self.menu_items_new = [{"text": f"{text[i]}", "viewclass": "OneLineListItem", "on_release": lambda x=f"{text[i]}", index=i: self.set_item_new(x, index)} for i in range(3)]
        menu_items_1 = [{"text": f"{i}", "viewclass": "OneLineListItem", "on_release": lambda x=f"{i}": self.set_item_1(x)} for i in range(7)]
        self.menu_items_2_set_1 = [{"text": f"{i}", "viewclass": "OneLineListItem", "on_release": lambda x=f"{i}": self.set_item_2(x)} for i in range(0,13)]
        self.menu_items_2_set_2 = [{"text": f"{i}", "viewclass": "OneLineListItem", "on_release": lambda x=f"{i}": self.set_item_2(x)} for i in range(0, 39, 3)]
        menu_items_3 = [{"text": f"{i}", "viewclass": "OneLineListItem", "on_release": lambda x=f"{i}": self.set_item_3(x)} for i in range(13)]
        menu_items_4 = [{"text": f"{i}", "viewclass": "OneLineListItem", "on_release": lambda x=f"{i}": self.set_item_4(x)} for i in range(13)]


        # Create dropdown menus for each button
        self.menu_new = MDDropdownMenu(
            caller=self.screen.ids.dropdown_btn_new,
            items=self.menu_items_new,  # The options for the new dropdown
            width_mult=4,  # Width multiplier for the dropdown menu
        )

        self.menu_1 = MDDropdownMenu(
            caller=self.screen.ids.dropdown_btn_1,
            items=menu_items_1,  # The options for the first dropdown
            width_mult=4,  # Width multiplier for the dropdown menu
        )

        self.menu_2 = MDDropdownMenu(
            caller=self.screen.ids.dropdown_btn_2,
            items=self.menu_items_2_set_1,  # Initially use Option Set 1 for the second dropdown
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

        self.selected_new_index = None  # To store the index of the selected item from the new dropdown
        return self.screen

    # Methods to set the selected item for each dropdown
    def set_item_new(self, text_item, index):
        self.screen.ids.dropdown_btn_new.text = text_item
        self.selected_new_index = index  # Store the index of the selected item
        self.menu_new.dismiss()  # Close the dropdown menu after selection

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

    # Method to handle the switch toggle
    def update_menu_2(self, is_active):
        if is_active:
            self.menu_2.items = self.menu_items_2_set_2  # Switch to Option Set 2
        else:
            self.menu_2.items = self.menu_items_2_set_1  # Switch to Option Set 1

    # Method to handle the Submit button press
    def on_button_press(self):
        # Get the selected options from all dropdowns
        selected_options = [
            self.screen.ids.dropdown_btn_new.text,
            self.screen.ids.dropdown_btn_1.text,
            self.screen.ids.dropdown_btn_2.text,
            self.screen.ids.dropdown_btn_3.text,
            self.screen.ids.dropdown_btn_4.text
        ]
        # Display the selected options and the index of the first dropdown item
        result_text = f"Selected Options: {', '.join(selected_options)}"
        if self.selected_new_index is not None:
            result_text += f"\nIndex of first dropdown: {self.selected_new_index}"
        #print(self.list2[self.selected_new_index])
        
        daily = Jade_Calc.daily(days=Calc_Days.calc_delta(self.list2[self.selected_new_index]))
        print(daily)
        weekly_su = Jade_Calc.weekly_su(weeks=Calc_Weeks.calc_delta(self.list2[self.selected_new_index]) ,eq_level=int(self.screen.ids.dropdown_btn_1.text))
        print(weekly_su)
        self.screen.ids.result_label.text = result_text

# Run the app
if __name__ == '__main__':
    MyApp().run()
