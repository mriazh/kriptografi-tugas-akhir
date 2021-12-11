# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class mainFrame
###########################################################################

class mainFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Chiper Test", pos = wx.DefaultPosition, size = wx.Size( 500,320 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.MINIMIZE_BOX|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )


		bSizer1.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_button1 = wx.Button( self, wx.ID_ANY, u"Caesar Chipher", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.m_button1, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.m_button2 = wx.Button( self, wx.ID_ANY, u"Vigenère Cipher", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.m_button2, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		bSizer1.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button1.Bind( wx.EVT_BUTTON, self.caesar_button )
		self.m_button2.Bind( wx.EVT_BUTTON, self.viginere_button )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def caesar_button( self, event ):
		event.Skip()

	def viginere_button( self, event ):
		event.Skip()


###########################################################################
## Class caesarCipher
###########################################################################

class caesarCipher ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Chiper Test", pos = wx.DefaultPosition, size = wx.Size( 500,320 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.MINIMIZE_BOX|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOTEXT ) )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		self.m_menubar1 = wx.MenuBar( 0 )
		self.home = wx.Menu()
		self.back = wx.MenuItem( self.home, wx.ID_ANY, u"Back", wx.EmptyString, wx.ITEM_NORMAL )
		self.home.Append( self.back )

		self.m_menubar1.Append( self.home, u"Home" )

		self.SetMenuBar( self.m_menubar1 )

		sbSizer3 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Caesar cipher" ), wx.VERTICAL )

		self.m_panel2 = wx.Panel( sbSizer3.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText1 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"Text", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )

		bSizer2.Add( self.m_staticText1, 0, wx.ALL, 5 )

		self.original_or_cipher = wx.TextCtrl( self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 473,-1 ), 0 )
		bSizer2.Add( self.original_or_cipher, 0, wx.ALL, 5 )

		self.m_staticText2 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"Key", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )

		bSizer2.Add( self.m_staticText2, 0, wx.ALL, 5 )

		self.the_key = wx.TextCtrl( self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 473,-1 ), 0 )
		bSizer2.Add( self.the_key, 0, wx.ALL, 5 )

		self.m_staticText3 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"Result", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )

		bSizer2.Add( self.m_staticText3, 0, wx.ALL, 5 )

		self.the_result = wx.TextCtrl( self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 473,-1 ), wx.TE_READONLY )
		bSizer2.Add( self.the_result, 0, wx.ALL, 5 )

		bSizer3 = wx.BoxSizer( wx.HORIZONTAL )

		self.encryptLabel = wx.Button( self.m_panel2, wx.ID_ANY, u"Encrypt !", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.encryptLabel, 0, wx.ALL, 5 )

		self.decryptLabel = wx.Button( self.m_panel2, wx.ID_ANY, u"Decrypt !", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.decryptLabel, 0, wx.ALL, 5 )


		bSizer2.Add( bSizer3, 1, wx.ALIGN_CENTER|wx.ALL, 5 )


		self.m_panel2.SetSizer( bSizer2 )
		self.m_panel2.Layout()
		bSizer2.Fit( self.m_panel2 )
		sbSizer3.Add( self.m_panel2, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( sbSizer3 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_MENU, self.comeback, id = self.back.GetId() )
		self.encryptLabel.Bind( wx.EVT_BUTTON, self.lets_encrypt )
		self.decryptLabel.Bind( wx.EVT_BUTTON, self.lets_decrypt )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def comeback( self, event ):
		event.Skip()

	def lets_encrypt( self, event ):
		event.Skip()

	def lets_decrypt( self, event ):
		event.Skip()


###########################################################################
## Class viginereCipher
###########################################################################

class viginereCipher ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Chiper Test", pos = wx.DefaultPosition, size = wx.Size( 500,320 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.MINIMIZE_BOX|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOTEXT ) )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		self.m_menubar2 = wx.MenuBar( 0 )
		self.home = wx.Menu()
		self.back = wx.MenuItem( self.home, wx.ID_ANY, u"Back", wx.EmptyString, wx.ITEM_NORMAL )
		self.home.Append( self.back )

		self.m_menubar2.Append( self.home, u"Home" )

		self.SetMenuBar( self.m_menubar2 )

		sbSizer6 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Vigenère cipher" ), wx.VERTICAL )

		self.m_panel2 = wx.Panel( sbSizer6.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText1 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"Text", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )

		bSizer2.Add( self.m_staticText1, 0, wx.ALL, 5 )

		self.original_or_cipher = wx.TextCtrl( self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 473,-1 ), 0 )
		bSizer2.Add( self.original_or_cipher, 0, wx.ALL, 5 )

		self.m_staticText2 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"Key", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )

		bSizer2.Add( self.m_staticText2, 0, wx.ALL, 5 )

		self.the_key = wx.TextCtrl( self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 473,-1 ), 0 )
		bSizer2.Add( self.the_key, 0, wx.ALL, 5 )

		self.m_staticText3 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"Result", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )

		bSizer2.Add( self.m_staticText3, 0, wx.ALL, 5 )

		self.the_result = wx.TextCtrl( self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 473,-1 ), wx.TE_READONLY )
		bSizer2.Add( self.the_result, 0, wx.ALL, 5 )

		bSizer3 = wx.BoxSizer( wx.HORIZONTAL )

		self.encryptLabel = wx.Button( self.m_panel2, wx.ID_ANY, u"Encrypt !", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.encryptLabel, 0, wx.ALL, 5 )

		self.decryptLabel = wx.Button( self.m_panel2, wx.ID_ANY, u"Decrypt !", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.decryptLabel, 0, wx.ALL, 5 )


		bSizer2.Add( bSizer3, 1, wx.ALIGN_CENTER|wx.ALL, 5 )


		self.m_panel2.SetSizer( bSizer2 )
		self.m_panel2.Layout()
		bSizer2.Fit( self.m_panel2 )
		sbSizer6.Add( self.m_panel2, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( sbSizer6 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_MENU, self.comeback, id = self.back.GetId() )
		self.encryptLabel.Bind( wx.EVT_BUTTON, self.lets_encrypt )
		self.decryptLabel.Bind( wx.EVT_BUTTON, self.lets_decrypt )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def comeback( self, event ):
		event.Skip()

	def lets_encrypt( self, event ):
		event.Skip()

	def lets_decrypt( self, event ):
		event.Skip()


