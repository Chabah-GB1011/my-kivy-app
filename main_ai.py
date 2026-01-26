import os
from gtts import gTTS
from textblob import TextBlob
from PIL import Image

def speak(text):
    # تحويل النص إلى صوت وحفظه كمؤقت
    tts = gTTS(text=text, lang='ar')
    tts.save("response.mp3")
    # تشغيل الصوت في Termux
    os.system("mpv --no-video response.mp3 > /dev/null 2>&1")

def start_voice_ai():
    print("\n🎤 [المساعد الصوتي قيد الانتظار...]")
    speak("أهلاً يا محمد، كيف يمكنني مساعدتك اليوم؟")
    
    while True:
        print("\n1. تحدث (نص) | 2. استعراض ملفات | 3. خروج")
        cmd = input("أدخل رقم المهمة أو اكتب أمرك: ")

        if cmd == '1':
            user_say = input("🗨️ ماذا تريد أن تقول؟: ")
            sentiment = TextBlob(user_say).sentiment.polarity
            response = "كلامك يبدو إيجابياً وجميلاً" if sentiment >= 0 else "يبدو أنك منزعج قليلاً"
            print(f"🤖 الرد: {response}")
            speak(response)

        elif cmd == '2':
            path = "/sdcard/Download/"
            files = [f for f in os.listdir(path) if f.lower().endswith(('.jpg', '.mp4'))]
            if files:
                msg = f"وجدت لك {len(files)} ملفات في مجلد التحميلات"
                print(f"📂 {msg}")
                speak(msg)
                for i, f in enumerate(files[:5]): print(f"[{i+1}] {f}")
            else:
                speak("لا توجد ملفات حالياً")

        elif cmd == '3':
            speak("وداعاً يا بطل، أراك لاحقاً")
            break

start_voice_ai()
