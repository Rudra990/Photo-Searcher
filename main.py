from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import wikipedia
import requests




Builder.load_file('frontend.kv')


class FirstScreen(Screen):
    def get_image_link(self):
        ## It gets user query from input
        query = self.manager.current_screen.ids.user_query.text

        ##get wikipedia page and list of image urls
        page = wikipedia.page(query)
        image_link = page.images[0]

        return image_link

    def download_image(self):

        req = requests.get(self.get_image_link())
        imagepath = 'files/image2.jpg'
        with open(imagepath, 'wb') as file:
            file.write(req.content)

        return imagepath

    def set_image(self):
        ##Set the image in the image widget

        self.manager.current_screen.ids.img.source = self.download_image()




class RootWidget(ScreenManager):
    pass


class MainApp(App):

    def build(self):
        return RootWidget()



MainApp().run()













