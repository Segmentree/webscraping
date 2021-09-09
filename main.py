import vote_lib
import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

VOTE, CYCLES, SLEEP = range(3)
size = 0


# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi! master')


def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')


def vote(update, context):
    global size
    size = 0
    """Vote with a custom user"""
    update.message.reply_text('Enter a number of cycles')
    return SLEEP


def sleep_time(update, context):
    global size
    try:
        size = int(update.message.text)
        update.message.reply_text(
            'Enter an interval in seconds ex: 120 [means that a vote will occur every two minutes]')
        return CYCLES
    except:
        update.message.reply_text(
            'There was an error please check if the input is a valid number')
        return VOTE


def start_vote_proccess(update, context):
    try:
        interval = int(update.message.text)
        update.message.reply_text(
            f'A cycle of {size} iterations and an interval {interval} is running now please wait to finish to use again the /vote command')
        total, succes = vote_lib.engine(size,
                                        update.message.reply_text, interval)
        update.message.reply_text(
            f'There was {succes} succes votes of a total of {total}')
        update.message.reply_text('The process has finished successfully')
    except:
        update.message.reply_text(
            'There was an error please check if the input is a valid number')
    return VOTE


def echo(update, context):
    """Echo the user message."""
    update.message.reply_text(update.message.text)


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater(
        "1996037339:AAHFMfNkXMeI-_Da-JBDhqCKazanD4d7hx0", use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(
        ConversationHandler(
            entry_points=[CommandHandler("vote", vote)],
            fallbacks=[],
            states={
                CYCLES: [MessageHandler(Filters.text, start_vote_proccess)],
                VOTE: [CommandHandler("vote", vote)],
                SLEEP: [MessageHandler(Filters.text, sleep_time)]
            }
        )
    )

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, echo))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
