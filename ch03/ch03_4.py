import numpy as np

np.random.seed(0)
card_deck = [1, 1, 0, 0]
np.random.shuffle(card_deck)
print(card_deck)

np.random.seed(0)
unshuffled_deck = [1, 1, 0, 0]
shuffled_deck = np.random.permutation(unshuffled_deck)
assert unshuffled_deck == [1, 1, 0, 0]
print(shuffled_deck)

import itertools
for permutation in list(itertools.permutations(unshuffled_deck))[:3]:
    print(permutation)

for permutation in list(itertools.permutations([0, 1, 2, 3]))[:3]:
    print(permutation)

from collections import defaultdict

weighted_sample_space = defaultdict(int)
for permutation in itertools.permutations(unshuffled_deck):
    weighted_sample_space[permutation] += 1

for permutation, count in weighted_sample_space.items():
    print(f"순열 {permutation}은 {count}번 발생합니다")

from ch01.ch01_3_1 import compute_event_probability

sample_space = set(itertools.permutations(unshuffled_deck))
event_condition = lambda x: list(x) == unshuffled_deck
prob = compute_event_probability(event_condition, sample_space)
assert prob == 1 / len(sample_space)
print(f"해당 뒤섞기 작업이 카드 덱을 변경하지 않을 확률은 {prob}입니다")

red_cards = 5 * [1]
black_cards = 5 * [0]
unshuffled_deck = red_cards + black_cards
sample_space = set(itertools.permutations(unshuffled_deck))
print(f"카드 열 장으로 구성된 카드 덱의 표본 공간에는 {len(sample_space)}개의 요소가 있습니다")