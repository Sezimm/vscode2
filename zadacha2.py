def word_sum(a):
    c = 0
    for x in a:
        if ('a' <= x <= 'z') or ('A' <= x <= 'Z') or ('а' <= x <= 'я') or ('А' <= x <= 'Я'):
            c += 1
        else:
            pass
    print(c)

a = input()
word_sum(a)