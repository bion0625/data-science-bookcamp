import matplotlib
# 한글 폰트 설정
matplotlib.rcParams['font.family'] = 'NanumGothic'  # 또는 'Malgun Gothic' 등 시스템에 따라 선택
matplotlib.rcParams['axes.unicode_minus'] = False  # 마이너스 기호 깨짐 방지

from ch01.ch01_3_1 import weighted_sample_space, weighted_sample_space_20_flips
from ch01.ch01_3_0 import is_in_interval

import matplotlib.pyplot as plt

x_10_flips = list(weighted_sample_space.keys())
y_10_flips = list(weighted_sample_space[key] for key in x_10_flips)
sample_space_size = sum(weighted_sample_space.values())
prob_x_10_flips = [value / sample_space_size for value in y_10_flips]

x_20_flips = list(weighted_sample_space_20_flips.keys())
y_20_flips = [weighted_sample_space_20_flips[key] for key in x_20_flips]
sample_space_size = sum(weighted_sample_space_20_flips.values())
prob_x_20_flips = [value / sample_space_size for value in y_20_flips]

# plt.plot(x_10_flips, prob_x_10_flips, label='A: 10번의 동전 뒤집기')
# plt.scatter(x_10_flips, prob_x_10_flips)
# plt.plot(x_20_flips, prob_x_20_flips, color='black', linestyle='--', label='B: 20번의 동전 뒤집기')
# plt.scatter(x_20_flips, prob_x_20_flips, color='k', marker='x')
# plt.xlabel('앞면 개수')
# plt.ylabel('확률')
# plt.legend()
# plt.show()

# plt.plot(x_10_flips, prob_x_10_flips, label='A: 10번의 동전 뒤집기')
# plt.plot(x_20_flips, prob_x_20_flips, color='k', linestyle=':', label='B: 20번의 동전 뒤집기')
where_10 = [not is_in_interval(value, 3, 7) for value in x_10_flips]
# plt.fill_between(x_10_flips, prob_x_10_flips, where=where_10)
where_20 = [not is_in_interval(value, 5, 15) for value in x_20_flips]
# plt.fill_between(x_20_flips, prob_x_20_flips, where=where_20)
# plt.xlabel('앞면 개수')
# plt.ylabel('확률')
# plt.legend()
# plt.show()

x_10_frequencies = [head_count / 10 for head_count in x_10_flips]
x_20_frequencies = [head_count / 20 for head_count in x_20_flips]
# plt.plot(x_10_frequencies, prob_x_10_flips, label='A: 10번의 동전 뒤집기')
# plt.plot(x_20_frequencies, prob_x_20_flips, color='k', linestyle=':', label='B: 20번의 동전 뒤집기')
# plt.legend()
# plt.xlabel('앞면 빈도')
# plt.ylabel('확률')
# plt.show()

relative_likelihood_10 = [10*prob for prob in prob_x_10_flips]
relative_likelihood_20 = [20*prob for prob in prob_x_20_flips]

plt.plot(x_10_frequencies, relative_likelihood_10, label='A: 10번의 동전 뒤집기')
plt.plot(x_20_frequencies, relative_likelihood_20, color='k', linestyle=':', label='B: 20번의 동전 뒤집기')
plt.fill_between(x_10_frequencies, relative_likelihood_10, where=where_10)
plt.fill_between(x_20_frequencies, relative_likelihood_20, where=where_20)
plt.legend()
plt.xlabel('앞면 빈도')
plt.ylabel('상대적 확률')
plt.show()