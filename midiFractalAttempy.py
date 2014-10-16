#Import the library

from midiutil.MidiFile import MIDIFile
import random
from random import randint
from midscalechord import MyMIDIchords



## create files
v = str(randint(1,1000))
filenameChords = v+"highSpeedrandChords"
filenameTune = v+"highSpeedrandTuneTest"
speed = 0.1

# Create the MIDIFile Object with 1 track
MyMIDITune = MIDIFile(1)
MyMIDIChords = MIDIFile(1)

# Tracks are numbered from zero. Times are measured in beats.

track = 0   
time = 0

# Add track name and tempo.
MyMIDITune.addTrackName(track,time,"Rand Python "+filenameTune)
MyMIDITune.addTempo(track,time,80)

## create scale
## midi range GP 21 a0 - 108 c8

scaleBase = [0,2,4,5,7,9,10]

def fillScale(scaleAdd = []):                         
    scale8ve = scaleAdd
    a8vecount = 0 
    while(scale8ve[-1] <= 127):
        scaleAdd = [x+12 for x in scaleAdd]
  ##      print scaleAdd
  ##      print a8vecount
        scale8ve.extend(scaleAdd)
        a8vecount =  a8vecount+ 1
    return scale8ve

scale = fillScale(scaleBase)
##print "done - scale ",scale

middleNote = 5*8

fractalBase = [[4,0],[8,1],[8,2],[4,'r'],[4,0]]

round=1
for note int fractalBase:
    pitch = 
    MyMIDITune.addNote(track,channel,pitch,time,duration,volume)
    


riff1 = 
sourceNotes = []


note = randint(0,20)



phrases = [phrase1,phrase2,phrase3, phrase4, phrase5]
chordPhrases = [chordSeq1, chordSeq2]
print "chordPhrases ", chordPhrases

tune =[]
#### create note list
barNo=1
while barNo <= 32:
    tune.extend(random.choice(phrases))
    barNo = barNo +1
##    print tune

print tune

chordTrack = []
####chords
##chordSeq1 = [random.choice[chords],random.choice[chords],random.choice[chords],random.choice[chords],random.choice[chords],random.choice[chords],random.choice[chords],random.choice[chords] ]
barNo=1
while barNo <= 64:
    chordTrack.extend(random.choice(chordPhrases))
    barNo = barNo +1
print "chord track " , chordTrack

track = 0
channel = 0
time = 0
duration = randint(2,7)
volume = randint(20,80)
time = 0
for note in tune:
    if note == "x":
        time = time+speed
##        break
    else:
        volume = randint(20,80)
        pitch = scale[note+middleNote]
        MyMIDITune.addNote(track,channel,pitch,time,duration,volume)
        time = time+speed
        
time = 0
##new_list = [x+1 for x in my_list]


# for chord in chordTrack:
#     if(chord =="x"):
#         time = time+(speed) 
#     else:
#         for pitch in chord:
#             volume = randint(20,80)
#             duration = randint(3,6)
#            ## print pitch
#             pitch = pitch + random.choice([-12,0,0,12])
# #                 print "pitch = ", str(pitch)
#             MyMIDIChords.addNote(track,channel,pitch,time,duration,volume)
#         time = time +(speed)                   
#     

##print filenameTune
print sourceNotes
filepath = "/Users/daniel/Documents/ableton/PythonMidi/highSpeed/"
filenameTune = filepath + filenameTune
print filenameTune
# And write it to disk.
binfile = open(filenameTune + ".mid", 'wb')
MyMIDITune.writeFile(binfile)
binfile.close()
### And write it to disk.
# filenameChords = filepath + filenameChords
# binfile = open(filenameChords + ".mid", 'wb')
# MyMIDIChords.writeFile(binfile)
# print filenameChords
# binfile.close()
