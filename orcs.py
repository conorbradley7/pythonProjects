class Character:
    def __init__(self, name, strength):
        if isinstance(name, str):
            self._name = str(name)
        else:
            print("type ERROR")
        self.__checkStrength__(strength)


    def __str__(self):
        try:
            return ("%s %s" % (self._name, self._strength))
        except AttributeError:
            return "ATTRIBUTE ERROR"


    def cmp_strength(self,opponent):
        if self._strength > opponent._strength:
            return True
        elif opponent._strength > self._strength:
            return False
        else:
            return None


    def __gt__(self,opponent):
        if isinstance(self,Orc):
            if isinstance(opponent,Orc):
                if self._weapon == opponent._weapon:
                    self.cmp_strength(opponent)
                else:
                    if self._weapon == True and opponent._weapon == False:
                        return True
                    elif opponent._weapon == True and self._weapon == False:
                        return False
            else:
                if not self.weapon:
                    return False
                else:
                    return self.cmp_strength(opponent)
        elif isinstance(self, Human):
            if isinstance(opponent, Orc):
                if not opponent.weapon:
                    return True
                else:
                    return self.cmp_strength(opponent)
            else:
                print("fightERROR")
                return "str for error catch"


    def fight(self, opponent):
        if type(self > opponent) == str:
            return None
        if self > opponent:
            self._strength += 1
            self.__checkStrength__(self._strength)
            return self.__str__()
        elif opponent > self:
            opponent._strength += 1
            opponent.__checkStrength__(opponent._strength)
            return opponent.__str__()
        else:
            self._strength -= 0.5
            self.__checkStrength__(self._strength)
            opponent._strength -= 0.5
            opponent.__checkStrength__(opponent._strength)
            return "TIE: " + self.__str__() + " | " + opponent.__str__()


    def __checkStrength__(self,strength):
        try:
            strength = float(strength)
            if strength > 5.0:
                self._strength = 5.0
            elif strength < 0:
                self._strength = 0
            else:
                self._strength = strength
        except (ValueError,TypeError):
            print("type ERROR")


    def getName(self):
        return self._name


    def setName(self, name):
        if isinstance(name,str):
            self._name = str(name)
        else:
            print("type ERROR")


    def getStrength(self):
        return self._strength


    def setStrength(self,strength):
        self.__checkStrength__(strength)


    name = property(getName, setName)
    strength = property(getStrength, setStrength)

#=============================================================================================================================================================================

class Orc(Character):
    def __init__(self, name, strength, weapon):
        Character.__init__(self,name,strength)
        if isinstance(weapon, bool):
            self._weapon = weapon
        else:
            print("type ERROR")

    def getWeapon(self):
        return self._weapon
    def setWeapon(self, weapon):
        if type(weapon) == bool:
            self._weapon = weapon
        else:
            print("type ERROR")

    def __str__(self):
        try:
            return Character.__str__(self) + (" %s" %(self._weapon))
        except AttributeError:
            return "ATTRIBUTE ERROR"

    weapon = property(getWeapon, setWeapon)

#=============================================================================================================================================================================


class Human(Character):
    def __init__(self,name,strength, kingdom):
        Character.__init__(self,name,strength)
        self._kingdom = str(kingdom)

    def __str__(self):
        try:
            return Character.__str__(self) + (" %s" %(self._kingdom))
        except AttributeError:
            return "ATTRIBUTE ERROR"
    def getKingdom(self):
        return self._kingdom

    def setKingdom(self, kingdom):
        if isinstance(kingdom,str):
            self._kingdom = kingdom
        else:
            print("type ERROR")

    kingdom = property(getKingdom, setKingdom)

#=============================================================================================================================================================================


class Archer(Human):
    def __init__(self,name,strength,kingdom):
        Human.__init__(self,name,strength,kingdom)

    def __str__(self):
        try:
            return Human.__str__(self)
        except AttributeError:
            return "ATTRIBUTE ERROR"

#=============================================================================================================================================================================


class Knight(Human):
    def __init__(self,name,strength,kingdom,archers_list=[]):
        Human.__init__(self,name,strength,kingdom)
        self._archers_list = self. __checkArchersList__(archers_list)

    def __str__(self):
        ans = Human.__str__(self)
        AL = [x.__str__() for x in self.archers_list]
        ans += " " + str(AL)
        return ans



    def __checkArchersList__(self,AL):
        if isinstance(AL, list):
            correct_al = []
            for i in AL:
                if isinstance(i, Archer):
                    if i._kingdom == self._kingdom:
                        correct_al.append(i)
                else:
                    print("archers list ERROR")
            return correct_al
        else:
            print("type ERROR")


    def getArchers_list(self):
        return self._archers_list

    def setArchers_list(self, archers_list):
        self._archers_list = __checkArchersList__(archers_list)

    archers_list = property(getArchers_list, setArchers_list)



#=============================================================================================================================================================================
