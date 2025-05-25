from ch01.ch01_1 import get_matching_event, is_heads_or_tails, event_conditions

weighted_sample_space = {'앞면':4, '뒷면':1}

sample_space_size = sum(weighted_sample_space.values())
assert sample_space_size == 5

event = get_matching_event(is_heads_or_tails, weighted_sample_space.keys())
event_size = sum(weighted_sample_space[outcome] for outcome in event)
assert event_size == 5

def compute_event_probability(event_condition, generic_sample_space: set):
    event = get_matching_event(event_condition, generic_sample_space)
    if type(generic_sample_space) == type(set()):
        return len(event) / len(generic_sample_space)

def compute_event_probability(event_condition, generic_sample_space: dict):
    event = get_matching_event(event_condition, generic_sample_space.keys())
    event_size = sum(generic_sample_space[outcome] for outcome in event)
    return event_size / sum(generic_sample_space.values())

for event_condition in event_conditions:
    prob = compute_event_probability(event_condition, weighted_sample_space)
    name = event_condition.__name__
    print(f"'{name}'에서 발생한 사건의 확률은 {prob}입니다")