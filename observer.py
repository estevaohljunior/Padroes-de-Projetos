from __future__ import annotations
from abc import ABC, abstractmethod
import tkinter as tk
from tkinter import *
class Sujeito(ABC):
    @abstractmethod
    def adicionar(self, observer: Observer) -> None:
        pass
    @abstractmethod
    def remover(self, observer: Observer) -> None:
        pass
    @abstractmethod
    def notificar(self) -> None:
        pass
    @abstractmethod
    def getMen(self) -> str:
        pass
    @abstractmethod
    def setMen(self, texto: str) -> None:
        pass
class JanelaTexto(Sujeito):
    _mensagem: str = None
    _observer: Observer = None
    def __init__(self):
        self.setMen("")
    def adicionar(self, observer: Observer) -> None:
        print("Observer criado e adicionado.")
        self._observer = observer
    def remover(self, observer: Observer) -> None:
        self._observer = observer
    def notificar(self):
        print("Set mensagem ...")
        return self._observer.update(self)
    def addText(self, texto: str):
        self.setMen(texto)
        return self.notificar()
    def getMen(self) -> str:
        return self._mensagem
    def setMen(self, texto=""):
        self._mensagem = texto
class Observer(ABC):
    @abstractmethod
    def update(self, sujeito: Sujeito) -> None:
        pass
    @abstractmethod
    def getRecebido(self) -> str:
        pass
class JanelaObserver(Observer):
    _recebido: str = None

    def __init__(self):
        self._recebido = ""
    def update(self, sujeito: Sujeito) -> None:
        self._recebido = sujeito.getMen()
    def getRecebido(self) -> str:
        return self._recebido
class GUI:
    _tmpMSG: str = None

    def __init__(self):
        self._tmpMSG = ""
        self.janela_1 = JanelaTexto()
        self.janela_2 = JanelaTexto()
        self.ObserverJ1 = JanelaObserver()
        self.ObserverJ2 = JanelaObserver()
        self.janela_1.adicionar(self.ObserverJ1)
        self.janela_2.adicionar(self.ObserverJ2)
        self.janela_tk1 = Tk()
        self.janela_tk2 = Toplevel()
        self.janela_tk1.configure(bg='#090')
        self.janela_tk2.configure(bg='#f0f')
        self.janela_tk1.title("Janela 1")
        self.janela_tk1.configure(bg='#090')
        self.janela_tk2.title("Janela 2")
        self.fontePadrao1 = ("Arial", "12")
        self.fontePadrao2 = ("Arial", "12", "bold")
        self.cont1J1 = Frame(self.janela_tk1)
        self.cont1J1.configure(bg='#090')
        self.cont1J1["pady"] = 10
        self.cont1J1.pack()
        self.cont2J1 = Frame(self.janela_tk1)
        self.cont2J1.configure(bg='#090')
        self.cont2J1["padx"] = 20
        self.cont2J1.pack()
        self.cont3J1 = Frame(self.janela_tk1)
        self.cont3J1["padx"] = 20
        self.cont3J1.configure(bg='#090')
        self.cont3J1.pack()
        self.cont4J1 = Frame(self.janela_tk1)
        self.cont4J1["pady"] = 20
        self.cont4J1.configure(bg='#090')
        self.cont4J1.pack()
        self.titJ1 = Label(self.cont1J1, text="Janela 1:", font=self.fontePadrao2)
        self.titJ1.configure(bg='#090')
        self.titJ1.pack()
        self.menJ1 = Entry(self.cont2J1)
        self.menJ1["width"] = 30
        self.menJ1["font"] = self.fontePadrao1
        self.menJ1.configure(bg='#090')
        self.menJ1.pack()
        self.envJ1 = Button(self.cont4J1, command=self.pressB1,cursor="circle #000")
        self.envJ1["text"] = "Set 2"
        self.envJ1["font"] = ("Helvetica", "10")
        self.envJ1["width"] = 12
        self.envJ1.configure(bg='#fff')
        self.envJ1.pack()
        self.cont1J2 = Frame(self.janela_tk2)
        self.cont1J2["pady"] = 10
        self.cont1J2.configure(bg='#f0f')
        self.cont1J2.pack()
        self.cont2J2 = Frame(self.janela_tk2)
        self.cont2J2["padx"] = 20
        self.cont2J2.configure(bg='#f0f')
        self.cont2J2.pack()
        self.cont3J2 = Frame(self.janela_tk2)
        self.cont3J2["padx"] = 20
        self.cont3J2.configure(bg='#f0f')
        self.cont3J2.pack()
        self.cont4J2 = Frame(self.janela_tk2)
        self.cont4J2["pady"] = 20
        self.cont4J2.configure(bg='#f0f')
        self.cont4J2.pack()
        self.titJ2 = Label(self.cont1J2, text="Janela 2:", font=self.fontePadrao2)
        self.titJ2.configure(bg='#f0f')
        self.titJ2.pack()
        self.menJ2 = Entry(self.cont2J2)
        self.menJ2["width"] = 30
        self.menJ2["font"] = self.fontePadrao1
        self.menJ2.configure(bg='#f0f')
        self.menJ2.pack()
        self.envJ2 = Button(self.cont4J2, command=self.pressB2,cursor="circle #000")
        self.envJ2["text"] = "Set 1"
        self.envJ2["font"] = ("Helvetica", "10")
        self.envJ2["width"] = 12
        self.envJ2.configure(bg='#fff')
        self.envJ2.pack()
        self.janela_tk1.mainloop()
    def pressB1(self):
        self.setMSG(self.menJ1.get())
        if self._tmpMSG != "":
            print("Observer Janela 1: ")
            self.janela_1.addText(self._tmpMSG)
            self.menJ2.delete(0,tk.END)
            self.menJ2.insert(0,self.ObserverJ1.getRecebido())

    def pressB2(self):
        self.setMSG(self.menJ2.get())
        if self._tmpMSG != "":
            print("Observer Janela 2: ")
            self.janela_2.addText(self._tmpMSG)
            self.menJ1.delete(0,tk.END)
            self.menJ1.insert(0,self.ObserverJ2.getRecebido())

    def setMSG(self, msg: str):
        self._tmpMSG = msg


if __name__ == "__main__":
    GUI()
