#!/usr/bin/env python3
# Welcome to the Item Generator ! #
import random
import json
import os


class ItemList:
    def __init__(self, deffile="fileindex.json", defmes=None, mode="normal"):
        if defmes is None:
            defmes = "L'évènement qui a été choisi est : {0}."
        
        if mode == "normal":
            deffilewithmode = deffile 
        else:
            deffilewithmode = "fileindex_expert.json"

        with open(deffilewithmode, "r", encoding="utf-8") as f:
            data = json.load(f)

        self.itemfile = data["item"]
        self.mobfile = data["mob"]
        self.weaponfile = data["weapon"]
        self.mealfile = data["meal"]

        self.msg = defmes
        self.msgmult = "- "

    def gen_event(self, eventnum, multiple):
        if eventnum == 1:
            blist = self.itemfile
            addmsg = "Obtenir"
        elif eventnum == 2:
            blist = self.mobfile
            addmsg = "Tuer"
        elif eventnum == 3:
            blist = self.weaponfile
            addmsg = "Obtenir"
        elif eventnum == 4:
            blist = self.mealfile
            addmsg = "Cuisiner"

        with open(str(blist), 'r', encoding="utf-8") as f:
            lines = f.readlines()

        chosenline = random.choice(lines)
        chosenline = chosenline[:-1].rstrip()
        chline = chosenline.split('_')
        chline2 = [each_string.capitalize() for each_string in chline]
        chline3 = " ".join(chline2)

        if not multiple:
            rightmsg = self.msg.format(addmsg + " " + chline3)
        else:
            rightmsg = self.msgmult + addmsg + " " + chline3
        return rightmsg
    
    def gen_all(self, multiple):
        choices = []
        for i in range(1, 5):
            choices.append(self.gen_event(i, multiple))
        return random.choice(choices)

if __name__ == '__main__':
    print("Bienvenue sur le générateur de Challenge Run TOTK !")
    while True:
        whichlist = int(input("Quel type d'évènement souhaitez-vous ?\n1 - Item\n2 - Tuer un monstre\n3 - Obtenir équipement\n4 - Obtenir plat\n5 - Tous\n-> "))
        if whichlist < 1 or whichlist > 5:
            print("--------")
            print("Veuillez entrer une valeur entre 1 et 5.")
            print("--------")
            continue

        while True:
            diff = int(input("Quelle difficulté souhaitez-vous ?\n1 - Normal\n2 - Expert\n-> "))
            if diff == 1:
                obj = ItemList(mode="normal")
                break
            elif diff == 2:
                obj = ItemList(mode="expert")
                break
            else:
                print("Veuillez entrer une valeur entre 1 et 2.")

        while True:
            howmany = int(input("Combien d'objectifs souhaitez-vous ? (1-20)\n-> "))
            if howmany == 1:
                mult = False
                break
            elif howmany > 1 and howmany < 21:
                mult = True
                break
            else:
                print("Veuillez rentrer une valeur entre 1 et 20.")

        if 0 < whichlist and whichlist < 5:
            if mult:
                print("Les évènements qui ont été choisis sont :")
            for i in range(1, howmany+1):
                print(obj.gen_event(whichlist, mult))
            break
        elif whichlist == 5:
            if mult:
                print("Les évènements qui ont été choisis sont :")
            for i in range(1, howmany+1):
                print(obj.gen_all(mult))
            break
