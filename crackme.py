import termcolor
from time import sleep


def banner():

    print(termcolor.colored("""
    
      _.-'''''-._
    .'  _     _  '.
   /   (o)   (o)   \\
  |                 |
  |  \           /  |
   \  '.       .'  /
    '.  `'---'`  .'
      '-._____.-' 

___________________    _____  _________  ____  __.    _____  __________
\_   ___ \______   \  /  _  \ \_   ___ \|    |/ _|   /     \ \_   _____/
/    \  \/|       _/ /  /_\  \/    \  \/|      <    /  \ /  \ |    __)_ 
\     \___|    |   \/    |    \     \___|    |  \  /    Y    \|        \\
 \______  /____|_  /\____|__  /\______  /____|__ \ \____|__  /_______  /
        \/       \/         \/        \/        \/         \/        \/ 
""", 'yellow'))



def checar_nome(nome):

    algoritmo_decimal = 0

    nome = nome.upper()

    for i in range(len(nome)):
        algoritmo_decimal += ord(nome[i])

    algoritmo_hexadecimal = hex(algoritmo_decimal)

    resultado = hex(int("0x5678", 16) ^ int(algoritmo_hexadecimal, 16))

    return resultado.upper()


def crack_serial(serial_nome):

    print(termcolor.colored("="*30,"yellow"))
    
    print(termcolor.colored("Cracking......","red"))

    print(termcolor.colored("="*30,"yellow"))

    for i in range(1, 9999999999):

        edi = 0

        j = 0

        quant_numero = len(str(i))
        
        while j < quant_numero:

            numeral = hex(ord(str(i)[j]))[2::]

            numeral = int(numeral) - 30

            edi = edi * 10

            edi = numeral + edi

            j += 1
        
        numero_hex = hex(edi).upper()
        
        resultado = hex(int("0x1234", 16) ^ int(numero_hex, 16))
        
        if resultado.upper() == serial_nome:
    
            return edi

def main():

    banner()

    nome = input("Digite um nome: ")

    print(termcolor.colored("\nChecando algoritmo de nome....\n", "blue"))

    sleep(1)

    serial_nome = checar_nome(nome)

    print(termcolor.colored("DONE :), cross your fingers\n", "green"))

    sleep(1)

    serial_checker = crack_serial(serial_nome)

    
    print(termcolor.colored(f"\nAnd your serial is: {serial_checker}", "green"))


if __name__ == "__main__":
    main()  