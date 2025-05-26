from itertools import product
from ch01.ch01_1_1 import compute_event_probability

possible_rolls = list(range(1, 7))
print(possible_rolls)

sample_space = set(product(possible_rolls, repeat=6))

def has_sum_of_21(outcome: list): return sum(outcome) == 21
prob = compute_event_probability(has_sum_of_21, sample_space)
print(f"6번 주사위를 굴린 결과의 합이 21일 확률은 {prob}입니다")

prob = compute_event_probability(lambda x: sum(x) == 21, sample_space)
assert prob == compute_event_probability(has_sum_of_21, sample_space)