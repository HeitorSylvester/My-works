value_a, value_b, value_c = map(float ,input().split())
bhascara_1 = (-value_b + (value_b ** 2)+(-4 * value_a * value_c)) ** 0.5
bhascara_2 = (-value_b - (value_b ** 2)+(-4 * value_a * value_c)) ** 0.5
print(bhascara_1,bhascara_2)