# coding=utf-8

from tkinter import *#Label, Button, Entry
import time

#self.label = Label (self.master, text = "Controller")
#self.label.pack ()

#self.ip_entry = Entry(self.master, text="enter robot ip")
#self.ip_entry.pack (side=TOP)

#self.ip_button = Button (self.master, text="изменить ip", command = self.change_ip)
#self.ip_button.pack (side=TOP)

#self.wiki_button = Button (self.master, text="Поиск в Википедии", command = self.set_wiki_search)
#self.wiki_button.pack (side=TOP)

#self.close_button = Button (self.master, text = "Close", command = self.join_and_exit)
#self.close_button.pack (side=TOP)

class Main_window:
    def __init__ (self, master_, robot_state_):
        self.master = master_
        self.master.title ("Controller")

        #self.label = Label (self.master, text = "Controller").grid (row=0)
        
        self.ip_entry = Entry(self.master, text="enter robot ip")
        self.ip_entry.grid (row=0, column=0)
        
        self.ip_button = Button (self.master, text="Изменить ip", command = self.change_ip, height=3, width = 25)
        self.ip_button.grid (row=1, column=0)
        
        self.wiki_button = Button (self.master, text="Википедия", command = self.set_wiki_search, height=3, width = 25)
        self.wiki_button.grid (row=2, column=0)
                
        #self.football_button = Button (self.master, text="Футбол", command = self.set_play_football, height=3, width = 25)
        #self.football_button.grid (row=3, column=0)

        #self.football_button = Button (self.master, text="Остановить футбол", command = self.stop_football, height=3, width = 25)
        #self.football_button.grid (row=4, column=0)

        self.best_button = Button (self.master, text="Лучший футбольный клуб", command = self.best, height=3, width = 25)
        self.best_button.grid (row=5, column=0)

        self.cska_button = Button (self.master, text="ЦСКА", command = self.cska, height=3, width = 25)
        self.cska_button.grid (row=6, column=0)

        self.zenit_button = Button (self.master, text="Зенит", command = self.zenit, height=3, width = 25)
        self.zenit_button.grid (row=3, column=0)

        self.spartak_button = Button (self.master, text="Спартак", command = self.spartak, height=3, width = 25)
        self.spartak_button.grid (row=4, column=0)

        #----------------------------------------------------------------------

        self.litso_button = Button (self.master, text="Лицо попроще", command = self.litso, height=3, width = 25)
        self.litso_button.grid (row=0, column=1)

        self.stih_button = Button (self.master, text="Стихотворение", command = self.stih, height=3, width = 25)
        self.stih_button.grid (row=1, column=1)

        self.bomba1_button = Button (self.master, text="Про бомбу", command = self.bomba1, height=3, width = 25)
        self.bomba1_button.grid (row=2, column=1)

        self.bomba2_button = Button (self.master, text="Про коронавирусную бомбу", command = self.bomba2, height=3, width = 25)
        self.bomba2_button.grid (row=3, column=1)

        self.pesnia_button = Button (self.master, text="Песня", command = self.pesnia, height=3, width = 25)
        self.pesnia_button.grid (row=4, column=1)

        self.basta_button = Button (self.master, text="Баста", command = self.basta, height=3, width = 25)
        self.basta_button.grid (row=5, column=1)

        self.jigan_button = Button (self.master, text="Жиган", command = self.jigan, height=3, width = 25)
        self.jigan_button.grid (row=6, column=1)

        self.hb_button = Button (self.master, text="C Днем Рождения!", command = self.hb, height=3, width = 25)
        self.hb_button.grid (row=7, column=1)

        self.dance1_button = Button (self.master, text="Танец 1", command = self.dance1, height=3, width = 25)
        self.dance1_button.grid (row=7, column=0)

        #----------------------------------------------------------------------

        self.dance2_button = Button (self.master, text="Танец 2", command = self.dance2, height=3, width = 25)
        self.dance2_button.grid (row=0, column=2)

        self.dance1_button = Button (self.master, text="Танец 3", command = self.dance3, height=3, width = 25)
        self.dance1_button.grid (row=1, column=2)

        self.hb_button = Button (self.master, text="Cтоп", command = self.stop, height=3, width = 25)
        self.hb_button.grid (row=2, column=2)

        self.greet_button = Button (self.master, text = "Привет", command = self.greet, height=3, width = 25)
        self.greet_button.grid (row=3, column=2)

        self.stand_button = Button (self.master, text = "Встань", command = self.stand, height=3, width = 25)
        self.stand_button.grid (row=4, column=2)

        self.rest_button = Button (self.master, text = "Сядь", command = self.rest, height=3, width = 25)
        self.rest_button.grid (row=5, column=2)

        self.udalen_button = Button (self.master, text = "Удален", command = self.udalen, height=3, width = 25)
        self.udalen_button.grid (row=6, column=2)

        #self.send_ths_button = Button (self.master, text = "Синхронизировать зрение", command = self.send_ths, height=3, width = 25)
        #self.send_ths_button.grid (row=7, column=2)
        
        self.close_button = Button (self.master, text = "Закрыть", command = self.join_and_exit, height=3, width = 25)
        self.close_button.grid (row=7, column=2)
        
        self.robot_state = robot_state_
        
        self.idle ()
        
    
    def send_ths (self):
        self.robot_state.send_ths ()
    
    def greet (self):
        curr = time.time ()
        
        command1 = {"type"           : "action",
                   "execution_time" : curr,
                   "contents"       : "/greet",
                   "parameter"      : "a"}
        
        self.robot_state.add_commands_to_queue ([command1])

    def udalen (self):
        curr = time.time ()
        
        command1 = {"type"           : "action",
                   "execution_time" : curr,
                   "contents"       : "/sit",
                   "parameter"      : "a"}

        command2 = {"type"           : "action",
                   "execution_time" : curr + 8,
                   "contents"       : "/lyingback",
                   "parameter"      : "a"}

        command3 = {"type"           : "action",
                   "execution_time" : curr + 16,
                   "contents"       : "/play_mp3",
                   "parameter"      : "4ston.mp3"}
        
        self.robot_state.add_commands_to_queue ([command1, command2, command3])

    def stand (self):
        curr = time.time ()
        
        command1 = {"type"           : "action",
                   "execution_time" : curr,
                   "contents"       : "/stand",
                   "parameter"      : "a"}
        
        self.robot_state.add_commands_to_queue ([command1])

    def rest (self):
        curr = time.time ()
        
        command1 = {"type"           : "action",
                   "execution_time" : curr,
                   "contents"       : "/rest",
                   "parameter"      : "a"}
        
        self.robot_state.add_commands_to_queue ([command1])
    
    def idle (self):
        self.robot_state.on_idle ()
        
        self.master.after (1000, self.idle)

    def join_and_exit (self):
        #self.robot_state.join ()
        self.master.quit ()

    def change_ip (self):
        new_ip = self.ip_entry.get()
        
        print ("new ip is", new_ip)
        
        self.robot_state.change_ip (new_ip)

    def set_wiki_search (self):
        print ("changing robot state to wiki_search")
        
        command = {"type"           : "state_change",
                   "execution_time" : 0,
                   "contents"       : "wiki_search",
                   "parameter"      : None}
        
        self.robot_state.add_commands_to_queue ([command])

    def set_play_football (self):
        print ("changing robot state to play_football")
        command = {"type"           : "state_change",
                   "execution_time" : 0,
                   "contents"       : "playing_football",
                   "parameter"      : None}
        
        self.robot_state.add_commands_to_queue ([command])

    def stop_football (self):
        print ("changing robot state to waiting")
        command = {"type"           : "state_change",
                   "execution_time" : 0,
                   "contents"       : "waiting",
                   "parameter"      : None}
        
        self.robot_state.add_commands_to_queue ([command])

    def best (self):
        curr = time.time ()
        
        command1 = {"type"           : "action",
                   "execution_time" : curr,
                   "contents"       : "/play_mp3",
                   "parameter"      : "3kakoiklub.mp3"}
        
        self.robot_state.add_commands_to_queue ([command1])

    def cska (self):
        curr = time.time ()
        
        command1 = {"type"           : "action",
                   "execution_time" : curr,
                   "contents"       : "/play_mp3",
                   "parameter"      : "6rasskazhi.mp3"}
        
        self.robot_state.add_commands_to_queue ([command1])

    def zenit (self):
        #print ("zenit mp3")
        curr = time.time ()
        
        command1 = {"type"           : "action",
                   "execution_time" : curr,
                   "contents"       : "/play_mp3",
                   "parameter"      : "7zenit1.mp3"}
        
        command2 = {"type"           : "action",
                   "execution_time" : curr + 7,
                   "contents"       : "/play_mp3",
                   "parameter"      : "7zenit2.mp3"}
        
        self.robot_state.add_commands_to_queue ([command1, command2])

    def spartak (self):
        curr = time.time ()
        
        command1 = {"type"           : "action",
                   "execution_time" : curr,
                   "contents"       : "/play_mp3",
                   "parameter"      : "8spartak.mp3"}
        
        self.robot_state.add_commands_to_queue ([command1])

    def litso (self):
        curr = time.time ()
        
        command1 = {"type"           : "action",
                   "execution_time" : curr,
                   "contents"       : "/play_mp3",
                   "parameter"      : "2litso.mp3"}
        
        self.robot_state.add_commands_to_queue ([command1])

    def stih (self):
        curr = time.time ()
        
        command1 = {"type"           : "action",
                   "execution_time" : curr,
                   "contents"       : "/play_mp3",
                   "parameter"      : "10giner.mp3"}
        
        self.robot_state.add_commands_to_queue ([command1])

    def bomba1 (self):
        curr = time.time ()
        
        command1 = {"type"           : "action",
                   "execution_time" : curr,
                   "contents"       : "/play_mp3",
                   "parameter"      : "10bomba1.mp3"}
        
        self.robot_state.add_commands_to_queue ([command1])

    def bomba2 (self):
        curr = time.time ()
        
        command1 = {"type"           : "action",
                   "execution_time" : curr,
                   "contents"       : "/play_mp3",
                   "parameter"      : "10bomba2.mp3"}
        
        self.robot_state.add_commands_to_queue ([command1])

    def pesnia (self):
        curr = time.time ()
        
        command1 = {"type"           : "action",
                   "execution_time" : curr,
                   "contents"       : "/play_mp3",
                   "parameter"      : "11basta.mp3"}

        command2 = {"type"           : "action",
                   "execution_time" : curr,
                   "contents"       : "/play_mp3",
                   "parameter"      : "11jigan.mp3"}
        
        self.robot_state.add_commands_to_queue ([command1, command2])

    def basta (self):
        curr = time.time ()
        
        command1 = {"type"           : "action",
                   "execution_time" : curr,
                   "contents"       : "/play_mp3",
                   "parameter"      : "11basta.mp3"}
        
        self.robot_state.add_commands_to_queue ([command1])

    def jigan (self):
        curr = time.time ()
        
        command2 = {"type"           : "action",
                   "execution_time" : curr,
                   "contents"       : "/play_mp3",
                   "parameter"      : "11jigan.mp3"}
        
        self.robot_state.add_commands_to_queue ([command2])

    def hb (self):
        curr = time.time ()
        
        command2 = {"type"           : "action",
                   "execution_time" : curr,
                   "contents"       : "/play_mp3",
                   "parameter"      : "14stih.mp3"}
        
        self.robot_state.add_commands_to_queue ([command2])

    def dance1 (self):
        curr = time.time ()
        
        command1 = {"type"           : "action",
                   "execution_time" : curr,
                   "contents"       : "/play_mp3",
                   "parameter"      : "music1.mp3"}
        
        command2 = {"type"           : "action",
                   "execution_time" : curr,
                   "contents"       : "/dance_tai",
                   "parameter"      : "14stih.mp3"}
        
        self.robot_state.add_commands_to_queue ([command1, command2])

    def dance2 (self):
        curr = time.time ()
        
        command1 = {"type"           : "action",
                   "execution_time" : curr,
                   "contents"       : "/play_mp3",
                   "parameter"      : "music2.mp3"}
        
        command2 = {"type"           : "action",
                   "execution_time" : curr,
                   "contents"       : "/dance_rock",
                   "parameter"      : "14stih.mp3"}
        
        self.robot_state.add_commands_to_queue ([command1, command2])
        
    def dance3 (self):
        curr = time.time ()
        
        command1 = {"type"           : "action",
                   "execution_time" : curr,
                   "contents"       : "/play_mp3",
                   "parameter"      : "music3.mp3"}
        
        command2 = {"type"           : "action",
                   "execution_time" : curr,
                   "contents"       : "/dance_disco",
                   "parameter"      : "14stih.mp3"}
        
        self.robot_state.add_commands_to_queue ([command1, command2])

    def stop (self):
        self.robot_state.stop ()
