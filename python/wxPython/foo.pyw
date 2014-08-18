#logic by itself in module

import wx
from wx import xrc

class MyApp(wx.App):

	def OnInit(self):
	    self.res = xrc.XmlResource('foo.xrc')
	    self.init_frame()
	    return True

	def init_frame(self):
	    self.frame = self.res.LoadFrame(None, 'my_frame')
	    self.panel = xrc.XRCCTRL(self.frame, 'm_panel')
	    self.text1 = xrc.XRCCTRL(self.frame, 'm_text1')
	    self.text2 = xrc.XRCCTRL(self.frame, 'm_text2')
	    self.text3 = xrc.XRCCTRL(self.frame, 'm_text3')
	    self.frame.Bind(wx.EVT_BUTTON, self.OnSubmit, id=xrc.XRCID('m_button'))
	    self.frame.Bind(wx.EVT_BUTTON, self.OnQuit, id=xrc.XRCID('m_quit_button'))
	    self.frame.Show()

	def OnSubmit(self, evt):
		#wx.MessageBox('Your name is %s %s!' %
		#	(self.text1.GetValue(), self.text2.GetValue()), 'Feedback')
		#wx.MessageBox(dir(self.text1).__str__(), 'Feedback')
		my_str = self.text3.GetValue()
		my_str = my_str + self.text1.GetValue() + ' ' + self.text2.GetValue()
		#wx.MessageBox(my_str, 'Info')
		self.text3.SetValue(my_str)
		#self.text3.SetValue( self.text1.GetValue() + self.text2.GetValue() )


	def OnQuit(self, evt):
		quit()


if __name__ == '__main__':
    app = MyApp(False)
    app.MainLoop()
