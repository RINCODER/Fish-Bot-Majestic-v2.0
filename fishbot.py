import pyautogui,time,keyboard,json,wget,os,ahk,traceback,numpy
from ahk import AHK
from threading import *
from vk_api import *
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.utils import get_random_id
ahk = AHK(executable_path="AHK\AutoHotkey.exe")
authorize = vk_api.VkApi(token = "deb669035093ff633fee8e9271a4aba21bef38143bec8135b903e2c6a0d2f0c67a75aed3981d360fe2a89")
id = 0
turnoff = "n"
def write_message(id, message):
    authorize.method('messages.send', {'user_id': id, 'message': message, 'random_id': get_random_id()})

def pcturnoff():
    write_message(id,"Компьютер выключен")
    os.system('shutdown -s')

def programm():
    dropfish = 0 #рыба дропается
    timingfish = 0 #проверка на то что бот стоит в пизде
    path = "img/iconfish.jpg" #Поиск рыбы
    path2 = "img/iconbar.jpg" #Рыба поймана
    path3 = "img/exit.jpg" #Рыба сорвалась
    path4 = "img/checkfish.jpg" #проверка на закинутую удочку
    path5 = "img/inv.jpg" #проверка на забитие инвентаря
    path51 = "img/inv2.jpg" #проверка на забитие инвентаря 2
    path6 = "img/trade.jpg" #трейд
    point = "Старт"
    write_message(id,"🎣 Бот на рыбалку запущен")
    if os.path.isfile('2Hs21sfaz912kfha.json'):
        os.remove('2Hs21sfaz912kfha.json')
    while keyboard.is_pressed('p') != True and point != "exit":
        if point == "Старт":
            ahk.key_press("E")
            time.sleep(0.6)
            cords4 = pyautogui.locateCenterOnScreen(path4, confidence=0.6, grayscale=True, region=(14,20, 341,63))
            if cords4 != None:
                point = "Ожидание рыбы"
                print("Потверждение закинутой удочки")
                timingfish = time.time()

        elif point == "Ожидание рыбы":
            try:
                cords = pyautogui.locateCenterOnScreen(path,confidence=0.62,grayscale=True,region=(14,20, 341,63))
                cords2 = pyautogui.locateCenterOnScreen(path2, confidence=0.6 , grayscale=True, region=(14,20, 341,63))
                cords3 = pyautogui.locateCenterOnScreen(path3, confidence=0.6,region=(21,11,245,61))
                cords6 = pyautogui.locateCenterOnScreen(path6, confidence=0.6,region=(653, 411, 1263, 662))

                if cords3 != None:
                    ahk.key_up("A")
                    ahk.key_up("D")
                    time.sleep(1)
                    print("Рыба сорвалась")
                    dropfish += 1
                    if dropfish > 3:
                        write_message(id,"🚫 Внимание рыба часто срывается, возможно бота сдвинули с места")
                    if dropfish > 10:
                        write_message(id,"😢 Бот немного немного, видимо все плохо")
                        if turnoff == "y":
                            pcturnoff()
                    point = "Старт"


                elif time.time() - timingfish > 180:
                    point = "exit"
                    print("Похоже бота сбили")
                    e = 1
                    while e <= 10:
                        write_message(id, f"👾 Меня сбили, я не могу нормально работать хелп {e}/10")
                        e += 1
                    if turnoff == "y":
                        pcturnoff()


                elif cords6 != None:
                    ahk.mouse_move(1102, 606, speed=10, relative=True)
                    ahk.click(1102, 606)
                    point = "Старт"
                    print("Кто то кинул трейд")
                    write_message(id, f"⚠️Кто то кинул трейд... Закрыл его и продолжаю работать")

                elif cords2 != None:
                    print("Рыба поймана")
                    ahk.key_up("A")
                    ahk.key_up("D")
                    pyautogui.mouseDown()
                    time.sleep(18)
                    pyautogui.mouseUp()
                    point = "Старт"
                    cords5 = pyautogui.locateCenterOnScreen(path5, confidence=0.8, region=(748, 991, 1168, 1051))
                    cords51 = pyautogui.locateCenterOnScreen(path51, confidence=0.8,region=(748, 991, 1168, 1051))
                    if cords5 != None or cords51 != None:
                        point = "exit"
                        print("Инвентарь забился")
                        write_message(id, f"💼 Закончилось место в инвентаре, бот остановлен")
                        if turnoff == "y":
                            pcturnoff()

                elif cords.x < 955:
                    ahk.key_up("A")
                    ahk.key_down("D")
                elif cords.x > 955:
                    ahk.key_up("D")
                    ahk.key_down("A")
            except: pass
                # print(traceback.format_exc())
    helloing = Thread(target=hello)
    helloing.start()
    return

def hello():
    if os.path.isfile('2Hs21sfaz912kfha.json'):
        os.remove('2Hs21sfaz912kfha.json')
    print("----------------------------------------------------------------------------------------------------------\n----------------------------------------------------------------------------------------------------------\n----------------------------------------------------------------------------------------------------------\n----------------------------------------------------------------------------------------------------------\n----------------------------------------------------------------------------------------------------------\n                     Запускайте программу от имени Администратора!!!\n                     FISH BOT BETA v2.1 by RINCODE | Клавиша для запуска O для остановки P\n---------------------Возможны баги, так же бота нельзя остановить в определенных ситуациях----------------\n------------------------Для остановки бота зажмите P---------------------------------\n----------------------------------------------------------------------------------------------------------\n----------------------------------------------------------------------------------------------------------\n----------------------------------------------------------------------------------------------------------\n")
    while keyboard.is_pressed('O') != True:
        pass
    programming = Thread(target=programm)
    programming.start()
    return

def start():
    global id, turnoff
    did = {}
    d1 = {}
    print("Загрузка....")
    time.sleep(1)
    print("Проверка доступа.......")
    time.sleep(0.2)
    if os.path.isfile("auth.token"):
        print("Файл авторизации найден")
        time.sleep(0.2)
        print("Проверка ключа авторизации доступа к боту | Обновление данных ключа занимает 5-10 минут\nЗагрузка: [")
        time.sleep(0.2)
        if os.path.isfile('2Hs21sfaz912kfha.json'):
            os.remove('2Hs21sfaz912kfha.json')
        url = "https://raw.githubusercontent.com/Egortttf/fishbot_majestik/main/2Hs21sfaz912kfha.json"
        wget.download(url)
        time.sleep(0.2)
        print("]\nИнформация получена, проверка данных")
        try:
            with open("2Hs21sfaz912kfha.json", 'r', encoding='utf-8') as file:  # Заполнение данных в переменную
                d1 = json.load(file)
        except json.decoder.JSONDecodeError:
            pass
        try:
            with open("auth.token", 'r', encoding='utf-8') as file:  # Заполнение данных в переменную
                d2 = json.load(file)

        except json.decoder.JSONDecodeError:
            print("error")
        if os.path.isfile('2Hs21sfaz912kfha.json'):
            os.remove('2Hs21sfaz912kfha.json')
        time.sleep(0.5)
        try:
            if d1[d2["authtoken"]] == 1:
                print("Ключ доступа подошел")
                time.sleep(0.5)
                if os.path.isfile('2Hs21sfaz912kfha.json'):
                    os.remove('2Hs21sfaz912kfha.json')
                if os.path.isfile("vkapi.json"):
                    try:
                        with open("vkapi.json", 'r',encoding='utf-8') as file:  # Заполнение данных в переменную
                            did = json.load(file)
                            id = did["id"]
                    except json.decoder.JSONDecodeError:
                        pass
                else:
                    print("Нет подключения к VK")
                    time.sleep(0.5)
                    print("Присоеднитесь в группу VK https://https://vk.com/rincode \nЭто нужно для отправки вам уведомлений")
                    time.sleep(5)
                    try:
                        id = int(input("Введите ваш id в VK (узнать его можно тут: https://regvk.com/id/)\nВаш ID в VK: "))
                    except:
                        print("Вы ввели не число id нужно вводить так: 463379321")
                        if os.path.isfile('vkapi.json'):
                            os.remove('vkapi.json')
                            time.sleep(10)
                            return
                    did["id"] = id

                if id != 0 and id != None and id != "":
                    try:
                        open('vkapi.json', 'w').close()
                        with open('vkapi.json', 'w', encoding='utf-8') as file:  # Выгрузка данных в txt файл
                            json.dump(did, file, indent=3, ensure_ascii=False)
                    except: print("Проблемма с записью файла")
                    print("Сейчас бот отправит вам сообщение")
                    write_message(id, f"🔋 Успешный вход: id {id}\n🗝️Ключ доступа: {d2['authtoken']}")
                    if os.path.isfile('2Hs21sfaz912kfha.json'):
                        os.remove('2Hs21sfaz912kfha.json')
                    time.sleep(3)
                    turnoff = input("Вы хотите чтобы пк сам выключился, если инвентарь забется, бот перестанет рыбачить?\nВведите Y для включения функции| N - для выключения\nВыключать пк?: ").lower()
                    if turnoff != "y" and turnoff !="n":
                        print(f"Вы ввели неверное значение вы отправили: {turnoff} а нужно было y или n")
                        time.sleep(3)
                        starting = Thread(target=start)
                        starting.start()
                        return
                    helloing = Thread(target=hello)
                    helloing.start()
                    return
            else:
                print("Ключ авторизации не подходит, пишите сюда: https://funpay.com/users/3779790/")
                if os.path.isfile('2Hs21sfaz912kfha.json'):
                    os.remove('2Hs21sfaz912kfha.json')
                input()
        except:
            print("Ключа не существует, пишите сюда: https://funpay.com/users/3779790/ или вы ввели не верный VK ID")
            if os.path.isfile('2Hs21sfaz912kfha.json'):
                os.remove('2Hs21sfaz912kfha.json')
            input()

    else:
        print("Файл авторизации не найден, пишите сюда: https://funpay.com/users/3779790/")
        if os.path.isfile('2Hs21sfaz912kfha.json'):
            os.remove('2Hs21sfaz912kfha.json')
        input()

starting = Thread(target = start)
starting.start()

