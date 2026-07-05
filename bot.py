import telebot
import mysql.connector
import time

# የቴሌግራም ቦት ቶከን
BOT_TOKEN = "7750018949:AAFwmVZ1arhMG7r3t5yZGm4HhyyhYeTR-MI"
bot = telebot.TeleBot(BOT_TOKEN)

# የዳታቤዝ ግንኙነት ፋንክሽን
def get_student_data(student_id):
    try:
        db = mysql.connector.connect(
            host="sql302.infinityfree.com",
            user="if0_42086616",
            password="abdueditor25",
            database="if0_42086616_school13"
        )
        cursor = db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM students WHERE student_id = %s", (student_id,))
        result = cursor.fetchone()
        db.close()
        return result
    except Exception as e:
        print(f"የዳታቤዝ ስህተት: {e}")
        return None

# /start ኮማንድ
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "እንኳን ደህና መጡ! እባክዎን የተማሪ መታወቂያ ቁጥር ይላኩልኝ።")

# መልእክት ሲደርሰው
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    student_id = message.text.strip()
    student = get_student_data(student_id)
    
    if student:
        reply = f"✅ <b>የተማሪ መረጃ ተገኝቷል!</b>\n\n"
        reply += f"👤 ስም: {student['full_name']}\n"
        reply += f"🎓 ክፍል: {student['grade_level']} {student['student_class']}"
        bot.reply_to(message, reply, parse_mode="HTML")
    else:
        bot.reply_to(message, f"❌ ይቅርታ፣ በዚህ መታወቂያ ({student_id}) የተመዘገበ ተማሪ አልተገኘም።")

print("ቦቱ እየሰራ ነው...")
bot.polling(none_stop=True)
