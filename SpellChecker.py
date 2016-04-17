#!/usr/bin/python
# -*- coding: windows-1253 -*-

regexp = ( r"\-", r"\[", r"\]", r"\n", r"\s", r"«", r"…", r"<i>", r"<b>", r"</i>", r"</b>", r"»", r"\.", r";", r",", r'"', r"!" )

import re


class SpellChecker:

    def __init__( self, d ):

        self.d = d + ".txt"

    def __readDictionary( self ):

        #self.__word = []
        self.__file = open( self.d, 'r+' )
        self.__word = self.__file.read()
        #r = self.__file.read()
        self.__file.close()
        #w = re.split( "\n", r )
        #for i in range( len( w ) ):
        #    self.__word.append( w[i] )

    def __str__( self ):

        total = ""
        #for i in range( len ( self.__word ) ):
        #    total += ( str( self.__word[i] ) + "\n" )
        #return total
        return self.__word

    def __appendWord( self, s ):

        #self.__file = open( self.d, 'a' )
        #self.__file.write( "\n" + s )
        #self.__file.close()
        self.__word = self.__word + "\n" + s
        
    def __recognizeWord( self, t ):

        reg = []
        for i in range( len( regexp ) ):
            reg.append( re.compile( regexp[i] ) )
            t = re.sub( reg[i], " ", t )

        t = re.split( "(\w+\'?)", t )

        index = []

        i = 0
        while i < len( t ):
            if re.match( " ", t[i] ) or re.match( "^$", t[i] ):
                t.pop( i )
                i -= 1
            i += 1
        
        self.__t = t
        #print( self.__t )

    def __wordExists( self, w ):
        self.__readDictionary()
        if re.search( w, self.__word ):
            return True
        else:
            return False
        #for i in range( len( self.__word ) ):
        #    try:
        #        if re.match( self.__word[i], w ):
        #        print( "exists" )
        #            return True
        #    except:
        #        print( w )
        #        return True
        #print( "not" )
        #return False

    def train( self, sent ):
        self.__readDictionary()
        self.__recognizeWord( sent )

        counter = 0
        for i in range( len( self.__t ) ):
            self.__wordExists( self.__t[i] )
            if self.__wordExists( self.__t[i] ) == False:
                self.__appendWord( self.__t[i] )
                counter += 1
        self.__file = open( self.d, 'w' )
        self.__file.write( self.__word )
        self.__file.close()
        return counter

    def sort( self ):
        #word = []
        self.__readDictionary()
        #self.__word.sort()
        #print( self.__word )
        w = re.split( "\n", self.__word )
        for i in range( len( w ) ):
            word.append( w[i] )
        word.sort()
        r = open( "dictionary.txt", "w" )
        for i in range( len ( word ) ):
        #for i in range( len ( self.__word ) ):
            if i != 0:
                r.write( "\n" + word[i] )
                #r.write( "\n" + self.__word[i] )
            else:
                r.write( word[i] )
                #r.write( self.__word[i] )
        r.close()
        
if __name__ == "__main__":
    sc = SpellChecker( "dictionary" )
    #file = open( "dictionary.txt", "a" )
    #file.write( "\nσου" )
    #file.close()
    #sc.train( "Σ' αυτό" )
    sc.train("Πού στα σκατά είσαι, ρε μαλάκα;" )
    #sc.sort()
