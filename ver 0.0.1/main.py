import kivy

from kivy.app import App
from kivy.uix.tabbedpanel import TabbedPanelHeader
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.lang import Builder

Builder.load_string("""
""")

class Proforma(App):
	def build(self):
	#*******ROOTWIDGET*******
		layout = GridLayout(rows=2)		
	#*******SUB-WIDGETS*******
		layoutTop = GridLayout(cols=3,rows=1)#SUB-WIDGET-1
		layoutTop.size_hint = (None, 0.1)
		layoutMid = FloatLayout()#SUB-WIDGET-2
	#*******CONTENT-OF-SUB-WIDGET-1*******	
		backbtn = Button()
		title = Label(text = 'Pro-Forma App', font_size = '20sp', pos = (0,300), size_hint_y = None,size_hint_x=None, width=200, halign ='right', valign='middle')
		title.size_hint = (None, 0.1)
		dropbtn = Button()
	#*******CONTENT-OF-SUB-WIDGET-2*******
		tp_panel = TabbedPanel()
		tp_panel.default_tab_text = "Login Tab"	
		#*******TAB1*******	
		th_tab1 = TabbedPanelHeader(text = 'Pro-Forma')
		#*******LAYOUT-FOR-TAB1*******
		layouttab1 = GridLayout(cols=2, pos_hint ={'center_x': .5, 'center_y': .5},row_force_default=True, row_default_height=40)
		layouttab1.add_widget(Label(text= 'Property Name', size_hint_x=None, width=200,size_hint_y=None, height=50, font_size='20sp'))
		layouttab1.add_widget(TextInput(text='input', font_size=15, halign ='left', valign='middle'))
		layouttab1.add_widget(Label(text= 'Property Address', size_hint_x=None, width=200,size_hint_y=None, height=50, font_size='20sp'))
		layouttab1.add_widget(TextInput(text='input', font_size=15, halign ='left', valign='middle'))
		layouttab1.add_widget(Label(text= 'Town/City', size_hint_x=None, width=200,size_hint_y=None, height=50, font_size='20sp'))
		layouttab1.add_widget(TextInput(text='input', font_size=15, halign ='left', valign='middle'))
		layouttab1.add_widget(Label(text= 'Asking Price', size_hint_x=None, width=200,size_hint_y=None, height=50, font_size='20sp'))
		layouttab1.add_widget(TextInput(text='input', font_size=15, halign ='left', valign='middle'))
		layouttab1.add_widget(Label(text= 'Total Units', size_hint_x=None, width=200,size_hint_y=None, height=50, font_size='20sp'))
		layouttab1.add_widget(TextInput(text='input', font_size=15, halign ='left', valign='middle'))
		layouttab1.add_widget(Label(text= 'Square Footage', size_hint_x=None, width=200,size_hint_y=None, height=50, font_size='20sp'))
		layouttab1.add_widget(TextInput(text='input', font_size=15, halign ='left', valign='middle'))
		#*******CALLING-LAYOUTTAB1-IN-TAB1*******
		th_tab1.content = layouttab1
		
		#___*******TAB2*******___#
		th_tab2 = TabbedPanelHeader(text = 'Info. Tab')
	 	
		#___*******TAB3*******___#
		th_tab3 = TabbedPanelHeader(text = 'Due Deligence')
		
		#___*******TAB4*******___#
		th_tab4 = TabbedPanelHeader(text = 'Saved Reports')
		
	#*******CALLING-TABS-TO-tp_panel*******
		tp_panel.add_widget(th_tab1)
		tp_panel.add_widget(th_tab2)
		tp_panel.add_widget(th_tab3)
		tp_panel.add_widget(th_tab4)	
	#*******ADDING-CONTENTS-OF-SUB-WIDGETS*******
		layoutTop.add_widget(backbtn)
		layoutTop.add_widget(title)
		layoutTop.add_widget(dropbtn)
		layoutMid.add_widget(tp_panel)
	#*******ADDING-CONTENTS-OF-ROOT-WIDGET*******
		layout.add_widget(layoutTop)
		layout.add_widget(layoutMid)
	#*******CALLING-THE-ROOT-WIDGET*******	
		return layout

if __name__ == '__main__':
	Proforma().run()
