import random

class Card(object):
    def __init__(self,Color,Num,Ability):
        self.color = Color
        self.num = Num
        self.ability = Ability
        
    def returnColor(self,string):
        self.color = string
        return string
    
    def returnColor(self,string):
        self.num = string
        return string
    
    def returnColor(self,string):
        self.ability = string
        return string
    
    def printCard(self):
        if self.color != 'no':
            print(self.color)
        if self.num<10 and self.num>-1:
            print(self.num)
        if self.ability != 'no':
            print(self.ability, ' ability')
        print('\n')
    
class Basic(Card):
    def __init__(self,Color,Num,Ability):
        self.color = Color
        self.num = Num
        self.ability = Ability
    
class Special(Card):
    def __init__(self,Color,Num,Ability):
        self.color = Color
        self.num = Num
        self.ability = Ability
    
class Deck(object):
    def __init__(self,cartdeck = []):
        self.cartdeck = []
        
    def deckinit(self):
        for j in range (2):
            for i in range(9):
                self.cartdeck.append(Basic('red',i,'no'))
                self.cartdeck.append(Basic('yellow',i,'no'))
                self.cartdeck.append(Basic('blue',i,'no'))
                self.cartdeck.append(Basic('green',i,'no'))
            self.cartdeck.append(Special('red',20,'reverse'))
            self.cartdeck.append(Special('blue',20,'reverse'))
            self.cartdeck.append(Special('yellow',20,'reverse'))
            self.cartdeck.append(Special('green',20,'reverse'))
            self.cartdeck.append(Special('red',20,'taketwo'))
            self.cartdeck.append(Special('blue',20,'taketwo'))
            self.cartdeck.append(Special('yellow',20,'taketwo'))
            self.cartdeck.append(Special('green',20,'taketwo'))
            self.cartdeck.append(Special('red',20,'skip'))
            self.cartdeck.append(Special('blue',20,'skip'))
            self.cartdeck.append(Special('yellow',20,'skip'))
            self.cartdeck.append(Special('green',20,'skip'))
            self.cartdeck.append(Special('no',50,'colorswap'))
            self.cartdeck.append(Special('no',50,'colorswap'))
            self.cartdeck.append(Special('no',50,'takefour'))
            self.cartdeck.append(Special('no',50,'takefour'))           
        self.cartdeck.append(Basic('red',0,'no'))
        self.cartdeck.append(Basic('yellow',0,'no'))
        self.cartdeck.append(Basic('blue',0,'no'))
        self.cartdeck.append(Basic('green',0,'no'))
        return self.cartdeck
    
    def subCardD(self):
        a = self.cartdeck[-1]
        self.cartdeck.pop()
        return a
    
    def addCardD(self,card):
        self.cartdeck.insert(0,card)
        
    def numDeck(self):
        return len(self.cartdeck)
    
#Всего в игре 108 карт(иногда 106), 112 с пустыми картами (см. рисунок):
#
#Карты 4 цветов (синий, жёлтый, красный, зелёный) с номерами от 0 до 9 (76 шт, с цифрами от 1 до 9, по две одинаковых на каждый цвет, и четыре карты разных цветов с цифрой 0) — обычные карты.
#8 карт «Возьми две», 8 карт «Ход обратно», 8 карт «Пропусти ход» по 2 на каждый цвет — карты действия.
#4 карты «Заказать цвет», 4 карты «Возьми четыре» на чёрном фоне — карты действия (дикие карты).


class Player(object):
    def __init__(self, kit = [], points = 0):
        self.kit = kit
        self.points = points
        
    def addCard(self,numlen):
        for i in range(numlen):
            self.kit.append(deck.subCardD())
            
    def printKit(self):
        print('Ваши карты:\n')
        for i in range(len(self.kit)):
            print('Номер карты:',i+1)
            self.kit[i].printCard()
            
    def subKitCard(self,index):
        a = self.kit[index]
        self.kit.pop(index)
        return a
    
    def printPoints(self):
        print('Баллы игрока: '+ self.points + '\n')
    
class Bot(Player):
    def __init__(self,kit = [], points = 0):
        self.kit = kit
        self.points = points
   
    
class Field(object):
    def __init__(self,deck,secdeck,player,botnum,lastcard, end = False):
       self.lastcard = lastcard
       self.botnum = botnum
       self.botset = []
       self.end = end
       self.addBot(self.botnum)
       player.addCard(7)
       self.lastCardChek(deck)
       self.printLastCard()
       self.end = end
       print(deck.numDeck())
       reverseFlag = False
       skipFlag = True
       while True:
           if(self.end ==True):
                    break
           for  i in range(len(self.botset)+1):
                if(skipFlag):
                    skipFlag = False
                    if (self.skip(lastcard)):
                        print('Пропуск хода!\n')
                        continue
                    if (lastcard.ability == 'taketwo'):
                        if((i == len(self.botset)+1 and reverseFlag == True ) or(i==0 and reverseFlag == False)):
                            player.addCard(2)
                        else:
                            botset[i].addCard(2)
                        print('Возьми две!\n')
                        continue
                    if (lastcard.ability == 'taketfour'):
                        if((i == len(self.botset)+1 and reverseFlag == True) or (i == 0 and reverseFlag == False)):
                            player.addCard(4)
                        else:
                            botset[i].addCard(4)
                        print('Возьми четыре!\n')
                        continue
                
                if(reverseFlag == False and i == 0):
                    print('Ваш ход\n')
                    self.move(1,0)
                    if(self.end ==True):
                        break
                    continue
                print('Ход бота номер: ', i, '\n')
                self.move(0,i)
                if(self.end ==True):
                    break
                if(reverseFlag == True and i == botnum+1):
                    print('Ваш ход\n')
                    self.move(1,0)
                    if(self.end ==True):
                        break
                    
    def addPoints(self,index):
        points = 0
        if index == -1:
            for i in range(len(self.botset)):
                for j  in range(len(self.botset[i].kit)):
                    points = points + self.botset[i].kit[j].num
            player.points = points
        else:
            for j  in range(len(self.player.kit)):
                    points = points + self.player.kit[j].num
            for i in (range(len(self.botset))):
                for j  in range(len(self.botset[i].kit)):
                    if index == i:
                        continue
                    points = points + self.botset[i].kit[j].num
            self.botset[index].points = points

    def UNOCheck(self, player):
        if player.kit == []:
            print('UNO')
            return 1
        return 0 
       
    def printLastCard(self):
        print('Последняя карта на столе:\n')
        self.lastcard.printCard()
    
    def lastCardChek(self,deck):
        while True:
            if self.lastcard.num == 50: # карта со способностью
                deck.addCardD(self.lastcard)
                self.lastcard = deck.subCardD()
            else:
                break
            
    def forDropCard(self,card,forFourFlag):  
        if self.lastcard.color == 'no' and self.lastcard.ability != 'no':
            return 1
        if self.lastcard.ability != 'no' and card.color == self.lastcard.color:
            return 1
        if (self.lastcard.ability == 'taketwo' or self.lastcard.ability == 'reverse' or self.lastcard.ability == 'skip' or self.lastcard.ability == 'colorswap') and self.lastcard.color == card.color :
            return 1
        if self.lastcard.num == card.num:
            return 1
        if self.lastcard.color == card.color:
            return 1
        if card.ability == 'colorswap':
            return 1
        if card.color == 'no' and card.ability == 'takefour':
            if(forFourFlag):
                return 1
        return 0
        
    def forFour(self, player1, card):
        for i in range(len(player1.kit)):
            if(player1.kit[i].ability== 'takefour'):
                continue
            if(self.forDropCard(player1.kit[i],0)):
                return 0
        return 1       
                    
    def dropCard(self,card):
        secdeck.addCardD(self.lastcard)
        self.lastcard = card
        
    def move(self,botflag,i):
        self.printLastCard()
        if botflag:
            player.printKit()
            while True:
                a = input('Введите номер действия\n1.Взять карту\n2.Положить карту\n')
                match a:
                    case '1':
                        self.defChek()
                        player.addCard(1)
                        a = self.forFour(player,player.kit[-1])
                        if(self.forDropCard(player.kit[-1],a)):
                            player.kit[-1].printCard()
                            b = input('Вы можете использовать эту карту\n1. Пасс\n2. Использовать карту\n')
                            if(player.kit[-1].ability == "colorswap" or player.kit[-1].ability == "takefour" ):
                                self.colorswap(botflag)
                            if b=='2':
                                self.dropCard(player.subKitCard(-1))
                            if(self.UNOCheck(player)):
                                self.end =self.WinLogic()
                        break
                    case '2':
                        b = input('Введите номер карты\n')
                        b = int(b)-1
                        a = self.forFour(player,player.kit[-1])
                        if(self.forDropCard(player.kit[b],a)):
                            if(player.kit[b].ability == "colorswap" or player.kit[b].ability == "takefour"):
                                self.colorswap(botflag)
                            self.dropCard(player.subKitCard(b))
                            if(self.UNOCheck(self.botset[i])):
                                self.end = self.WinLogic()
                            break
                        else:
                            print('Нельзя использовать эту карту!')
                           
        else:
            self.logic(self.botset[i-1])
        self.printLastCard()
        
    def deckChek(self,deck,secdeck):
        if deck.cartdeck == []:
            deck.cartdeck = secdeck.certdeck
        return deck.cartdeck
    
    def addBot(self,botnum):
        for i in range(botnum):
            bot = Bot()
            bot.addCard(7)
            self.botset.append(bot)

    def logic(self,bot):
        for i in range(len(bot.kit)):
            if(self.forDropCard(bot.kit[i],self.forFour(bot,bot.kit[i]))):
                if(bot.kit[i].ability == "colorswap" or bot.kit[i].ability == "takefour" ):
                        self.colorswap(0)
                self.dropCard(bot.subKitCard(i))
                print('Бот выбросил карту!')
                break
            else:
                self.defChek()
                bot.addCard(1)
                print('Бот взял карту')
                break
            
    def reverse(self):
        print('Смена направления')
        self.botset.reverse()
        self.lastcard.num = 1;
        if(self.reverseFlag == True):
            self.reverseFlag == False
        else:
            self.reverseFlag == True
            
    def colorswap(self,botflag):
        if(botflag == False):
            self.lastcard.color = 'red'
        else:
            while True:
                a = input('Введите номер цвета, чтобы его задать\n1 Красный\n2 Зеленый\n3 Желтый \n4 Синий\n')
                match a:
                    case '1':
                        self.lastcard.color = 'red'
                        break
                    case '2':
                        self.lastcard.color = 'green'
                        break
                    case '3':
                        self.lastcard.color = 'yellow'
                        break
                    case '4':
                        self.lastcard.color = 'blue'
                        break
        self.printLastCard()
        print('Смена цвета!\n')
        
    def skip(self, card):
        if(card.ability == 'skip' or card.ability == 'takefour' or card.ability == 'taketwo'):
            return 1
        return 0
    
    def defChek(self):
        if(len(deck.cartdeck) == 0):
            print('Колода заменена и перетасована')
            deck.cartdeck = secdeck.cartdeck
            random.shuffle(deck.cartdeck)
            secdeck.cartdeck = []
            
    def winLogic(self):
        player.printPoints()
        for i in range(len(self.botset[i])):
            self.botset[i].printPoints()
        for i in range(len(self.botset[i])):
            if self.botset[i].points >= 500:
                print('Выйграл бот с номером ' + i + '!')
                return True
            if player.points >=500:
                print('Вы выйграли!')
                return True
        return False
        
    
            
#Стрелочки – смена направления. Игра переходит в обратную сторону. Например, если ходили по часовой стрелке, то продолжать действие следует против часовой и наоборот.
#Возьми 2. Следующий игрок пропускает ход и берет 2 карты из колоды.
#Пропуск хода. С ним все ясно.
#Дикая карта или карта выбора цвета. Воспользовавшийся ей получает право определить, какую картинку должен разыграть соперник.
#Дикая карта +4. Самая чудодейственная и всемогущая. Основная функция – выбор цвета, а в дополнение соседний игрок берет 4 штуки из колоды и пропускает ход.
        

deck = Deck()
secdeck = Deck()
deck.deckinit()
random.shuffle(deck.cartdeck)
player = Player([])
numbot = int(input('Введите количество ботов(1-9)\n'))
while True:
    if numbot<10 and numbot>0:
        break
    numbot = int(input('Введите количество ботов еще раз (от 1 до 9) \n'))

user_inp = input("Введите \'1\', чтобы начать игру\n")
user_inp.lower()

if user_inp =='1':
    while True:
        field = Field(deck,secdeck,player,numbot,deck.subCardD())
        break
else:
    print('Выход')
    exit()
                
#Выигрывает игру игрок, первый набравший 500 баллов, а проигрывает тот, кто на этот момент набрал меньше всех баллов.



