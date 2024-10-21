import os
import json
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

TOKEN = '7943917934:AAFlfQqO-7Rm1giXntcnoBUsYi9QgSVAWTI'

# Функция загрузки всех билетов
def load_tickets():
    # Путь относительно текущего файла
    tickets_dir = os.path.join(os.path.dirname(__file__), 'tickets')



    tickets = {}
    for file in os.listdir(tickets_dir):
        ticket_name, ticket_extension = os.path.splitext(file)
        if ticket_extension == '.json':
            ticket_path = os.path.join(tickets_dir, file)
            with open(ticket_path) as f:
                ticket = json.load(f)
            tickets[ticket_name] = ticket
    return tickets

# Функция для загрузки конкретного билета
def load_ticket(ticket_id):
    tickets = load_tickets()  # Загружаем все билеты
    return tickets.get(ticket_id)  # Возвращаем конкретный билет по его ID

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

    keyboard = [[InlineKeyboardButton(f"№ {i}", callback_data=f"ticket_{i}") for i in range(1, 6)],  
                [InlineKeyboardButton(f"№ {i}", callback_data=f"ticket_{i}") for i in range(6, 11)]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.message.reply_text("Выберите номер билета:", reply_markup=reply_markup)

# Обработка выбора билета
async def select_ticket(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    logger.info(f"User {query.message.chat.id} selected ticket {query.data}.")
    await query.answer()

    ticket_id = query.data  # Получаем ID билета (например, "ticket_1")
    ticket_data = load_ticket(ticket_id)  # Загружаем данные билета

    if not ticket_data:
        logger.error(f"Ticket {ticket_id} not found")
        await query.message.reply_text(f"Билет {ticket_id} не найден.")
        return

    await send_question(update, context, ticket_id, 0)  # Отправляем первый вопрос билета

# Функция отправки вопроса с фото или без
async def send_question(update: Update, context: ContextTypes.DEFAULT_TYPE, ticket_id, question_index):
    question_data = load_ticket(ticket_id)[question_index]

    question_text = f"Билет № {ticket_id.split('_')[1]}, вопрос {question_index + 1} из 20\n\n"
    question_text += f"{question_data['question']}\n\n"

    for i, option in enumerate(question_data['options']):
        question_text += f"{i + 1}. {option}\n"

    if 'image_path' in question_data:
        photo_path = question_data['image_path']
        await update.callback_query.message.reply_photo(photo=open(photo_path, 'rb'))

    options = [
        [InlineKeyboardButton(f"{i + 1}. {option}", callback_data=f"{ticket_id}_q{question_index}_{i}")]
        for i, option in enumerate(question_data['options'])
    ]
    reply_markup = InlineKeyboardMarkup(options)

    await update.callback_query.message.reply_text(question_text, reply_markup=reply_markup)

# Обработка ответа пользователя
async def handle_answer(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    callback_data = query.data
    logger.info(f"User {query.message.chat.id} answered question: {callback_data}")

    await query.answer()

    try:
        data_parts = callback_data.split('_')
        logger.info(f"Data parts after split: {data_parts}")

        if len(data_parts) != 4:
            raise ValueError(f"Неверное количество элементов в callback_data: {len(data_parts)}")

        ticket_id = f"ticket_{data_parts[1]}"  
        question_id = int(data_parts[2][1:])   
        selected_option = int(data_parts[3])   

        logger.info(f"Ticket ID: {ticket_id}, Question ID: {question_id}, Selected Option: {selected_option}")

        question_data = load_ticket(ticket_id)[question_id]
        correct_option = question_data['correct_option']

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

        if selected_option != correct_option:
            await query.message.reply_text(f"Подсказка💡 {question_data['hint']}")

        next_question = question_id + 1
        if next_question < len(load_ticket(ticket_id)):
            await send_question(update, context, ticket_id, next_question)
        else:
            await query.message.reply_text("Тест завершён!")

    except ValueError as e:
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
