import numpy as np
from ch01.ch01_3_1 import compute_event_probability

np.random.seed(0)
total_cards = 52
red_card_count = np.random.randint(0, total_cards)

black_card_count = total_cards - red_card_count
assert black_card_count != red_card_count

weighted_sample_space = {'red_card': red_card_count, 'black_card': black_card_count}
prob_red = compute_event_probability(lambda x: x == 'red_card', weighted_sample_space)

assert prob_red == red_card_count / total_cards

np.random.seed(0)
color = 'red' if np.random.binomial(1, prob_red) else 'black'
print(f"뒤섞인 카드 덱에서 꺼낸 첫 번째 카드는 {color}입니다")

np.random.seed(0)
red_count = np.random.binomial(10, prob_red)
print(f"10번 카드를 뒤섞었을 때 {red_count}번이 빨간색입니다")

np.random.seed(0)
red_card_count_array = np.random.binomial(50000, prob_red, 100000)
frequency_array = red_card_count_array / 50000

def compute_high_confidence_interval(likelihoods, bin_width):
    peak_index = likelihoods.argmax()
    area = likelihoods[peak_index] * bin_width
    start_index, end_index = peak_index, peak_index + 1
    while area < 0.95:
        if start_index > 0:
            start_index -= 1
        if end_index < likelihoods.size - 1:
            end_index += 1
        
        area = likelihoods[start_index: end_index+1].sum() * bin_width
    
    range_start, range_end = bin_edges[start_index], bin_edges[end_index]
    range_string = f"{range_start:.6f} - {range_end:.6f}"
    print(f"빈도 범위 {range_string}는 {100 * area:.2f}% 신뢰 구간을 나타냅니다")
    return start_index, end_index

likelihoods, bin_edges = np.histogram(frequency_array, bins='auto', density=True)
bin_width = bin_edges[1] - bin_edges[0]
start_index, end_index = compute_high_confidence_interval(likelihoods, bin_width)

range_start = round(0.842865*total_cards)
range_end = round(0.849139*total_cards)
print(f"빨간색 카드 개수는 {range_start}와 {range_end} 사이입니다")

if red_card_count == 44:
    print('맞췄습니다! 카드 덱에는 44장의 빨간색 카드가 들어 있습니다')
else:
    print(f'저런! 샘플링 추정이 틀렸습니다')