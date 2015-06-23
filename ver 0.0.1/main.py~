import kivy

from kivy.app import App
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.tabbedpanel import TabbedPanelHeader
from kivy.uix.scrollview import ScrollView
from kivy.lang import Builder

class controller(ScrollView):
	def __init__(self, **kwargs):
		super(Controller, self).__init__(**kwargs)
        	self.layout_content.bind(minimum_height=self.layout_content.setter('height'))
	
class Tabs(TabbedPanel):
	pass

class Estate(App):
	def build(self):
		return Tabs()

if __name__ == '__main__':
	Estate().run()
