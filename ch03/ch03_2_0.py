import numpy as np

np.random.seed(0)
head_count_list = [np.random.binomial(1000, 0.7) for _ in range(500)]

np.random.seed(0)
head_count_array = np.random.binomial(1000, 0.7, 500)

assert head_count_array.tolist() == head_count_list

new_array = np.array(head_count_list)
assert np.array_equal(new_array, head_count_array) == True

frequency_array = head_count_array / 1000
assert frequency_array.tolist() == [head_count / 1000 for head_count in head_count_list]
assert frequency_array.tolist() == list(map(lambda x: x / 1000, head_count_list))

print(frequency_array[:20])

min_freq = frequency_array.min()
max_freq = frequency_array.max()
print(f"관측된 최소 빈도: {min_freq}")
print(f"관측된 최대 빈도: {max_freq}")
print(f"빈도의 범위: {max_freq - min_freq}")

import matplotlib
# 한글 폰트 설정
matplotlib.rcParams['font.family'] = 'NanumGothic'  # 또는 'Malgun Gothic' 등 시스템에 따라 선택
matplotlib.rcParams['axes.unicode_minus'] = False  # 마이너스 기호 깨짐 방지

from collections import defaultdict
import matplotlib.pyplot as plt

frequency_counts = defaultdict(int)
for frequency in frequency_array:
    frequency_counts[frequency] += 1

frequencies = list(frequency_counts.keys())
counts = [frequency_counts[freq] for freq in frequencies]

plt.scatter(frequencies, counts)
plt.xlabel('빈도')
plt.ylabel('횟수')
plt.show()