# Домашнее задание по теме "Декораторы" v2

def decorator(func):
    def mod(*args):
        mod_result = func(*args)
        if mod_result == 2:
            print('Простое')
        if isinstance(mod_result, int) and mod_result > 1:
            for i in range(2, mod_result):
                if mod_result % i == 0:
                    print('Составное')
                    break
                else:
                    print('Простое')
                    break
        else:
            print('Другое')
        return mod_result
    return mod



@decorator
def sum_three(*args):
    result_sum = sum(args)
    return result_sum

# Пример:
result = sum_three(2, 3, 6)
print(result)


