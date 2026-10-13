
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class MyApp(App):
    def build(self):
        layout = BoxLayout(
            orientation="vertical",
            padding=30,
            spacing=20
        )
        self.message = Label(
            text="မင်္ဂလာပါ!",
            font_size=28
        )
        button = Button(
            text="နှိပ်ပါ",
            font_size=22
        )
        button.bind(on_press=self.change_text)
        layout.add_widget(self.message)
        layout.add_widget(button)
        return layout

    def change_text(self, instance):
        self.message.text = "ကျွန်တော့်ရဲ့ ပထမဆုံး App!"

MyApp().run()
