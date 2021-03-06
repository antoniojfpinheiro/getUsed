from kivy.uix.screenmanager import Screen
from kivy.app import App
from kivy.uix.widget import Widget


class CollectionScreen(Screen):
    pass


class PongScreen(Screen):
    pass


class MediaScreen(Screen):
    pass


class PaintScreen(Screen):
    pass


class BackButton(Widget):
    pass


class GetUsedApp(App):

    def build(self):
        # TUIO/Multitouch enabled
        # Config.set('input', 'multitouchscreen1', 'tuio,127.0.0.1:3333')

        self.title = 'getUsed App Collection'
        self.icon = '../resources/getused_icon.ico'
        print(self.get_application_icon())


if __name__ == '__main__':
    GetUsedApp().run()
