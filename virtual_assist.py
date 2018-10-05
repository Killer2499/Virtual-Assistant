import wolframalpha
import wikipedia
import wx
import talkey
import speech_recognition as sr

tts = talkey.Talkey()
tts.say('Welcome')

class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,None,pos =wx.DefaultPosition, size=wx.Size(450,100),
                          style=wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION |
                          wx.CLOSE_BOX | wx.CLIP_CHILDREN, title="Killer")
        panel=wx.Panel(self)
        my_sizer=wx.BoxSizer(wx.VERTICAL)
        lbl=wx.StaticText(panel,label="Hello I am Killer -- Python Virtual Assistant")
        my_sizer.Add(lbl,0,wx.ALL,5)
        self.txt=wx.TextCtrl(panel,style=wx.TE_PROCESS_ENTER,size=(400,30))
        self.txt.SetFocus()
        self.txt.Bind(wx.EVT_TEXT_ENTER,self.OnEnter)
        my_sizer.Add(self.txt,0,wx.ALL,5)
        panel.SetSizer(my_sizer)
        self.Show() #Show the application


    def OnEnter(self,event):
        input =self.txt.GetValue()
        input =input.lower()

        if input == "":
            r=sr.Recognizer()
            with sr.Microphone() as source:
                audio=r.listen(source)

                try:
                    self.txt.SetValue(r.recognize_google(audio))
                except sr.UnknownValueError:
                    print("Google Speech Recognition could not understand audio")
                except sr.ReqestError as e:
                    print("Could not request results from google Speech Recognition Service; {0} ".format(e))
        else:
            try:
                    #wolframalpha
                    app_id ="976492-LH43H5QT5V"
                    client =wolframalpha.Client(app_id)
                    res=client.query(input)
                    answer=next(res.results).text
                    print answer
                    tts = talkey.Talkey()
                    tts.say(answer)
                    
                    

            except:
                    #wikipedia
                    stopwords = ['what','who','is','a','at','is','he']
                    querywords = input.split()

                    resultwords  = [word for word in querywords if word.lower() not in stopwords]
                    input = ' '.join(resultwords)
                    tts = talkey.Talkey()
                    tts.say('Results are ready')
                    print wikipedia.summary(input)
                    

        
if __name__ == "__main__":
    app=wx.App(True) #Create an application Object
    frame=MyFrame() #wx.Frame --Create a frame
    app.MainLoop() #Start the event Loop
