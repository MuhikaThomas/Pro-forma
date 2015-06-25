import kivy

from kivy.app import App
from kivy.uix.tabbedpanel import TabbedPanelHeader
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.dropdown import DropDown
from kivy.uix.label import Label
from kivy.lang import Builder

Builder.load_string("""
""")

class Proforma(App):
	def build(self):
	#*******ROOTWIDGET*******
		layout = GridLayout(rows=2)
	#*******SUB-WIDGETS*******
		layoutTop = FloatLayout()#SUB-WIDGET-1
		layoutMid = FloatLayout()#SUB-WIDGET-2
	#*******CONTENT-OF-SUB-WIDGET-1*******	
		title = Label(text = 'Pro-Forma App', font_size = '40sp', pos = (0,280))
	#*******CONTENT-OF-SUB-WIDGET-2*******
		tp_panel = TabbedPanel()		
		th_tab1 = TabbedPanelHeader(text = 'Pro-Forma')
		th_tab1.content =  Label(text= 'Property Name', font_size='20sp')
		th_tab1.content = TextInput(text='input', font_size=15, halign ='left', valign='middle')
		th_tab2 = TabbedPanelHeader(text = 'Info. Tab')
		th_tab3 = TabbedPanelHeader(text = 'Due Deligence')
		th_tab4 = TabbedPanelHeader(text = 'Saved Reports')
	#*******CALLING-TABS-TO-tp_panel*******
		tp_panel.add_widget(th_tab1)
		tp_panel.add_widget(th_tab2)
		tp_panel.add_widget(th_tab3)
		tp_panel.add_widget(th_tab4)	
	#*******ADDING-CONTENTS-OF-SUB-WIDGETS*******
		layoutTop.add_widget(title)
		layoutMid.add_widget(tp_panel)
	#*******ADDING-CONTENTS-OF-ROOT-WIDGET*******
		layout.add_widget(layoutTop)
		layout.add_widget(layoutMid)
	#*******CALLING-THE-ROOT-WIDGET*******	
		return layout

if __name__ == '__main__':
	Proforma().run()
