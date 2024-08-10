import sys

def convertir_monedas(tasa_sol, tasa_peso_arg, tasa_dolar, valor_peso_chile):
    # Convertir al valor  de las otras monedas en pesos chilenos 
    valor_sol = valor_peso_chile * tasa_sol
    valor_peso_arg = valor_peso_chile * tasa_peso_arg
    valor_dolar = valor_peso_chile * tasa_dolar
    
    # Imprimir las respuestas
    print(f"Los {valor_peso_chile} pesos equivalen a:")
    print(f"{valor_sol} Soles")
    print(f"{valor_peso_arg} Pesos Argentinos")
    print(f"{valor_dolar} Dólares")

if __name__ == "__main__":
    # Obtener los argumentos desde la línea de comandos
    tasa_sol = float(sys.argv[1])
    tasa_peso_arg = float(sys.argv[2])
    tasa_dolar = float(sys.argv[3])
    valor_peso_chile = float(sys.argv[4])
    
    # Llamar a la función para la conversion de monedas
    convertir_monedas(tasa_sol, tasa_peso_arg, tasa_dolar, valor_peso_chile)