import win32com.client, os
from Sub import *

wdDoNotSaveChanges = 0

class wordChecker:

    def __init__( self, s ):

        self.s = s

    def spellCheck( self ):

        path = os.path.abspath( self.s.filename )
        word = win32com.client.Dispatch( "Word.Application" )
        #word.Visible = 1
        doc = word.Documents.Open( path )
        if doc.SpellingErrors.Count:
            for err in doc.SpellingErrors:
                print( err.Text )
        else:
            print ( "No errors" )
        word.Quit(wdDoNotSaveChanges)
        word = None
