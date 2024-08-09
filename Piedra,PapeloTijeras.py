import random

class PiedraPapelTijera:
    def __init__(self):
        self.opciones = ['piedra', 'papel', 'tijera']
        self.resultado = {
            ('piedra', 'tijera'): 'gana',
            ('tijera', 'papel'): 'gana',
            ('papel', 'piedra'): 'gana'
        }
    
    def elegir_opcion(self, jugador):
        while True:
            eleccion = input(f"Elige entre {', '.join(self.opciones)}: ").lower()
            if eleccion in self.opciones:
                return eleccion
            print("Opción no válida. Inténtalo de nuevo.")
    
    def jugar_ronda(self):
        print("¡Comienza una nueva ronda!")
        eleccion_jugador = self.elegir_opcion('jugador')
        eleccion_computadora = random.choice(self.opciones)
        print(f"La computadora elige: {eleccion_computadora}")
        
        if eleccion_jugador == eleccion_computadora:
            return "Empate"
        
        if (eleccion_jugador, eleccion_computadora) in self.resultado:
            return "Ganaste"
        else:
            return "Perdiste"
    
    def jugar(self):
        print("Bienvenido al juego de Piedra, Papel o Tijera!")
        while True:
            resultado = self.jugar_ronda()
            print(f"Resultado de la ronda: {resultado}")
            
            jugar_de_nuevo = input("¿Quieres jugar otra ronda? (s/n): ").lower()
            if jugar_de_nuevo != 's':
                break
        print("Gracias por jugar. ¡Hasta la próxima!")

if __name__ == "__main__":
    juego = PiedraPapelTijera()
    juego.jugar()