def play(deck1, deck2):  # return True if player1 wins
    seen = set()
    while deck1 and deck2:
        if str(deck1 + [0] + deck2) in seen:
            return True
        seen.add(str(deck1 + [0] + deck2))
        p1 = deck1.pop(0)
        p2 = deck2.pop(0)
        if p1 <= len(deck1) and p2 <= len(deck2):
            if play(deck1[:p1], deck2[:p2]):
                deck1.append(p1)
                deck1.append(p2)
            else:
                deck2.append(p2)
                deck2.append(p1)
        elif p1 > p2:
            deck1.append(p1)
            deck1.append(p2)
        else:
            deck2.append(p2)
            deck2.append(p1)
    return deck2 == []


with open('d22.in', 'r') as f:
    content = f.read()
ll = content.split('\n\n')
players = [x.split(':')[0] for x in ll]
cards = [[int(y) for y in x.split(':\n')[1].split('\n')] for x in ll]
print(p1win := play(cards[0], cards[1]))
cc = len(cards[0])
score = 0
for i in cards[0]:
    score += cc * i
    cc -= 1
print(score)
# 32427 too low
# 32769 OK