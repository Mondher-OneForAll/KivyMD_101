from kivymd.app import MDApp
from kivymd.uix.label import MDLabel, MDIcon


class DemoApp(MDApp):
    def build(self):
        label = MDLabel(text="Hello World", halign="center", theme_text_color="Custom",
                        text_color=(0, 1, 0, 1), font_style="H2")
        icon_label = MDIcon(icon="language-python", pos_hint={"center_x":0.5, "center_y":0.5})
        return icon_label


if __name__ == "__main__":
    DemoApp().run()
