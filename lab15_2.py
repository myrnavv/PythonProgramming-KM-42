def card_deck():
    suit = ('diamonds', 'clubs', 'hearts', 'spades')
    value = ('A',) + tuple(range(2, 11)) + ('J', 'Q', 'K')
    for i in suit:
        for j in value:
            yield f'{j} {i}'

deck = card_deck()
while True:
    print(next(deck)) 