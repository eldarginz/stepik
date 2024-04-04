def ves_v_den(day, weight):
    plan = 100 - 0.2*day

    if weight <= plan:
        return ('Все идет по плану')
    if weight > plan:
        return ('Что-то пошло не так')


n = float(input())
w = float(input())

print(ves_v_den(n, w))
print(f'#{int(n)} ДЕНЬ: ТЕКУЩИЙ ВЕС = {w} кг, ЦЕЛЬ по ВЕСУ = {100 - 0.2*n} кг')
