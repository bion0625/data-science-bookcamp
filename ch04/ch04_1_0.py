red_card = 26 * [1]
black_card = 26 * [0]
unshuffled_deck = red_card + black_card

import numpy as np
np.random.seed(1)
shuffled_deck = np.random.permutation(unshuffled_deck)

remaining_red_cards = 26
for i, card in enumerate(shuffled_deck[:-1]):
    remaining_red_cards -= card
    remaining_total_cards = 52 - i - 1
    if remaining_red_cards / remaining_total_cards > 0.5:
        break

print(f"{i}번째 인덱스에서 게임이 종료되었습니다")
final_card = shuffled_deck[i+1]
color = 'red' if final_card else 0
print(f"카드 덱의 다음 카드는 {'빨간색' if final_card else '검은색'}입니다")
print(f"{'이겼' if final_card else '졌'}습니다!")



np.random.seed(0)
total_cards = 52
total_red_cards = 26
def execute_strategy(min_red_fraction=0.5, shuffled_deck=None, return_index=False):
    if shuffled_deck is None:
        shuffled_deck = np.random.permutation(unshuffled_deck)
    
    remaining_red_cards = total_red_cards

    for i, card in enumerate(shuffled_deck[:-1]):
        remaining_red_cards -= card
        fraction_red_cards = remaining_red_cards / (total_cards - i - 1)
        if fraction_red_cards > min_red_fraction:
            break
    
    return (i+1, shuffled_deck[i+1]) if return_index else shuffled_deck[i+1]