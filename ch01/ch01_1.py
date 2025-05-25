sample_space = {'앞면', '뒷면'}

probability_heads = 1 / len(sample_space)
print(f"앞면이 선택될 확률은 {probability_heads}입니다.")

def is_heads_or_tails(outcome): return outcome in {'앞면', '뒷면'}
def is_neithier(outcome): return not is_heads_or_tails(outcome)

def is_heads(outcome): return outcome == '앞면'
def is_tails(outcome): return outcome == '뒷면'

def get_matching_event(event_condition, sample_space):
    return set([outcome for outcome in sample_space 
                if event_condition(outcome)])

event_conditions = [is_heads_or_tails, is_heads, is_tails, is_neithier]

for event_condition in event_conditions:
    print(f'사건 조건: {event_condition.__name__}')
    event = get_matching_event(event_condition, sample_space)
    print(f'사건: {event}\n')

def comput_probability(event_condition, generic_sample_space):
    event = get_matching_event(event_condition, generic_sample_space)
    return len(event) / len(generic_sample_space)

for event_condition in event_conditions:
    prob = comput_probability(event_condition, sample_space)
    name = event_condition.__name__
    print(f"'{name}에서 발생한 사건의 확률은 {prob}입니다.")