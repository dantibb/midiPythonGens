#Import the library

from midiutil.MidiFile import MIDIFile
import random
from random import randint

# Create the MIDIFile Object with 1 track
MyMIDItune = MIDIFile(1)
MyMIDIchords = MIDIFile(1)

# Tracks are numbered from zero. Times are measured in beats.

track = 0   
time = 0

# Add track name and tempo.
MyMIDItune.addTrackName(track,time,"Random Pyhton Tune")
MyMIDItune.addTempo(track,time,80)
MyMIDIchords.addTrackName(track,time,"Random Python Chords")
MyMIDIchords.addTempo(track,time,80)

counter = 0.0
p=30
v = str(randint(1,1000))
filenameChords = v+"randChords"
filenameTune = v+"randTune"

scale = [50,52,54,55,58,60,61,62,65,67,70]
chordI = [scale[0],scale[2],scale[5], scale[0]+12]
chordIV= [scale[2],scale[4],scale[6], scale[2]+12]
chordV= [scale[3],scale[5],scale[8],scale[9]]
chordV7= [scale[3],scale[6],scale[8], scale[10]]

chords = [chordI,chordI,chordV7,chordIV,chordIV,chordV]
note = randint(0,10)
while(counter < 200):

##    # Add a note. addNote expects the following information:
##    track = 0
##    channel = 0
##    time = counter/20
##    duration = 0.1
##    volume = 27
##
##    # Now add the note.
##    MyMIDI.addNote(track,channel,p,time,duration,volume)
##    # Add a note. addNote expects the following information:
##  descant  
    track = 0
    channel = 0
    time = counter
    duration =randint(1,12)
    volume =  randint(15,100)
    if(randint(1,10) > 6) or ((counter % 4 ==0)and (randint(1,10) > 2)):
        if(randint(1,10) >3) and  (1 <= note <10):
            note=note+random.choice([-1,-1,0,+1,+1])
            pitch = scale[note]
        else:
            note = randint(0,10)
            pitch = scale[note]
        
            MyMIDItune.addNote(track,channel,pitch,time,duration,volume)
            if(randint(1,10) >7):
                pitch = scale[note - randint(2,5)]
                MyMIDItune.addNote(track,channel,pitch,time,duration,volume)
                
## chrd
    if(counter % 4 ==0):
        if(randint(1,5) > 2):
            duration = duration * 4
            volume =  randint(15,70)
            for pitch in chords[randint(0,5)]:
  
                pitch = pitch + random.choice([-12,0,0,12])
                print "pitch = ", str(pitch)
                MyMIDIchords.addNote(track,channel,pitch,time,duration,volume)

                
    # Now add the note.
    
    counter +=1
    p += 1
    print p
print filenameTune
print filenameChords
# And write it to disk.
binfile = open(filenameTune + ".mid", 'wb')
MyMIDItune.writeFile(binfile)
binfile.close()
# And write it to disk.
binfile = open(filenameChords + ".mid", 'wb')
MyMIDIchords.writeFile(binfile)
binfile.close()
