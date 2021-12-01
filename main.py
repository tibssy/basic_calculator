from kivymd.app import MDApp
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window

Window.size = 540, 1120
Builder.load_file('calc_layout.kv')


class MyLayout(Widget):
    history_left = ''
    history_right = ''
    history_list = []

    def clear(self):
        self.ids.calc_input.text = '0'

    def clear_history(self):
        self.history_left = ''
        self.history_right = ''
        self.clear()
        self.history()

    def erase(self):
        self.ids.calc_input.text = self.ids.calc_input.text[:-1] if len(str(self.ids.calc_input.text)) > 1 else '0'

    def undo(self):
        self.history_list.insert(0, self.history_list.pop())
        self.ids.calc_input.text = self.history_list[0]

    def button_press(self, button):
        prior = self.ids.calc_input.text
        if 'Error' in prior:
            self.ids.calc_input.text = ''
        if prior == '0' and button != '.':
            if button in ['+', '*', '/']:
                self.ids.calc_input.text = '0'
            else:
                self.ids.calc_input.text = str(button)
        else:
            self.ids.calc_input.text += str(button)

    def equals(self):
        try:
            res = round(eval(self.ids.calc_input.text), 8)
            if str(res).endswith('.0'):
                res = int(res)
            self.history_left += '\n' + self.ids.calc_input.text
            self.ids.calc_input.text = str(res)
            self.history_right += '\n' + self.ids.calc_input.text
            self.history()
        except:
            self.ids.calc_input.text = 'Error'

    def history(self):
        self.ids.history_left.text = self.history_left
        self.ids.history_right.text = self.history_right
        self.history_list = list(sum(list(zip(self.history_left.split('\n')[1:], self.history_right.split('\n')[1:])), ()))


class CalculatorApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Orange"
        self.theme_cls.primary_hue = 'A700'
        self.theme_cls.theme_style = "Dark"
        return MyLayout()


CalculatorApp().run()
