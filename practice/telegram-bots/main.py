from faker import Faker

# Updater - chứa API_KEY có từ BotFather để chỉ ra bot nào
# chúng ta đang thêm các tính năng để sử dụng python code
# của chúng ta
from telegram.ext.updater import Updater

# Update - gọi mỗi lần một bot nhận một cập nhật
# Nói cách khác: tin nhắn hay lệnh và sẽ gửi người dùng một tin nhắn
from telegram.update import Update

# CallbackContext - khi thêm vào Dispatcher nó bắt buộc (hoạt động bên trong)
from telegram.ext.callbackcontext import CallbackContext

# CommandHandler class - xử lý bất kỳ lệnh được gửi bởi người dùng
# tới bot. Một lệnh luôn bắt đầu với '/' nói cách khác '/start', '/help' vv
from telegram.ext.commandhandler import CommandHandler

# MessageHandler class - xử lý bất kỳ tin nhắn thông thường được
# gửi bởi người dùng tới bot
from telegram.ext.messagehandler import MessageHandler

# Filters: lọc văn bản thông thường, hình ảnh, lệnh, etc từ một
# tin nhắn nhận đc
from telegram.ext.filters import Filters

updater = Updater(
    'API_KEY',
    use_context=True
)

faker = Faker()


'''
Nó sẽ hiển thị hội thoại đầu tiên, bạn có thể đặt tên nó
là thứ gì đó khác nhưng tin nhắn bên trong nó sẽ được
gửi tới người dùng bất cứ khi nào họ nhấn 'start' ngay lúc đầu
'''
def start(update: Update, context: CallbackContext):
    update.message.reply_text(
        'Hello sir. Welcome to the Bot. Please write\
 /help to see the commands available.')

'''
Thêm bất kỳ loại trợ giúp nào người dùng có thể cần.
Hay tất cả các lệnh bot của bạn hiểu,
thông tin có liên quan tới bot, etc
'''
def help(update: Update, context: CallbackContext):
    update.message.reply_text('''Available Commands :-
/youtube - To get the youtube URL
/linkedin - To get the LinkedIn profile URL
/email - To get the email
/geeks - To get the GeeksforGeeks URL''')


def email_url(update: Update, context: CallbackContext):
    update.message.reply_text(
        faker.free_email()
    )


def youtube_url(update: Update, context: CallbackContext):
    update.message.reply_text(
        'https://www.youtube.com/watch?v=1U973ef6kJE&ab_channel=L%C6%B0%C6%A1ngGiaH%C3%B9ngOfficial'
    )


def linked_in_url(update: Update, context: CallbackContext):
    update.message.reply_text('https://vn.linkedin.com/in/chaungo27')


def geeks_url(update: Update, context: CallbackContext):
    update.message.reply_text('https://www.geeksforgeeks.org/')


def unknown_text(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Sorry, I can't recognize you, you said {}".format(
            update.message.text
        )
    )


def unknown(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Sorry {} is not a valid command".format(
            update.message.text
        )
    )


def main():
    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CommandHandler('youtube', youtube_url))
    updater.dispatcher.add_handler(CommandHandler('help', help))
    updater.dispatcher.add_handler(CommandHandler('linkedin', linked_in_url))
    updater.dispatcher.add_handler(CommandHandler('email', email_url))
    updater.dispatcher.add_handler(CommandHandler('geeks', geeks_url))
    updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown))
    updater.dispatcher.add_handler(MessageHandler(Filters.command, unknown))

    updater.dispatcher.add_handler(MessageHandler(
        Filters.text, unknown_text
    ))

    updater.start_polling()


if __name__ == "__main__":
    main()
