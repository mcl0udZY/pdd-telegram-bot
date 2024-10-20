import telebot
import webbrowser
from telebot import types

bot = telebot.TeleBot('8188856331:AAEClLW5DNEWunRcwZuYNACG8131U6U1do0', parse_mode='HTML')


@bot.message_handler(commands=['start'])
def start(message):
    knop = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('🤠 Начать тест')
    knop.add(btn1)
    bot.send_message(message.chat.id, 'Данный бот поможет тебе подглядеть правильный вариант в билете экзамена!\n<b>*Правильный ответ подчеркнут</b>', reply_markup=knop)
    bot.register_next_step_handler(message, on_click)


def on_click(message):
    markups = types.InlineKeyboardMarkup()
    btns1 = types.InlineKeyboardButton('#1', callback_data='n1')
    btns2 = types.InlineKeyboardButton('#2', callback_data='n2')
    btns3 = types.InlineKeyboardButton('#3', callback_data='n3')
    btns4 = types.InlineKeyboardButton('#4', callback_data='n4')
    markups.row(btns1, btns2, btns3, btns4)
    if message.text == '🤠 Начать тест':
        bot.send_message(message.chat.id, 'Выберите номер билета:', reply_markup=markups)


@bot.callback_query_handler(func=lambda callback: callback.data == 'n1')
def callback_message(callback):
    markup = types.InlineKeyboardMarkup()
    next = types.InlineKeyboardButton('2 воп.', callback_data='q_1_2')
    markup.add(next)
    bot.send_message(callback.message.chat.id, "Вопрос 1 Билет 1.\n"
                                               "В каком случае водитель совершит вынужденную остановку?\n\n"
                                               "1.Остановившись непосредственно перед пешеходным переходом, чтобы уступить дорогу пешеходу.\n"
                                               "<u>2.Остановившись на проезжей части из-за технической неисправности транспортного средства.</u>\n"
                                               "3. В обоих перечисленных случаях.", reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: callback.data == 'q_1_2')
def callback_message(callback):
    markup = types.InlineKeyboardMarkup()
    next = types.InlineKeyboardButton('3 воп.', callback_data='q_1_3')
    markup.add(next)
    bot.send_photo(callback.message.chat.id, open('n1_2.jpg', 'rb'))
    bot.send_message(callback.message.chat.id, "Вопрос 2 Билет 1.\n"
                                               "Разрешен ли Вам съезд на дорогу с грунтовым покрытием?\n\n"
                                               "<u>1. Разрешен.</u>\n"
                                               "2. Разрешен только при технической неисправности транспортного средства.\n"
                                               "3. Запрещен.", reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: callback.data == 'q_1_3')
def callback_message(callback):
    markup = types.InlineKeyboardMarkup()
    next = types.InlineKeyboardButton('4 воп.', callback_data='q_1_4')
    markup.add(next)
    bot.send_photo(callback.message.chat.id, open('n1_3.jpg', 'rb'))
    bot.send_message(callback.message.chat.id, "Вопрос 3 Билет 1.\n"
                                               "Можно ли Вам остановиться в указанном месте для посадки пассажира?\n\n"
                                               "<u>1. Можно.</u>\n"
                                               "2. Можно, если Вы управляете такси.\n"
                                               "3. Нельзя.", reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: callback.data == 'q_1_4')
def callback_message(callback):
    markup = types.InlineKeyboardMarkup()
    next = types.InlineKeyboardButton('5 воп.', callback_data='q_1_5')
    markup.add(next)
    bot.send_photo(callback.message.chat.id, open('n1_4.jpg', 'rb'))
    bot.send_message(callback.message.chat.id, "Вопрос 4 Билет 1.\n"
                                               "Какие из указанных знаков запрещают движение водителям мопедов?\n\n"
                                               "1. Только А.\n"
                                               "2. Только Б.\n"
                                               "3. В и Г.\n"
                                               "<u>4. Все.</u>", reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: callback.data == 'q_1_5')
def callback_message(callback):
    markup = types.InlineKeyboardMarkup()
    next = types.InlineKeyboardButton('6 воп.', callback_data='q_1_6')
    markup.add(next)
    bot.send_photo(callback.message.chat.id, open('n1_5.jpg', 'rb'))
    bot.send_message(callback.message.chat.id, "Вопрос 5 Билет 1.\n"
                                               "Вы намерены повернуть налево. Где следует остановиться, чтобы уступить дорогу легковому автомобилю?\n\n"
                                               "1. Перед знаком.\n"
                                               "<u>2. Перед перекрестком у линии разметки.</u>\n"
                                               "3. На перекрестке перед прерывистой линией разметки.\n"
                                               "4. В любом месте по усмотрению водителя.", reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: callback.data == 'q_1_6')
def callback_message(callback):
    markup = types.InlineKeyboardMarkup()
    next = types.InlineKeyboardButton('7 воп.', callback_data='q_1_7')
    markup.add(next)
    bot.send_message(callback.message.chat.id, "Вопрос 6 Билет 1.\n"
                                               "Что означает мигание зеленого сигнала светофора?\n\n"
                                               "1. Предупреждает о неисправности светофора.\n"
                                               "<u>2. Разрешает движение и информирует о том, что вскоре будет включен запрещающий сигнал.</u>\n"
                                               "3. Запрещает дальнейшее движение.\n", reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: callback.data == 'q_1_7')
def callback_message(callback):
    markup = types.InlineKeyboardMarkup()
    next = types.InlineKeyboardButton('8 воп.', callback_data='q_1_8')
    markup.add(next)
    bot.send_message(callback.message.chat.id, "Вопрос 7 Билет 1.\n"
                                               "Водитель обязан подавать сигналы световыми указателями поворота (рукой):\n\n"
                                               "1. Перед началом движения или перестроением.\n"
                                               "2. Перед поворотом или разворотом.\n"
                                               "3. Перед остановкой.\n"
                                               "<u>4. Во всех перечисленных случаях.</u>", reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: callback.data == 'q_1_8')
def callback_message(callback):
    markup = types.InlineKeyboardMarkup()
    next = types.InlineKeyboardButton('9 воп.', callback_data='q_1_9')
    markup.add(next)
    bot.send_photo(callback.message.chat.id, open('n1_8.jpg', 'rb'))
    bot.send_message(callback.message.chat.id, "Вопрос 8 Билет 1.\n"
                                               "Как Вам следует поступить при повороте направо?\n\n"
                                               "1. Перестроиться на правую полосу, затем осуществить поворот.\n"
                                               "2. Продолжить движение по второй полосе до перекрестка, затем повернуть.\n"
                                               "<u>3. Возможны оба варианта действий.</u>\n", reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: callback.data == 'q_1_9')
def callback_message(callback):
    markup = types.InlineKeyboardMarkup()
    next = types.InlineKeyboardButton('10 воп.', callback_data='q_1_10')
    markup.add(next)
    bot.send_photo(callback.message.chat.id, open('n1_9.jpg', 'rb'))
    bot.send_message(callback.message.chat.id, "Вопрос 9 Билет 1.\n"
                                               "По какой траектории Вам разрешено выполнить разворот?\n\n"
                                               "<u>1. Только по А.</u>\n"
                                               "2. Только по Б.\n"
                                               "3. По любой из указанных.\n", reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: callback.data == 'q_1_10')
def callback_message(callback):
    markup = types.InlineKeyboardMarkup()
    next = types.InlineKeyboardButton('11 воп.', callback_data='q_1_11')
    markup.add(next)
    bot.send_photo(callback.message.chat.id, open('n1_10.jpg', 'rb'))
    bot.send_message(callback.message.chat.id, "Вопрос 10 Билет 1.\n"
                                               "С какой скоростью Вы можете продолжить движение вне населенного пункта по левой полосе на легковом автомобиле?\n\n"
                                               "1. Не более 50 км/ч.\n"
                                               "2. Не менее 50 км/ч и не более 70 км/ч.\n"
                                               "<u>3. Не менее 50 км/ч и не более 90 км/ч.</u>\n", reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: callback.data == 'q_1_11')
def callback_message(callback):
    markup = types.InlineKeyboardMarkup()
    next = types.InlineKeyboardButton('12 воп.', callback_data='q_1_12')
    markup.add(next)
    bot.send_photo(callback.message.chat.id, open('n1_11.jpg', 'rb'))
    bot.send_message(callback.message.chat.id, "Вопрос 11 Билет 1.\n"
                                               "Можно ли водителю легкового автомобиля выполнить опережение грузовых автомобилей вне населенного пункта по такой траектории?\n\n"
                                               "<u>1. Можно.</u>\n"
                                               "2. Можно, если скорость грузовых автомобилей менее 30 км/ч.\n"
                                               "3. Нельзя.\n", reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: callback.data == 'q_1_12')
def callback_message(callback):
    markup = types.InlineKeyboardMarkup()
    next = types.InlineKeyboardButton('13 воп.', callback_data='q_1_13')
    markup.add(next)
    bot.send_photo(callback.message.chat.id, open('n1_12.jpg', 'rb'))
    bot.send_message(callback.message.chat.id, "Вопрос 12 Билет 1.\n"
                                               "В каком случае водителю разрешается поставить автомобиль на стоянку в указанном месте?\n\n"
                                               "1. Только если расстояние до сплошной линии разметки не менее 3 м.\n"
                                               "2. Только если расстояние до края пересекаемой проезжей части не менее 5 м.\n"
                                               "<u>3. При соблюдении обоих перечисленных условий.</u>", reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: callback.data == 'q_1_13')
def callback_message(callback):
    markup = types.InlineKeyboardMarkup()
    next = types.InlineKeyboardButton('14 воп.', callback_data='q_1_14')
    markup.add(next)
    bot.send_photo(callback.message.chat.id, open('n1_13.jpg', 'rb'))
    bot.send_message(callback.message.chat.id, "Вопрос 13 Билет 1.\n"
                                               "При повороте направо Вы должны уступить дорогу:\n\n"
                                               "1. Только велосипедисту.\n"
                                               "2. Только пешеходам.\n"
                                               "<u>3. Пешеходам и велосипедисту.</u>\n"
                                               "4. Никому.", reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: callback.data == 'q_1_14')
def callback_message(callback):
    markup = types.InlineKeyboardMarkup()
    next = types.InlineKeyboardButton('15 воп.', callback_data='q_1_15')
    markup.add(next)
    bot.send_photo(callback.message.chat.id, open('n1_14.jpg', 'rb'))
    bot.send_message(callback.message.chat.id, "Вопрос 14 Билет 1.\n"
                                               "Вы намерены проехать перекресток в прямом направлении. Кому Вы должны уступить дорогу?\n\n"
                                               "<u>1. Обоим трамваям.</u>\n"
                                               "2. Только трамваю А.\n"
                                               "3. Только трамваю Б.\n"
                                               "4. Никому.", reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: callback.data == 'q_1_15')
def callback_message(callback):
    markup = types.InlineKeyboardMarkup()
    next = types.InlineKeyboardButton('16 воп.', callback_data='q_1_16')
    markup.add(next)
    bot.send_photo(callback.message.chat.id, open('n1_15.jpg', 'rb'))
    bot.send_message(callback.message.chat.id, "Вопрос 15 Билет 1.\n"
                                               "Кому Вы обязаны уступить дорогу при повороте налево?\n\n"
                                               "1. Только автобусу.\n"
                                               "2. Только легковому автомобилю.\n"
                                               "<u>3. Никому.</u>\n", reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: callback.data == 'q_1_16')
def callback_message(callback):
    markup = types.InlineKeyboardMarkup()
    next = types.InlineKeyboardButton('17 воп.', callback_data='q_1_17')
    markup.add(next)
    bot.send_photo(callback.message.chat.id, open('n1_16.jpg', 'rb'))
    bot.send_message(callback.message.chat.id, "Вопрос 16 Билет 1.\n"
                                               "С какой максимальной скоростью можно продолжить движение за знаком?\n\n"
                                               "1. 60 км/ч.\n"
                                               "2. 50 км/ч.\n"
                                               "3. 30 км/ч.\n"
                                               "<u>4. 20 км/ч</u>", reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: callback.data == 'q_1_17')
def callback_message(callback):
    markup = types.InlineKeyboardMarkup()
    next = types.InlineKeyboardButton('18 воп.', callback_data='q_1_18')
    markup.add(next)
    bot.send_message(callback.message.chat.id, "Вопрос 17 Билет 1.\n"
                                               "Для перевозки людей на мотоцикле водитель должен иметь водительское удостоверение на право управления транспортными средствами:\n\n"
                                               "1. Категории «A» или подкатегории «A1».\n"
                                               "2. Любой категории или подкатегории в течение 2 и более лет.\n"
                                               "<u>3. Только категории «A» или подкатегории «A1» в течение 2 и более лет.</u>\n", reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: callback.data == 'q_1_18')
def callback_message(callback):
    markup = types.InlineKeyboardMarkup()
    next = types.InlineKeyboardButton('19 воп.', callback_data='q_1_19')
    markup.add(next)
    bot.send_message(callback.message.chat.id, "Вопрос 18 Билет 1.\n"
                                               "При какой неисправности разрешается эксплуатация транспортного средства?\n\n"
                                               "1. Не работают запорные устройства топливных баков.\n"
                                               "2. Не работают механизм регулировки и фиксирующее устройство сиденья водителя.\n"
                                               "3. Не работает устройство обдува ветрового стекла.\n"
                                               "<u>4. Не работает стеклоподъемник.</u>", reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: callback.data == 'q_1_19')
def callback_message(callback):
    markup = types.InlineKeyboardMarkup()
    next = types.InlineKeyboardButton('20 воп.', callback_data='q_1_20')
    markup.add(next)
    bot.send_message(callback.message.chat.id, "Вопрос 19 Билет 1.\n"
                                               "В случае, когда правые колеса автомобиля наезжают на неукрепленную влажную обочину, рекомендуется:\n\n"
                                               "1. Затормозить и полностью остановиться.\n"
                                               "2. Затормозить и плавно направить автомобиль на проезжую часть.\n"
                                               "<u>3. Не прибегая к торможению, плавно направить автомобиль на проезжую часть.</u>\n", reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: callback.data == 'q_1_20')
def callback_message(callback):
    bot.send_message(callback.message.chat.id, "Вопрос 20 Билет 1.\n"
                                               "Что понимается под временем реакции водителя?\n\n"
                                               "1. Время с момента обнаружения водителем опасности до полной остановки транспортного средства.\n"
                                               "<u>2. Время с момента обнаружения водителем опасности до начала принятия мер по ее избежанию.</u>\n"
                                               "3. Время, необходимое для переноса ноги с педали управления подачей топлива на педаль тормоза.\n")
    bot.send_message(callback.message.chat.id, '/start - Нажмите, чтобы вернуться к выбору билета')


@bot.callback_query_handler(func=lambda callback: callback.data == 'n2')
def callback_message(callback):
    markup = types.InlineKeyboardMarkup()
    next = types.InlineKeyboardButton('2 воп.', callback_data='q_2_2')
    markup.add(next)
    bot.send_photo(callback.message.chat.id, open('n2_1.jpg', 'rb'))
    bot.send_message(callback.message.chat.id, "Вопрос 1 Билет 2.\n"
                                               "Сколько полос для движения имеет данная дорога?\n\n"
                                               "1. Две.\n"
                                               "<u>2. Четыре.</u>\n"
                                               "3. Пять.\n", reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: callback.data == 'q_2_2')
def callback_message(callback):
    markup = types.InlineKeyboardMarkup()
    next = types.InlineKeyboardButton('3 воп.', callback_data='q_2_3')
    markup.add(next)
    bot.send_photo(callback.message.chat.id, open('n2_2.jpg', 'rb'))
    bot.send_message(callback.message.chat.id, "Вопрос 2 Билет 2.\n"
                                               "Можно ли Вам въехать на мост первым?\n\n"
                                               "<u>1. Можно.</u>\n"
                                               "2. Можно, если Вы не затрудните движение встречному автомобилю.\n"
                                               "3. Нельзя.\n", reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: callback.data == 'q_2_3')
def callback_message(callback):
    markup = types.InlineKeyboardMarkup()
    next = types.InlineKeyboardButton('4 воп.', callback_data='q_2_4')
    markup.add(next)
    bot.send_photo(callback.message.chat.id, open('n2_3.jpg', 'rb'))
    bot.send_message(callback.message.chat.id, "Вопрос 3 Билет 2.\n"
                                               "Разрешено ли Вам произвести остановку для посадки пассажира?\n\n"
                                               "<u>1. Разрешено.</u>\n"
                                               "2. Разрешено только по четным числам месяца.\n"
                                               "3. Разрешено только по нечетным числам месяца.\n"
                                               "4. Запрещено.", reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: callback.data == 'q_2_4')
def callback_message(callback):
    markup = types.InlineKeyboardMarkup()
    next = types.InlineKeyboardButton('5 воп.', callback_data='q_2_5')
    markup.add(next)
    bot.send_photo(callback.message.chat.id, open('n2_4.jpg', 'rb'))
    bot.send_message(callback.message.chat.id, "Вопрос 4 Билет 2.\n"
                                               "Что запрещено в зоне действия этого знака?\n\n"
                                               "1. Движение любых транспортных средств.\n"
                                               "2. Движение всех транспортных средств со скоростью не более 20 км/ч.\n"
                                               "<u>3. Движение механических транспортных средств.</u>\n", reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: callback.data == 'q_2_5')
def callback_message(callback):
    markup = types.InlineKeyboardMarkup()
    next = types.InlineKeyboardButton('6 воп.', callback_data='q_2_6')
    markup.add(next)
    bot.send_photo(callback.message.chat.id, open('n2_5.jpg', 'rb'))
    bot.send_message(callback.message.chat.id, "Вопрос 5 Билет 2.\n"
                                               "Разрешен ли Вам выезд на полосу с реверсивным движением, если реверсивный светофор выключен?\n\n"
                                               "1. Разрешен.\n"
                                               "2. Разрешен, если скорость автобуса менее 30 км/ч.\n"
                                               "<u>3. Запрещен.</u>\n", reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: callback.data == 'q_2_6')
def callback_message(callback):
    markup = types.InlineKeyboardMarkup()
    next = types.InlineKeyboardButton('7 воп.', callback_data='q_2_7')
    markup.add(next)
    bot.send_photo(callback.message.chat.id, open('n2_6.jpg', 'rb'))
    bot.send_message(callback.message.chat.id, "Вопрос 6 Билет 2.\n"
                                               "Информационная световая секция в виде силуэта пешехода и стрелки с мигающим сигналом белолунного цвета, расположенная под светофором, информирует водителя о том, что:\n\n"
                                               "<u>1. На пешеходном переходе, в направлении которого он поворачивает, включен сигнал светофора, разрешающий движение пешеходам</u>\n"
                                               "2. На пешеходном переходе, в направлении которого он поворачивает, включен сигнал светофора, запрещающий движение пешеходам.\n"
                                               "3. Он поворачивает в направлении пешеходного перехода.", reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: callback.data == 'q_2_7')
def callback_message(callback):
    markup = types.InlineKeyboardMarkup()
    next = types.InlineKeyboardButton('8 воп.', callback_data='q_2_8')
    markup.add(next)
    bot.send_photo(callback.message.chat.id, open('n2_7.jpg', 'rb'))
    bot.send_message(callback.message.chat.id, "Вопрос 7 Билет 2.\n"
                                               "Поднятая вверх рука водителя легкового автомобиля является сигналом, информирующим Вас о его намерении:\n\n"
                                               "1. Повернуть направо.\n"
                                               "2. Продолжить движение прямо.\n"
                                               "<u>3. Снизить скорость, чтобы остановиться и уступить дорогу мотоциклу.</u>", reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: callback.data == 'q_2_8')
def callback_message(callback):
    markup = types.InlineKeyboardMarkup()
    next = types.InlineKeyboardButton('9 воп.', callback_data='q_2_9')
    markup.add(next)
    bot.send_photo(callback.message.chat.id, open('n2_8.jpg', 'rb'))
    bot.send_message(callback.message.chat.id, "Вопрос 8 Билет 2.\n"
                                               "Двигаясь по левой полосе, водитель намерен перестроиться на правую. На каком из рисунков показана ситуация, в которой он обязан уступить дорогу?\n\n"
                                               "1. На левом.\n"
                                               "2. На правом.\n"
                                               "<u>3. На обоих.</u>", reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: callback.data == 'q_2_9')
def callback_message(callback):
    markup = types.InlineKeyboardMarkup()
    next = types.InlineKeyboardButton('10 воп.', callback_data='q_2_10')
    markup.add(next)
    bot.send_photo(callback.message.chat.id, open('n2_9.jpg', 'rb'))
    bot.send_message(callback.message.chat.id, "Вопрос 9 Билет 2.\n"
                                               "Можно ли Вам выполнить разворот в этом месте?\n\n"
                                               "<u>1. Можно.</u>\n"
                                               "2. Можно только при отсутствии приближающегося поезда.\n"
                                               "3. Нельзя.", reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: callback.data == 'q_2_10')
def callback_message(callback):
    markup = types.InlineKeyboardMarkup()
    next = types.InlineKeyboardButton('11 воп.', callback_data='q_2_11')
    markup.add(next)
    bot.send_message(callback.message.chat.id, "Вопрос 10 Билет 2.\n"
                                               "В каких случаях разрешается наезжать на прерывистые линии разметки, разделяющие проезжую часть на полосы движения?\n\n"
                                               "1. Только если на дороге нет других транспортных средств.\n"
                                               "2. Только при движении в темное время суток.\n"
                                               "<u>3. Только при перестроении.</u>\n"
                                               "4. Во всех перечисленных случаях.", reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: callback.data == 'q_2_11')
def callback_message(callback):
    markup = types.InlineKeyboardMarkup()
    next = types.InlineKeyboardButton('12 воп.', callback_data='q_2_12')
    markup.add(next)
    bot.send_photo(callback.message.chat.id, open('n2_11.jpg', 'rb'))
    bot.send_message(callback.message.chat.id, "Вопрос 11 Билет 2.\n"
                                               "Разрешено ли Вам обогнать мотоцикл?\n\n"
                                               "1. Разрешено.\n"
                                               "2. Разрешено, если водитель мотоцикла снизил скорость.\n"
                                               "<u>3. Запрещено.</u>\n", reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: callback.data == 'q_2_12')
def callback_message(callback):
    markup = types.InlineKeyboardMarkup()
    next = types.InlineKeyboardButton('13 воп.', callback_data='q_2_13')
    markup.add(next)
    bot.send_photo(callback.message.chat.id, open('n2_12.jpg', 'rb'))
    bot.send_message(callback.message.chat.id, "Вопрос 12 Билет 2.\n"
                                               "Разрешается ли Вам остановиться в указанном месте?\n\n"
                                               "1. Разрешается.\n"
                                               "<u>2. Разрешается, если автомобиль будет находиться не ближе 5 м от края пересекаемой проезжей части.</u>\n"
                                               "3. Запрещается.\n", reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: callback.data == 'q_2_13')
def callback_message(callback):
    markup = types.InlineKeyboardMarkup()
    next = types.InlineKeyboardButton('14 воп.', callback_data='q_2_14')
    markup.add(next)
    bot.send_photo(callback.message.chat.id, open('n2_13.jpg', 'rb'))
    bot.send_message(callback.message.chat.id, "Вопрос 13 Билет 2.\n"
                                               "Вы намерены повернуть налево. Кому Вы должны уступить дорогу?\n\n"
                                               "1. Только пешеходам.\n"
                                               "2. Только автобусу.\n"
                                               "<u>3. Автобусу и пешеходам.</u>\n", reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: callback.data == 'q_2_14')
def callback_message(callback):
    markup = types.InlineKeyboardMarkup()
    next = types.InlineKeyboardButton('15 воп.', callback_data='q_2_15')
    markup.add(next)
    bot.send_photo(callback.message.chat.id, open('n2_14.jpg', 'rb'))
    bot.send_message(callback.message.chat.id, "Вопрос 14 Билет 2.\n"
                                               "В каком случае Вы имеете преимущество?\n\n"
                                               "1. Только при повороте направо.\n"
                                               "2. Только при повороте налево.\n"
                                               "<u>3. В обоих перечисленных случаях.</u>\n", reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: callback.data == 'q_2_15')
def callback_message(callback):
    markup = types.InlineKeyboardMarkup()
    next = types.InlineKeyboardButton('16 воп.', callback_data='q_2_16')
    markup.add(next)
    bot.send_photo(callback.message.chat.id, open('n2_15.jpg', 'rb'))
    bot.send_message(callback.message.chat.id, "Вопрос 15 Билет 2.\n"
                                               "Обязан ли водитель мотоцикла уступить Вам дорогу?\n\n"
                                               "<u>1. Обязан.</u>\n"
                                               "2. Не обязан.\n", reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: callback.data == 'q_2_16')
def callback_message(callback):
    markup = types.InlineKeyboardMarkup()
    next = types.InlineKeyboardButton('17 воп.', callback_data='q_2_17')
    markup.add(next)
    bot.send_photo(callback.message.chat.id, open('n2_16.jpg', 'rb'))
    bot.send_message(callback.message.chat.id, "Вопрос 16 Билет 2.\n"
                                               "Разрешается ли водителю выполнить объезд грузового автомобиля?\n\n"
                                               "1. Разрешается.\n"
                                               "2. Разрешается, если между шлагбаумом и остановившимся грузовым автомобилем расстояние более 5 м.\n"
                                               "<u>3. Запрещается.</u>", reply_markup=markup)

@bot.callback_query_handler(func=lambda callback: callback.data == 'q_2_17')
def callback_message(callback):
    markup = types.InlineKeyboardMarkup()
    next = types.InlineKeyboardButton('18 воп.', callback_data='q_2_18')
    markup.add(next)
    bot.send_message(callback.message.chat.id, "Вопрос 17 Билет 2.\n"
                                               "В каких из перечисленных случаев запрещена буксировка на гибкой сцепке?\n\n"
                                               "1. Только на горных дорогах.\n"
                                               "<u>2. Только в гололедицу.</u>\n"
                                               "3. Только в темное время суток и в условиях недостаточной видимости.\n"
                                               "4. Во всех перечисленных случаях.", reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: callback.data == 'q_2_18')
def callback_message(callback):
    markup = types.InlineKeyboardMarkup()
    next = types.InlineKeyboardButton('19 воп.', callback_data='q_2_19')
    markup.add(next)
    bot.send_message(callback.message.chat.id, "Вопрос 18 Билет 2.\n"
                                               "Запрещается эксплуатация мототранспортных средств (категории L), если остаточная глубина рисунка протектора шин (при отсутствии индикаторов износа) составляет не более:\n\n"
                                               "<u>1. 0,8 мм.</u>\n"
                                               "2. 1,0 мм.\n"
                                               "3. 1,6 мм.\n"
                                               "4. 2,0 мм.", reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: callback.data == 'q_2_19')
def callback_message(callback):
    markup = types.InlineKeyboardMarkup()
    next = types.InlineKeyboardButton('20 воп.', callback_data='q_2_20')
    markup.add(next)
    bot.send_message(callback.message.chat.id, "Вопрос 19 Билет 2.\n"
                                               "Исключает ли антиблокировочная тормозная система возможность возникновения заноса или сноса при прохождении поворота?\n\n"
                                               "1. Полностью исключает возможность возникновения только заноса.\n"
                                               "2. Полностью исключает возможность возникновения только сноса.\n"
                                               "<u>3. Не исключает возможность возникновения сноса или заноса.</u>", reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: callback.data == 'q_2_20')
def callback_message(callback):
    bot.send_message(callback.message.chat.id, "Вопрос 20 Билет 2.\n"
                                               "В каких случаях следует начинать сердечно-легочную реанимацию пострадавшего?\n\n"
                                               "1. При наличии болей в области сердца и затрудненного дыхания.\n"
                                               "2. При отсутствии у пострадавшего сознания, независимо от наличия дыхания.\n"
                                               "<u>3. При отсутствии у пострадавшего сознания, дыхания и кровообращения.</u>")
    bot.send_message(callback.message.chat.id, '/start - Нажмите, чтобы вернуться к выбору билета')

@bot.callback_query_handler(func=lambda callback: callback.data == 'n3')
def callback_message(callback):
    markup = types.InlineKeyboardMarkup()
    next = types.InlineKeyboardButton('2 воп.', callback_data='q_3_2')
    markup.add(next)
    bot.send_photo(callback.message.chat.id, open('n3_1.jpg', 'rb'))
    bot.send_message(callback.message.chat.id, "Вопрос 1 Билет 3.\n"
                                               "Выезжая с грунтовой дороги на перекресток, Вы попадаете:\n\n"
                                               "<u>1. На главную дорогу.</u>\n"
                                               "2. На равнозначную дорогу, поскольку отсутствуют знаки приоритета.\n"
                                               "3. На равнозначную дорогу, поскольку проезжая часть имеет твердое покрытие перед перекрестком.", reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: callback.data == 'q_3_2')
def callback_message(callback):
    markup = types.InlineKeyboardMarkup()
    next = types.InlineKeyboardButton('3 воп.', callback_data='q_3_3')
    markup.add(next)
    bot.send_photo(callback.message.chat.id, open('n3_2.jpg', 'rb'))
    bot.send_message(callback.message.chat.id, "Вопрос 2 Билет 3.\n"
                                               "Где Вы должны остановиться?\n\n"
                                               "1. Перед знаком (А).\n"
                                               "2. Перед перекрестком (Б).\n"
                                               "<u>3. Перед краем пересекаемой проезжей части (В).</u>", reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: callback.data == 'q_3_3')
def callback_message(callback):
    markup = types.InlineKeyboardMarkup()
    next = types.InlineKeyboardButton('4 воп.', callback_data='q_3_4')
    markup.add(next)
    bot.send_photo(callback.message.chat.id, open('n3_3.jpg', 'rb'))
    bot.send_message(callback.message.chat.id, "Вопрос 3 Билет 3.\n"
                                               "Вам необходимо двигаться со скоростью не более 40 км/ч:\n\n"
                                               "1. Только во время дождя.\n"
                                               "2. Во время выпадения осадков (дождя, града, снега).\n"
                                               "<u>3. Во всех случаях, когда покрытие проезжей части влажное.</u>", reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: callback.data == 'q_3_4')
def callback_message(callback):
    markup = types.InlineKeyboardMarkup()
    next = types.InlineKeyboardButton('5 воп.', callback_data='q_3_5')
    markup.add(next)
    bot.send_photo(callback.message.chat.id, open('n3_4.jpg', 'rb'))
    bot.send_message(callback.message.chat.id, "Вопрос 3 Билет 4.\n"
                                               "Какой из указанных знаков устанавливается в начале дороги с односторонним движением?\n\n"
                                               "1. Только А.\n"
                                               "<u>2. Только Б.</u>\n"
                                               "3. Б или Г."
                                               "4. Б или В.", reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: callback.data == 'q_3_5')
def callback_message(callback):
    markup = types.InlineKeyboardMarkup()
    next = types.InlineKeyboardButton('6 воп.', callback_data='q_3_6')
    markup.add(next)
    bot.send_photo(callback.message.chat.id, open('n3_5.jpg', 'rb'))
    bot.send_message(callback.message.chat.id, "Вопрос 3 Билет 5.\n"
                                               "Можно ли Вам остановиться в этом месте для посадки или высадки пассажиров?\n\n"
                                               "1. Можно.\n"
                                               "<u>2. Можно, если при этом не будут созданы помехи движению маршрутных транспортных средств.</u>\n"
                                               "3. Нельзя.", reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: callback.data == 'q_3_6')
def callback_message(callback):
    markup = types.InlineKeyboardMarkup()
    next = types.InlineKeyboardButton('7 воп.', callback_data='q_3_7')
    markup.add(next)
    bot.send_photo(callback.message.chat.id, open('n3_6.jpg', 'rb'))
    bot.send_message(callback.message.chat.id, "Вопрос 3 Билет 6.\n"
                                               "При повороте направо Вы:\n\n"
                                               "1. Имеете право проехать перекресток первым.\n"
                                               "2. Должны уступить дорогу только пешеходам.\n"
                                               "<u>3. Должны уступить дорогу автомобилю с включенными проблесковым маячком и специальным звуковым сигналом, а также пешеходам.</u>", reply_markup=markup)



@bot.callback_query_handler(func=lambda callback: callback.data == 'q_3_7')
def callback_message(callback):
    markup = types.InlineKeyboardMarkup()
    next = types.InlineKeyboardButton('8 воп.', callback_data='q_3_8')
    markup.add(next)
    bot.send_message(callback.message.chat.id, "Вопрос 3 Билет 7.\n"
                                               "В каких случаях водитель не должен подавать сигнал указателями поворота?\n\n"
                                               "1. Только при отсутствии на дороге других участников движения.\n"
                                               "<u>2. Только если сигнал может ввести в заблуждение других участников движения.</u>\n"
                                               "3. В обоих перечисленных случаях.", reply_markup=markup)

@bot.callback_query_handler(func=lambda callback: callback.data == 'q_3_8')
def callback_message(callback):
    markup = types.InlineKeyboardMarkup()
    next = types.InlineKeyboardButton('9 воп.', callback_data='q_3_9')
    markup.add(next)
    bot.send_photo(callback.message.chat.id, open('n3_8.jpg', 'rb'))
    bot.send_message(callback.message.chat.id, "Вопрос 3 Билет 8.\n"
                                               "Вам разрешено выполнить поворот направо:\n\n"
                                               "<u>1. Только по траектории А.</u>\n"
                                               "2. Только по траектории Б.\n"
                                               "3. По любой траектории из указанных.", reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: callback.data == 'q_3_9')
def callback_message(callback):
    markup = types.InlineKeyboardMarkup()
    next = types.InlineKeyboardButton('10 воп.', callback_data='q_3_10')
    markup.add(next)
    bot.send_photo(callback.message.chat.id, open('n3_9.jpg', 'rb'))
    bot.send_message(callback.message.chat.id, "Вопрос 3 Билет 9.\n"
                                               "Разрешается ли Вам выполнить разворот на перекрестке по указанной траектории?\n\n"
                                               "1. Разрешается.\n"
                                               "2. Разрешается, если видимость дороги не менее 100 м.\n"
                                               "<u>3. Запрещается.</u>", reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: callback.data == 'q_3_10')
def callback_message(callback):
    markup = types.InlineKeyboardMarkup()
    next = types.InlineKeyboardButton('11 воп.', callback_data='q_3_11')
    markup.add(next)
    bot.send_photo(callback.message.chat.id, open('n3_10.jpg', 'rb'))
    bot.send_message(callback.message.chat.id, "Вопрос 3 Билет 10.\n"
                                               "По какой полосе Вы имеете право двигаться с максимально разрешенной скоростью вне населенных пунктов?\n\n"
                                               "<u>1. Только по правой.</u>\n"
                                               "2. Только по левой.\n"
                                               "3. По любой.", reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: callback.data == 'q_3_11')
def callback_message(callback):
    markup = types.InlineKeyboardMarkup()
    next = types.InlineKeyboardButton('12 воп.', callback_data='q_3_12')
    markup.add(next)
    bot.send_message(callback.message.chat.id, "Вопрос 3 Билет 11.\n"
                                               "В каком случае водитель может начать обгон, если такой маневр на данном участке дороги не запрещен?\n\n"
                                               "1. Только если полоса, предназначенная для встречного движения, свободна на достаточном для обгона расстоянии.\n"
                                               "2. Только если его транспортное средство никто не обгоняет.\n"
                                               "<u>3. В случае, если выполнены оба условия.</u>", reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: callback.data == 'q_3_12')
def callback_message(callback):
    markup = types.InlineKeyboardMarkup()
    next = types.InlineKeyboardButton('13 воп.', callback_data='q_3_13')
    markup.add(next)
    bot.send_photo(callback.message.chat.id, open('n3_12.jpg', 'rb'))
    bot.send_message(callback.message.chat.id, "Вопрос 3 Билет 12.\n"
                                               "Кто из водителей нарушил правила стоянки?\n\n"
                                               "1. Оба.\n"
                                               "<u>2. Только водитель автомобиля.</u>\n"
                                               "3. Только водитель мотоцикла.", reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: callback.data == 'q_3_13')
def callback_message(callback):
    markup = types.InlineKeyboardMarkup()
    next = types.InlineKeyboardButton('14 воп.', callback_data='q_3_14')
    markup.add(next)
    bot.send_photo(callback.message.chat.id, open('n3_13.jpg', 'rb'))
    bot.send_message(callback.message.chat.id, "Вопрос 3 Билет 13.\n"
                                               "При движении прямо Вы:\n\n"
                                               "1. Должны остановиться перед стоп-линией.\n"
                                               "<u>2. Можете продолжить движение через перекресток без остановки.</u>\n"
                                               "3. Должны уступить дорогу транспортным средствам, движущимся с других направлений.", reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: callback.data == 'q_3_14')
def callback_message(callback):
    markup = types.InlineKeyboardMarkup()
    next = types.InlineKeyboardButton('15 воп.', callback_data='q_3_15')
    markup.add(next)
    bot.send_photo(callback.message.chat.id, open('n3_14.jpg', 'rb'))
    bot.send_message(callback.message.chat.id, "Вопрос 3 Билет 14.\n"
                                               "Вы намерены повернуть направо. Ваши действия?\n\n"
                                               "1. Уступите дорогу легковому автомобилю.\n"
                                               "<u>2. Проедете перекресток первым.</u>\n"
                                               "3. Уступите дорогу обоим транспортным средствам.", reply_markup=markup)

@bot.callback_query_handler(func=lambda callback: callback.data == 'q_3_15')
def callback_message(callback):
    markup = types.InlineKeyboardMarkup()
    next = types.InlineKeyboardButton('16 воп.', callback_data='q_3_16')
    markup.add(next)
    bot.send_photo(callback.message.chat.id, open('n3_15.jpg', 'rb'))
    bot.send_message(callback.message.chat.id, "Вопрос 3 Билет 15.\n"
                                               "Кому Вы обязаны уступить дорогу при повороте налево?\n\n"
                                               "1. Трамваям А и Б.\n"
                                               "2. Трамваю А и легковому автомобилю.\n"
                                               "<u>3. Только трамваю А.</u>\n"
                                               "4. Никому.", reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: callback.data == 'q_3_16')
def callback_message(callback):
    markup = types.InlineKeyboardMarkup()
    next = types.InlineKeyboardButton('17 воп.', callback_data='q_3_17')
    markup.add(next)
    bot.send_photo(callback.message.chat.id, open('n3_16.jpg', 'rb'))
    bot.send_message(callback.message.chat.id, "Вопрос 3 Билет 16.\n"
                                               "Кто из водителей нарушил правила остановки?\n\n"
                                               "1. Только водитель легкового автомобиля.\n"
                                               "2. Только водитель грузового автомобиля.\n"
                                               "<u>3. Оба.</u>", reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: callback.data == 'q_3_17')
def callback_message(callback):
    markup = types.InlineKeyboardMarkup()
    next = types.InlineKeyboardButton('18 воп.', callback_data='q_3_18')
    markup.add(next)
    bot.send_message(callback.message.chat.id, "Вопрос 3 Билет 17.\n"
                                               "Какое оборудование должно иметь механическое транспортное средство, используемое для обучения вождению?\n\n"
                                               "1. Дополнительные педали привода сцепления (кроме транспортных средств с автоматической трансмиссией) и тормоза.\n"
                                               "2. Зеркало заднего вида для обучающего вождению.\n"
                                               "3. Опознавательные знаки «Учебное транспортное средство».\n"
                                               "<u>4. Все перечисленное оборудование.</u>", reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: callback.data == 'q_3_18')
def callback_message(callback):
    markup = types.InlineKeyboardMarkup()
    next = types.InlineKeyboardButton('19 воп.', callback_data='q_3_19')
    markup.add(next)
    bot.send_message(callback.message.chat.id, "Вопрос 3 Билет 18.\n"
                                               "В каких случаях запрещается эксплуатация мотоцикла?\n\n"
                                               "1. Подножки или рукоятки пассажиров на седле не имеют прорезиненного покрытия.\n"
                                               "<u>2. Имеется люфт в соединениях рамы мотоцикла с рамой бокового прицепа.</u>\n"
                                               "3. Отсутствует огнетушитель.", reply_markup=markup)

@bot.callback_query_handler(func=lambda callback: callback.data == 'q_3_19')
def callback_message(callback):
    markup = types.InlineKeyboardMarkup()
    next = types.InlineKeyboardButton('20 воп.', callback_data='q_3_20')
    markup.add(next)
    bot.send_message(callback.message.chat.id, "Вопрос 3 Билет 19.\n"
                                               "На повороте возник занос задней оси переднеприводного автомобиля. Ваши действия?\n\n"
                                               "1. Уменьшите подачу топлива, рулевым колесом стабилизируете движение.\n"
                                               "2. Притормозите и повернете рулевое колесо в сторону заноса.\n"
                                               "<u>3. Слегка увеличите подачу топлива, корректируя направление движения рулевым колесом.</u>\n"
                                               "4. Значительно увеличите подачу топлива, не меняя положения рулевого колеса.", reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: callback.data == 'q_3_20')
def callback_message(callback):
    bot.send_message(callback.message.chat.id, "Вопрос 3 Билет 20.\n"
                                               "Какие сведения необходимо сообщить диспетчеру для вызова скорой медицинской помощи при дорожно-транспортном происшествии (ДТП)?\n\n"
                                               "1. Указать общеизвестные ориентиры, ближайшие к месту ДТП. Сообщить о количестве пострадавших, указать их пол и возраст.\n"
                                               "2. Указать улицу и номер дома, ближайшего к месту ДТП. Сообщить, кто пострадал в ДТП (пешеход, водитель автомобиля или пассажиры), и описать травмы, которые они получили.\n"
                                               "<u>3. Указать место ДТП (назвать улицу, номер дома и общеизвестные ориентиры, ближайшие к месту ДТП). Сообщить: количество пострадавших, их пол, примерный возраст, наличие у них сознания, дыхания, кровообращения, а также сильного кровотечения, переломов и других травм. Дождаться сообщения диспетчера о том, что вызов принят.</u>")
    bot.send_message(callback.message.chat.id, '/start - Нажмите, чтобы вернуться к выбору билета')


@bot.callback_query_handler(func=lambda callback: callback.data == 'n4')
def callback_message(callback):
    markup = types.InlineKeyboardMarkup()
    next = types.InlineKeyboardButton('2 воп.', callback_data='q_4_2')
    markup.add(next)
    bot.send_photo(callback.message.chat.id, open('n4_1.jpg', 'rb'))
    bot.send_message(callback.message.chat.id, "Вопрос 1 Билет 4.\n"
                                               "Сколько полос для движения имеет проезжая часть данной дороги?\n\n"
                                               "1. Одну полосу.\n"
                                               "<u>2. Две полосы.</u>\n"
                                               "3. Три полосы.", reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: callback.data == 'q_4_2')
def callback_message(callback):
    markup = types.InlineKeyboardMarkup()
    next = types.InlineKeyboardButton('3 воп.', callback_data='q_4_3')
    markup.add(next)
    bot.send_photo(callback.message.chat.id, open('n4_2.jpg', 'rb'))
    bot.send_message(callback.message.chat.id, "Вопрос 2 Билет 4.\n"
                                               "Эти знаки предупреждают Вас:\n\n"
                                               "1. О наличии через 500 м опасных поворотов.\n"
                                               "<u>2. О том, что на расстоянии 150-300 м за дорожным знаком начнется участок дороги протяженностью 500 м с опасными поворотами.</u>\n"
                                               "3. О том, что сразу за знаком начнется участок протяженностью 500 м с опасными поворотами.", reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: callback.data == 'q_4_3')
def callback_message(callback):
    markup = types.InlineKeyboardMarkup()
    next = types.InlineKeyboardButton('4 воп.', callback_data='q_4_4')
    markup.add(next)
    bot.send_photo(callback.message.chat.id, open('n4_3.jpg', 'rb'))
    bot.send_message(callback.message.chat.id, "Вопрос 3 Билет 4.\n"
                                               "Какой из указанных знаков распространяет свое действие только на ту полосу, над которой он установлен?\n\n"
                                               "<u>1. Только А.</u>\n"
                                               "2. Только Б.\n"
                                               "3. Б и В.", reply_markup=markup)

@bot.callback_query_handler(func=lambda callback: callback.data == 'q_4_4')
def callback_message(callback):
    markup = types.InlineKeyboardMarkup()
    next = types.InlineKeyboardButton('5 воп.', callback_data='q_4_5')
    markup.add(next)
    bot.send_photo(callback.message.chat.id, open('n4_4.jpg', 'rb'))
    bot.send_message(callback.message.chat.id, "Вопрос 4 Билет 4.\n"
                                               "Вы буксируете неисправный автомобиль. По какой полосе Вам можно продолжить движение в населенном пункте?\n\n"
                                               "<u>1. Только по правой.</u>\n"
                                               "2. Только по левой.\n"
                                               "3. По любой.", reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: callback.data == 'q_4_5')
def callback_message(callback):
    markup = types.InlineKeyboardMarkup()
    next = types.InlineKeyboardButton('6 воп.', callback_data='q_4_6')
    markup.add(next)
    bot.send_message(callback.message.chat.id, "Вопрос 5 Билет 4.\n"
                                               "Что означает разметка в виде надписи «СТОП» на проезжей части?\n\n"
                                               "1. Предупреждает о приближении к стоп-линии перед регулируемым перекрестком.\n"
                                               "<u>2. Предупреждает о приближении к стоп-линии и знаку «Движение без остановки запрещено».</u>\n"
                                               "3. Предупреждает о приближении к знаку «Уступите дорогу».", reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: callback.data == 'q_4_6')
def callback_message(callback):
    markup = types.InlineKeyboardMarkup()
    next = types.InlineKeyboardButton('7 воп.', callback_data='q_4_7')
    markup.add(next)
    bot.send_photo(callback.message.chat.id, open('n4_6.jpg', 'rb'))
    bot.send_message(callback.message.chat.id, "Вопрос 6 Билет 4.\n"
                                               "Каким транспортным средствам разрешено движение прямо?\n\n"
                                               "<u>1. Только грузовому автомобилю.</u>\n"
                                               "2. Легковому и грузовому автомобилям.\n"
                                               "3. Грузовому автомобилю и автобусу.", reply_markup=markup)

@bot.callback_query_handler(func=lambda callback: callback.data == 'q_4_7')
def callback_message(callback):
    markup = types.InlineKeyboardMarkup()
    next = types.InlineKeyboardButton('8 воп.', callback_data='q_4_8')
    markup.add(next)
    bot.send_photo(callback.message.chat.id, open('n4_7.jpg', 'rb'))
    bot.send_message(callback.message.chat.id, "Вопрос 7 Билет 4.\n"
                                               "Вы намерены продолжить движение по главной дороге. Обязаны ли Вы при этом включить указатели правого поворота?\n\n"
                                               "<u>1. Обязаны.</u>\n"
                                               "2. Обязаны только при наличии движущегося сзади транспортного средства.\n"
                                               "3. Не обязаны.", reply_markup=markup)

@bot.callback_query_handler(func=lambda callback: callback.data == 'q_4_8')
def callback_message(callback):
    markup = types.InlineKeyboardMarkup()
    next = types.InlineKeyboardButton('9 воп.', callback_data='q_4_9')
    markup.add(next)
    bot.send_photo(callback.message.chat.id, open('n4_8.jpg', 'rb'))
    bot.send_message(callback.message.chat.id, "Вопрос 8 Билет 4.\n"
                                               "Кто должен уступить дорогу?\n\n"
                                               "1. Водитель грузового автомобиля.\n"
                                               "<u>2. Водитель легкового автомобиля.</u>\n", reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: callback.data == 'q_4_9')
def callback_message(callback):
    markup = types.InlineKeyboardMarkup()
    next = types.InlineKeyboardButton('10 воп.', callback_data='q_4_10')
    markup.add(next)
    bot.send_photo(callback.message.chat.id, open('n4_9.jpg', 'rb'))
    bot.send_message(callback.message.chat.id, "Вопрос 9 Билет 4.\n"
                                               "Кто должен уступить дорогу?\n\n"
                                               "1. Только по траектории А.\n"
                                               "<u>2. Только по траектории Б.</u>\n"
                                               "3. По любой траектории из указанных.", reply_markup=markup)

@bot.callback_query_handler(func=lambda callback: callback.data == 'q_4_10')
def callback_message(callback):
    markup = types.InlineKeyboardMarkup()
    next = types.InlineKeyboardButton('11 воп.', callback_data='q_4_11')
    markup.add(next)
    bot.send_message(callback.message.chat.id, "Вопрос 10 Билет 4.\n"
                                               "По какой полосе проезжей части разрешено движение в населенном пункте, если по техническим причинам транспортное средство не может развивать скорость более 40 км/ч?\n\n"
                                               "<u>1. Только по крайней правой.</u>\n"
                                               "2. Не далее второй полосы.\n"
                                               "3. По любой, кроме крайней левой.", reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: callback.data == 'q_4_11')
def callback_message(callback):
    markup = types.InlineKeyboardMarkup()
    next = types.InlineKeyboardButton('12 воп.', callback_data='q_4_12')
    markup.add(next)
    bot.send_photo(callback.message.chat.id, open('n4_11.jpg', 'rb'))
    bot.send_message(callback.message.chat.id, "Вопрос 11 Билет 4.\n"
                                               "Разрешено ли Вам обогнать мотоцикл?\n\n"
                                               "<u>1. Разрешено.</u>\n"
                                               "2. Разрешено только после проезда перекрестка.\n"
                                               "3. Запрещено.", reply_markup=markup)

@bot.callback_query_handler(func=lambda callback: callback.data == 'q_4_12')
def callback_message(callback):
    markup = types.InlineKeyboardMarkup()
    next = types.InlineKeyboardButton('13 воп.', callback_data='q_4_13')
    markup.add(next)
    bot.send_photo(callback.message.chat.id, open('n4_12.jpg', 'rb'))
    bot.send_message(callback.message.chat.id, "Вопрос 12 Билет 4.\n"
                                               "Разрешается ли Вам остановка для посадки пассажира в этом месте?\n\n"
                                               "1. Разрешается.\n"
                                               "<u>2. Разрешается, если при этом не будут созданы помехи для движения маршрутных транспортных средств.</u>\n"
                                               "3. Запрещается.", reply_markup=markup)

@bot.callback_query_handler(func=lambda callback: callback.data == 'q_4_13')
def callback_message(callback):
    markup = types.InlineKeyboardMarkup()
    next = types.InlineKeyboardButton('14 воп.', callback_data='q_4_14')
    markup.add(next)
    bot.send_photo(callback.message.chat.id, open('n4_13.jpg', 'rb'))
    bot.send_message(callback.message.chat.id, "Вопрос 13 Билет 4.\n"
                                               "Вы намерены проехать перекресток в прямом направлении. Ваши действия?\n\n"
                                               "1. Проедете перекресток первым.\n"
                                               "2. Уступите дорогу только встречному автомобилю.\n"
                                               "<u>3. Уступите дорогу только автомобилю с включенными проблесковым маячком и специальным звуковым сигналом.</u>\n"
                                               "4. Уступите дорогу обоим транспортным средствам.", reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: callback.data == 'q_4_14')
def callback_message(callback):
    markup = types.InlineKeyboardMarkup()
    next = types.InlineKeyboardButton('15 воп.', callback_data='q_4_15')
    markup.add(next)
    bot.send_photo(callback.message.chat.id, open('n4_14.jpg', 'rb'))
    bot.send_message(callback.message.chat.id, "Вопрос 14 Билет 4.\n"
                                               "Кому Вы должны уступить дорогу при повороте направо?\n\n"
                                               "1. Только пешеходу, переходящему проезжую часть по нерегулируемому пешеходному переходу.\n"
                                               "2. Только пешеходам, переходящим проезжую часть, на которую Вы поворачиваете.\n"
                                               "<u>3. Всем пешеходам.</u>\n", reply_markup=markup)

@bot.callback_query_handler(func=lambda callback: callback.data == 'q_4_15')
def callback_message(callback):
    markup = types.InlineKeyboardMarkup()
    next = types.InlineKeyboardButton('16 воп.', callback_data='q_4_16')
    markup.add(next)
    bot.send_photo(callback.message.chat.id, open('n4_15.jpg', 'rb'))
    bot.send_message(callback.message.chat.id, "Вопрос 15 Билет 4.\n"
                                               "Как Вам следует поступить при выполнении разворота?\n\n"
                                               "1. Проехать перекресток первым.\n"
                                               "<u>2. Уступить дорогу только легковому автомобилю.</u>\n"
                                               "3. Уступить дорогу обоим транспортным средствам.\n", reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: callback.data == 'q_4_16')
def callback_message(callback):
    markup = types.InlineKeyboardMarkup()
    next = types.InlineKeyboardButton('17 воп.', callback_data='q_4_17')
    markup.add(next)
    bot.send_message(callback.message.chat.id, "Вопрос 16 Билет 4.\n"
                                               "Какие из перечисленных действий запрещены водителям механических транспортных средств в жилой зоне?\n\n"
                                               "1. Сквозное движение.\n"
                                               "2. Учебная езда.\n"
                                               "3. Стоянка с работающим двигателем.\n"
                                               "<u>4. Все перечисленные действия.</u>", reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: callback.data == 'q_4_17')
def callback_message(callback):
    markup = types.InlineKeyboardMarkup()
    next = types.InlineKeyboardButton('18 воп.', callback_data='q_4_18')
    markup.add(next)
    bot.send_message(callback.message.chat.id, "Вопрос 17 Билет 4.\n"
                                               "Какое расстояние должно быть обеспечено между буксирующим и буксируемым транспортными средствами при буксировке на жесткой сцепке?\n\n"
                                               "<u>1. Не более 4 м.</u>\n"
                                               "2. От 4 до 6 м.\n"
                                               "3. От 6 до 8 м.", reply_markup=markup)

@bot.callback_query_handler(func=lambda callback: callback.data == 'q_4_18')
def callback_message(callback):
    markup = types.InlineKeyboardMarkup()
    next = types.InlineKeyboardButton('19 воп.', callback_data='q_4_19')
    markup.add(next)
    bot.send_message(callback.message.chat.id, "Вопрос 18 Билет 4.\n"
                                               "В каком случае разрешается эксплуатация транспортного средства?\n\n"
                                               "1. Установлены непредусмотренные конструкцией светового прибора оптические элементы.\n"
                                               "2. Регулировка фар не соответствует установленным требованиям.\n"
                                               "3. Рассеиватели внешних световых приборов отсутствуют или повреждены.\n"
                                               "<u>4. На транспортном средстве спереди установлены световые приборы с огнями оранжевого цвета</u>", reply_markup=markup)

@bot.callback_query_handler(func=lambda callback: callback.data == 'q_4_19')
def callback_message(callback):
    markup = types.InlineKeyboardMarkup()
    next = types.InlineKeyboardButton('20 воп.', callback_data='q_4_20')
    markup.add(next)
    bot.send_message(callback.message.chat.id, "Вопрос 19 Билет 4.\n"
                                               "Что следует предпринять водителю для предотвращения опасных последствий заноса автомобиля при резком повороте рулевого колеса на скользкой дороге?\n\n"
                                               "<u>1. Быстро, но плавно повернуть рулевое колесо в сторону заноса, затем опережающим воздействием на рулевое колесо выровнять траекторию движения автомобиля.</u>\n"
                                               "2. Выключить сцепление и повернуть рулевое колесо в сторону заноса.\n"
                                               "3. Нажать на педаль тормоза и воздействием на рулевое колесо выровнять траекторию движения.\n", reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: callback.data == 'q_4_20')
def callback_message(callback):
    bot.send_message(callback.message.chat.id, "Вопрос 20 Билет 4.\n"
                                               "Как следует расположить руки на грудной клетке пострадавшего при проведении сердечно-легочной реанимации?\n\n"
                                               "1. Основания ладоней обеих кистей, взятых в «замок», должны располагаться на грудной клетке на два пальца выше мечевидного отростка так, чтобы большой палец одной руки указывал в сторону левого плеча пострадавшего, а другой – в сторону правого плеча. Руки выпрямляются в локтевых суставах.\n"
                                               "<u>2. Основание ладони одной руки накладывают на середину грудной клетки на два пальца выше мечевидного отростка, вторую руку накладывают сверху, пальцы рук берут в замок. Руки выпрямляются в локтевых суставах, большие пальцы рук указывают на подбородок и живот. Надавливания должны проводиться без резких движений.</u>\n"
                                               "3. Давление руками на грудину выполняют основанием ладони одной руки, расположенной на грудной клетке на два пальца выше мечевидного отростка. Рука выпрямлена в локтевом суставе. Направление большого пальца не имеет значения.\n")
    bot.send_message(callback.message.chat.id, '/start - Нажмите, чтобы вернуться к выбору билета')

@bot.callback_query_handler(func=lambda callback: callback.data == 'n5')
def callback_message(callback):
    markup = types.InlineKeyboardMarkup()
    next = types.InlineKeyboardButton('2 воп.', callback_data='q_5_2')
    markup.add(next)
    bot.send_photo(callback.message.chat.id, open('n5_1.jpg', 'rb'))
    bot.send_message(callback.message.chat.id, "Вопрос 1 Билет 5.\n"
                                               "Сколько проезжих частей имеет данная дорога?\n\n"
                                               "<u>1. Одну.</u>\n"
                                               "2. Две.\n"
                                               "3. Четыре.\n", reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: callback.data == 'q_5_2')
def callback_message(callback):
    markup = types.InlineKeyboardMarkup()
    next = types.InlineKeyboardButton('3 воп.', callback_data='q_5_3')
    markup.add(next)
    bot.send_photo(callback.message.chat.id, open('n5_2.jpg', 'rb'))
    bot.send_message(callback.message.chat.id, "Вопрос 2 Билет 5.\n"
                                               "При наличии какого знака водитель должен уступить дорогу, если встречный разъезд затруднен?\n\n"
                                               "1. Только В.\n"
                                               "<u>2. А и В.</u>\n"
                                               "3. Б и В.\n"
                                               "4. Б и Г.", reply_markup=markup)

@bot.callback_query_handler(func=lambda callback: callback.data == 'q_5_3')
def callback_message(callback):
    markup = types.InlineKeyboardMarkup()
    next = types.InlineKeyboardButton('4 воп.', callback_data='q_5_4')
    markup.add(next)
    bot.send_photo(callback.message.chat.id, open('n5_3.jpg', 'rb'))
    bot.send_message(callback.message.chat.id, "Вопрос 3 Билет 5.\n"
                                               "Разрешена ли Вам стоянка в указанном месте?\n\n"
                                               "<u>1. Разрешена.</u>\n"
                                               "2. Разрешена только в светлое время суток.\n"
                                               "3. Запрещена.\n", reply_markup=markup)

@bot.callback_query_handler(func=lambda callback: callback.data == 'q_5_4')
def callback_message(callback):
    markup = types.InlineKeyboardMarkup()
    next = types.InlineKeyboardButton('5 воп.', callback_data='q_5_5')
    markup.add(next)
    bot.send_photo(callback.message.chat.id, open('n5_4.jpg', 'rb'))
    bot.send_message(callback.message.chat.id, "Вопрос 4 Билет 5.\n"
                                               "Нарушил ли водитель грузового автомобиля правила стоянки?\n\n"
                                               "<u>1. Нарушил.</u>\n"
                                               "2. Не нарушил, если разрешенная максимальная масса автомобиля не более 3,5 т.\n"
                                               "3. Не нарушил.\n", reply_markup=markup)

@bot.callback_query_handler(func=lambda callback: callback.data == 'q_5_5')
def callback_message(callback):
    markup = types.InlineKeyboardMarkup()
    next = types.InlineKeyboardButton('6 воп.', callback_data='q_5_6')
    markup.add(next)
    bot.send_photo(callback.message.chat.id, open('n5_5.jpg', 'rb'))
    bot.send_message(callback.message.chat.id, "Вопрос 5 Билет 5.\n"
                                               "О чем предупреждает Вас вертикальная разметка, нанесенная на ограждение дороги?\n\n"
                                               "1. О приближении к железнодорожному переезду.\n"
                                               "2. О приближении к опасному перекрестку.\n"
                                               "<u>3. О движении по опасному участку дороги.</u>\n", reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: callback.data == 'q_5_6')
def callback_message(callback):
    markup = types.InlineKeyboardMarkup()
    next = types.InlineKeyboardButton('7 воп.', callback_data='q_5_7')
    markup.add(next)
    bot.send_message(callback.message.chat.id, "Вопрос 6 Билет 5.\n"
                                               "Разрешается ли водителю продолжить движение после переключения зеленого сигнала светофора на желтый, если возможно остановиться перед перекрестком, только применив экстренное торможение?\n\n"
                                               "<u>1. Разрешается.</u>\n"
                                               "2. Разрешается, если водитель намерен проехать перекресток только в прямом направлении.\n"
                                               "3. Запрещается.", reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: callback.data == 'q_5_7')
def callback_message(callback):
    markup = types.InlineKeyboardMarkup()
    next = types.InlineKeyboardButton('8 воп.', callback_data='q_5_8')
    markup.add(next)
    bot.send_photo(callback.message.chat.id, open('n5_7.jpg', 'rb'))
    bot.send_message(callback.message.chat.id, "Вопрос 7 Билет 5.\n"
                                               "Поднятая вверх рука водителя мотоцикла является сигналом, информирующим Вас о его намерении:\n\n"
                                               "1. Продолжить движение прямо.\n"
                                               "2. Повернуть направо.\n"
                                               "<u>3. Снизить скорость, чтобы остановиться и уступить дорогу легковому автомобилю.</u>", reply_markup=markup)

@bot.callback_query_handler(func=lambda callback: callback.data == 'q_5_8')
def callback_message(callback):
    markup = types.InlineKeyboardMarkup()
    next = types.InlineKeyboardButton('9 воп.', callback_data='q_5_9')
    markup.add(next)
    bot.send_photo(callback.message.chat.id, open('n5_8.jpg', 'rb'))
    bot.send_message(callback.message.chat.id, "Вопрос 8 Билет 5.\n"
                                               "В каких направлениях Вам можно продолжить движение по левой полосе на грузовом автомобиле с разрешенной максимальной массой не более 3,5 т?\n\n"
                                               "1. Только прямо.\n"
                                               "2. Прямо и направо.\n"
                                               "<u>3. Прямо, налево и в обратном направлении.</u>", reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: callback.data == 'q_5_9')
def callback_message(callback):
    markup = types.InlineKeyboardMarkup()
    next = types.InlineKeyboardButton('10 воп.', callback_data='q_5_10')
    markup.add(next)
    bot.send_photo(callback.message.chat.id, open('n5_9.jpg', 'rb'))
    bot.send_message(callback.message.chat.id, "Вопрос 9 Билет 5.\n"
                                               "Вам необходимо повернуть на примыкающую справа дорогу. Ваши действия?\n\n"
                                               "1. Не меняя полосы, снизить скорость, затем перестроиться на полосу торможения.\n"
                                               "<u>2. Не меняя скорости, перестроиться на полосу торможения, затем снизить скорость.</u>\n"
                                               "3. Возможны оба варианта действий.", reply_markup=markup)

@bot.callback_query_handler(func=lambda callback: callback.data == 'q_5_10')
def callback_message(callback):
    markup = types.InlineKeyboardMarkup()
    next = types.InlineKeyboardButton('11 воп.', callback_data='q_5_11')
    markup.add(next)
    bot.send_photo(callback.message.chat.id, open('n5_10.jpg', 'rb'))
    bot.send_message(callback.message.chat.id, "Вопрос 10 Билет 5.\n"
                                               "С какой максимальной скоростью Вы имеете право продолжить движение вне населенных пунктов на легковом автомобиле с прицепом?\n\n"
                                               "1. 50 км/ч.\n"
                                               "<u>2. 70 км/ч.</u>\n"
                                               "3. 80 км/ч.", reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: callback.data == 'q_5_11')
def callback_message(callback):
    markup = types.InlineKeyboardMarkup()
    next = types.InlineKeyboardButton('12 воп.', callback_data='q_5_12')
    markup.add(next)
    bot.send_photo(callback.message.chat.id, open('n5_11.jpg', 'rb'))
    bot.send_message(callback.message.chat.id, "Вопрос 11 Билет 5.\n"
                                               "Разрешен ли Вам обгон?\n\n"
                                               "<u>1. Разрешен.</u>\n"
                                               "2. Разрешен, если обгон будет завершен до перекрестка.\n"
                                               "3. Запрещен.", reply_markup=markup)

@bot.callback_query_handler(func=lambda callback: callback.data == 'q_5_12')
def callback_message(callback):
    markup = types.InlineKeyboardMarkup()
    next = types.InlineKeyboardButton('13 воп.', callback_data='q_5_13')
    markup.add(next)
    bot.send_photo(callback.message.chat.id, open('n5_12.jpg', 'rb'))
    bot.send_message(callback.message.chat.id, "Вопрос 12 Билет 5.\n"
                                               "Кто из водителей нарушил правила стоянки?\n\n"
                                               "1. Оба.\n"
                                               "<u>2. Только водитель автомобиля А.</u>\n"
                                               "3. Только водитель автомобиля Б.", reply_markup=markup)

@bot.callback_query_handler(func=lambda callback: callback.data == 'q_5_13')
def callback_message(callback):
    markup = types.InlineKeyboardMarkup()
    next = types.InlineKeyboardButton('14 воп.', callback_data='q_5_14')
    markup.add(next)
    bot.send_photo(callback.message.chat.id, open('n5_13.jpg', 'rb'))
    bot.send_message(callback.message.chat.id, "Вопрос 13 Билет 5.\n"
                                               "Вы намерены развернуться. Ваши действия?\n\n"
                                               "1. Проедете перекресток первым.\n"
                                               "<u>2. Выполните разворот, уступив дорогу легковому автомобилю.</u>\n"
                                               "3. Дождетесь, когда регулировщик опустит правую руку.", reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: callback.data == 'q_5_14')
def callback_message(callback):
    markup = types.InlineKeyboardMarkup()
    next = types.InlineKeyboardButton('15 воп.', callback_data='q_5_15')
    markup.add(next)
    bot.send_photo(callback.message.chat.id, open('n5_14.jpg', 'rb'))
    bot.send_message(callback.message.chat.id, "Вопрос 14 Билет 5.\n"
                                               "Кому Вы должны уступить дорогу при движении в прямом направлении?\n\n"
                                               "<u>1. Только трамваю.</u>\n"
                                               "2. Только легковому автомобилю.\n"
                                               "3. Обоим транспортным средствам.", reply_markup=markup)

@bot.callback_query_handler(func=lambda callback: callback.data == 'q_5_15')
def callback_message(callback):
    markup = types.InlineKeyboardMarkup()
    next = types.InlineKeyboardButton('16 воп.', callback_data='q_5_16')
    markup.add(next)
    bot.send_photo(callback.message.chat.id, open('n5_15.jpg', 'rb'))
    bot.send_message(callback.message.chat.id, "Вопрос 15 Билет 5.\n"
                                               "Как Вам следует поступить при повороте налево?\n\n"
                                               "<u>1. Проехать перекресток первым.</u>\n"
                                               "2. Уступить дорогу только грузовому автомобилю с включенным проблесковым маячком.\n"
                                               "3. Уступить дорогу обоим транспортным средствам.", reply_markup=markup)

@bot.callback_query_handler(func=lambda callback: callback.data == 'q_5_16')
def callback_message(callback):
    markup = types.InlineKeyboardMarkup()
    next = types.InlineKeyboardButton('17 воп.', callback_data='q_5_17')
    markup.add(next)
    bot.send_photo(callback.message.chat.id, open('n5_16.jpg', 'rb'))
    bot.send_message(callback.message.chat.id, "Вопрос 16 Билет 5.\n"
                                               "Разрешено ли Вам проехать железнодорожный переезд?\n\n"
                                               "1. Разрешено, поскольку дежурный по переезду запрещает движение только встречному автомобилю.\n"
                                               "2. Разрешено, если отсутствует приближающийся поезд.\n"
                                               "<u>3. Запрещено.</u>", reply_markup=markup)

@bot.callback_query_handler(func=lambda callback: callback.data == 'q_5_17')
def callback_message(callback):
    markup = types.InlineKeyboardMarkup()
    next = types.InlineKeyboardButton('18 воп.', callback_data='q_5_18')
    markup.add(next)
    bot.send_message(callback.message.chat.id, "Вопрос 17 Билет 5.\n"
                                               "В каких случаях разрешено применять звуковые сигналы в населенных пунктах?\n\n"
                                               "1. Только для предупреждения о намерении произвести обгон.\n"
                                               "<u>2. Только для предотвращения дорожно-транспортного происшествия.</u>\n"
                                               "3. В обоих перечисленных случаях.", reply_markup=markup)

@bot.callback_query_handler(func=lambda callback: callback.data == 'q_5_18')
def callback_message(callback):
    markup = types.InlineKeyboardMarkup()
    next = types.InlineKeyboardButton('19 воп.', callback_data='q_5_19')
    markup.add(next)
    bot.send_message(callback.message.chat.id, "Вопрос 18 Билет 5.\n"
                                               "При каком максимальном значении суммарного люфта в рулевом управлении допускается эксплуатация легкового автомобиля?\n\n"
                                               "<u>1. 10 градусов.</u>\n"
                                               "2. 20 градусов.\n"
                                               "3. 25 градусов.", reply_markup=markup)

@bot.callback_query_handler(func=lambda callback: callback.data == 'q_5_19')
def callback_message(callback):
    markup = types.InlineKeyboardMarkup()
    next = types.InlineKeyboardButton('20 воп.', callback_data='q_5_20')
    markup.add(next)
    bot.send_message(callback.message.chat.id, "Вопрос 19 Билет 5.\n"
                                               "Как следует поступить водителю при высадке из автомобиля, стоящего у тротуара или на обочине?\n\n"
                                               "1. Обойти автомобиль спереди.\n"
                                               "<u>2. Обойти автомобиль сзади.</u>\n"
                                               "3. Допустимы оба варианта действий.", reply_markup=markup)

@bot.callback_query_handler(func=lambda callback: callback.data == 'q_5_20')
def callback_message(callback):
    bot.send_message(callback.message.chat.id, "Вопрос 20 Билет 5.\n"
                                               "Как следует поступить водителю при высадке из автомобиля, стоящего у тротуара или на обочине?\n\n"
                                               "1. Обойти автомобиль спереди.\n"
                                               "<u>2. Обойти автомобиль сзади.</u>\n"
                                               "3. Допустимы оба варианта действий.")
    bot.send_message(callback.message.chat.id, '/start - Нажмите, чтобы вернуться к выбору билета')

bot.polling(non_stop=True)




