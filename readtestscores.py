#Marisa Gross
#readtestscores.py
#CIS 125 Week 11 Assignment
#Collaborated with Rebekah Orth and Evan Sauers and Jacob Wright

from BowlingGame import Game

newFile = open("testscores.txt", "r")
scoresList = [ ]

for line in newFile:
    
    line = line.strip( )
    scoresList = line.split (",")
    scoresList = [int(e) for e in scoresList]
    totalScore = scoresList.pop( )
    
    g = Game( )
    
    for pins in scoresList:
        g.roll(pins)
    score = g.score( )
    
    print ("Your score is { }, and the original given score is { }" .format(score, totalScore))
    if score == totalScore:
        print (" The score is correct!")
    else: 
        print ("The score is incorrect! The score should be" , score)

newFile.close( )

