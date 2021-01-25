# coding: utf-8
# author: Josileno Bezerra do Nascimento


""" This application aims to show a Home Page built with python and the kivy framework.
"""


from kivy.app import App
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout
import kivy
kivy.require("1.11.1")

Window.clearcolor = 1, 1, 1, 1


class HomePage(FloatLayout):
	
	def increment_counter(self, *args):
		counter = self.ids.counter
		counter.text = str(int(counter.text) + 1)


class HomePageApp(App):
	pass


if __name__ == "__main__":
	HomePageApp().run()

