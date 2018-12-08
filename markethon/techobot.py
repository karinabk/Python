from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments bot and
# update. Error handlers also receive the raised TelegramError object in error.

from telegram.ext import Handler

class Myhandler(Handler):
	def check_update(self, update):
		return True
		

	def handle_update(self, update, dispatcher):
		
		return self.callback(dispatcher.bot, update)

	def unused_method(bot, update):
		bot.send_message(update.message.chat_id, text="when unused_method will run?")


def start(bot, update):
	"""Send a message when the command /start is issued."""


def echo(bot, update):
	"""Echo the user message."""
	user_id =update.message.from_user['id']
	bot.restrictChatMember(update.message.chat['id'],user_id,can_send_messages=False)

def remove(bot,update):
	print(update.message)
	user_id =update.message.from_user['id']
	print("Hellooooooo")
	bot.restrictChatMember(update.message.chat['id'],user_id,can_send_messages=False)
	bot.delete_message(update.message.chat_id,update.message.message_id)
	
	

def error(bot, update, error):
	"""Log Errors caused by Updates."""
	logger.warning('Update "%s" caused error "%s"', update, error)



def main():
	"""Start the bot."""
    # Create the EventHandler and pass it your bot's token.
	updater = Updater("766883353:AAF1F2Ac2FkmofSH8ox4SJIjqd57V4D-0xs")

    # Get the dispatcher to register handlers
	db = updater.dispatcher		
	db.add_handler(Myhandler(remove))
	db.add_handler(MessageHandler(Filters.text,remove))
	db.add_handler(MessageHandler(Filters.status_update.new_chat_members,remove))
	db.add_handler(MessageHandler(Filters.status_update.left_chat_member,remove))
	db.add_handler(MessageHandler(Filters.status_update.pinned_message,remove))
	db.add_handler(MessageHandler(Filters.status_update.delete_chat_photo,remove))
	db.add_handler(MessageHandler(Filters.status_update.new_chat_photo,remove))
	db.add_handler(MessageHandler(Filters.status_update.new_chat_members,remove))
	db.add_handler(MessageHandler(Filters.status_update.new_chat_title,remove))
	db.add_handler(MessageHandler(Filters.status_update.migrate,remove))
	

    # Start the Bot
	updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
	updater.idle()


if __name__ == '__main__':
	main()
