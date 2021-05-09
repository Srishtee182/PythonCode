
from playsound import playsound
from threading import Timer
from datetime import datetime

currentTime = datetime.now().strftime('%H:%M:%S')
start = '20:19:00'
end = '23:50:20'
print(currentTime)


def isNowInTimePeriod(startTime, endTime, nowTime):
    if startTime < nowTime < endTime:
        playsound("Gargling-Water.mp3")


isNowInTimePeriod(start, end, currentTime)
