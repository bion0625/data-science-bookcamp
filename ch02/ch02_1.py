import matplotlib.pyplot as plt
from ch01.ch01_3_0 import is_in_interval

x = range(0, 10)
y = [2*value for value in x]
# plt.plot(x, y)
# plt.show()

# plt.scatter(x, y)
# plt.show()

# plt.plot(x, y)
where = [is_in_interval(value, 2, 6) for value in x]
# plt.fill_between(x, y, where=where)
# plt.show()

# plt.scatter(x, y)
# plt.plot(x, y)
# plt.fill_between(x, y, where=where)
# plt.show()


import matplotlib
# 한글 폰트 설정
matplotlib.rcParams['font.family'] = 'NanumGothic'  # 또는 'Malgun Gothic' 등 시스템에 따라 선택
matplotlib.rcParams['axes.unicode_minus'] = False  # 마이너스 기호 깨짐 방지

plt.plot(x, y)
plt.xlabel('0부터 10 사이의 값')
plt.ylabel('x 값의 두 배')
plt.show()