import os
import json
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

TOKEN = '7943917934:AAFlfQqO-7Rm1giXntcnoBUsYi9QgSVAWTI'

def load_tickets():
    tickets_dir = os.path.join(os.path.dirname(__file__), 'tickets')
    tickets = {}

    if not os.path.exists(tickets_dir):
        return tickets

    for file in os.listdir(tickets_dir):
        ticket_name, ticket_extension = os.path.splitext(file)
        if ticket_extension == '.json':
            ticket_path = os.path.join(tickets_dir, file)
            with open(ticket_path) as f:
                ticket = json.load(f)
            tickets[ticket_name] = ticket

    return tickets

def load_ticket(ticket_id):
    tickets = load_tickets()
    return tickets.get(ticket_id)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton("📄 Начать новый тест", callback_data='start_test')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Билеты ПДД 2023, 2024 г.\n\nВыберите действие:", reply_markup=reply_markup)

async def start_test(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    keyboard = [[InlineKeyboardButton(f"№ {i}", callback_data=f"ticket_{i}") for i in range(1, 6)], 
                [InlineKeyboardButton(f"№ {i}", callback_data=f"ticket_{i}") for i in range(6, 11)],
                [InlineKeyboardButton(f"№ {i}", callback_data=f"ticket_{i}") for i in range(11, 16)],
                [InlineKeyboardButton(f"№ {i}", callback_data=f"ticket_{i}") for i in range(16, 21)],
                [InlineKeyboardButton(f"№ {i}", callback_data=f"ticket_{i}") for i in range(21, 26)],
                [InlineKeyboardButton(f"№ {i}", callback_data=f"ticket_{i}") for i in range(26, 31)],
                [InlineKeyboardButton(f"№ {i}", callback_data=f"ticket_{i}") for i in range(31, 36)],
                [InlineKeyboardButton(f"№ {i}", callback_data=f"ticket_{i}") for i in range(36, 41)]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.message.reply_text("Выберите номер билета:", reply_markup=reply_markup)

async def select_ticket(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    ticket_id = query.data 
    ticket_data = load_ticket(ticket_id)  

    if not ticket_data:
        await query.message.reply_text(f"Билет {ticket_id} не найден.")
        return

    await send_question(update, context, ticket_id, 0) 

async def send_question(update: Update, context: ContextTypes.DEFAULT_TYPE, ticket_id, question_index):
    ticket_data = load_ticket(ticket_id)
    question_data = ticket_data[question_index]

    question_text = f"Билет № {ticket_id.split('_')[1]}, вопрос {question_index + 1} из 20\n\n"
    question_text += f"{question_data['question']}\n\n"

    for i, option in enumerate(question_data['options']):
        question_text += f"{i + 1}. {option}\n"

    if 'image_path' in question_data:
        photo_path = question_data['image_path']
        await update.callback_query.message.reply_photo(photo=open(photo_path, 'rb'))

    options = [[InlineKeyboardButton(f"{i + 1}. {option}", callback_data=f"{ticket_id}_q{question_index}_{i}")]
               for i, option in enumerate(question_data['options'])]
    reply_markup = InlineKeyboardMarkup(options)

    await update.callback_query.message.reply_text(question_text, reply_markup=reply_markup)

async def handle_answer(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    callback_data = query.data
    await query.answer()

    data_parts = callback_data.split('_')

    ticket_id = f"ticket_{data_parts[1]}"  
    question_id = int(data_parts[2][1:])   
    selected_option = int(data_parts[3])   

    ticket_data = load_ticket(ticket_id)
    question_data = ticket_data[question_id]
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
    if next_question < len(ticket_data):
        await send_question(update, context, ticket_id, next_question)
    else:
        await query.message.reply_text("Тест завершён!")

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(start_test, pattern='start_test'))
    app.add_handler(CallbackQueryHandler(select_ticket, pattern=r'^ticket_\d+$'))
    app.add_handler(CallbackQueryHandler(handle_answer, pattern=r'^ticket_\d+_q\d+_\d+$'))

    app.run_polling()

if __name__ == '__main__':
    main()