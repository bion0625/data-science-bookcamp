from ch01.ch01_3_1 import weighted_sample_space, weighted_sample_space_20_flips
from ch01.ch01_3_0 import is_in_interval

import matplotlib
# 한글 폰트 설정
matplotlib.rcParams['font.family'] = 'NanumGothic'  # 또는 'Malgun Gothic' 등 시스템에 따라 선택
matplotlib.rcParams['axes.unicode_minus'] = False  # 마이너스 기호 깨짐 방지

import matplotlib.pyplot as plt

x_10_flips = list(weighted_sample_space.keys())
y_10_flips = list(weighted_sample_space[key] for key in x_10_flips)
# plt.scatter(x_10_flips, y_10_flips)
# plt.xlabel('앞면 개수')
# plt.ylabel('앞면 개수 x에 따른 동전 뒤집기 조합 개수')
# plt.show()

sample_space_size = sum(weighted_sample_space.values())
prob_x_10_flips = [value / sample_space_size for value in y_10_flips]
# plt.scatter(x_10_flips, prob_x_10_flips)
# plt.xlabel('앞면 개수')
# plt.ylabel('확률')
# plt.show()

assert sum(prob_x_10_flips) == 1.0

# plt.plot(x_10_flips, prob_x_10_flips)
# plt.scatter(x_10_flips, prob_x_10_flips)
# where = [is_in_interval(value, 8, 10) for value in x_10_flips]
# plt.fill_between(x_10_flips, prob_x_10_flips, where=where)
# plt.xlabel('앞면 개수')
# plt.ylabel('확률')
# plt.show()

plt.plot(x_10_flips, prob_x_10_flips)
plt.scatter(x_10_flips, prob_x_10_flips)
where = [not is_in_interval(value, 3, 7) for value in x_10_flips]
plt.fill_between(x_10_flips, prob_x_10_flips, where=where)
plt.xlabel('앞면 개수')
plt.ylabel('확률')
plt.show()