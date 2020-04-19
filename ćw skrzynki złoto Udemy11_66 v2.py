"""
Napisz krótką grę w której masz 5 ruchów w jedną stronę poprzez KOMNATĘ.

Za każdym razem masz szansę spotkać po drodzę skrzynkę lub NIC.

Skrzynki mają różne kolory.

Kolor skrzynki oznacza jak rzadka jest ta skrzynka.

zielona - 75%
pomarańczowa - 20%
fioletowa - 4%
złota (legendarna) - 1%

Ustaw, że jest 40% szansy, że nie spotkasz niczego. 60%, że będzie skrzynka.

Ustaw złoto jako to co może "wypaść" ze skrzynki:
zielony - 1000,
pomaranczowy - 4000,
fioletowy - 9000,
zlota - 16000

1 1 0+1
4 2 1 +1
9 3 2+1
16 4 3 +1

Pamiętaj o:
1) czystym kodzie
2) nazywaniu zmiennych tak by bylo samoopisujace sie
3) spróbuj napisać program po angielsku
"""

import random

boxGift = [{"green": 1000}, {"orange": 4000}, {"purple": 9000}, {"legendary": 16000}]
boxesYouWon = []

def summary(newBox, collectedSum): #wszystkie wylosowane pudełka
    collectedSum.append(newBox)
    print(collectedSum)


def will_box_find(boxChanceToFindPercentage, gifts): #losowanie pudełek
    isFindChance = random.uniform(0,100)
    collected = {"no_box": 0}
    if (isFindChance > boxChanceToFindPercentage):
        print("You found BOX!")
        collected = (random.choices(gifts, [75, 20, 4, 1])[0])
    else:
        print("You missed :(")
    return summary(collected, boxesYouWon) # dodawanie pudełek do wszystkich wylosowanych



gameLenght = 5

while gameLenght > 0:
    gameAnswer = input("Do you want to move forward? y/n")
    if gameAnswer == "y":
        will_box_find(40, boxGift)
    else: continue
    gameLenght = gameLenght - 1

