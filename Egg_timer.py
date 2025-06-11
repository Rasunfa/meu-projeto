import time

def egg_timer(egg_type):
    # Tempos em segundos para diferentes tipos de ovos cozidos
    egg_times = {
        "mole": 300,    # 5 minutos
        "médio": 420,   # 7 minutos
        "duro": 600     # 10 minutos
    }
    
    if egg_type.lower() not in egg_times:
        print("Tipo de ovo inválido! Escolha entre: mole, médio, duro")
        return
    
    seconds = egg_times[egg_type.lower()]
    print(f"Iniciando timer para ovo {egg_type.lower()} ({seconds//60} minutos)...")
    
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        timer = f"{mins:02d}:{secs:02d}"
        print(f"Tempo restante: {timer}", end="\r")
        time.sleep(1)
        seconds -= 1
    
    print("\nTimer finalizado! Seu ovo está pronto!")

def main():
    print("Bem-vindo ao Timer de Ovos Cozidos!")
    print("Tipos de ovos disponíveis: mole, médio, duro")
    egg_type = input("Digite o tipo de ovo desejado: ")
    egg_timer(egg_type)

if __name__ == "__main__":
    main()