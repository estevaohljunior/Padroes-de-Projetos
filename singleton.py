class SingletonMeta(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        else: 
            cls._instances[cls].add_solit()
        return cls._instances[cls]
class Singleton(metaclass=SingletonMeta):
    def __init__(self)->None:
        self.__init=1
    def add_solit(self):
        self.__init+=1
    def return_solit(self):
        return self.__init
class fabric():
    def __init__(self)->None:
        self.__h1=Singleton()
        self.__h2=Singleton()
        self.__h3=Singleton()
        self.__h4=[]
    def sao_iguais(self):
        if(self.__h2==self.__h3):
            print("h2 e h3 são mesmo objeto!")
    def solicitar(self):
        
        a=int(input("Quantas solicitações deseja:"))
        for i in range(a):
            self.__h4.append(Singleton())
        print("As",a,"solicitações foram efetuadas com sucesso.")
    def chamadas(self):
        print("Foram efetuadas",self.__h1.return_solit(),"chamadas.")
if __name__ == "__main__":
    fa=fabric()
    fa.solicitar()
    fa.sao_iguais()
    fa.chamadas()
    