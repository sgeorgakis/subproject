import re
from Sub import *
#from SpellChecker import *
from wordChecker import *
import settings
import os

class Checker:

    def __init__( self, s ):

        self.s = s
        self.wc = wordChecker( self.s )
        #self.sc = SpellChecker( "dictionary" )

    def timeCheck( self ):
        """
         ( Checker ) --> [string]

         Checks the duration of the lines
         is more than max duration or less than min duration.
        """
        error = []                                                                                                                                      # Empty list that will be filled with the number of unsynchronized lines
        for i in range( len( self.s.line ) ):
            if self.s.line[i].duration > settings.max_dur:
                error.append( "line " + str( self.s.line[i].number ) + ": more than " + str( settings.max_dur ) + " seconds." )
            elif self.s.line[i].duration < settings.min_dur:
                error.append( "line " + str( self.s.line[i].number ) + ": less than " + str( settings.min_dur ) + " seconds." )
        return error

    def checkCPS( self ):
        """
         ( Checker ) --> [string]

         Checks if the Characters Per Second of a line is more than the target
        """

        error = []
        for i in range( len( self.s.line ) ):
            offset = self.__specialChars( self.s.line[i].text )
            CPS = ( len( self.s.line[i].text ) - offset ) / self.s.line[i].duration
            if ( CPS > settings.cps ):
                error.append( "line " + str( self.s.line[i].number ) + ": CPS more than " + str( settings.cps ) )
        return error

            
    def checkGap( self ):
        """
         ( Checker ) --> [string]

         Checks if the gap between two sequential lines
         is more or equal than gap duration.
        """
        error = []                                  # Empty list that will be filled with the number of lines that have gap less than the desirable
        for i in range( len( self.s.line ) - 1 ):
            if ( self.s.line[i+1].start.absSec() - self.s.line[i].end.absSec() ) < settings.gap:    # If the end of a line and the start of the next line is less than the desirable, append the number of the lines
                error.append( "line " + str( self.s.line[i].number ) + " and line " + str( self.s.line[i+1].number ) + " have gap less than " + str( settings.gap ) + " seconds." )
        return error
    
    def checkLines( self ):
        """
         ( Checker ) --> [string]

         Reads the file to see each line's length.
         If it is a single line, it must be 30 characters or less.
         If it is a double line, it must be 40 characters or less.
        """
        error = []                                                                                              # Empty list that will be filled with the number of too long lines
        for i in range( len( self.s.line ) ):
            if not( self.s.line[i].isDouble ):
                offset = self.__specialChars( self.s.line[i].text )
                if ( len( self.s.line[i].text ) - offset ) > settings.single:
                    error.append( "line " + str( self.s.line[i].number ) + ": more than " + str( settings.single ) + " characters." )
            else:
                line = re.split( "\n", self.s.line[i].text )
                offset = self.__specialChars( line[0] )
                offset2 = self.__specialChars( line[1] )
                if ( ( len( line[0] ) - offset ) > settings.double ) or ( ( len( line[1] ) - offset2 ) > settings.double ):
                    error.append( "line " + str( self.s.line[i].number ) + ": more than " + str( settings.double ) + " characters." )
        return error

    def __checkDots( self ):

        error = []
        for i in range( len(self.s.line ) ):
            if self.s.line[i].text[-1] == '>':
                if self.s.line[i].text[-5] != '.' and self.s.line[i].text[-5] != '…' and self.s.line[i].text[-5] != ';':
                    error.append( "line " + str( self.s.line[i].number ) + ": " + " does not end in the specified characters." + self.s.line[i].text[-5])

            elif self.s.line[i].text[-1] != '.' and self.s.line[i].text[-1] != '…' and self.s.line[i].text[-1] != ';':
                error.append( "line " + str( self.s.line[i].number ) + ": " + " does not end in the specified characters." + self.s.line[i].text[-1] )
            if self.s.line[i].isDouble and self.s.line[i].text[0] == '-'  and self.s.line[i].text[1] == ' ':
                if re.search( "[^\.;…]\n-\s", self.s.line[i].text ):
                    error.append( "line " + str( self.s.line[i].number ) + ": " + "has a dialogue that the first line does not end in a specified character" )
        return error

    def __specialChars( self, s ):
        """
         ( Checker, string ) --> int

         Checks if there are special characters in a string
         and returns the lenght of them
         Special characters are '<i>', '</i>', '<b>', '</b>'
       """
        lenght = 0                                      # Stores the lenght of total special characters
        for i in range( len( settings.special ) ):      # Search the entire tuple of special characters for match
            if re.search( settings.special[i], s ):     
                lenght += len( settings.special[i] )    # If there is a match, add to lenght its size
        return lenght

    def correct( self ):
        """
         ( Checker ) --> None

         Corrects the wrong words
         Reads from the file, replaces the wrong words with the right ones
         and then writes to the file
         Works with Regular Expressions
        """

        changes = 0
        previous_changes = changes
        log = open( 'log.'+self.s.filename[0:-4]+'.txt', 'w' )
        for i in range( len( self.s.line ) ):
            for j in range( len( settings.regExp ) ):
               changes += len( re.findall( settings.regExp[j], self.s.line[i].text ) )
               if changes > previous_changes:
                   previous_changes = changes
                   log.write( 'previous:\n' + str(self.s.line[i]) + '\n\n' )
                   self.s.line[i].text = re.sub( settings.regExp[j], settings.rightExp[j], self.s.line[i].text )
                   log.write( 'corrected:\n' + str(self.s.line[i]) + '\n\n\n' )
        log.close()
        if changes == 0:
            os.remove( 'log.' + self.s.filename[0:-4] + '.txt' )
        return changes

    def __computeRS( self ):
        """
         ( Checker ) --> None

         Checks every line's RS and prints the number of the red and the green lines
        """

        self.__total_rs = []
        too_slow        = []
        slow            = []
        bit_slow        = []
        good            = []
        perfect         = []
        bit_fast        = []
        fast            = []
        too_fast        = []
        
        for i in range( len( self.s.line ) ):
            offset = self.__specialChars( self.s.line[i].text )
            RS = round( ( len( self.s.line[i].text ) - offset ) * 1000 / ( ( self.s.line[i].duration - 0.5) * 1000 ) )
            if ( RS < 5 ):
                too_slow.append( "line " + str( self.s.line[i].number ) + " TOO SLOW!" )
            elif ( RS < 10):
                slow.append( "line " + str( self.s.line[i].number ) + " Slow, acceptable." )
            elif ( RS < 13 ):
                bit_slow.append( "line " + str( self.s.line[i].number ) + " A bit slow." )
            elif ( RS < 15 ):
                good.append( "line " + str( self.s.line[i].number ) + " Good." )
            elif ( RS < 23 ):
                perfect.append( "line " + str( self.s.line[i].number ) + " Perfect." )
            elif ( RS < 27 ):
                good.append( "line " + str( self.s.line[i].number ) + " Good." )
            elif ( RS < 31 ):
                bit_fast.append( "line " + str( self.s.line[i].number ) + " A bit fast." )
            elif ( RS < 35 ):
                fast.append( "line " + str( self.s.line[i].number ) + " Fast, acceptable." )
            else:
                too_fast.append( "line " + str( self.s.line[i].number ) + " TOO FAST!" )

        self.__total_rs.append( too_slow )
        self.__total_rs.append( slow )
        self.__total_rs.append( bit_slow )
        self.__total_rs.append( good )
        self.__total_rs.append( perfect )
        self.__total_rs.append( bit_fast )
        self.__total_rs.append( fast )
        self.__total_rs.append( too_fast )

    def RSPercentage( self ):
        """
         ( Checker ) --> None

         Computes the percentage of every RS type in a subtitle
         and prints them.
        """
        
        self.__computeRS()
        total_len = len( self.__total_rs[0] ) + len( self.__total_rs[1] ) + len( self.__total_rs[2] ) + len( self.__total_rs[3] ) + len( self.__total_rs[4] ) + len( self.__total_rs[5] ) + len( self.__total_rs[6] ) + len( self.__total_rs[7] )

        too_slow = ( len( self.__total_rs[0] ) / total_len ) * 100
        slow     = ( len( self.__total_rs[1] ) / total_len ) * 100
        bit_slow = ( len( self.__total_rs[2] ) / total_len ) * 100
        good     = ( len( self.__total_rs[3] ) / total_len ) * 100
        perfect  = ( len( self.__total_rs[4] ) / total_len ) * 100
        bit_fast = ( len( self.__total_rs[5] ) / total_len ) * 100
        fast     = ( len( self.__total_rs[6] ) / total_len ) * 100
        too_fast = ( len( self.__total_rs[7] ) / total_len ) * 100

        print( "------ Subtitle Count: " + str( total_len ) + " ------" )
        print( "Too slow (purple): " + str( too_slow ) + "%" )
        print( "Slow (deep blue): " + str( slow ) + "%" )
        print( "A bit slow (light blue): " + str( bit_slow ) + "%" )
        print( "Good (light green): " + str( good ) + "%" )
        print( "Perfect (green): " + str( perfect ) + "%" )
        print( "A bit fast (yellow): " + str( bit_fast ) + "%" )
        print( "Fast (orange): " + str( fast ) + "%" )
        print( "Too fast (red): " + str( too_fast ) + "%" )


    def checkRS( self ):
       """
        ( Checker ) --> [string]

        Returns a list with the number of lines
        that have too fast (red) or fast (orange) RS.
       """

       error = []
       self.__computeRS()
       error.append( self.__total_rs[6] )
       error.append( self.__total_rs[7] )
       return error

    #def spellCheckTrain( self ):

        #counter = 0
        #for i in range( len( self.s.line ) ):
            #counter += self.sc.train( self.s.line[i].text )
        #return counter

    def __checkSW( self ):

        error = []

        for i in range( len(self.s.line ) ):
            for j in range( len( settings.swChars ) ):
               if re.search( settings.swChars[j], self.s.line[i].text ):
                   error.append( "line " + str( self.s.line[i].number) + ": contains an illegal character." )

        return error

    
    def checkCharacters( self ):

        error = []
        error1 = self.__checkDots()
        error2 = self.__checkSW()

        for i in range( len( error1 ) ):
            error.append( error1[i] )
        for i in range( len( error2 ) ):
            error.append( error2[i] )

        return error

        
    def checkAll( self ):
      """
       ( Checker ) --> None

       Does every check and correction that has
       been defined above in a subtitle
      """
      
      changes = self.correct()
      self.s.saveSub()
      time    = self.timeCheck()
      length  = self.checkLines()
      gap     = self.checkGap()
      rs      = self.checkRS()
      cps     = self.checkCPS()
      dots    = self.checkCharacters()
      #words   = self.spellCheckTrain()


      print( "------Changes in subtitle: " + str( changes ) + "------" )
      print( "\n\n" )
       
      print( "------Time------" )
      for i in range( len( time ) ):
          print( time[i] )
      print( "\n\n" )

      print( "------Line length------" )
      for i in range( len( length ) ):
          print( length[i] )
      print( "\n\n" )

      print( "------Subtitle gap------" )
      for i in range( len( gap ) ):
          print( gap[i] )
      print( "\n\n" )

      print( "------RS------" )
      for i in range( len( rs ) ):
          for j in range( len( rs[i] ) ):
              print( rs[i][j] )
      print( "\n\n" )

      print( "------Character Per Second------" )
      for i in range( len( cps ) ):
          print( cps[i] )
      print( "\n\n" )
       
      self.RSPercentage()
      print( "\n\n" )

      print( "-------Lines with error at the end------" )
      for i in range( len( dots ) ):
          print( dots[i] )
      print( "\n\n" )
      
      self.wc.spellCheck()
      #print( "------" + str( words ) + " words were added in the dictionary------" )


    def toGreeklish( self ):
        """Easter Egg method. Turns greek characters to english"""

        for i in range( len( self.s.line ) ):
            for j in range( len( settings.greek ) ):
               self.s.line[i].text = re.sub( settings.greek[j], settings.english[j], self.s.line[i].text )
        
if __name__ == "__main__":

    s = Sub( "Τίτλοι.srt" )
    c = Checker( s )
    #c.correct()
    #c.s.saveSub()
    print (c.checkCharacters())
    #c.checkAll()
    #s.split(4)
    
