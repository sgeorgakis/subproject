import re
from Subline import *

class Sub:

    def __init__( self, filename, exists = True ):
        """
          ( Sub, string, bool, string ) --> Sub
          Opens or creates a subtitle with ".srt" extension
          Gets as arguments the subtitle's name
          and optional if exists and encoding
        """
        # If the filename does not contain '.srt' extension, add it 
        pattern = re.compile( ".srt" )
        if pattern.search( filename, -4 ):
            self.filename = filename
        else:
            self.filename = filename + ".srt"

        self.line = []
        if exists:
            try:
                self.__file = open( self.filename, "r+" )
                r = self.__file.read()
                self.__encoding = "windows-1253"
            except UnicodeDecodeError:
                self.__file = open( self.filename, "r+", encoding = "utf-8" )
                self.__encoding = "utf-8"
                r = self.__file.read()
            except ValueError:
                print("hi")
            finally:
                #r = self.__file.read()
                #print(r)
                self.__file.close()
                l = re.split( "\n\n", r )
                for i in range( len( l ) ):
                    if l[i] != "":
                        self.line.append( SubLine( l[i] ) )
        else:
            raise IOError

    def __str__( self ):

        total = ""
        for i in range( len ( self.line ) ):
            total += ( str( self.line[i] ) + "\n\n" )
        return total

    def split( self, number ):
        """
          ( Sub, int ) --> None
          Splits the subtitle in as many pieces
          as the number variable defines
        """
        lines = []
        division = len( self.line ) // number
        modulo = len( self.line ) % number
        for i in range( number ):
            if modulo > 0:
                modulo -= 1
                lines.append( division + 1 )
            else:
                lines.append( division )

        k = 0
        for i in range( number ):
            name = self.filename[0:-4] + ".part" + str( i + 1 ) + ".srt"
            f = open( name, "w", encoding = self.__encoding )
            counter = 0
            for j in range( k, lines[i] + k ):
                counter += 1
                string = str( counter ) + self.line[j].noNum()
                f.write( string + "\n\n" )
            f.close()
            k += ( lines[i] )
            if i == ( number - 1 ):
                k -= 2

    def changeFrame( self, inputFPS, outputFPS ):
        factor = ( inputFPS * 1000 ) / ( outputFPS * 1000 )
        for i in range( len( self.line ) ):
            self.line[i].changeTime( factor )


    def delaySub( self, delay_time ):
        for i in range( len( self.line ) ):
            self.line[i].delay( delay_time )


            
    def saveSub( self ):
        f = open( self.filename, "w" )
        for i in range( len( self.line ) ):
            f.write( str( self.line[i] ) + "\n\n" )
        f.close()

if __name__ == "__main__":
    s = Sub("Ray Donovan - 03x04 - Breakfast of Champions.LOL.English.HI.C.orig.Addic7ed.com.srt" )
    s.split( 4 )
    print(s)
