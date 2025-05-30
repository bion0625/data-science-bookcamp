import matplotlib.pyplot as plt
import numpy as np
import matplotlib
# 한글 폰트 설정
matplotlib.rcParams['font.family'] = 'NanumGothic'  # 또는 'Malgun Gothic' 등 시스템에 따라 선택
matplotlib.rcParams['axes.unicode_minus'] = False  # 마이너스 기호 깨짐 방지

np.random.seed(0)
head_count_array = np.random.binomial(1000, 0.7, 500)
frequency_array = head_count_array / 1000
min_freq = frequency_array.min()
max_freq = frequency_array.max()

# plt.hist(frequency_array, bins='auto', edgecolor='black')
# plt.xlabel('유사한 것들끼리 묶인 빈도')
# plt.ylabel('횟수')
# plt.show()

counts, _, _ = plt.hist(frequency_array, bins='auto', edgecolor='black')

print(f"빈의 개수: {counts.size}")

counts, bin_edges, _ = plt.hist(frequency_array, bins='auto', edgecolor='black')

bin_width = bin_edges[1] - bin_edges[0]
assert bin_width == (max_freq - min_freq) / counts.size
print(f"빈 너비: {bin_width}")

def output_bin_coverage(i):
    count = int(counts[i])
    range_start, range_end = bin_edges[i], bin_edges[i+1]
    range_string = f"{range_start} - {range_end}"
    print(f"빈도 번위 {range_string}에 대한 빈은 "
          f"{count}개의 요소를 포함합니다")

output_bin_coverage(0)
output_bin_coverage(5)

assert counts[counts.argmax()] == counts.max()

output_bin_coverage(counts.argmax())