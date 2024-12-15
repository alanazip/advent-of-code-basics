class SingletonMeta(type):
    """
    Metaclasse para implementar o padrão Singleton.
    """
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            # Se a classe não tiver uma instância, cria uma.
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class SingletonClass(metaclass=SingletonMeta):
    """
    Classe que utiliza a metaclasse SingletonMeta para garantir que tenha apenas uma instância.
    """
    def __init__(self, value):
        self.value = value


# Teste do Singleton
singleton_1 = SingletonClass("Primeira Instância")
singleton_2 = SingletonClass("Segunda Instância")

print(singleton_1.value)  # Output: Primeira Instância
print(singleton_2.value)  # Output: Primeira Instância
print(singleton_1 is singleton_2)  # Output: True