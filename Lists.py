from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.list import MDList, ThreeLineListItem, ThreeLineAvatarIconListItem, \
    ThreeLineIconListItem, IconLeftWidget, ImageRightWidget
from kivy.uix.scrollview import ScrollView
from kivy.lang import Builder

list_helper = """
Screen:
    ScrollView:
        MDList:
            id : container
        
"""


class DemoApp(MDApp):
    def build(self):
        """
        screen = Screen()
        list_view = MDList()
        scroll = ScrollView()
        for i in range(1, 21):
            icon = IconLeftWidget(icon="language-python")
            image = ImageRightWidget(source="KivyMD.jpg")
            items = ThreeLineAvatarIconListItem(text="item " + str(i),
                                          secondary_text="Hello from " + str(i),
                                          tertiary_text="........")
            items.add_widget(icon)
            items.add_widget(image)
            list_view.add_widget(items)

        scroll.add_widget(list_view)
        screen.add_widget(scroll)
        """
        screen = Builder.load_string(list_helper)
        return screen

    def on_start(self):
        for i in range(1, 21):
            icon = IconLeftWidget(icon="language-python")
            image = ImageRightWidget(source="KivyMD.jpg")
            items = ThreeLineAvatarIconListItem(text="item " + str(i),
                                                secondary_text="Hello from " + str(i),
                                                tertiary_text="........")

            items.add_widget(icon)
            items.add_widget(image)
            self.root.ids.container.add_widget(items)


if __name__ == '__main__':
    DemoApp().run()
