import random

answers_good = ['Бесспорно', 'Предрешено', 'Никаких сомнений', 'Определённо да', 'Можешь быть уверен в этом']
answers_smallgood = ['Мне кажется - да', 'Вероятнее всего', 'Хорошие перспективы', 'Знаки говорят - да', 'Да']
answers_neutral = ['Пока неясно, попробуй снова', 'Спроси позже', 'Лучше не рассказывать', 'Сейчас нельзя предсказать', 'Сконцентрируйся и спроси опять']
answers_bad = ['Даже не думай', 'Мой ответ - нет', 'По моим данным - нет', 'Перспективы не очень хорошие', 'Весьма сомнительно']

answers_list = [answers_good, answers_smallgood, answers_neutral, answers_bad]

def choice(answers):
    return random.choice(answers)

print('Привет Мир, я магическая консоль, и я знаю ответ на любой вопрос.')
name = input('Назови себя: ')
print(f'Привет {name}!')

while True:
    question = input(f'{name}, задай свой вопрос, на который я смогу дать однозначный ответ: ')
    print(choice(choice(answers_list)))
    question_next = input(f'{name}, хочешь ли задать еще один вопрос? ')
    if question_next.lower() == 'да':
        continue
    elif question_next.lower() == 'нет':
        break
    else:
        print('ошибка')
        break