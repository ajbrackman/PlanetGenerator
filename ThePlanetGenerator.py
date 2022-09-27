from asyncio.windows_events import NULL
from turtle import width
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
import pandas as pd
import numpy
import random
import csv
import sys

PlanetTypes = pd.read_excel(r"C:\Users\brack\Documents\github\PlanetGenerator\planetTypes.xlsx", header=0)
StarTypes = pd.read_excel(r"C:\Users\brack\Documents\github\PlanetGenerator\starTypes.xlsx", header=0)

print(PlanetTypes)
print(StarTypes)
PlanetList = list(PlanetTypes['Planet Types'].astype(str).values.tolist())
print(PlanetList)
StarList = list(StarTypes['Star Types'].astype(str).values.tolist())
print(StarList)
# PlanetList = PlanetTypes.to_string()

class GeneratorApp(App):
    def build(self):

        layout = GridLayout(cols=2, row_force_default=True, row_default_height=40)
        self.welcomeLabel = Label(text="[b]Welcome to the Planet Generator![/b]", markup=True)
        layout.add_widget(self.welcomeLabel)

        layout.add_widget(Label(text=""))

        self.PlanetType = Label(text="Planet Type: ")
        layout.add_widget(self.PlanetType)

        self.planetSpinner = Spinner(text='Random', values=(PlanetList))
        self.planetSpinner.size_hint = (0.3,0.2)
        self.planetSpinner.pos_hint = {'x': .1, 'y':.75}
        layout.add_widget(self.planetSpinner)
        self.planetSpinner.bind(text=self.on_spinner_select)

        self.starType = Label(text="Star Type: ")
        layout.add_widget(self.starType)


        self.starSpinner = Spinner(text='Random', values=(StarList))
        self.starSpinner.size_hint = (0.3,0.2)
        self.starSpinner.pos_hint = {'x': .1, 'y':.75}
        layout.add_widget(self.starSpinner)
        self.starSpinner.bind(text=self.on_spinner_select)

        self.GeneratePlanet = Button(text='Generate a planet!')
        layout.add_widget(self.GeneratePlanet)
        self.GeneratePlanet.bind(on_press = self.on_button_press)

        self.GeneratedPlanetObject = Label(text=f'You have entered orbit around a {self.planetSpinner.text} which is in orbit around a {self.starSpinner.text})', font_size = self.texture_size)
        self.GeneratedPlanetObject.size_hint = (0.2,0.2)
        layout.add_widget(self.GeneratedPlanetObject)

        return layout;
    
    def on_spinner_select(self, spinner, text):
        self.GeneratedPlanetObject.text = f'You have entered orbit around a {self.planetSpinner.text} world which is in orbit around a {self.starSpinner.text} star'
        print('The planet spinner has chosen:', self.planetSpinner.text)
        print('The star spinner has chosen', self.starSpinner.text)
    
    def on_button_press(self, instance):

        if self.planetSpinner.text == 'Random' and self.starSpinner.text == 'Random':
            RandomPlanet = random.choice(PlanetList)
            RandomStar = random.choice(StarList)
            print(RandomStar)
            print(RandomPlanet)
            self.GeneratedPlanetObject.text = f'You have entered orbit around a {RandomPlanet} world, which is in orbit around a {RandomStar} star.'

        elif self.planetSpinner.text == 'Random':
            RandomPlanet = random.choice(PlanetList)
            print(RandomPlanet)
            self.GeneratedPlanetObject.text = f'You have entered orbit around a {RandomPlanet} world, which is in orbit around a {self.starSpinner.text} star.'
        
        elif self.starSpinner.text == 'Random':
            RandomStar = random.choice(StarList)
            print(RandomStar)
            self.GeneratedPlanetObject.text = f'You have entered orbit around a {self.planetSpinner.text} world, which is in orbit around a {RandomStar} star.'

        elif self.planetSpinner.text == 'Random' and self.starSpinner.text == 'Random':
            RandomPlanet = random.choice(PlanetList)
            RandomStar = random.choice(StarList)
            print(RandomStar)
            print(RandomPlanet)
            self.GeneratedPlanetObject.text = f'You have entered orbit around a {RandomPlanet}, which is in orbit around a {RandomStar} star.'
           
        else:
            print(self.planetSpinner.text)       

if __name__ == '__main__':
    GeneratorApp().run()