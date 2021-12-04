from utils.file import read_file

squid_bingo = read_file('2021/assets/squid_bingo.txt')

call_list = list(map(lambda str: int(str), squid_bingo[0].split(',')))
cards = []

class Card:
    def __init__(self, rows):
        self.rows = rows
        values = dict()

        for i, row in enumerate(rows):
            for j, value in enumerate(row):
                square = dict()
                square['location'] = [i,j]
                square['checked'] = False
                values[value] = square
        
        self.values = values
        self.winner = False


card_rows = []
for row in squid_bingo[2:]:
    filtered = list(filter(lambda i: len(i) > 0, row.split(' ')))
    if len(filtered) == 0:
        cards.append(Card(card_rows))
        card_rows = []
        continue

    mapped = list(map(lambda str: int(str), filtered))
    card_rows.append(mapped)

cards.append(Card(card_rows))

# Start calling

def check_win(card, row, column):
    # Check for complete row
    complete_row = True
    for value in card.rows[row]:
        if card.values[value]['checked'] == False:
            complete_row = False
            break 
    # Check for complete column
    complete_column = True
    for row in card.rows:
        if card.values[row[column]]['checked'] == False:
            complete_column = False
            break
    return complete_row or complete_column

def calculate_score(winner, last_called_value):
    sum = 0
    for value, details in winner.values.items():
        if details['checked'] == False:
            sum += value
    return sum * last_called_value

winners = []
last_called = None
for call in call_list:
    for card in cards:
        if call in card.values:
            card.values[call]['checked'] = True

            if check_win(card, card.values[call]['location'][0], card.values[call]['location'][1]):
                if card.winner == False:
                    winners.append(card)
                    card.winner = True
    if len(winners) == len(cards):
        last_called = call
        break

print('part 1:', calculate_score(winners[0], last_called))
print('part 2', calculate_score(winners[-1], last_called))