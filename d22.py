seen = {}

def play(deck1, deck2):
    global seen
    while deck1 and deck2:
        if deck1 and str(deck1) in seen:
            seen = {}
            return True
        seen[str(deck1)] = 1
        p1 = deck1.pop(0)
        p2 = deck2.pop(0)
        if p1 <= len(deck1) and p2 <= len(deck2):
            if play(deck1[:p1], deck2[:p2]):
                deck1.append(p1)
                deck1.append(p2)
                #return True
            else:
                deck2.append(p2)
                deck2.append(p1)
                #return False
        elif p1 > p2:
            deck1.append(p1)
            deck1.append(p2)
        else:
            deck2.append(p2)
            deck2.append(p1)
    seen = {}
    return deck2 == []


with open('d22.in1', 'r') as f:
    content = f.read()
l = content.split('\n\n')
players = [x.split(':')[0] for x in l]
cards = [[int(y) for y in x.split(':\n')[1].split('\n')] for x in l]
round = 0
print(play(cards[0],cards[1]))
cc = len(cards[1])
winsum = 0
for i in cards[1]:
    winsum += cc * i
    cc -= 1
print(winsum)