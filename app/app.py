from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout


class GetUsedScreen(AnchorLayout):
    pass


class GetUsedApp(App):

    def build(self):
        self.title = 'getUsed App Collection'
        self.icon = '../resources/getused_icon.ico'
        print(self.get_application_icon())
        return GetUsedScreen()


if __name__ == '__main__':
    GetUsedApp().run()
