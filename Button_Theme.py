from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDFloatingActionButton, MDIconButton, MDRoundFlatButton


class DemoApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "DeepPurple"
        self.theme_cls.primary_hue = "A700"
        self.theme_cls.theme_style = "Dark"
        screen = MDScreen()
        btn_flat = MDRoundFlatButton(text="Hello World", pos_hint={"center_x": 0.5, "center_y": 0.5})
        icon_btn = MDFloatingActionButton(icon="language-python", pos_hint={"center_x": 0.5, "center_y": 0.7})
        screen.add_widget(icon_btn)
        screen.add_widget(btn_flat)

        return screen


if __name__ == "__main__":
    DemoApp().run()
