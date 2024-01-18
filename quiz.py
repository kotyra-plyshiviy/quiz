print("добро пожаловать в квиз по стартапам")
print("ответь на следуйшие вопросы: ")

questions= ["1. Как называется компания, которая создается для развития новой идеи или инновационного продукта?",
           "2. Как назвается человек или компания, который вкладывает деньги в бизнес с целью получения прибыли?",
           "3. Как называется капитал, который дают инвесторы на развитие стартапа?",
           "4. Как пишется минимально жизнеспособный продукт, который создается для тестирования идей и концепций?",
           "5. Какой план создают перед тем, как открывать стартап и занимать деньги?",
           "6. Как называются другие компании на рынке, которые предлагают аналогичные товары или услуги?",
           "7. Как называется разница между выручкой и затратами компании?"]
answers=["Стартап", "Инвестор", "Инвестиция", "MVP", "Бизнес-план", "Конкуренты", "Прибыль"]
score=0
print(questions[0])
user_input=input("ведите свой ответ: ")
if user_input.lower()==answers[0].lower():
    print("правельно")
    score=score+1
else:
    print("не правельно")

print(questions[1])
user_input=input("ведите свой ответ: ")
if user_input.lower()==answers[1].lower():
    print("правельно")
    score=score+1
else:
    print("не правельно")

print(questions[2])
user_input=input("ведите свой ответ: ")
if user_input.lower()==answers[2].lower():
    print("правельно")
    score=score+1
else:
    print("не правельно")

print(questions[3])
user_input=input("ведите свой ответ: ")
if user_input.lower()==answers[3].lower():
    print("правельно")
    score=score+1
else:
    print("не правельно")

print(questions[4])
user_input=input("ведите свой ответ: ")
if user_input.lower()==answers[4].lower():
    print("правельно")
    score=score+1
else:
    print("не правельно")

print(questions[5])
user_input=input("ведите свой ответ: ")
if user_input.lower()==answers[5].lower():
    print("правельно")
    score=score+1
else:
    print("не правельно")

print(questions[6])
user_input = input("ведите свой ответ: ")
if user_input.lower() == answers[6].lower():
    print("правельно")
    score=score+1
else:
    print("не правельно")

if score>5:
    print("Это отличный результат! Ты много знаешь о стартапах.")
elif score>3:
    print("Неплохой результат! Как здорово, что тебе предстоит узнать ещё так много о стартапах.")
else:score>0
print("Видимо, ты только начинаешь свой путь к стартапам! Ты ещё много чего узнаешь о мире, где мы живём.")