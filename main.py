import os
import telebot
import reply
from reply import get_response

bot = telebot.TeleBot(os.environ['API_KEY'])


@bot.message_handler(commands=['start'])
def start(message):
  bot.send_message(
      message.chat.id,
      "Hi! I'm a bot, created by  @donkorBN to help you with stress. Don't text me if you're not stressed please"
  )


@bot.message_handler(commands=['greet'])
def greet(message):
  bot.send_message(message.chat.id, "Hey! How's it going?")


@bot.message_handler(commands=['about'])
def about(message):
  bot.send_message(
      message.chat.id,
      "🤖 About This Bot 🤖 => I'm here to provide support and motivation to students facing stress and depression. Life as a student can be challenging, but you're not alone on this journey. I'm here to lend a helping hand and offer words of encouragement when you need them the most. Let's work together to overcome challenges and stay motivated. Remember, you've got what it takes to succeed! If you have any questions or need assistance, feel free to reach out. 🌟 #YouAreNotAlone"
  )


@bot.message_handler(func=lambda message: True)
def handle_text(message):
  bot_response = get_response(
      message.text)  # Pass the message text to get_response
  bot.send_message(message.chat.id, bot_response)  # Send the response


bot.polling()
