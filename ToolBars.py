from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window


Window.size = (360, 600)
screen_helper = """
Screen:
    MDBoxLayout:
        orientation: "vertical"
        MDTopAppBar:
            title: "Demo Application"
            left_action_items: [["menu", lambda x: app.navigation_draw()]]
            right_action_items: [["clock", lambda x: app.navigation_draw()]]
            elevation: 4
            
        MDLabel:
            text: "Hello World"
            halign: "center"
            
        MDBottomAppBar:
            MDTopAppBar:
                icon: "language-python"
                icon_color: 1, 1, 1, 1
                mode: "end"
                type: "bottom"
                left_action_items: [["coffee", lambda x: app.navigation_draw()]]
                on_action_button: app.navigation_draw()
"""


class DemoApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Red"
        screen = Builder.load_string(screen_helper)
        return screen

    def navigation_draw(self):
        print("navigation")


if __name__ == '__main__':
    DemoApp().run()
