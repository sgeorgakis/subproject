#!/usr/bin/python
# -*- coding: windows-1253 -*-

import sys
from SubsCheck import *
from Sub import *

def printFPSmenu():

    print( "Select source fps:")
    print( " 1. 23.976" )
    print( " 2. 24" )
    print( " 3. 25" )
    print( " 4. 29.97" )
    print( " 5. 30" )


def computeFPS( choice ):
    if choice == "1":
        FPS = 24000 / 1001
    elif choice == "2":
        FPS = 24
    elif choice == "3":
        FPS = 25
    elif choice == "4":
        FPS = 30000 / 1001
    else:
        FPS = 30
    return FPS


def userSelection( choice ):

    if choice == 1:   # Correct
        changes = c.correct()
        c.s.saveSub()
        print( "\n" + str( changes ) + " changes were made to the subtitle" )
    elif choice == 2: # Line Check
        lines = c.checkLines()
        print( "\n" )
        for i in range( len( lines ) ):
            print( lines[i] )
    elif choice == 3: # Time Check
        print( "\n" )
        time = c.timeCheck()
        for i in range( len( time ) ):
            print( time[i] )
    elif choice == 4: # Check Ending and other characters
        print( "\n" )
        dots = c.checkCharacters()
        for i in range( len( dots ) ):
            print( dots[i] )
    elif choice == 5: # Gap Check
        print( "\n" )
        gap = c.checkGap()
        for i in range( len( gap ) ):
            print( gap[i] )
    elif choice == 6: # Check RS
        print( "\n" )
        rs = c.checkRS()
        for i in range( len( rs ) ):
          for j in range( len( rs[i] ) ):
              print( rs[i][j] )
    elif choice == 7: # Check CPS
        print( "\n" )
        cps = c.checkCPS()
        for i in range( len( cps ) ):
          print( cps[i] )
    elif choice == 8: # Spell Check
        print( "\n" )
        c.wc.spellCheck()
    elif choice == 9: # Split Subtitle
        print( "\n" )
        parts = input( "In how many parts should I split the subtitle? ")
        c.s.split( int(parts) )
    elif choice == 10: # Delay Subtitle
        print( "\n" )
        time = input( "How long should I delay the subtitle in seconds? ")
        c.s.delaySub( time )
    elif choice == 666: # Make subtitle to greeklish
        c.toGreeklish()
        c.s.saveSub()
        print( "\n" )
        print( "Done ;)" )
    elif choice == 11: # Change FPS
        source = ""
        while source != "1" and source != "2" and source != "3" and source != "4" and source != "5":
            print( "What's the original frame rate?\n" )
            printFPSmenu()
            source = input()
        inputFPS = computeFPS( source )
        target = ""
        while target != "1" and target != "2" and target != "3" and target != "4" and target != "5":
            print( "And what's the desired frame rate?\n" )
            printFPSmenu()
            target = input()
        outputFPS = computeFPS( target )
        print( "Framerate changed!")
        c.s.changeFrame( inputFPS, outputFPS )
    return

def printMenu():
    print( "1. Correct Subtitle"  )
    print( "2. Check line length" )
    print( "3. Check time length" )
    print( "4. Check characters" )
    print( "5. Check gaps" )
    print( "6. Check RS" )
    print( "7. Check CPS" )
    print( "8. Spell Check" )
    print( "9. Split Subtitle" )
    print( "10. Delay Subtitle" )
    print( "11. Change FPS" )
    #print( "666. Easter Egg" )
    print( "0. Quit" )

def mainLoop():
    try:
        choice = -1
        while choice != 0:
            printMenu()
            choice = int( input( "What's your choice? " ) )
            userSelection( choice )
            print( "\n\n" )
        return
    except ValueError:
        choice = -1
        while choice != 0:
            printMenu()
            choice = int( input( "What's your choice? " ) )
            userSelection( choice )
            print( "\n\n" )
        return


print( "The subtitle file should be in the same folder with this program" )
print( "If not, you should give the path of the subtitle as name\n" )
try:
    name = sys.argv[1]
except IndexError:
    name = input( "What's the subtitle's name? " )
    print( '\n' )
finally:
    try:
        #coding = sys.argv[2]
        s = Sub( name )
    except IOError:
        print( "Program will terminate" )
    #except IndexError:
    else:
        c = Checker( s )
        mainLoop()
        #c.checkAll()
        #print( '\n\n' )
        print( "All went well" )
        del s
        del c
