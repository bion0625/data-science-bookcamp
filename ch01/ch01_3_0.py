from ch01.ch01_1_1 import compute_event_probability
from ch01.ch01_2_3 import weighted_sample_space

def is_in_interval(number: int, minimum: int, maximum: int):
    return minimum <= number <= maximum

prob = compute_event_probability(lambda x: is_in_interval(x, 10, 21), weighted_sample_space)
print(f'구간에 대한 확률은 {prob}입니다')