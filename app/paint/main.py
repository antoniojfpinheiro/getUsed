from random import random
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.graphics import Color, Ellipse, Line


class PaintWidget(Widget):

    # Generate a new starting point
    def on_touch_down(self, touch):
        color = (random(), 1, 1)
        with self.canvas:
            Color(*color, mode='hsv')
            d = 30.
            Ellipse(pos=(touch.x - d / 2, touch.y - d / 2), size=(d, d))
            touch.ud['line'] = Line(points=(touch.x, touch.y))

    # Create the line for each new touch
    def on_touch_move(self, touch):
        touch.ud['line'].points += [touch.x, touch.y]


class PaintApp(App):

    def build(self):
        parent = Widget()
        self.painter = PaintWidget()
        btn_clear = Button(text='Clear', pos=(200, 0))
        btn_clear.bind(on_release=self.clear_canvas)
        parent.add_widget(self.painter)
        parent.add_widget(btn_clear)

        self.title = 'getUsed App Collection'
        self.icon = '../resources/getused_icon.ico'
        print(self.get_application_icon())

        return parent

    def clear_canvas(self, obj):
        self.painter.canvas.clear()


if __name__ == '__main__':
    PaintApp().run()
