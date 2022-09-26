from asyncio.windows_events import NULL
import kivy
kivy.require('2.1.0')
from kivy.base import runTouchApp
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button

PlanetTypes = ["Random", "Garden", "Ruins", "Megacity"]
StarTypes = ["Binary", "Red Giant", "White Dwarf", "Red Dwarf", "Medium Yellow", "Medium Orange", "Blue Giant", "Supernova"]

# class PlanetGenerator(GridLayout):

#     def __init__(self, **kwargs):
#         super(PlanetGenerator, self).__init__(**kwargs)
#         self.cols = 2
#         self.size = (300, 300)
#         self.add_widget(Label(text='Planet Type'))
#         self.add_widget(Spinner(text='Random',
#             values=(PlanetTypes)))
#     # PlanetTypeSpinner = Spinner(text='Random',
#     # values=(PlanetTypes),
#     # size=(100, 44)

# class GeneratorApp(App):
#     def build(self):

#         layout = GridLayout(cols=2, row_force_default=True, row_default_height=40)
#         self.labelObject = Label(text="Planet Type: ")
#         layout.add_widget(self.labelObject)
#         self.spinnerObject = Spinner(text='Random', values=(PlanetTypes))
#         self.spinnerObject.size_hint = (0.3,0.2)
#         self.spinnerObject.pos_hint = {'x': .1, 'y':.75}

#         layout.add_widget(self.spinnerObject)
#         # self.spinnerObject.bind(text=self.on_spinner_select)

#         return layout;
class GeneratorApp(App):
    def build(self):

        layout = GridLayout(cols=2, row_force_default=True, row_default_height=40)
        self.welcomeLabel = Label(text="[b]Welcome to the Planet Generator![/b]", markup=True)
        layout.add_widget(self.welcomeLabel)

        layout.add_widget(Label(text=""))

        self.PlanetType = Label(text="Planet Type: ")
        layout.add_widget(self.PlanetType)

        self.planetSpinner = Spinner(text='Random', values=(PlanetTypes))
        self.planetSpinner.size_hint = (0.3,0.2)
        self.planetSpinner.pos_hint = {'x': .1, 'y':.75}
        layout.add_widget(self.planetSpinner)
        self.planetSpinner.bind(text=self.on_spinner_select)

        self.starType = Label(text="Star Type: ")
        layout.add_widget(self.starType)


        self.starSpinner = Spinner(text='Random', values=(StarTypes))
        self.starSpinner.size_hint = (0.3,0.2)
        self.starSpinner.pos_hint = {'x': .1, 'y':.75}
        layout.add_widget(self.starSpinner)
        self.starSpinner.bind(text=self.on_spinner_select)

        self.GeneratePlanet = Button(text='Generate a planet!')
        layout.add_widget(self.GeneratePlanet)

        self.GeneratedPlanetObject = Label(text=f'You have entered orbit around a {self.planetSpinner.text} which is in orbit around a {self.starSpinner.text})')
        layout.add_widget(self.GeneratedPlanetObject)

        return layout;
    
    def on_spinner_select(self, spinner, text):
        self.GeneratedPlanetObject.text = f'You have entered orbit around a {self.planetSpinner.text} world which is in orbit around a {self.starSpinner.text} star'
        print('The planet spinner has chosen:', self.planetSpinner.text)
        print('The star spinner has chosen', self.starSpinner.text)
    
    def on_button_press(self, instance):
         if self.planetSpinner.text == 'Random':
            

    

if __name__ == '__main__':
    GeneratorApp().run()