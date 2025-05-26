from ch01.ch01_2_2 import sample_space, has_sum_of_21
from ch01.ch01_1 import get_matching_event
from ch01.ch01_1_1 import compute_event_probability

from collections import defaultdict
weighted_sample_space = defaultdict(int)
for outcome in sample_space:
    total = sum(outcome)
    weighted_sample_space[total] += 1

assert weighted_sample_space[6] == 1
assert weighted_sample_space[36] == 1

num_combinations = weighted_sample_space[21]
print(f'주사위를 6번 굴렷을 때의 합계가 21이 될 수 있는 조합 개수는 {num_combinations}입니다')

assert sum([4, 4, 4, 4, 3, 2]) == 21
assert sum([4, 4, 4, 5, 3, 1]) == 21

event = get_matching_event(lambda x: sum(x) == 21, sample_space)
assert weighted_sample_space[21] == len(event)
assert sum(weighted_sample_space.values()) == len(sample_space)

prob = compute_event_probability(lambda x: x == 21, weighted_sample_space)
assert prob == compute_event_probability(has_sum_of_21, sample_space)
print(f'주사위를 6번 굴렸을 때의 합계가 21이 될 확률은 {prob}입니다')

print(f'가중되지 않은 표본 공간 내 요소 개수:')
print(len(sample_space))
print(f'가중된 표본 공간 내 요소 개수:')
print(len(weighted_sample_space))