from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window

Window.size = (360, 600)

navigation_helper = """
Screen:
    MDNavigationLayout:
        MDScreenManager:
            Screen:
                MDBoxLayout:
                    orientation: "vertical"
                    MDTopAppBar:
                        title: "Demo"
                        left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]
                        elevation: 4
                    Widget:
        MDNavigationDrawer:
            id: nav_drawer
            MDBoxLayout:
                orientation: "vertical"
                spacing: "8dp"
                padding: "8dp"
       
                Image:
                    source: "KivyMD.jpg"
                MDLabel:
                    text: "Tokito"
                    font_style: "Subtitle1"
                    size_hint_y: None
                    height: self.texture_size[1]
                    
                MDLabel:
                    text: "Tokito@Hashira.com"
                    font_style: "Caption"
                    size_hint_y: None
                    height: self.texture_size[1]
                    
                ScrollView:
                    MDList:
                        OneLineIconListItem:
                            text: "Profile"
                            IconLeftWidget:
                                icon: "face-man-profile"
                                
                        OneLineIconListItem:
                            text: "Upload"
                            IconLeftWidget:
                                icon: "file-upload"
                                
                        OneLineIconListItem:   
                            text: "Logout"   
                            IconLeftWidget:   
                                icon: "logout"
                            
"""


class DemoApp(MDApp):
    def build(self):
        screen = Builder.load_string(navigation_helper)
        return screen


if __name__ == '__main__':
    DemoApp().run()
