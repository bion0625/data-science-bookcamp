import numpy as np
print("동전을 한 번 뒤집어 봅시다")
coin_flip = np.random.binomial(1, 0.7)
print(f"편향된 동전은 {'앞면' if coin_flip == 1 else '뒷면'}으로 떨어졌습니다")

print("\n동전을 10번 뒤집어 봅니다")
number_coin_flips = 10
head_count = np.random.binomial(number_coin_flips, 0.7)
print(f"{number_coin_flips}번의 편향된 동전 뒤집기 중 앞면은 "
      f"{head_count}번 관측되었습니다")

np.random.seed(0)
head_count = np.random.binomial(1000, 0.7)
frequency = head_count / 1000
print(f"동전의 앞면이 관측된 빈도는 {frequency}입니다")

np.random.seed(0)
assert np.random.binomial(1000, 0.7) / 1000 == 0.697
for i in range(1, 6):
    head_count = np.random.binomial(1000, 0.7)
    frequency = head_count / 1000
    print(f"{i}번째 반복에서의 빈도는 {frequency}입니다")
    if frequency == 0.7:
        print("빈도와 실제 확률이 일치합니다!\n")