import re
from Time import *

class SubLine:

    def __init__( self, line ):
        """
          ( Line, string ) --> SubLine
          Gets a string of a subtitle line and splits it
          in number, starting time, ending time and content
        """
        try:
            buffer = re.split( "\n", line )
            self.number = int( buffer[0] )
        except ValueError:
            #print( str(int(buffer[0]) ))
            self.number = buffer[0].encode('ascii', 'ignore')
        finally:
            buffer2 = re.split( " --> ", buffer[1] )
            self.start = Time( buffer2[0] )
            self.end = Time( buffer2[1] )
            if len( buffer ) < 3:
                self.text = ""
            else:
                self.text = buffer[2]
            if len( buffer ) == 4:
                self.isDouble = True
                self.text +=  ( "\n" + buffer[3] )
            else:
                self.isDouble = False
            self.duration = self.end.absSec() - self.start.absSec()


    def __str__( self ):
        """
         ( Line ) --> string
         Returns the subtitle's line
         in order to be printed
        """

        return str( self.number ) + "\n" + str( self.start ) + " --> " + str( self.end ) + "\n" + self.text

    def noNum( self ):
        return "\n" + str( self.start ) + " --> " + str( self.end ) + "\n" + self.text


    def changeTime( self, factor ):
        self.start.mult( factor )
        self.end.mult( factor )
        self.duration = self.end.absSec() - self.start.absSec()

    def delay( self, delay_time ):
        self.start.add( delay_time )
        self.end.add( delay_time )
