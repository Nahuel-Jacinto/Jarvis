
from datetime import datetime
import speech_recognition as sr
import pyttsx3
import webbrowser as wb
import time
import wikipedia
# Corazón
engine = pyttsx3.init()
import Alarm_TATA as AT

# Configuración de Voz

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

voiceRate = 200
engine.setProperty('rate', voiceRate)




dicc_names = 'dcc/dicc_names.txt'
dicc_presentation = 'dcc/dicc_presentation.txt'
dicc_sp_names = 'dcc/dicc_sp_names.txt'
dicc_wkp = 'dcc/dicc_wkp.txt'
dicc_ON_dsp = "dcc/dicc_ON_dsp.txt"
dicc_OFF_dsp = "dcc/dicc_OFF_dsp.txt"

ON_DSP = {None}
OFF_DSP = {None}
names={None}
wkp ={None}
sp_names={None}
presentations={None}
speaked={None}
dicc_cd_general = [dicc_names,dicc_presentation,dicc_sp_names, ON_DSP, OFF_DSP]
dicc_general = [names, presentations, sp_names]

#salto de linea necesario al final de cada diccionario

wikipedia.set_lang("es")
#region Essencials

def say(audio):
    engine.say(audio)
    engine.runAndWait()

def Listen(query):
    engine.runAndWait()
    Recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Escuchando...")
        Recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = Recognizer.listen(source)
    try:
        print("Reconociendo...")
        query = Recognizer.recognize_google(audio, language ="es-ES")
        #query_en = r.recognize_google(audio, language ="es-EN")
        print(query)
        return query
    except:
        pass
def Update_dicc():
    val_0 = -1
    dicc = [dicc_names,dicc_presentation,dicc_sp_names,dicc_wkp, dicc_ON_dsp, dicc_OFF_dsp]
    dicc_set = [names, presentations, sp_names,wkp, ON_DSP, OFF_DSP]
    for i in dicc:
        val_0+=1
        words = ""
        with open(i, encoding="utf-8") as file:
            dicc_read = file.read()
            for letters in dicc_read:
                if (letters != "\n"):
                    words += letters
                else:                   
                    dicc_set[val_0].add(words)
                    words = ""
#endregion 



#region Functions
def add_comand():
    val_b = False
    say("desea agregar una nueva palabra a la libreria")
    val_v = 99
    val_b = False
    if 'sí' in str(Listen(query="")):
        say("A que diccionario de funcion desea añadirlo")
        print("Diccionario de funcion...")
        val_d = Listen("")
        if 'nombres' in val_d:
            val_v = 0
            val_b = True
        elif 'presentación' in val_d:
            val_v = 1
            val_b = True
        elif "nombres especiales" in val_d:
            val_v = 2
            val_b = True
        elif "Wikipedia" in val_d:
            val_v = 3
            val_b = True
        elif "encendido de dispositivos" in val_d:
            val_v = 4
            val_b = True
        elif "apagado de dispositivos" in val_d:
            val_v = 5
            val_b = True            
        else:
            say("No se logro reconocer un diccionario")
            functions()
        if val_d:
            say(f"repita el nuevo comando para agregar al diccionario de {str(dicc_general[val_v])}")
            new_word = str(Listen(""))
            print("Repeat...")

            with open(dicc_cd_general[val_v], 'a', encoding="utf-8") as dicc:
                    dicc.write(new_word + '\n')
                    say("nueva palabra "+new_word +" adquirida")
                    dicc.close()
                    Update_dicc()
                    print(new_word + " añadida")
                    functions()
        else:
            say("palabras descartadas")
            functions()


#endregion

#region Special Functions
def Cantinero():
    say("Que lo disfrute señor")
    wb.open_new_tab("https://Instagram.com/nahu_dev")
    functions()




#endregion


def functions():
    f = 0
    test0 = []
    def_search = ""
    speaked.clear()
    
    Upper_str_speaked = str(Listen(query=""))+ " "
    if(Upper_str_speaked != " "):
        str_speaked = str.lower(Upper_str_speaked)
    cache_word_0 = ""    
    for z in str_speaked:
            if(z !=" "):
                cache_word_0 += z
            else: 
                speaked.add(str(cache_word_0))
                cache_word_0 = ""
    print(speaked)
    for name in names:
        for speak in speaked:
            for solve_0 in speaked:
                test0.append(str(solve_0))
            if speak == name:
                for presentation in speaked:
                    for present in presentations:
                        if presentation == present:
                            pres()
                for definitions in speaked:
                    
                    for definition in wkp:
                            
                        if definition == definitions:
                            for a in speaked:
                                f += 1
                                if a == definition:                                   
                                    define = str(test0[f])
                                    resultado = wikipedia.summary(define, sentences = 2)
                                    say(resultado)

                if "diccionario" in speaked:
                    print(names)
                    print(sp_names)
                    print(presentations)

                elif "función agregar" in str_speaked:
                    add_comand()
                elif "actualiza las palabras":
                    Update_dicc()
    for sp_name in names:
        for speak in speaked:
            if sp_name == speak:
                if("dame lo de siempre" in str_speaked):
                    Cantinero()
                
    functions()
    #recog()
                
    
def pres():
    say("Hola señor")
    



Update_dicc()
say("hola de nuevo señor")
functions()
