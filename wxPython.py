import wx
#Import the wxPython Package

class HelloFrame(wx.Frame):
    #Creating a frame

    def __init__(self,*args, **kw):
        super(HelloFrame,self).__init__(*args,**kw)

        #create a panel in the frame
        pnl =wx.Panel(self)

        #Some text with a larger bold font on it
        st=wx.StaticText(pnl,label="Hello World!",pos=(25,25))
        font=st.GetFont()
        font.PointSize +=10
        font=font.Bold()
        st.SetFont(font)

        #creates a menu bar
        self.makeMenuBar()

        #create a status bar
        self.CreateStatusBar()
        self.SetStatusText("Welcome to wxPython")

    def makeMenuBar(self):
        #Can be Composed of menus,which are with menu items

        #Make a file menu with Hello and Exit Items
        fileMenu=wx.Menu()

        ## The "\t..." syntax defines an accelerator key that also triggers
        # the same event
        helloItem = fileMenu.Append(-1, "&Hello...\tCtrl-H",
                "Help string shown in status bar for this menu item")
        fileMenu.AppendSeparator()
        # When using a stock ID we don't need to specify the menu item's
        # label

        exitItem=fileMenu.Append(wx.ID_EXIT)

        #Now a help menu for about item
        helpMenu=wx.Menu()
        aboutItem=helpMenu.Append(wx.ID_ABOUT)

         # Make the menu bar and add the two menus to it. The '&' defines
        # that the next letter is the "mnemonic" for the menu item. On the
        # platforms that support it those letters are underlined and can be
        # triggered from the keyboard.
        menuBar = wx.MenuBar()
        menuBar.Append(fileMenu, "&File")
        menuBar.Append(helpMenu, "&Help")

        # Give the menu bar to the frame
        self.SetMenuBar(menuBar)

        # Finally, associate a handler function with the EVT_MENU event for
        # each of the menu items. That means that when that menu item is
        # activated then the associated handler function will be called.
        self.Bind(wx.EVT_MENU, self.OnHello, helloItem)
        self.Bind(wx.EVT_MENU, self.OnExit,  exitItem)
        self.Bind(wx.EVT_MENU, self.OnAbout, aboutItem)

    def OnExit(self,event):
        #Close the frame,exiting the application"

        self.Close(True)

    def OnHello(self, event):
        """Say hello to the user."""
        wx.MessageBox("Hello again from wxPython")


    def OnAbout(self, event):
        """Display an About Dialog"""
        wx.MessageBox("This is a wxPython Hello World sample",
                      "About Hello World 2",
                      wx.OK|wx.ICON_INFORMATION)


if __name__ == '__main__':
    # When this module is run (not imported) then create the app, the
    # frame, show it, and start the event loop.
    app = wx.App()  #Create an application object
    frm = HelloFrame(None, title='Hello World ') #Create a frame
    frm.Show() #Show the frame
    app.MainLoop() #Start the event Loop

        

