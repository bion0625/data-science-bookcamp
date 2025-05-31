import numpy as np
import matplotlib.pyplot as plt
# from ch03.ch03_2_2 import compute_high_confidence_interval
from matplotlib import rc

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

rc('font', family='Malgun Gothic')  # Windows 기본 한글 폰트

# np.random.seed(0)
# head_count_array = np.random.binomial(1000, 0.7, 100000)
# frequency_array = head_count_array / 1000
# assert frequency_array.size == 100000

# likelihoods, bin_edges, patches = plt.hist(frequency_array, bins='auto',
#                                            edgecolor='black', density=True)
# bin_width = bin_edges[1] - bin_edges[0]
# start_index, end_index = compute_high_confidence_interval(likelihoods, bin_width)

# for i in range(start_index, end_index):
#     patches[i].set_facecolor('yellow')
# plt.xlabel('빈도 구간')
# plt.ylabel('상대적 확률')
# plt.show()

np.random.seed(0)
head_count_array = np.random.binomial(50000, 0.7, 100000)
frequency_array = head_count_array / 50000

likelihoods, bin_edges, patches = plt.hist(frequency_array, bins='auto',
                                           edgecolor='black', density=True)
bin_width = bin_edges[1] - bin_edges[0]
start_index, end_index = compute_high_confidence_interval(likelihoods, bin_width)

for i in range(start_index, end_index):
    patches[i].set_facecolor('yellow')
plt.xlabel('빈도 구간')
plt.ylabel('상대적 확률')
plt.show()