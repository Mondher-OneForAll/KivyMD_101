from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp


class DemoApp(MDApp):
    def build(self):
        screen = Screen()
        table = MDDataTable(pos_hint={"center_x": 0.5, "center_y": 0.5},
                            size_hint=(0.9, 0.7), check=True, rows_num=10,
                            column_data=[
                                ("No.", dp(18)),
                                ("Food", dp(20)),
                                ("Calories", dp(20))
                            ],
                            row_data=[
                                ("1", "Pizza", "300"),
                                ("2", "Burger", "250"),
                                ("3", "Tacos", "200"),
                                ("4", "Otas", "150"),
                                ("5", "Orange Jus", "100"),
                                ("6", "Pizza", "300"),
                                ("7", "Pizza", "300"),
                                ("8", "Pizza", "300"),
                                ("9", "Pizza", "300"),
                            ])
        table.bind(on_check_press=self.check_press)
        table.bind(on_row_press=self.row_press)

        screen.add_widget(table)
        return screen

    def check_press(self, instance_table, current_row):
        print(instance_table, current_row)

    def row_press(self, instance_table, instance_row):
        print(instance_table, instance_row)


if __name__ == '__main__':
    DemoApp().run()
