import kivy

from kivy.app import App
from kivy.uix.tabbedpanel import TabbedPanelHeader
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.dropdown import DropDown
from kivy.uix.slider import Slider
from kivy.uix.button import Button
from kivy.uix.label import Label

class Proforma(App):
	def operations(click):	
		pass
		
	def build(self):
	#*******ROOTWIDGET*******
		layout = GridLayout(rows=2)		
	#*******SUB-WIDGETS*******
		layoutTop = GridLayout(cols=3,rows=1)#SUB-WIDGET-1
		layoutTop.size_hint = (1, 0.1)
		layoutMid = FloatLayout()#SUB-WIDGET-2
		layoutMid.size_hint = (1, 1)
		
	#*******CONTENT-OF-SUB-WIDGET-1*******	
		menubtn = Button(text='Menu')
		menubtn.size_hint = (0.1, 0.1)
		head = Label(text='PRO-FORMA',size_hint_y = None,size_hint_x=None, width=200)
		head.size_hint = (0.8, 0.1)
		backbtn = Button(text='Drop')
		backbtn.size_hint = (0.1, 0.1)
		#dropbtn = Button()
	#*******CONTENT-OF-SUB-WIDGET-2*******
		tp_panel = TabbedPanel()
		tp_panel.default_tab_text = "Global News"	
		
		layoutnews = GridLayout(rows=2)
		upperlayout = GridLayout(cols=3, pos_hint ={'center_x': .5, 'center_y': .5},row_force_default=True, row_default_height=40, size_hint_y=None, height = 50, size_hint_x=1)
		lowerlayout = GridLayout(row=1)
		
		upperlayout.add_widget(Button(text='S', size_hint=(0.1, None)))
		upperlayout.add_widget(TextInput(text='search', size_hint=(0.8, None), focus=True, multiline=False))
		upperlayout.add_widget(Button(text='settings', size_hint=(0.1, None)))
		
		lowerlayout.add_widget(Label())
		
		layoutnews.add_widget(upperlayout)
		layoutnews.add_widget(lowerlayout)
		tp_panel.default_tab_content = layoutnews
		
		#*******TAB1*******	
		th_tab1 = TabbedPanelHeader(text = 'Pro-Forma')
		#*******SCROLLABILITY-WIDGET*******
		scroll = ScrollView(size_hint=(1, None), size=(800, 1000))
		
		mainlayout = GridLayout(cols = 1, spacing = 10, size_hint_y=None, size_hint_x=1)
		mainlayout.bind(minimum_height=mainlayout.setter('height'))
		#*******LAYOUT-FOR-PROPERTY-INFORMATION*******
		layouttab1 = GridLayout(cols=2,rows=6, pos_hint ={'center_x': .5, 'center_y': .5},row_force_default=True, row_default_height=40, size_hint_y=None, height = 250, size_hint_x=1)
		#*******LAYOUT-FOR-UNIT-MIX*******
		layoutmix = GridLayout(cols=4, pos_hint ={'center_x': .5, 'center_y': .5},row_force_default=True, row_default_height=40,size_hint_y=None, height = 80)
		#*******LAYOUT-FOR-EXPENSES*******
		layoutexpense = GridLayout(cols=2, pos_hint ={'center_x': .5, 'center_y': .5},row_force_default=True, row_default_height=40, size_hint_y=None, height = 960)
		#*******LAYOUT-FOR-ACCOUNTS*******
		layoutacc = GridLayout(cols=2, pos_hint ={'center_x': .5, 'center_y': .5},row_force_default=True, row_default_height=40,size_hint_y=None, height = 240)
		#*******CONTENT1*****
		mainlayout.add_widget(Label(text='Property Information',size_hint=(None, 1)))
		#*******CONTENT2*******
		layouttab1.add_widget(Label(text= 'Property Name', font_size=15, size_hint=(0.4, None)))
		layouttab1.add_widget(TextInput(text='input', font_size=15, halign ='left', valign='middle',size_hint=(0.6, None),multiline=False, focus=True))
		layouttab1.add_widget(Label(text= 'Property Address', font_size=15, size_hint=(0.4, None)))
		layouttab1.add_widget(TextInput(text='input', font_size=15, halign ='left', valign='middle',size_hint=(0.6, None),multiline=False, focus=True))
		layouttab1.add_widget(Label(text= 'Town/City', font_size=15, size_hint=(0.4, None)))
		layouttab1.add_widget(TextInput(text='input', font_size=15, halign ='left', valign='middle',size_hint=(0.6, None),multiline=False, focus=True))
		layouttab1.add_widget(Label(text= 'Asking Price', font_size=15, size_hint=(0.4, None)))
		layouttab1.add_widget(TextInput(text='input', font_size=15, halign ='left', valign='middle',size_hint=(0.6, None),multiline=False, focus=True))
		layouttab1.add_widget(Label(text= 'Total Units', font_size=15, size_hint=(0.4, None)))
		layouttab1.add_widget(TextInput(text='input', font_size=15, halign ='left', valign='middle',size_hint=(0.6, None),multiline=False, focus=True))
		layouttab1.add_widget(Label(text= 'Square Footage', font_size=15, size_hint=(0.4, None)))
		layouttab1.add_widget(TextInput(text='input', font_size=15, halign ='left', valign='middle',size_hint=(0.6, None),multiline=False, focus=True))
		mainlayout.add_widget(layouttab1)
		#*******CONTENT3*******
		mainlayout.add_widget(Label(text='Unit Mix',size_hint_x=None, width=200, size_hint_y=None, height=50))
		#*******CONTENT4*******
		layoutmix.add_widget(Label(text='# of Units'))
		layoutmix.add_widget(Label(text='Unit Type'))
		layoutmix.add_widget(Label(text='SquareFeet'))
		layoutmix.add_widget(Label(text='Monthly Rent'))
		layoutmix.add_widget(TextInput(text='Input', font_size=15))
		layoutmix.add_widget(TextInput(text='Input', font_size=15))
		layoutmix.add_widget(TextInput(text='Input', font_size=15))
		layoutmix.add_widget(TextInput(text='Input', font_size=15))
		mainlayout.add_widget(layoutmix)
		#*******CONTENT7*******
		mainlayout.add_widget(Label(text='Accounts',size_hint_x=None, width=200, size_hint_y=None, height=50))
		#*******CONTENT7*******
		layoutacc.add_widget(Label(text='Purchase Price'))
		layoutacc.add_widget(TextInput(text='Input'))
		layoutacc.add_widget(Label(text='Deposit'))
		layoutacc.add_widget(TextInput(text='Input'))
		layoutacc.add_widget(Label(text='Loan Amount'))
		layoutacc.add_widget(TextInput(text='Input'))
		layoutacc.add_widget(Label(text='Annual Interest'))
		layoutacc.add_widget(TextInput(text='Input'))
		layoutacc.add_widget(Label(text='Period'))
		layoutacc.add_widget(TextInput(text='Input'))
		layoutacc.add_widget(Label(text='Total Cash Outlay'))
		layoutacc.add_widget(TextInput(text='Input'))
		mainlayout.add_widget(layoutacc)
		#*******CONTENT5*******
		mainlayout.add_widget(Label(text='Expenses',size_hint_x=None, width=200, size_hint_y=None, height=50))
		#*******CONTENT6*******
		layoutexpense.add_widget(Label(text='Accounting'))
		layoutexpense.add_widget(TextInput(text='Input', font_size=15,))
		layoutexpense.add_widget(Label(text='Advertising'))
		layoutexpense.add_widget(TextInput(text='Input', font_size=15))
		layoutexpense.add_widget(Label(text='Bank Charges'))
		layoutexpense.add_widget(TextInput(text='Input', font_size=15))
		layoutexpense.add_widget(Label(text='Electricity'))
		layoutexpense.add_widget(TextInput(text='Input', font_size=15))
		layoutexpense.add_widget(Label(text='Gas'))
		layoutexpense.add_widget(TextInput(text='Input', font_size=15))
		layoutexpense.add_widget(Label(text='Security'))
		layoutexpense.add_widget(TextInput(text='Input', font_size=15))
		layoutexpense.add_widget(Label(text='All insurance'))
		layoutexpense.add_widget(TextInput(text='Input', font_size=15))
		layoutexpense.add_widget(Label(text='Permits and fees'))
		layoutexpense.add_widget(TextInput(text='Input', font_size=15))
		layoutexpense.add_widget(Label(text='Maintenance'))
		layoutexpense.add_widget(TextInput(text='Input', font_size=15))
		layoutexpense.add_widget(Label(text='Trash Pick-up'))
		layoutexpense.add_widget(TextInput(text='Input', font_size=15))
		layoutexpense.add_widget(Label(text='All other'))
		layoutexpense.add_widget(TextInput(text='Input', font_size=15))
		mainlayout.add_widget(layoutexpense)
		#*******CALLING-MAINLAYOUT-IN-TAB1*******
		scroll.add_widget(mainlayout)
		th_tab1.content = scroll
		tp_panel.add_widget(th_tab1)
		
		#___*******TAB3*******___#
		th_tab3 = TabbedPanelHeader(text = 'Saved Reports')
		tp_panel.add_widget(th_tab3)
	
	#*******ADDING-CONTENTS-OF-SUB-WIDGETS*******
		layoutTop.add_widget(menubtn)
		layoutTop.add_widget(head)
		layoutTop.add_widget(backbtn)
		layoutMid.add_widget(tp_panel)
	#*******ADDING-CONTENTS-OF-ROOT-WIDGET*******
		layout.add_widget(layoutTop)
		layout.add_widget(layoutMid)
	#*******CALLING-THE-ROOT-WIDGET*******	
		return layout

if __name__ == '__main__':
	Proforma().run()
