import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

# Логирование
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Токен вашего бота
TOKEN = '7943917934:AAFlfQqO-7Rm1giXntcnoBUsYi9QgSVAWTI'

# Данные для вопросов и ответов по билетам
questions_data = {
    'ticket_1': [
        {
            'question': "В каком случае водитель совершит вынужденную остановку?",
            'options': [
                "Остановившись непосредственно перед пешеходным переходом, чтобы уступить дорогу пешеходу",
                "Остановившись на проезжей части из-за технической неисправности транспортного средства",
                "В обоих перечисленных случаях"
            ],
            'correct_option': 1,
            'explanation': "Остановившись на проезжей части из-за технической неисправности транспортного средства.",
            'hint': "\n«Вынужденная остановка» - прекращение движения транспортного средства, связанное с его технической неисправностью, опасностью, создаваемой перевозимым грузом, состоянием водителя (пассажира) или появления препятствия на дороге. (Пункт 1.2 ПДД, термин «Вынужденная остановка»)"
        },
        {
            'question': "Разрешено ли Вам съехать на дорогу с грунтовым покрытием?",
            'options': [
                "Разрешено",
                "Разрешено только при технической неисправности транспортного средства",
                "Запрещено"
            ],
            'correct_option': 0,
            'explanation': "Съезд на дорогу с грунтовым покрытием разрешен.",
            'hint': "\nВпереди по ходу Вашего движения предупреждающий знак 1.11.2 «Опасный поворот» и знаки 1.34.2 «Направление поворота», которые указывают направление движения на закруглении дороги малого радиуса с ограниченной видимостью. Ничего, что бы Вам запрещало поворот на дорогу с грунтовым покрытием, нет. По Вашему желанию поворачиваете направо. («Дорожные знаки»).",
            'image_path': '/Users/kirillivanov/Desktop/Programtraining/PDD bot/photoforticket/n1_2.jpg'
        },
        {
            'question': "Можно ли Вам остановиться в указанном месте для посадки пассажира?",
            'options': [
                "Можно",
                "Можно, если Вы управляете такси",
                "Нельзя"
            ],
            'correct_option': 0,
            'explanation': "Съезд на дорогу с грунтовым покрытием разрешен.",
            'hint': "\nЗнак 3.28 «Стоянка запрещена» не запрещает производить остановку. В указанном месте Вам совершить остановку можно. («Дорожные знаки»)",
            'image_path': '/Users/kirillivanov/Desktop/Programtraining/PDD bot/photoforticket/n1_3.jpg'
        },
        {
            'question': "Какие из указанных знаков запрещают движение водителям мопедов?",
            'options': [
                "Только А",
                "Только Б",
                "В и Г",
                "Все"
            ],
            'correct_option': 3,
            'explanation': "Все указанные знаки запрещают движение водителям мопедов.",
            'hint': "\nЗапрещают движение водителям мопедов все знаки из перечисленных: А – 4.4.1 «Велосипедная дорожка»; Б – 5.14.1 «Полоса для маршрутных транспортных средств»; В – 4.5.2 «Пешеходная и велосипедная дорожка с совмещенным движением»; Г – 4.5.4 «Пешеходная и велосипедная дорожка с разделением движения».",
            'image_path': '/Users/kirillivanov/Desktop/Programtraining/PDD bot/photoforticket/n1_4.jpg'
        },
    ],
    'ticket_2': [
        {
            'question': "Сколько полос для движения имеет данная дорога?",
            'options': [
                "Две",
                "Четыре",
                "Пять"
            ],
            'correct_option': 1,
            'explanation': "Съезд на дорогу с грунтовым покрытием разрешен.",
            'hint': "\nРазделительная полоса делит дорогу на проезжие части. Данная дорога имеет две проезжие части, четыре полосы движения. (Пункт 1.2 ПДД)",
            'image_path': '/Users/kirillivanov/Desktop/Programtraining/PDD bot/photoforticket/n2_1.jpg'
        },

    ]
}

# Стартовая команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logger.info(f"User {update.message.chat.id} started the bot.")
    keyboard = [
        [InlineKeyboardButton("📄 Начать новый тест", callback_data='start_test')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Билеты ПДД 2023, 2024 г.\n\nВыберите действие:", reply_markup=reply_markup)

# Обработка нажатия кнопки "Начать новый тест"
async def start_test(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    logger.info(f"User {query.message.chat.id} clicked 'Начать новый тест'.")
    await query.answer()

    # Показываем список билетов (например, билеты от 1 до 40)
    keyboard = [[InlineKeyboardButton(f"№ {i}", callback_data=f"ticket_{i}") for i in range(1, 6)],  # билеты 1-5
                [InlineKeyboardButton(f"№ {i}", callback_data=f"ticket_{i}") for i in range(6, 11)]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.message.reply_text("Выберите номер билета:", reply_markup=reply_markup)

# Обработка выбора билета
async def select_ticket(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    logger.info(f"User {query.message.chat.id} selected ticket {query.data}.")
    await query.answer()

    ticket_id = query.data  # Получаем ID билета (например, "ticket_1")
    await send_question(update, context, ticket_id, 0)

# Функция отправки вопроса с фото или без
async def send_question(update: Update, context: ContextTypes.DEFAULT_TYPE, ticket_id, question_index):
    question_data = questions_data[ticket_id][question_index]

    # Форматирование текста вопроса
    question_text = f"Билет № {ticket_id.split('_')[1]}, вопрос {question_index + 1} из 20\n\n"
    question_text += f"{question_data['question']}\n\n"

    # Динамически добавляем варианты ответа в текст
    for i, option in enumerate(question_data['options']):
        question_text += f"{i + 1}. {option}\n"

    # Отправляем фото, если оно есть
    if 'image_path' in question_data:
        photo_path = question_data['image_path']
        await update.callback_query.message.reply_photo(photo=open(photo_path, 'rb'))

    # Генерация инлайн-кнопок для каждого варианта ответа
    options = [
        [InlineKeyboardButton(f"{i + 1}. {option}", callback_data=f"{ticket_id}_q{question_index}_{i}")]
        for i, option in enumerate(question_data['options'])
    ]
    reply_markup = InlineKeyboardMarkup(options)

    # Отправляем вопрос с кнопками
    await update.callback_query.message.reply_text(question_text, reply_markup=reply_markup)

# Обработка ответа пользователя
async def handle_answer(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    callback_data = query.data
    logger.info(f"User {query.message.chat.id} answered question: {callback_data}")

    # Ответим на callback_query (чтобы не зависал интерфейс)
    await query.answer()

    try:
        # Разбиваем данные callback на 4 части
        data_parts = callback_data.split('_')
        logger.info(f"Data parts after split: {data_parts}")

        # Убедимся, что разбиваем корректно: ticket, q0, question_index, selected_option
        if len(data_parts) != 4:
            raise ValueError(f"Неверное количество элементов в callback_data: {len(data_parts)}")

        ticket_id = f"ticket_{data_parts[1]}"  # Формируем ticket_id (например, ticket_1)
        question_id = int(data_parts[2][1:])   # Получаем номер вопроса
        selected_option = int(data_parts[3])   # Получаем выбранный вариант

        # Логируем, чтобы убедиться, что всё верно
        logger.info(f"Ticket ID: {ticket_id}, Question ID: {question_id}, Selected Option: {selected_option}")

        # Получаем данные вопроса
        question_data = questions_data[ticket_id][question_id]
        correct_option = question_data['correct_option']
        explanation = question_data['explanation']

        # Обновляем кнопки с отображением правильного/неправильного ответа
        options = []
        for i, option in enumerate(question_data['options']):
            if i == correct_option:
                options.append([InlineKeyboardButton(f"✅ {i + 1}. {option}", callback_data=f"{ticket_id}_q{question_id}_{i}")])
            elif i == selected_option:
                options.append([InlineKeyboardButton(f"❌ {i + 1}. {option}", callback_data=f"{ticket_id}_q{question_id}_{i}")])
            else:
                options.append([InlineKeyboardButton(f"{i + 1}. {option}", callback_data=f"{ticket_id}_q{question_id}_{i}")])

        reply_markup = InlineKeyboardMarkup(options)
        await query.message.edit_reply_markup(reply_markup=reply_markup)

        # Если ответ неправильный, отправляем подсказку
        if selected_option != correct_option:
            await query.message.reply_text(f"Подсказка💡 {question_data['hint']}")

        # Переход к следующему вопросу
        next_question = question_id + 1
        if next_question < len(questions_data[ticket_id]):
            await send_question(update, context, ticket_id, next_question)
        else:
            await query.message.reply_text("Тест завершён!")

    except ValueError as e:
        # Логируем ошибку и отправляем сообщение для отладки
        logger.error(f"Error processing callback data: {e}")
        await query.message.reply_text(f"Ошибка в обработке данных: {e}")


# Основная функция для запуска бота
def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(start_test, pattern='start_test'))
    app.add_handler(CallbackQueryHandler(select_ticket, pattern=r'^ticket_\d+$'))
    app.add_handler(CallbackQueryHandler(handle_answer, pattern=r'^ticket_\d+_q\d+_\d+$'))

    app.run_polling()

if __name__ == '__main__':
    main()
