# Program to simulate genetic combination according to Randall Munroe's (XKCD) "what if?" book, page 158.
# WILLIAM BATTS III 2024
# Written with <3 on a ThinkPad T490S
#
# If there's a number for both versions of a chromosome, you get the bigger number.
# If you have a multiplier for one chromosome and a number for another, you get the number times the multiplier.
# If you have a multiplier on both sides, you get a stat of 1.
#
# When the parents generate DNA (egg or sperm) to be passed down, values are picked from their parents' DNA (randomly with a 50/50 shot)
# For DNA, each chromosome has either a stat (a number usually from 1-18), or a multiplier.
# (Stats can be over 18 if inherited from a parent who somehow got it with a multiplier)
# 
# Each parent contributes one strand of DNA, according to the above.
# Keep in mind that although the final stats are a combination of the parental DNA, DNA passing down is generated from the parental DNA.
#
# Strength       (STR)
# Constitution   (CON)
# Dexterity      (DEX)
# Charisma       (CHR)
# Wisdom         (WIS)
# Intelligence   (INT)
# Sex            (SEX)
#
import random
multipliervalues = [0.5, 1.5, 2, 2.5]
multiplierweights = [25, 45, 25, 5]

def generatemultiplier():
    return (random.choices(multipliervalues, multiplierweights)[0], True)

def generategenestat():
    return (random.randint(1, 18), False)

def setgenerandom():
    if(random.randint(0, 3) == 2):
        return generatemultiplier()
    else:
        return generategenestat()

#def combinegene(Gene paternal, Gene maternal):
#    pass



def setrandomgenes():
    str = setgenerandom()
    con = setgenerandom()
    dex = setgenerandom()
    chr = setgenerandom()
    wis = setgenerandom()
    int = setgenerandom()
    sex = random.choice(["XX", "XY"])
    return (str, con, dex, chr, wis, int, sex)

class Gene:
    def __init__(self, str, con, dex, chr, wis, int, sex):
        self.str = str
        self.con = con
        self.dex = dex
        self.chr = chr
        self.wis = wis
        self.int = int
        self.sex = sex
    def printgenes(self):
        print(f"STR = {self.str}")
        print(f"CON = {self.con}")
        print(f"DEX = {self.dex}")
        print(f"CHR = {self.chr}")
        print(f"WIS = {self.wis}")
        print(f"INT = {self.int}")
        print(f"SEX = {self.sex}")

        

def randomgenome():
    return (Gene(*setrandomgenes), Gene(*setrandomgenes))

class Person:
    def __init__(self, genome='', maternal='', paternal=''):
        self.maternal = maternal
        self.paternal = paternal
        self.genome = genome


people = [0]



def main():
    for i in range(len(people)):
        people[i] = Gene(*setrandomgenes())
    for i in range(len(people)):
        people[i].printgenes()
        print("\n")


main()