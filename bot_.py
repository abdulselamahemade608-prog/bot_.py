import telebot
import mysql.connector

bot = telebot.TeleBot("7750018949:AAFwmVZ1arhMG7r3t5yZGm4HhyyhYeTR-MI")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "እንኳን ደህና መጡ! የተማሪ መታወቂያ ቁጥር ይላኩ።")

@bot.message_handler(func=lambda message: True)
def get_student(message):
    # InfinityFree ዳታቤዝዎን ከኢንተርኔት ያነባል
    db = mysql.connector.connect(
        host="sql302.infinityfree.com",
        user="if0_42086616",
        password="abdueditor25",
        database="if0_42086616_school13"
    )
    cursor = db.cursor()
    cursor.execute(f"SELECT full_name FROM students WHERE student_id = '{message.text}'")
    result = cursor.fetchone()
    
    if result:
        bot.reply_to(message, f"✅ የተማሪ ስም: {result[0]}")
    else:
        bot.reply_to(message, "❌ አልተገኘም")

bot.polling()
