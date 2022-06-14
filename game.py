from colorama import init,Fore, Back, Style
import random as rd
import os
import math

init(autoreset=True)

class Hero:
    lvl = 1
    maxHp = 100
    hp = 100
    expForLvlUp = 100
    exp = 0
    critChanse = 0
    coins = 0
    baseDmg = 5
    potions = 5
    bph = 15

    def __init__(self, name = 'Unknown'):
        self.name = name

    def hit(self):
        if rd.random() < self.critChanse:
            hit = self.baseDmg * 2
        else:
            hit = self.baseDmg
        return hit
    
    def upBaseDmg(self, ):
        self.baseDmg += 1
        
    def upMaxHp(self):
        self.maxHp += 10
        
    def lvlUp(self):
        os.system('clear')
        print('-----------------------')
        print('       LVL UP')
        print('-----------------------')
        print('hp +', math.ceil(self.maxHp * 1.1) - self.maxHp)
        print('dmg +', math.ceil(self.baseDmg * 1.05) - self.baseDmg)
        print('-----------------------')
        self.lvl += 1
        self.maxHp = math.ceil(self.maxHp * 1.15)
        self.hp = self.maxHp
        self.expForLvlUp = math.ceil(self.expForLvlUp * 1.2)
        self.exp = 0
        self.baseDmg = math.ceil(self.baseDmg * 1.1)
        self.bph += 5
        self.heroInfo()
        input()
        os.system('clear')
    def heroInfo(self):
        print('\nexp:' + str(self.exp), 'next lvl - ' + str(self.expForLvlUp),  '\npotions:' + str(hero.potions), Fore.YELLOW + 'coins:' + str(self.coins), '\ndmg:' + str(self.baseDmg), 'crit:' + str(round(self.critChanse * 100, 2)), '%')
        
class Enemy:
    lvl = 1
    maxHp = 60
    hp = 60
    baseDmg = 3
    coins = 5
    exp = 20
    
    def __init__(self):
        pass

    def lvlUp(self):
        self.lvl += 1
        self.maxHp = math.ceil(self.maxHp * 1.2)
        self.hp = self.maxHp
        self.baseDmg = math.ceil(self.baseDmg * 1.1)
        #self.coins += 2
        self.exp = math.ceil(self.exp * 1.2)
    


def battleScr():
    
    print(Fore.RED + '''    ______   ___   _____  _____  _      _____ 
    | ___ \ / _ \ |_   _||_   _|| |    |  ___|
    | |_/ // /_\ \  | |    | |  | |    | |__  
    | ___ \|  _  |  | |    | |  | |    |  __| 
    | |_/ /| | | |  | |    | |  | |____| |___ 
    \____/ \_| |_/  \_/    \_/  \_____/\____/ 
                                         ''')
    hpBar(en.name, en.maxHp, en.hp, en.lvl)
    print('''                    .      .
                    |\____/|
                   (\|----|/)
                    \ 0  0 /
                     |    |
                  ___/\../\____
                 /     --       \\
                /  \         /   \\ 
               |    \___/___/(   |
               \   /|  }{   | \  )
                \  ||__}{__|  |  |
                 \  |;;;;;;;\  \ / \_______
                  \ /;;;;;;;;| [,,[|======'
                    |;;;;;;/ |     /
                    ||;;|\   |
                    ||;;/|   /
                    \_|:||__|
                     \ ;||  /
                     |= || =|
                     |= /\ =|
                     /_/  \_\  \n''')
    hpBar(hero.name, hero.maxHp, hero.hp, hero.lvl)
    hero.heroInfo()
    print()
    print('p - use potion(+' + str(hero.bph) + 'hp)')
    
def hpBar(name, maxHp, hp, lvl):
    lenBar = 50
    freeSpace = lenBar - len(str(lvl)) - len(name) - len(str(hp)) - 2
    if freeSpace % 2 != 0:
        frontSpace = freeSpace // 2
        backSpace = freeSpace - frontSpace
    else:
        backSpace = freeSpace // 2
        frontSpace = backSpace
    strBar = ' ' * frontSpace + str(lvl) + ' ' + name + ' ' + str(hp) + ' ' * backSpace
    lenGreen = round((hp / (maxHp / 100)) / 2)
    if lenGreen == 0 and hp > 0:
        lenGreen = 1
    lenRed = 50 - lenGreen
    strGreen = strBar[0: lenGreen]
    strRed = strBar[lenGreen:]
    print(Back.GREEN + Fore.BLACK + strGreen + Back.RED + strRed)

def battle():
    r = rd.randint(1, 4)
    global en
    en = Enemy()
    en.lvl = enemy.lvl
    if r == 1:
        en.name = 'Goblin'
        en.maxHp = enemy.maxHp
        en.hp = en.maxHp
        en.baseDmg = enemy.baseDmg
    elif r == 2:
        en.name = 'Troll'
        en.maxHp = math.ceil(enemy.maxHp * 1.2)
        en.hp = en.maxHp
        en.baseDmg = math.ceil(enemy.baseDmg * 1.1)
    elif r == 3:
        en.name = 'Slime cube'
        en.maxHp = math.ceil(enemy.maxHp * 1.1)
        en.hp = en.maxHp
        en.baseDmg = math.ceil(enemy.baseDmg * 1.1)
    else:
        en.name = 'Keltir'
        en.maxHp = math.ceil(enemy.maxHp * 0.8)
        en.hp = en.maxHp
        en.baseDmg = math.ceil(enemy.baseDmg * 1.3)
    while True:
        battleScr()
        #input()
        #print(enemy.__dict__)
        #print(en.__dict__)
        #print(hero.__dict__)
        g = input()
        en.hp -= hero.hit()
        hero.hp -= en.baseDmg
        #g = input()
        if g == 'p':
            if hero.potions == 0:
                print('нет хилок')
                input()
                os.system('clear')
                continue
            hero.potions -= 1
            hero.hp += hero.bph
            if hero.hp > hero.maxHp:
                hero.hp = hero.maxHp
        os.system('clear')
        if hero.hp <= 0:
            break
        if en.hp <= 0:
            hero.exp += enemy.exp
            hero.coins += enemy.coins
            if hero.exp >= hero.expForLvlUp:
                hero.lvlUp()
                enemy.lvlUp()
                break
            break

def shop():
    while True:
        os.system('clear')
        print(Fore.MAGENTA + '''\n\n                   _____  _   _  _____ ______ 
                  /  ___|| | | ||  _  || ___ \\
                  \ `--. | |_| || | | || |_/ /
                   `--. \|  _  || | | ||  __/ 
                  /\__/ /| | | |\ \_/ /| |    
                  \____/ \_| |_/ \___/ \_|    \n\n''')
        print('                1 - crit + 1%           5 coins')
        print('                2 - hp + 3              5 coins')
        print('                3 - dmg + 2             5 coins')
        print('                4 - potion              5 coins\n\n')
        print('                -------------------------------')
        print(Fore.YELLOW + '                coins:' + str(hero.coins), '             q - quit')
        l = input('                ')
        if l == '1':
            if hero.coins - 5 < 0:
                print('                 Недостаточно средств')
                input()
                continue
            hero.critChanse += 0.01
            hero.coins -= 5
        elif l == '2':
            if hero.coins - 5 < 0:
                print('Недостаточно средств')
                input()
                continue
            hero.maxHp += 3
            hero.hp = hero.maxHp
            hero.coins -= 5
        elif l == '3':
            if hero.coins - 5 < 0:
                print('Недостаточно средств')
                input()
                continue
            hero.baseDmg += 2
            hero.coins -= 5
        elif l == '4':
            if hero.coins - 5 < 0:
                print('Недостаточно средств')
                input()
                continue
            hero.potions += 1
            hero.coins -= 5
        elif l == 'q':
            break
    os.system('clear')
        

def game():
    os.system('clear')
    battle()
    while hero.hp > 0:
        x = rd.randint(1,2)
        if x == 1:
            shop()
            battle()
            if hero.hp <= 0:
                break
        else:
            battle()
            if hero.hp <= 0:
                break

def mainScr():
    print(Fore.YELLOW + '''   ______                                          
   |  _  \                                         
   | | | | _   _  _ __    __ _   ___   ___   _ __  
   | | | || | | || '_ \  / _` | / _ \ / _ \ | '_ \ 
   | |/ / | |_| || | | || (_| ||  __/| (_) || | | |
   |___/   \__,_||_| |_| \__, | \___| \___/ |_| |_|
                          __/ |                    
                         |___/                     \n''')
    print(Fore. YELLOW + '''           _   _  _____ ______  _____ 
          | | | ||  ___|| ___ \|  _  |
          | |_| || |__  | |_/ /| | | |
          |  _  ||  __| |    / | | | |
          | | | || |___ | |\ \ \ \_/ /
          \_| |_/\____/ \_| \_| \___/ \n''')

def main():
    while True:
        os.system('clear')
        mainScr()
        m = input('              1 - новая игра\n              2 - выход\n              ')
        if m == '1':
            os.system('clear')
            mainScr()
            name = input('              Имя персонажа:')
            global hero
            global enemy
            hero = Hero(name)
            enemy = Enemy()
            game()
        elif m == '2':
            os.system('clear')
            exit()

main()        
