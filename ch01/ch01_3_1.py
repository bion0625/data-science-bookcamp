from collections import defaultdict
from itertools import product
from ch01.ch01_1_1 import compute_event_probability
from ch01.ch01_3_0 import is_in_interval

def generate_coin_sample(num_flips=10):
    weighted_sample_space = defaultdict(int)
    for coin_flips in product(['Heads', 'Tails'], repeat=num_flips):
        heads_count = len([outcome for outcome in coin_flips
                           if outcome == 'Heads'])
        weighted_sample_space[heads_count] += 1
    return weighted_sample_space

weighted_sample_space = generate_coin_sample()
assert weighted_sample_space[10] == 1
assert weighted_sample_space[9] == 10

prob = compute_event_probability(lambda x: is_in_interval(x, 8, 10), weighted_sample_space)
print(f'앞면이 7번보다 많이 관측될 확률은 {prob}입니다')

prob = compute_event_probability(lambda x: not is_in_interval(x, 3, 7), weighted_sample_space)
print(f'앞면 또는 뒷면이 7번보다 많이 관측될 확률은 {prob}입니다')

weighted_sample_space_20_flips = generate_coin_sample(num_flips=20)
prob = compute_event_probability(lambda x: not is_in_interval(x, 5, 15), weighted_sample_space_20_flips)
print(f'앞면 또는 뒷면이 15번보다 많이 관측될 확률은 {prob}입니다')