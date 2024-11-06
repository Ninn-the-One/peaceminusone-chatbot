from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, CallbackContext

# Define the options for the /start command
async def start(update: Update, context: CallbackContext) -> None:
    # Define the inline keyboard with 2 options
    keyboard = [
        [InlineKeyboardButton("Add me to my group", callback_data='add_peaceminusone')],
        # Direct link to login without confirmation
        [InlineKeyboardButton("Log in to PEACEMINUSONE", web_app=WebAppInfo(url="https://peaceminusone-chatbot.herokuapp.com/dashboard.html"))]
    ]
    
    # Create the inline keyboard markup
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    # Send the message with the inline keyboard
    await update.message.reply_text("Welcome to PEACEMINUSONE!\n" 
                                    "I am a Telegram bot for managing your Telegram groups.\n\n" 
                                    "Please choose the option below:\n\n"
                                    "1. Add me to your group - become your assistant to manage your group.\n\n"
                                    "2. Log in to PEACEMINUSONE - Go straight to your dashboard for group management.", 
                                    reply_markup=reply_markup)

# Define a function to handle button presses
async def button(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    await query.answer()
    
    # Handle different button presses (for callback buttons, not for URL buttons)
    if query.data == 'add_peaceminusone':
        # Message instructing user to add the bot to a group
        await query.edit_message_text(text=
                                        "To add me to your group, please follow these steps:\n"
                                        "1. Go to your group chat on Telegram.\n"
                                        "2. Tap on the group name at the top of the screen.\n"
                                        "3. Select 'Add member' and search for my name.\n"
                                        "4. Add me to your group to start managing it!")
    # No need to handle "login_peaceminusone" as it's a direct URL button

# Main function to set up the bot
def main():
    # Replace YOUR_TOKEN with your bot's token from BotFather
    application = Application.builder().token("7600399326:AAGbRK3yWgGvUR7s_t2i2c2OrdX86idVXC0").build()

    # Register the /start command handler
    application.add_handler(CommandHandler("start", start))
    
    # Register the button handler
    application.add_handler(CallbackQueryHandler(button))

    # Start polling for updates
    application.run_polling()

if __name__ == '__main__':
    main()
