import kivy

from kivy.app import App
from kivy.uix.tabbedpanel import TabbedPanelHeader
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.dropdown import DropDown
from kivy.uix.label import Label
from kivy.lang import Builder

class Tabs(TabbedPanel):


class Estate(App):
	def build(self):
		return Tabs()

if __name__ == '__main__':
	Estate().run()
