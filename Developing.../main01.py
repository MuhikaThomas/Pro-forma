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

class Layout(GridLayout):
	pass

class Proforma(App):
	def build(self):
		tp_panel = TabbedPanel()
		
		th_tab1 = TabbedPanelHeader(text = 'Pro-Forma')
		th_tab1.content =  Label(text= 'Property Name')
		th_tab1.content = TextInput()

		tp_panel.add_widget(th_tab1)
		layout = GridLayout(cols = 2, rows = 1)
		return tp_panel	

if __name__ == '__main__':
	Proforma().run()
