import random, time

DELAY = 0.1
dnaRows = [
'    #C-G#',
'   #C---G#',
'  #A-----T#',
' #T------A#',
'#A------T#',
'#G-----C#',
' #C---G#',
' #G-C#',
'  ##',
' #G-C#',
' #G---C#',
'#A-----T#',
'#A------T#',
' #A------T#',
'  #C-----G#',
'   #C---G#',
'    #G-C#',
'     ##',
]

while True:  # Main program loop.
    for row in dnaRows:
        print(row)
        time.sleep(DELAY)
