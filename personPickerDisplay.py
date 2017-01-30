#!.env/bin/python

import time
import traceback

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

import models

text_font = ImageFont.truetype("/usr/share/fonts/truetype/droid/DroidSans.ttf", 12)

class PersonDraw:
    def __init__(self, name, yPos, isVisible):
        self.name = name
        self.yPos = yPos
        self.isVisible = isVisible

    def incrementY(self):
        if self.isVisible:
            self.yPos += 1
        if self.yPos >= 32:
            self.yPos = -10
            self.isVisible = False

    def makeVisible(self):
        self.isVisible = True

    def makeHidden(self):
        self.yPos = -10
        self.isVisible = False

def drawIntro(matrix):
    image = Image.new("RGB", (64, 32))
    draw = ImageDraw.Draw(image)
    draw.text([10, 2], 'Person', font=text_font, fill='white')
    draw.text([10, 18], 'Picker', font=text_font, fill='white')
    matrix.Clear()
    matrix.SetImage(image.im.id, 0, 0)

def main(matrix, person_picker_state):
    global cycles
    global personList
    choosePerson = False
    cycles = 0
    chosenPerson = person_picker_state.chosen_index
    personList = buildPersonList(person_picker_state.people)
    while True:
        image = Image.new("RGB", (64, 32))
        draw = ImageDraw.Draw(image)
        for person in personList:
            if person.isVisible:
                if choosePerson and person.yPos == 10:
                    draw.text([3, person.yPos], person.name, font=text_font, fill='red')
                else:
	            draw.text([3, person.yPos], person.name, font=text_font, fill='white')
        matrix.Clear()
	matrix.SetImage(image.im.id, 0, 0)
	if choosePerson and personList[chosenIndex].yPos == 10:
            break
        else:
            updatePersonList()
            if cycles < 4:
               time.sleep(.008)
            elif cycles < 7:
               time.sleep(.01)
            elif cycles == 7:
               choosePerson = True
               time.sleep(.05)
            else:
               time.sleep(.05)

def updatePersonList():
    global cycles
    makeNextVisible = False
    for index, person in enumerate(personList):
        person.incrementY()
        if makeNextVisible:
            person.makeVisible()
            makeNextVisible = False
        if person.yPos == 2:
            makeNextVisible = True 
        personList[index] = person
    # If makeNextvisible is still true, update the first index
    if makeNextVisible and not personList[0].isVisible:
            person = personList[0]
            person.makeVisible()
            personList[0] = person
            cycles += 1 # We're at the beginning again
    return personList

def buildPersonList(people):
    result = []
    firstPass = True
    while len(result) < 4:
        for index, person in enumerate(people):
	    if firstPass and index == 0:
                result.append(PersonDraw(person, 24, True))
            # This is to handle only chosing between 2 people
            elif not firstPass and index == 0 and len(result) == 2:
                result.append(PersonDraw(person, 0, True))
            elif firstPass and index == 1:
                result.append(PersonDraw(person, 12, True))
            elif firstPass and index == 2:
                result.append(PersonDraw(person, 0, True))
            else:
                result.append(PersonDraw(person, -10, False))
        firstPass = False
    return result


if __name__ == "__main__":
    main(None, None)
