tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б', '9В']  # , '8Б', '10А', '10Б', '9А']


def check_gen(tutors: list, klasses: list):
    tutor_func = tutors
    klass_func = klasses
    if len(tutor_func) > len(klass_func):
        for i in range((len(tutor_func) - len(klass_func)), len(tutor_func)):
            klass_func.append('None')
    # реализация с yield
    # for i in range(len(tutor_func)):
    #     tuple_out = (tutor_func[i], klass_func[i])
    #     yield tuple_out
    # реализация с генераторным выражением
    tuple_out = ((tutor_func[i], klass_func[i]) for i in range(len(tutor_func)))
    return tuple_out


generator = check_gen(tutors, klasses)
# print(generator) дает результат <generator object check_gen.<locals>.<genexpr> at 0x000001A3BF945FC0>
for _ in range(len(tutors)):
    print(next(generator))
# next(generator)  # если раскомментировать, то должно падать в traceback по StopIteration

