from ch01.ch01_1_1 import compute_event_probability

passible_children = ['Boy', 'Girl']
sample_space = set()
for child1 in passible_children:
    for child2 in passible_children:
        for child3 in passible_children:
            for child4 in passible_children:
                outcome = (child1, child2, child3, child4)
                sample_space.add(outcome)

from itertools import product
# all_combinations = product(*(4*[passible_children]))
all_combinations = product(passible_children, repeat=4)
assert set(all_combinations) == sample_space

def has_two_boys(outcome): return len([child for child in outcome 
                                       if child == 'Boy']) == 2
prob = compute_event_probability(has_two_boys, sample_space)
print(f"남아 두 명이 포함되었을 확률은 {prob}입니다")