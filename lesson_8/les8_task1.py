# 1) Определение количества различных подстрок с использованием хеш-функции. Пусть на вход функции дана строка.
# Требуется вернуть количество различных подстрок в этой строке. Примечание: в сумму не включаем пустую строку и строку целиком.
import hashlib


def count_subs(s):
    count = []
    for i in range(len(s)):
        temp = hashlib.sha1(s[i].encode('utf-8')).hexdigest()
        if temp and temp not in count:
            count.append(temp)
            new_sub = s[i]
            for j in range(i + 1, len(s)):
                new_sub += s[j]
                temp = hashlib.sha1(new_sub.encode('utf-8')).hexdigest()
                if temp and temp not in count:
                    count.append(temp)
    return len(count) - 1


print(count_subs("sova"))
