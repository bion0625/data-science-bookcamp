import numpy as np

die_roll = np.random.randint(1, 7)
assert 1 <= die_roll <= 6

np.random.seed(0)
die_rolls = [np.random.randint(1, 7) for _ in range(3)]
assert die_rolls == [5, 6, 1]

np.random.seed(0)
coin_flip = np.random.randint(0, 2)
print(f"동전은 {'앞면' if coin_flip == 1 else '뒷면'}으로 떨어졌습니다")

np.random.seed(0)
def frequency_heads(coin_flip_sequence):
    total_heads = len([head for head in coin_flip_sequence if head == 1])
    return total_heads / len(coin_flip_sequence)

coin_flips = [np.random.randint(0, 2) for _ in range(10)]
freq_heads = frequency_heads(coin_flips)
print(f"동전 앞면이 관측된 빈도는 {freq_heads}입니다")

import matplotlib.pyplot as plt
from matplotlib import rc
# 한글 폰트 설정
rc('font', family='Malgun Gothic')  # Windows 기본 한글 폰트

np.random.seed(0)
coin_flips = []
frequencies = []
for _ in range(1000):
    coin_flips.append(np.random.randint(0, 2))
    frequencies.append(frequency_heads(coin_flips))

plt.plot(list(range(1000)), frequencies)
plt.axhline(0.5, color='k')
plt.xlabel('시행된 동전 뒤집기 횟수')
plt.ylabel('앞면이 관측된 빈도')
plt.show()