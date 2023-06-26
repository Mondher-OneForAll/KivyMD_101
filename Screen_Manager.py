from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager

Window.size = (360, 600)

screen_helper = """
ScreenManager:
    MenuScreen:
    ProfileScreen:
    UploadScreen:
    
<MenuScreen>:
    name: "menu"
    MDRectangleFlatButton:
        text: "Profile"
        pos_hint: {"center_x":0.5, "center_y":0.5}
        on_press: root.manager.current = "profile"
        
    MDRectangleFlatButton:
        text: "Upload"
        pos_hint: {"center_x":0.5, "center_y":0.6}
        on_press: root.manager.current = "upload"


<ProfileScreen>:
    name: "profile"
    MDLabel:
        text: "Welcome Gabimaru"
        halign: "center"

    MDRectangleFlatButton:
        text: "Back"
        pos_hint: {"center_x":0.5, "center_y":0.2}
        on_press: root.manager.current = "menu"

<UploadScreen>:
    name: "upload"
    MDLabel:
        text: "Let's upload some files"
        halign: "center"

    MDRectangleFlatButton:
        text: "Back"
        pos_hint: {"center_x":0.5, "center_y":0.2}
        on_press: root.manager.current = "menu"
        
"""


class MenuScreen(Screen):
    pass


class ProfileScreen(Screen):
    pass


class UploadScreen(Screen):
    pass


sm = ScreenManager()
sm.add_widget(MenuScreen(name="menu"))
sm.add_widget(ProfileScreen(name="profile"))
sm.add_widget(UploadScreen(name="upload"))


class DemoApp(MDApp):
    def build(self):
        screen = Builder.load_string(screen_helper)
        return screen


if __name__ == '__main__':
    DemoApp().run()
