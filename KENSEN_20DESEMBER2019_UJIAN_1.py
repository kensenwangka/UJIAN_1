# Soal 1
def hashtag(string):
    hashtag = "".join(string.title().split())
    return [False, f"#{hashtag}"][bool(string and 0 < len(hashtag) <= 140)]
# print(hashtag("Helo there how are you doing"))
# print(hashtag(" "))


# Soal 2
def create_phone_number(n):
  return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)
# print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))


# Soal 3
def sort_odd_even(num):
    even = sorted(x for x in num if x % 2 == 0)
    odd = sorted((x for x in num if x % 2 != 0), reverse=True)
    return [(even if x % 2 == 0 else odd).pop() for x in num]
# print(sort_odd_even([5, 3, 2, 8, 1, 4]))

# Soal 4
# "Height" nya di ganti N aja ya biar cepet
def hollowTriangle(n):
    return ['_' * (n - i - 1) + '#' + '_' * (2 * i - 1) + '#' * (i >= 1) + '_' * (n - i - 1) \
    for i in range(n - 1)] + ['#' * (2 * n - 1)]
# print(hollowTriangle(6))

# gak ngerti gw wkwkwk jadi yaudah seadanya hehe
# selamat natal dan tahun baru 2020. semoga liburannya menyenangkan di Jogja. see you!





















































































# nyari apaan?