import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rc
rc('font', family='Malgun Gothic')  # Windows 기본 한글 폰트

np.random.seed(0)
head_count_array = np.random.binomial(1000, 0.7, 500)
frequency_array = head_count_array / 1000

likelihoods, bin_edges, _ = plt.hist(frequency_array, bins='auto',
         edgecolor='black', density=True)
# plt.xlabel('빈도 구간')
# plt.ylabel('상대적 확률')
# plt.show()

bin_width = bin_edges[1] - bin_edges[0]
assert bin_width * likelihoods.sum() == 1.0

index = likelihoods.argmax()
area = likelihoods[index] * bin_width
range_start, range_end = bin_edges[index], bin_edges[index+1]
range_string = f"{range_start} - {range_end}"
print(f"샘플링된 빈도가 {range_string} 구간에 속할 확률은 {area}입니다")

peak_index = likelihoods.argmax()
start_index, end_index = (peak_index-1, peak_index+2)
area = likelihoods[start_index: end_index+1].sum() * bin_width
range_start, range_end = bin_edges[start_index], bin_edges[end_index]
range_string = f"{range_start} - {range_end}"
print(f"샘플링된 빈도가 {range_string} 구간에 속할 확률은 {area}입니다")

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

compute_high_confidence_interval(likelihoods, bin_width)