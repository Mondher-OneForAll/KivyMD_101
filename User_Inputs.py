from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRoundFlatButton, MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivy.lang import Builder
from helpers import username_helper


class DemoApp(MDApp):

    def build(self):
        screen = MDScreen()
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.theme_style = "Light"
        # username = MDTextField(text="Enter username",
        # pos_hint={"center_x":0.5, "center_y":0.5},
        #                       size_hint_x=None, width=300)

        button = MDRoundFlatButton(text="Show", pos_hint={"center_x": 0.5, "center_y": 0.4},
                                   on_release=self.showData)
        self.username = Builder.load_string(username_helper)
        screen.add_widget(self.username)
        screen.add_widget(button)
        return screen

    def showData(self, obj):
        if self.username.text is "":
            check_string = "Please enter a username"
        else:
            check_string = self.username.text + " doesn't exist!!"

        close_button = MDFlatButton(text="Close", on_release=self.closeDialog)
        more_button = MDFlatButton(text="More")
        self.dialog = MDDialog(title="Username Check", text=check_string,
                               size_hint=(0.7, 1), buttons=[close_button, more_button])
        self.dialog.open()

    def closeDialog(self, obj):
        self.dialog.dismiss()


if __name__ == "__main__":
    DemoApp().run()
