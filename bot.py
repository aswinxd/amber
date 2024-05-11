from telegram.ext import Updater, CommandHandler
from telegram import ChatPermissions

# Function to handle the /start command
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hello! I am your bot.")

# Function to handle the /clone command
def clone(update, context):
    # Check if the user has provided a bot token
    if len(context.args) > 0:
        # Extract the bot token from the message
        new_token = context.args[0]
        
        # Create a new updater object using the provided token
        new_updater = Updater(token=new_token, use_context=True)
        
        # Start polling for updates with the new updater
        new_updater.start_polling()

        context.bot.send_message(chat_id=update.effective_chat.id, text="Bot cloned successfully.")
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Please provide a bot token to clone.")
# Function to handle errors
def error(update, context):
    print(f"Update {update} caused error {context.error}")

# Function to start the bot
def main():
    # Replace 'YOUR_TOKEN' with your bot's token
    TOKEN = '7111525295:AAHNh9AQJ4Wejldqm_qb-3P37c4HGGkAAus'
    updater = Updater(token=TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    # Add command handlers
    start_handler = CommandHandler('start', start)
    clone_handler = CommandHandler('clone', clone)
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(clone_handler)

    # Add error handler
    dispatcher.add_error_handler(error)

    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
