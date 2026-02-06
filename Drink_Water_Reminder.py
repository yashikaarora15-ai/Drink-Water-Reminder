#using plyer to push notification 
from plyer import notification
import time
import win32com.client as wincl

# Initialize text-to-speech
speaker = wincl.Dispatch("SAPI.SpVoice")
voices = speaker.GetVoices()
speaker.Voice = voices.Item(1)  # Change index if you want another voice ex '0' for male voice


def send_water_notification(title, message, timeout=10):
    #Sends a desktop notification and speaks the title aloud.
   
    notification.notify(
        title=title,
        message=message,
        app_name="Drink Water Reminder",
        timeout=timeout
    )
    speaker.Speak(title)


# Time interval (in seconds)
REMINDER_INTERVAL = 60 * 60  # 1 hour

print("Drink Water Reminder started. Press Ctrl+C to stop.")

try:
    while True:
        send_water_notification(
            "Time to Drink Water!",
            "Hey Yashika ,Stay hydrated. Please drink a glass of water.",
            timeout=10
        )
        time.sleep(REMINDER_INTERVAL)

except KeyboardInterrupt:
    print("\nWater reminder stopped. Stay healthy!")
