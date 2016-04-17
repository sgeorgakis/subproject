from tkinter import *
from SubsCheck import *
from Sub import *
import csv
import re

class Window:       
    def __init__( self, master ):     
        self.filename = ""
        master.title( "Check Subtitle" )
        csvfile = Label( root, text = "File" ).grid( row = 1, column = 0 )
        self.bar = Entry( master )
        self.bar.grid( row = 1, column = 1 )

        #Buttons  
        self.browseButton = Button( root, text = "Browse", command = self.browsecsv )
        self.browseButton.grid( row = 1, column = 3 )
        self.correctButton = Button( root, text = "Correct", command = self.correct )
        self.correctButton.grid( row = 2, column = 0 )
        self.lineButton = Button( root, text = "Check Line Lenght", command = self.checkLines )
        self.lineButton.grid( row = 3, column = 0 )
        self.timeButton = Button( root, text = "Check Time Lenght", command = self.checkTime )
        self.timeButton.grid( row = 3, column = 1 )
        self.gapButton = Button( root, text = "Check Gaps", command = self.checkGap )
        self.gapButton.grid( row = 4, column = 0 )
        self.dotButton = Button( root, text = "Check Characters", command = self.checkCharacters )
        self.dotButton.grid( row = 4, column = 1 )
        self.RSButton = Button( root, text = "Check RS", command = self.checkRS )
        self.RSButton.grid( row = 4, column = 2 )
        self.CPSButton = Button( root, text = "Check CPS", command = self.checkCPS )
        self.CPSButton.grid( row = 4, column = 3 )
        self.SpellCheckButton = Button( root, text = "Spell Check", command = self.spellCheck )
        self.SpellCheckButton.grid( row = 5, column = 1 )
        self.SplitButton = Button( root, text = "Split Subtitle", command = self.split )
        self.SplitButton.grid ( row = 5, column = 1 )
        self.AnsiButton = Button( root, text = 'Open as ANSI', command = self.getEncoding( 'A' ) )
        self.AnsiButton.grid ( row = 6, column = 1 )
        self.UTF8Button = Button( root, text = 'Open as UTF-8', command = self.getEncoding( 'U' ) )
        self.UTF8Button.grid ( row = 6, column = 2 )
        self.Text = []
        self.row = 7

    def browsecsv(self):

        Tk().withdraw()
        self.filename = filedialog.askopenfilename()
        if self.filename[-4:] == '.srt':
            name = re.split( '/', self.filename )
            self.bar.delete( 0, END )
            self.bar.insert( 0, name[-1][0: -4] )
            self.encoding = "windows-1253"
            #self.encodingWindow = Toplevel()
            s = Sub( self.filename, encoding = self.encoding )
            self.c = Checker( s )
            for i in range( len( s.line ) ):
                self.Text.append( Text( root, height=4, width=120 ) )
                self.Text[i].grid( row = self.row )
                self.row = self.row + 1
                self.Text[i].insert(INSERT,str(s.line[i].number)+"\n"+s.line[i].text)
            #scrollbar = Scrollbar(root)
            #scrollbar.pack(side=RIGHT, fill=Y)
        else:
            messagebox.showwarning( "Warning", "Choose a Subtitle file\n(.srt file)" )

    def correct( self ):
        if self.filename:
            changes = c.correct()
            self.c.s.saveSub()
            print( str( changes ) + " changes were made to the subtitle" )

    def checkLines( self ):
        if self.filename:
            lines = self.c.checkLines()
            for i in range( len( lines ) ):
                print( lines[i] )

    def checkTime( self ):
        if self.filename:
            time = self.c.timeCheck()
            for i in range( len( time ) ):
                print( time[i] )

    def checkGap( self ):
        if self.filename:
            gap = self.c.checkGap()
            for i in range( len( gap ) ):
                print( gap[i] )

    def checkCharacters( self ):
        if self.filename:
            dots = self.c.checkCharacters()
            for i in range( len( dots ) ):
                print( dots[i] )

    def checkRS( self ):
        if self.filename:
            rs = self.c.checkRS()
            for i in range( len( rs ) ):
              for j in range( len( rs[i] ) ):
                  print( rs[i][j] )

    def checkCPS( self ):
        if self.filename:
            cps = self.c.checkCPS()
            for i in range( len( cps ) ):
              print( cps[i] )

    def spellCheck(self):
        if self.filename:
            self.c.wc.spellCheck()

    def split( self ):
        if self.filename:
            parts = IntVar()
            splitWindow = Toplevel( self )
            label = Label( splitWindow, text = "Parts:" ).grid( row = 1, column = 0 )
            spinBox = Spinbox( splitWindow, from_ = 1, to = 1000, textvariable = parts )
            spinBox.grid( row = 1, column = 1 )
            splitButton = Button( splitWindow, text = "Split!", command = lambda:self.c.s.split( int( spinBox.get() ) ) )
            splitButton.grid( row = 2, column = 1 )

    def getEncoding( self, encoding ):
        if encoding == 'A':
            self.encoding = 'windows-1253'
        elif encoding == 'U':
            self.encoding = 'utf-8'
#        #self.encodingWindow.destroy()
            
root = Tk()
window=Window(root)
root.mainloop()  
