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

bot.polling(non_stop=True)


