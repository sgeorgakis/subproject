import re


class Time:

    def __init__( self, time ):
        """
         ( Time, string ) --> Time
         Gets a string of time of a subtitle
         and splits it in minutes, seconds and milliseconds
        """

        self.timeString = time
        buffer = re.split( "\:", time )
        self.hours = int( buffer[0] )
        self.minutes = int( buffer[1] )
        buffer2 = re.split( ",", buffer[2] )
        self.seconds = int( buffer2[0] )
        self.milliseconds = int( buffer2[1] )
        
    def absSec( self ):
        """
         ( Time ) --> None
         Returns the time in seconds
        """

        return float( self.hours * 3600 ) + float( ( self.minutes * 60 ) ) + float( self.seconds ) + ( float( self.milliseconds ) / 1000 )

    def __str__( self ):
        """
         ( Time ) --> string
         Returns the hours, minutes, seconds and milliseconds of the time
        """

        return self.timeString

    def mult( self, factor ):
        time = self.absSec() * factor
        self.hours = int ( time // 3600 )
        self.minutes = int( ( time // 60 ) - ( self.hours * 60 ) )
        self.seconds = int( time - ( self.minutes * 60 ) - ( self. hours * 3600 ) )
        self.milliseconds = int( time % 1 * 1000 )
        self.timeString = str( self. hours ).zfill(2) + ":" + str( self.minutes ).zfill(2) + ":" + str( self.seconds ).zfill(2) + "," + str( self.milliseconds ).zfill(3)



    def add( self, delay_time ):
        time = self.absSec() + delay_time
        self.hours = int ( time // 3600 )
        self.minutes = int( ( time // 60 ) - ( self.hours * 60 ) )
        self.seconds = int( time - ( self.minutes * 60 ) - ( self. hours * 3600 ) )
        self.milliseconds = int( time % 1 * 1000 )
        self.timeString = str( self. hours ).zfill(2) + ":" + str( self.minutes ).zfill(2) + ":" + str( self.seconds ).zfill(2) + "," + str( self.milliseconds ).zfill(3) 


if __name__ == "__main__":
    t=Time("00:00:05,712")
    t.add(1)
