import time
import webbrowser as wb
import JARVIS_v1 as J
def Alarm():
    print("work")
    if "20:12" == str(time.datetime.now().strftime("%H:%M")):
        J.say("Es hora de seguir estudiando Python para aumentar su conocimiento y poder mejorarme señor")
        wb.open_new_tab("")
        
        print("well")
    else:
        time.sleep(10)
        Alarm()

