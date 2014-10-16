#Import the library

from midiutil.MidiFile import MIDIFile
import random
from random import randint
from midscalechord import MyMIDIchords



## create files
v = str(randint(1,1000))
filenameChords = v+"highpeedrandChords"
filenameTune = v+"highpeedrandTuneTest"
speed = 1

# Create the MIDIFile Object with 1 track
MyMIDITune = MIDIFile(1)
MyMIDIChords = MIDIFile(1)

# Tracks are numbered from zero. Times are measured in beats.

track = 0   
time = 0

# Add track name and tempo.
MyMIDITune.addTrackName(track,time,"Rand Python "+filenameTune)
MyMIDITune.addTempo(track,time,80)
MyMIDIChords.addTrackName(track,time,"Rand Python "+filenameChords)
MyMIDIChords.addTempo(track,time,80)

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

def makeChord(chord,oct):
    chordNotes = [x + oct for x  in chord]
    return chordNotes


##
chordI =  makeChord([0,2,5,8],middleNote)
chordIV =  makeChord([3,5,7],middleNote)
chordV =  makeChord([4,6,8],middleNote)
chordV7 =  makeChord([4,6,8,10],middleNote)


chordRand = makeChord([randint(0,7),randint(0,7),randint(3,10),randint(2,8)],middleNote)

# [scale[0],scale[2],scale[5], scale[0]+12]
# chordI = [x+middleNote for x in chordI]
# 
# chordIV= [scale[2],scale[4],scale[6], scale[2]+12]
# chordIV = [x+middleNote for x in chordIV]
# 
# chordV= [scale[3],scale[5],scale[8],scale[9]]
# chordV = [x+middleNote for x in chordV]


# chordV7= [scale[3],scale[6],scale[8], scale[10]]
# chordV7 = [x+middleNote for x in chordV7]

chords = [chordI,chordV7,chordIV,chordIV,chordV,chordRand]


sourceNotes = []


note = randint(0,20)


##build source
i=0
while i < 128:
    if(randint(1,10) >= 5):
                if(randint(1,10) >2):
                    note=note+random.choice([-2,-1,-1,0,+1,+1])

                else:
                    note = randint(0,20)
                sourceNotes.append(note)
    else:
        sourceNotes.append("x")
    i=i+1
    
i=0
## build chords
sourceChords = []
while i < 64:
    if(randint(1,10) >= 6):
        sourceChords.append(random.choice(chords))
    else:
        sourceChords.append("x")
    i=i+1        
print "sourceChords ", sourceChords
def randomPhraseGen(leng, source =[]):
    start = randint(0,leng)
    end = (len(source)  - leng)
    phrase = source[start:end]
    return phrase

phrase1 = randomPhraseGen(16, sourceNotes)
phrase2 = randomPhraseGen(16, sourceNotes)
phrase3 = randomPhraseGen(16, sourceNotes)
phrase4 = randomPhraseGen(8, sourceNotes)
phrase5 = randomPhraseGen(8, sourceNotes)

chordSeq1 = randomPhraseGen(4, sourceChords)
chordSeq2 = randomPhraseGen(2, sourceChords)
##chordSeq3 = randomPhraseGen(16, sourceChords)

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


for chord in chordTrack:
    if(chord =="x"):
        time = time+(speed) 
    else:
        for pitch in chord:
            volume = randint(20,80)
            duration = randint(3,6)
           ## print pitch
            pitch = pitch + random.choice([-12,0,0,12])
#                 print "pitch = ", str(pitch)
            MyMIDIChords.addNote(track,channel,pitch,time,duration,volume)
        time = time +(speed)                   
    

##print filenameTune
print sourceNotes
filepath = "/Users/daniel/Documents/ableton/PythonMidi/highspeed/"
filenameTune = filepath + filenameTune
print filenameTune
# And write it to disk.
binfile = open(filenameTune + ".mid", 'wb')
MyMIDITune.writeFile(binfile)
binfile.close()
### And write it to disk.
filenameChords = filepath + filenameChords
binfile = open(filenameChords + ".mid", 'wb')
MyMIDIChords.writeFile(binfile)
print filenameChords
binfile.close()
