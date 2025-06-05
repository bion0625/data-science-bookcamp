import numpy as np
from ch04.ch04_1_0 import execute_strategy

observations = np.array([execute_strategy() for _ in range(1000)])

frequency_wins = observations.sum() / 1000
assert frequency_wins == observations.mean()
print(f"이긴 빈도는 {frequency_wins}입니다")

dollers_won = frequency_wins * 1000
deolors_lost = (1-frequency_wins) * 1000
total_profit = dollers_won - deolors_lost
print(f"총 수익은 ${total_profit:.2f}입니다")

np.random.seed(0)
def repeat_game(number_repeats):
    observations = np.array([execute_strategy() for _ in range(number_repeats)])
    return observations.mean()

# frequencies = []
# for i in range(1, 1000):
#     frequencies.append(repeat_game(i))

import matplotlib.pyplot as plt
from matplotlib import rc
rc('font', family='Malgun Gothic')  # Windows 기본 한글 폰트

# plt.plot(list(range(1, 1000)), frequencies)
# plt.axhline(0.5, color='k')
# plt.xlabel('플레이된 게임 수')
# plt.ylabel('승리 빈도수')
# plt.show()
# print(f"10,000번 뒤섞기로 얻은 이긴 빈도는 {frequencies[-1]}입니다")


# np.random.seed(0)
# frequency_array = np.array([repeat_game(10000) for _ in range(300)])

# likelihoods, bin_edges, patches = plt.hist(frequency_array, bins='auto',
#                                            edgecolor='black', density=True)
# bin_width = bin_edges[1] - bin_edges[0]

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

# start_index, end_index = compute_high_confidence_interval(likelihoods, bin_width)

# for i in range(start_index, end_index):
#     patches[i].set_facecolor('yellow')
# plt.xlabel('빈도 구간')
# plt.ylabel('상대적 확률')
# plt.show()

# np.random.seed(0)
# frequency_array = np.array([repeat_game(50000) for _ in range(3000)])
# likelihoods, bin_edges = np.histogram(frequency_array, bins='auto', density=True)
# bin_width = bin_edges[1] - bin_edges[0]
# compute_high_confidence_interval(likelihoods, bin_width)

# np.random.seed(0)
# def repeat_game(number_repeats, min_red_fraction):
#     observations = np.array([execute_strategy(min_red_fraction) 
#                              for _ in range(number_repeats)])
#     return observations.mean()

# frequency_array = np.array([repeat_game(50000, 0.75) for _ in range(3000)])
# likelihoods, bin_edges = np.histogram(frequency_array, bins='auto', density=True)
# bin_width = bin_edges[1] - bin_edges[0]
# compute_high_confidence_interval(likelihoods, bin_width)