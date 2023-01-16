from android.permissions import request_permissions, Permission
request_permissions([Permission.WRITE_EXTERNAL_STORAGE])
from android.storage import app_storage_path, primary_external_storage_path, secondary_external_storage_path
#импорты выше только для android сборки
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.audio import SoundLoader
from kivy.properties import StringProperty, ObjectProperty, NumericProperty
from kivy.uix.button import Button
from kivy.base import runTouchApp
from kivy.uix.scrollview import ScrollView
from kivy.clock import Clock
from kivy.logger import Logger
import os
from os.path import join
from kivy.core.window import Window
Window.clearcolor = (1, 1, 1, 1)

code_p = 0
age_p = 0
edu_p = 0
email_p = ''
answers_p = []
#Defining screens
class PrefirstWindow(Screen):
    pass
class FirstWindow(Screen):
    global code_p, age_p, edu_p, email_p
    code = ObjectProperty(None)
    age = ObjectProperty(None)
    edu = ObjectProperty(None)
    email = ObjectProperty(None)
    def prrr (self):
        global code_p, age_p, edu_p, email_p
        code_p = self.code.text
        age_p = self.age.text
        edu_p = self.edu.text
        email_p = self.email.text
        print(code_p, age_p, edu_p, email_p)
    pass
class SecondWindow(Screen):
    global answers_p
    sumka = ObjectProperty(None)
    sapog = ObjectProperty(None)
    tsep = ObjectProperty(None)
    kulak = ObjectProperty(None)
    chay = ObjectProperty(None)
    okno = ObjectProperty(None)
    volosy = ObjectProperty(None)
    devochka = ObjectProperty(None)
    telefon = ObjectProperty(None)
    most = ObjectProperty(None)
    divan = ObjectProperty(None)
    portret = ObjectProperty(None)
    scheka = ObjectProperty(None)
    pismo = ObjectProperty(None)
    kletka = ObjectProperty(None)
    class SuperButton(Button):
        colors = [[0,1,0, 1], [1,0,0,1]]
        def __init__ (self, number=0, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.number = 0
            self.color = [30/256, 19/256, 23/256,1]
            
    class AudioButton(Button):
        filename = StringProperty(None)
        sound = ObjectProperty(None, allownone=True)
        def on_press(self):
            if self.sound is None:
                self.sound = SoundLoader.load(self.filename)
        # stop the sound if it's currently playing
            if self.sound.status != 'stop':
                self.sound.stop()
            self.sound.volume = 1
            self.sound.play()
        def release_audio(self):
            if self.sound:
                self.sound.stop()
                self.sound.unload()
                self.sound = None
    def btn_press(self, instance):
        instance.background_color = colors[instance.number%2]
        instance.background_normal = ''
        instance.number +=1
        
        print(instance.number)
    def save_answers(self):
        if self.ids.retret.sound:
            self.ids.retret.sound.stop()
        answers = []
        answers.append(self.sumka.number%2)
        answers.append(self.sapog.number%2)
        answers.append(self.tsep.number%2)
        answers.append(self.kulak.number%2)
        answers.append(self.chay.number%2)
        answers.append(self.okno.number%2)
        answers.append(self.volosy.number%2)
        answers.append(self.devochka.number%2)
        answers.append(self.telefon.number%2)
        answers.append(self.most.number%2)
        answers.append(self.divan.number%2)
        answers.append(self.portret.number%2)
        answers.append(self.scheka.number%2)
        answers.append(self.pismo.number%2)
        answers.append(self.kletka.number%2)
        answers_p.append(answers)
        print(answers)
    pass
class ThirdWindow(Screen):
    global answers_p
    sumka = ObjectProperty(None)
    sapog = ObjectProperty(None)
    tsep = ObjectProperty(None)
    kulak = ObjectProperty(None)
    chay = ObjectProperty(None)
    okno = ObjectProperty(None)
    volosy = ObjectProperty(None)
    devochka = ObjectProperty(None)
    telefon = ObjectProperty(None)
    most = ObjectProperty(None)
    divan = ObjectProperty(None)
    portret = ObjectProperty(None)
    scheka = ObjectProperty(None)
    pismo = ObjectProperty(None)
    kletka = ObjectProperty(None)
    class SuperButton(Button):
        colors = [[0,1,0, 1], [1,0,0,1]]
        def __init__ (self, number=0, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.number = 0
            self.color = [30/256, 19/256, 23/256,1]
            
    class AudioButton(Button):
        filename = StringProperty(None)
        sound = ObjectProperty(None, allownone=True)
        def on_press(self):
            self.sound.stop()
            if self.sound is None:
                self.sound = SoundLoader.load(self.filename)
        # stop the sound if it's currently playing
            if self.sound.status != 'stop':
                self.sound.stop()
            self.sound.volume = 1
            self.sound.play()
        def release_audio(self):
            if self.sound:
                self.sound.stop()
                self.sound.unload()
                self.sound = None
    def btn_press(self, instance):
        instance.background_color = colors[instance.number%2]
        instance.background_normal = ''
        instance.number +=1
        
        print(instance.number)
    def save_answers(self):
        if self.ids.retret.sound:
            self.ids.retret.sound.stop()
        answers = []
        answers.append(self.sumka.number%2)
        answers.append(self.sapog.number%2)
        answers.append(self.tsep.number%2)
        answers.append(self.kulak.number%2)
        answers.append(self.chay.number%2)
        answers.append(self.okno.number%2)
        answers.append(self.volosy.number%2)
        answers.append(self.devochka.number%2)
        answers.append(self.telefon.number%2)
        answers.append(self.most.number%2)
        answers.append(self.divan.number%2)
        answers.append(self.portret.number%2)
        answers.append(self.scheka.number%2)
        answers.append(self.pismo.number%2)
        answers.append(self.kletka.number%2)
        answers_p.append(answers)
        print(answers)
    pass
class FourthWindow(Screen):
    global answers_p
    sumka = ObjectProperty(None)
    sapog = ObjectProperty(None)
    tsep = ObjectProperty(None)
    kulak = ObjectProperty(None)
    chay = ObjectProperty(None)
    okno = ObjectProperty(None)
    volosy = ObjectProperty(None)
    devochka = ObjectProperty(None)
    telefon = ObjectProperty(None)
    most = ObjectProperty(None)
    divan = ObjectProperty(None)
    portret = ObjectProperty(None)
    scheka = ObjectProperty(None)
    pismo = ObjectProperty(None)
    kletka = ObjectProperty(None)
    class SuperButton(Button):
        colors = [[0,1,0, 1], [1,0,0,1]]
        def __init__ (self, number=0, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.number = 0
            self.color = [30/256, 19/256, 23/256,1]
            
    class AudioButton(Button):
        filename = StringProperty(None)
        sound = ObjectProperty(None, allownone=True)
        def on_press(self):
            if self.sound is None:
                self.sound = SoundLoader.load(self.filename)
        # stop the sound if it's currently playing
            if self.sound.status != 'stop':
                self.sound.stop()
            self.sound.volume = 1
            self.sound.play()
        def release_audio(self):
            if self.sound:
                self.sound.stop()
                self.sound.unload()
                self.sound = None
                
    def btn_press(self, instance):
        instance.background_color = colors[instance.number%2]
        instance.background_normal = ''
        instance.number +=1
        
        print(instance.number)
    def save_answers(self):
        if self.ids.retret.sound:
            self.ids.retret.sound.stop()
        answers = []
        answers.append(self.sumka.number%2)
        answers.append(self.sapog.number%2)
        answers.append(self.tsep.number%2)
        answers.append(self.kulak.number%2)
        answers.append(self.chay.number%2)
        answers.append(self.okno.number%2)
        answers.append(self.volosy.number%2)
        answers.append(self.devochka.number%2)
        answers.append(self.telefon.number%2)
        answers.append(self.most.number%2)
        answers.append(self.divan.number%2)
        answers.append(self.portret.number%2)
        answers.append(self.scheka.number%2)
        answers.append(self.pismo.number%2)
        answers.append(self.kletka.number%2)
        answers_p.append(answers)
        print(answers)
    pass
class FifthWindow(Screen):
    global answers_p
    sumka = ObjectProperty(None)
    sapog = ObjectProperty(None)
    tsep = ObjectProperty(None)
    kulak = ObjectProperty(None)
    chay = ObjectProperty(None)
    okno = ObjectProperty(None)
    volosy = ObjectProperty(None)
    devochka = ObjectProperty(None)
    telefon = ObjectProperty(None)
    most = ObjectProperty(None)
    divan = ObjectProperty(None)
    portret = ObjectProperty(None)
    scheka = ObjectProperty(None)
    pismo = ObjectProperty(None)
    kletka = ObjectProperty(None)
    class SuperButton(Button):
        colors = [[0,1,0, 1], [1,0,0,1]]
        def __init__ (self, number=0, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.number = 0
            self.color = [30/256, 19/256, 23/256,1]
    class AudioButton(Button):
        filename = StringProperty(None)
        sound = ObjectProperty(None, allownone=True)
        def on_press(self):
            if self.sound is None:
                self.sound = SoundLoader.load(self.filename)
        # stop the sound if it's currently playing
            if self.sound.status != 'stop':
                self.sound.stop()
            self.sound.volume = 1
            self.sound.play()
        def release_audio(self):
            if self.sound:
                self.sound.stop()
                self.sound.unload()
                self.sound = None
    def btn_press(self, instance):
        instance.background_color = colors[instance.number%2]
        instance.background_normal = ''
        instance.number +=1
        
        print(instance.number)
    def save_answers(self):
        if self.ids.retret.sound:
            self.ids.retret.sound.stop()
        answers = []
        answers.append(self.sumka.number%2)
        answers.append(self.sapog.number%2)
        answers.append(self.tsep.number%2)
        answers.append(self.kulak.number%2)
        answers.append(self.chay.number%2)
        answers.append(self.okno.number%2)
        answers.append(self.volosy.number%2)
        answers.append(self.devochka.number%2)
        answers.append(self.telefon.number%2)
        answers.append(self.most.number%2)
        answers.append(self.divan.number%2)
        answers.append(self.portret.number%2)
        answers.append(self.scheka.number%2)
        answers.append(self.pismo.number%2)
        answers.append(self.kletka.number%2)
        answers_p.append(answers)
        print(answers)
    pass
class SixthWindow(Screen):
    global answers_p
    sumka = ObjectProperty(None)
    sapog = ObjectProperty(None)
    tsep = ObjectProperty(None)
    kulak = ObjectProperty(None)
    chay = ObjectProperty(None)
    okno = ObjectProperty(None)
    volosy = ObjectProperty(None)
    devochka = ObjectProperty(None)
    telefon = ObjectProperty(None)
    most = ObjectProperty(None)
    divan = ObjectProperty(None)
    portret = ObjectProperty(None)
    scheka = ObjectProperty(None)
    pismo = ObjectProperty(None)
    kletka = ObjectProperty(None)
    class SuperButton(Button):
        colors = [[0,1,0, 1], [1,0,0,1]]
        def __init__ (self, number=0, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.number = 0
            self.color = [30/256, 19/256, 23/256,1]
         
    class AudioButton(Button):
        filename = StringProperty(None)
        sound = ObjectProperty(None, allownone=True)
        def on_press(self):
            if self.sound is None:
                self.sound = SoundLoader.load(self.filename)
        # stop the sound if it's currently playing
            if self.sound.status != 'stop':
                self.sound.stop()
            self.sound.volume = 1
            self.sound.play()
        def release_audio(self):
            if self.sound:
                self.sound.stop()
                self.sound.unload()
                self.sound = None
    def btn_press(self, instance):
        instance.background_color = colors[instance.number%2]
        instance.background_normal = ''
        instance.number +=1
        
        print(instance.number)
    def save_answers(self):
        if self.ids.retret.sound:
            self.ids.retret.sound.stop()
        answers = []
        answers.append(self.sumka.number%2)
        answers.append(self.sapog.number%2)
        answers.append(self.tsep.number%2)
        answers.append(self.kulak.number%2)
        answers.append(self.chay.number%2)
        answers.append(self.okno.number%2)
        answers.append(self.volosy.number%2)
        answers.append(self.devochka.number%2)
        answers.append(self.telefon.number%2)
        answers.append(self.most.number%2)
        answers.append(self.divan.number%2)
        answers.append(self.portret.number%2)
        answers.append(self.scheka.number%2)
        answers.append(self.pismo.number%2)
        answers.append(self.kletka.number%2)
        answers_p.append(answers)
        print(answers)
    pass
class SeventhWindow(Screen):
    global answers_p
    sumka = ObjectProperty(None)
    sapog = ObjectProperty(None)
    tsep = ObjectProperty(None)
    kulak = ObjectProperty(None)
    chay = ObjectProperty(None)
    okno = ObjectProperty(None)
    volosy = ObjectProperty(None)
    devochka = ObjectProperty(None)
    telefon = ObjectProperty(None)
    most = ObjectProperty(None)
    divan = ObjectProperty(None)
    portret = ObjectProperty(None)
    scheka = ObjectProperty(None)
    pismo = ObjectProperty(None)
    kletka = ObjectProperty(None)
    class SuperButton(Button):
        colors = [[0,1,0, 1], [1,0,0,1]]
        def __init__ (self, number=0, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.number = 0
            self.color = [30/256, 19/256, 23/256,1]
            
    class AudioButton(Button):
        filename = StringProperty(None)
        sound = ObjectProperty(None, allownone=True)
        def on_press(self):
            if self.sound is None:
                self.sound = SoundLoader.load(self.filename)
        # stop the sound if it's currently playing
            if self.sound.status != 'stop':
                self.sound.stop()
            self.sound.volume = 1
            self.sound.play()
        def release_audio(self):
            if self.sound:
                self.sound.stop()
                self.sound.unload()
                self.sound = None    
        
    def btn_press(self, instance):
        instance.background_color = colors[instance.number%2]
        instance.background_normal = ''
        instance.number +=1
        
        print(instance.number)
    def save_answers(self):
        if self.ids.retret.sound:
            self.ids.retret.sound.stop()
        answers = []
        answers.append(self.sumka.number%2)
        answers.append(self.sapog.number%2)
        answers.append(self.tsep.number%2)
        answers.append(self.kulak.number%2)
        answers.append(self.chay.number%2)
        answers.append(self.okno.number%2)
        answers.append(self.volosy.number%2)
        answers.append(self.devochka.number%2)
        answers.append(self.telefon.number%2)
        answers.append(self.most.number%2)
        answers.append(self.divan.number%2)
        answers.append(self.portret.number%2)
        answers.append(self.scheka.number%2)
        answers.append(self.pismo.number%2)
        answers.append(self.kletka.number%2)
        answers_p.append(answers)
        print(answers)
    pass
class EighthWindow(Screen):
    global answers_p
    sumka = ObjectProperty(None)
    sapog = ObjectProperty(None)
    tsep = ObjectProperty(None)
    kulak = ObjectProperty(None)
    chay = ObjectProperty(None)
    okno = ObjectProperty(None)
    volosy = ObjectProperty(None)
    devochka = ObjectProperty(None)
    telefon = ObjectProperty(None)
    most = ObjectProperty(None)
    divan = ObjectProperty(None)
    portret = ObjectProperty(None)
    scheka = ObjectProperty(None)
    pismo = ObjectProperty(None)
    kletka = ObjectProperty(None)
    class SuperButton(Button):
        colors = [[0,1,0, 1], [1,0,0,1]]
        def __init__ (self, number=0, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.number = 0
            self.color = [30/256, 19/256, 23/256,1]
    def btn_press(self, instance):
        instance.background_color = colors[instance.number%2]
        instance.background_normal = ''
        instance.number +=1
        
        print(instance.number)
    def save_answers(self):
        answers = []
        answers.append(self.sumka.number%2)
        answers.append(self.sapog.number%2)
        answers.append(self.tsep.number%2)
        answers.append(self.kulak.number%2)
        answers.append(self.chay.number%2)
        answers.append(self.okno.number%2)
        answers.append(self.volosy.number%2)
        answers.append(self.devochka.number%2)
        answers.append(self.telefon.number%2)
        answers.append(self.most.number%2)
        answers.append(self.divan.number%2)
        answers.append(self.portret.number%2)
        answers.append(self.scheka.number%2)
        answers.append(self.pismo.number%2)
        answers.append(self.kletka.number%2)
        answers_p.append(answers)
        print(answers)
    pass
class NinethWindow(Screen):
    global seconds
    def on_start(self):
        Clock.schedule_interval(self.update_label, 1)
    def update_label(self, *args):
        global seconds
        seconds=seconds+1
        if seconds < 1200:
            self.ids.counter.text = str(int((1200-seconds)//60)) + ":" + str(int((1200-seconds)%60))
        else:
            self.ids.counter.text = "20 минут прошли! Нажмите <<Продолжить>>"
    def btn_press(self):
        if seconds == 0:
            self.on_start()
        
    pass
class TenthWindow(Screen):
    global answers_p
    sumka = ObjectProperty(None)
    sapog = ObjectProperty(None)
    tsep = ObjectProperty(None)
    kulak = ObjectProperty(None)
    chay = ObjectProperty(None)
    okno = ObjectProperty(None)
    volosy = ObjectProperty(None)
    devochka = ObjectProperty(None)
    telefon = ObjectProperty(None)
    most = ObjectProperty(None)
    divan = ObjectProperty(None)
    portret = ObjectProperty(None)
    scheka = ObjectProperty(None)
    pismo = ObjectProperty(None)
    kletka = ObjectProperty(None)
    class SuperButton(Button):
        colors = [[0,1,0, 1], [1,0,0,1]]
        def __init__ (self, number=0, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.number = 0
            self.color = [30/256, 19/256, 23/256,1]
    def btn_press(self, instance):
        instance.background_color = colors[instance.number%2]
        instance.background_normal = ''
        instance.number +=1
        
        print(instance.number)
    def save_answers(self):
        answers = []
        answers.append(self.sumka.number%2)
        answers.append(self.sapog.number%2)
        answers.append(self.tsep.number%2)
        answers.append(self.kulak.number%2)
        answers.append(self.chay.number%2)
        answers.append(self.okno.number%2)
        answers.append(self.volosy.number%2)
        answers.append(self.devochka.number%2)
        answers.append(self.telefon.number%2)
        answers.append(self.most.number%2)
        answers.append(self.divan.number%2)
        answers.append(self.portret.number%2)
        answers.append(self.scheka.number%2)
        answers.append(self.pismo.number%2)
        answers.append(self.kletka.number%2)
        answers_p.append(answers)
        print(answers)
    pass
class EleventhWindow(Screen):
    global answers_p
    sumka = ObjectProperty(None)
    sapog = ObjectProperty(None)
    tsep = ObjectProperty(None)
    kulak = ObjectProperty(None)
    chay = ObjectProperty(None)
    okno = ObjectProperty(None)
    volosy = ObjectProperty(None)
    devochka = ObjectProperty(None)
    telefon = ObjectProperty(None)
    most = ObjectProperty(None)
    divan = ObjectProperty(None)
    portret = ObjectProperty(None)
    scheka = ObjectProperty(None)
    pismo = ObjectProperty(None)
    kletka = ObjectProperty(None)
    class SuperButton(Button):
        colors = [[0,1,0, 1], [1,0,0,1]]
        def __init__ (self, number=0, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.number = 0
            self.color = [30/256, 19/256, 23/256,1]
    def btn_press(self, instance):
        instance.background_color = colors[instance.number%2]
        instance.background_normal = ''
        instance.number +=1
        
        print(instance.number)
    def save_answers(self):
        answers = []
        answers.append(self.sumka.number%2)
        answers.append(self.sapog.number%2)
        answers.append(self.tsep.number%2)
        answers.append(self.kulak.number%2)
        answers.append(self.chay.number%2)
        answers.append(self.okno.number%2)
        answers.append(self.volosy.number%2)
        answers.append(self.devochka.number%2)
        answers.append(self.telefon.number%2)
        answers.append(self.most.number%2)
        answers.append(self.divan.number%2)
        answers.append(self.portret.number%2)
        answers.append(self.scheka.number%2)
        answers.append(self.pismo.number%2)
        answers.append(self.kletka.number%2)
        answers_p.append(answers)
        print(answers)
    pass
class TwelvethWindow(Screen):
    global answers_p, code_p, email_p, age_p, edu_p
    def export(self,*args):
            fname = os.path.join(primary_external_storage_path(),'RAVLTapp',str(str(code_p)+"_results.png"))
            self.ids.bigtable.export_to_png(fname)
    class MyLayout (GridLayout):
        def export(self,*args):
            fname = os.path.join(primary_external_storage_path(),'RAVLTapp',str(str(code_p)+"_results.png"))
            self.ids.bigtable.export_to_png(fname)
    
    def press(self):
        self.ids.code_p.text = str(code_p)
        self.ids.age_p.text = str(age_p)
        self.ids.edu_p.text = str(edu_p)
        self.ids.email_p.text = str(email_p)
        print(answers_p)
        self.ids.z11.text, self.ids.z12.text, self.ids.z13.text  = count(answers_p[0], 1)
        self.ids.z21.text, self.ids.z22.text, self.ids.z23.text  = count(answers_p[1], 1)
        self.ids.z31.text, self.ids.z32.text, self.ids.z33.text  = count(answers_p[2], 1)
        self.ids.z41.text, self.ids.z42.text, self.ids.z43.text  = count(answers_p[3], 1)
        self.ids.z51.text, self.ids.z52.text, self.ids.z53.text  = count(answers_p[4], 1)
        self.ids.i11.text, self.ids.i12.text, self.ids.i13.text  = count(answers_p[5], 2)
        self.ids.v11.text, self.ids.v12.text, self.ids.v13.text  = count(answers_p[6], 1)
        self.ids.v21.text, self.ids.v22.text, self.ids.v23.text  = count(answers_p[7], 1)
        self.ids.o11.text, self.ids.o12.text, self.ids.o13.text  = count(answers_p[8], 1)
        self.ids.z11.color, self.ids.z12.color, self.ids.z13.color = [[55/256, 1/256, 25/256, 1]]*3
        self.ids.z21.color, self.ids.z22.color, self.ids.z23.color = [[55/256, 1/256, 25/256, 1]]*3
        self.ids.z31.color, self.ids.z32.color, self.ids.z33.color = [[55/256, 1/256, 25/256, 1]]*3
        self.ids.z41.color, self.ids.z42.color, self.ids.z43.color = [[55/256, 1/256, 25/256, 1]]*3
        self.ids.z51.color, self.ids.z52.color, self.ids.z53.color = [[55/256, 1/256, 25/256, 1]]*3
        self.ids.i11.color, self.ids.i12.color, self.ids.i13.color = [[55/256, 1/256, 25/256, 1]]*3
        self.ids.v11.color, self.ids.v12.color, self.ids.v13.color = [[55/256, 1/256, 25/256, 1]]*3
        self.ids.v21.color, self.ids.v22.color, self.ids.v23.color = [[55/256, 1/256, 25/256, 1]]*3
        self.ids.o11.color, self.ids.o12.color, self.ids.o13.color = [[55/256, 1/256, 25/256, 1]]*3
        self.ids.p2.color, self.ids.p3.color, self.ids.p4.color, self.ids.p5.color, self.ids.p6.color, self.ids.p7.color, self.ids.p8.color = [[55/256, 1/256, 25/256, 1]]*7
        self.ids.p9.color, self.ids.p10.color, self.ids.p12.color, self.ids.p13.color, self.ids.p14.color, self.ids.p16.color, self.ids.p17.color, self.ids.p18.color = [[55/256, 1/256, 25/256, 1]]*8
        self.ids.p19.color, self.ids.p20.color, self.ids.p21.color, self.ids.p23.color, self.ids.p24.color, self.ids.p25.color = [[55/256, 1/256, 25/256, 1]]*6
        self.ids.p1.color, self.ids.p11.color, self.ids.p15.color, self.ids.p22.color = [[55/256, 1/256, 25/256, 1]]*4
        self.ids.p1.background_color, self.ids.p11.background_color, self.ids.p15.background_color, self.ids.p22.background_color = [[222/256, 164/256, 189/256, 1]]*4
    pass
class WindowManager(ScreenManager):
    pass

kv = Builder.load_file('new_window.kv')
#from kivy.config import Config
#Config.set('graphics', 'resizable', '0')
#Config.set('graphics', 'width', '720')
#Config.set('graphics', 'height' , '540')


class MyApp(App):
    def build(self):
        Window.clearcolor = (1, 1, 1, 1)
        return kv
    
    class AudioButton(Button):
        filename = StringProperty(None)
        sound = ObjectProperty(None, allownone=True)
        def on_press(self):
            if self.sound is None:
                self.sound = SoundLoader.load(self.filename)
        # stop the sound if it's currently playing
            if self.sound.status != 'stop':
                self.sound.stop()
            self.sound.volume = 1
            self.sound.play()
        def release_audio(self):
            if self.sound:
                self.sound.stop()
                self.sound.unload()
                self.sound = None
    
    def btn_press(self, instance):
        instance.background_color = colors[instance.number%2]
        instance.background_normal = ''
        instance.number +=1
        print(self.number)
    def next_press(self, instance):
        global numpage
        numpage = 2
        print(numpage)

def count(mylist, v):
    global words1, words2
    summa = 0
    total = 15
    mystring = ""
    for a in range(0,15,1):
        summa += mylist[a]
        if v == 1:
            if mylist[a] == 1:
                mystring+=words1[a] +', '
        if v == 2:
            if mylist[a] == 1:
                mystring+=words2[a] +', '
    if len(mystring) <= 2:
        mystring = '  '
    return str(summa), str(round(100*summa/total, 2)), str(mystring[:-2])
	
if __name__ == "__main__":
    seconds = 0
    words1 = ['сумка', 'сапог', 'цепь', 'кулак', 'чай', 'окно', 'волосы', 'девочка', 'телефон', 'мост', 'диван', 'портрет', 'щека', 'письмо', 'клетка']
    words2 = ['платье', 'газета','театр','хлеб','лодка','мешок','хвост','голова','замок','танк','старик','поле','река','дерево','золото']
        
    colors = [[163/256,244/256,153/256, 1], [244/256,163/256,153/256,1]]
    MyApp().run()