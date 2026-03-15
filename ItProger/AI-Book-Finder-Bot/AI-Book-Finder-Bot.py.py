import telebot
from telebot import types
import pytesseract
from PIL import Image
import io

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

bot = telebot.TeleBot('YOUR_BOT_TOKEN_HERE')


def save_customer_data(data):
    with open("bookstore_customers.txt", "a", encoding="utf-8") as file:
        file.write(f"ID: {data['id']} | Name: {data['name']} | Age: {data['age']} | Author: {data['author']}\n")


def main_keyboard():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    markup.add(types.KeyboardButton('Find by Author'), types.KeyboardButton('Scan Book Cover'))
    return markup


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, f"Welcome, {message.from_user.first_name}!", reply_markup=main_keyboard())


@bot.message_handler(func=lambda message: message.text == 'Find by Author')
def ask_age(message):
    msg = bot.send_message(message.chat.id, "How old are you?", reply_markup=types.ReplyKeyboardRemove())
    bot.register_next_step_handler(msg, get_age)


def get_age(message):
    age = message.text
    user_data = {'id': message.from_user.id, 'name': message.from_user.first_name, 'age': age}
    msg = bot.send_message(message.chat.id, "Favorite author?")
    bot.register_next_step_handler(msg, get_author, user_data)


def get_author(message, user_data):
    author = message.text
    user_data['author'] = author
    save_customer_data(user_data)
    search_url = f"https://www.knihydobrovsky.cz/vyhledavani?search={author.replace(' ', '+')}"
    bot.send_message(message.chat.id, f"Link for {author}:\n{search_url}", reply_markup=main_keyboard())


@bot.message_handler(func=lambda message: message.text == 'Scan Book Cover')
def request_photo(message):
    bot.send_message(message.chat.id, "Send a photo of the cover.")


@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    try:
        file_info = bot.get_file(message.photo[-1].file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        img = Image.open(io.BytesIO(downloaded_file))

        text = pytesseract.image_to_string(img, lang='eng+ukr').strip()

        if len(text) > 2:
            query = text.replace('\n', ' ')
            url = f"https://www.knihydobrovsky.cz/vyhledavani?search={query.replace(' ', '+')}"
            bot.send_message(message.chat.id, f"Recognized: {text[:100]}\nSearch link: {url}")
        else:
            bot.send_message(message.chat.id, "Could not read text.")
    except Exception as e:
        bot.send_message(message.chat.id, f"Error: {e}. Check Tesseract path.")


bot.infinity_polling()