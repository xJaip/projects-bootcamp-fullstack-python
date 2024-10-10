import csv

class Vehiculo:
    def __init__(self, marca, modelo, numero_ruedas):
        self.marca = marca
        self.modelo = modelo
        self.numero_ruedas = numero_ruedas

    def __str__(self):
        return f"Marca {self.marca}, Modelo {self.modelo}, {self.numero_ruedas} ruedas"
    
    def guardar_datos_csv(self):
        with open('vehiculos.csv', 'a', newline='') as archivo_csv:
            writer = csv.writer(archivo_csv)
            writer.writerow([str(self.__class__), str(self.__dict__)])
    
    @staticmethod
    def leer_datos_csv():
        try:
            automoviles = recuperar("vehiculos.csv")
            if not automoviles:
                print("No se encontraron vehículos en el archivo.")
                return

            lista_particular = []
            lista_carga = []
            lista_bicicleta = []
            lista_motocicleta = []

            for vehiculo in automoviles:
                clase_vehiculo = vehiculo[0]
                datos_vehiculo = eval(vehiculo[1])

                if "Particular" in clase_vehiculo:
                    lista_particular.append(datos_vehiculo)
                elif "Carga" in clase_vehiculo:
                    lista_carga.append(datos_vehiculo)
                elif "Bicicleta" in clase_vehiculo:
                    lista_bicicleta.append(datos_vehiculo)
                elif "Motocicleta" in clase_vehiculo:
                    lista_motocicleta.append(datos_vehiculo)

            if lista_particular:
                print("Lista de Vehiculos Particular")
                for particular in lista_particular:
                    print(particular)

            if lista_carga:
                print("\nLista de Vehiculos Carga")
                for carga in lista_carga:
                    print(carga)

            if lista_bicicleta:
                print("\nLista de Vehiculos Bicicleta")
                for bicicleta in lista_bicicleta:
                    print(bicicleta)

            if lista_motocicleta:
                print("\nLista de Vehiculos Motocicleta")
                for motocicleta in lista_motocicleta:
                    print(motocicleta)

        except Exception as e:
            print(f"Ocurrió un error al procesar los datos: {e}")


        

class Automovil(Vehiculo):
    def __init__(self, marca, modelo, numero_ruedas, velocidad, cilindrada):
        super().__init__(marca, modelo, numero_ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return f"{super().__str__()} {self.velocidad} Km/h, {self.cilindrada} cc"

class Particular(Automovil):
    def __init__(self, marca, modelo, numero_ruedas, velocidad, cilindrada, puestos):
        super().__init__(marca, modelo, numero_ruedas, velocidad, cilindrada)
        self.puestos = puestos

    def __str__(self):
        return f"{super().__str__()} Puestos: {self.puestos}"

class Carga(Automovil):
    def __init__(self, marca, modelo, numero_ruedas, velocidad, cilindrada, peso):
        super().__init__(marca, modelo, numero_ruedas, velocidad, cilindrada)
        self.peso = peso

    def __str__(self):
        return f"{super().__str__()} Carga: {self.peso} Kg"

class Bicicleta(Vehiculo):
    def __init__(self, marca, modelo, numero_ruedas, tipo):
        super().__init__(marca, modelo, numero_ruedas)
        self.tipo = tipo

    def __str__(self):
        return f"{super().__str__()} Tipo: {self.tipo}"

class Motocicleta(Bicicleta):
    def __init__(self, marca, modelo, numero_ruedas, tipo, motor, cuadro, nro_radios):
        super().__init__(marca, modelo, numero_ruedas, tipo)
        self.motor = motor
        self.cuadro = cuadro
        self.nro_radios = nro_radios

    def __str__(self):
        return f"{super().__str__()} Motor: {self.motor}, Cuadro: {self.cuadro}, Nro Radios: {self.nro_radios}"

def guardar(nombre_archivo, Automovil):
    archivo = open(nombre_archivo, "w")
    datos = [(Automovil.__class__,Automovil.__dict__)]
    archivo_csv = csv.writer(archivo)
    archivo_csv.writerows(datos)
    archivo.close()
    
def recuperar(nombre_archivo):
    vehiculos = []
    try:
        with open(nombre_archivo, "r") as archivo:
            archivo_csv = csv.reader(archivo)
            for vehiculo in archivo_csv:
                vehiculos.append(vehiculo)
    except FileNotFoundError:
        print(f"Error: El archivo '{nombre_archivo}' no fue encontrado.")
    except IOError:
        print(f"Error: Ocurrió un problema al leer el archivo '{nombre_archivo}'.")
    except Exception as e:
        print(f"Error inesperado: {e}")
    return vehiculos
        

def main():
    """Parte 1: Crear instancias de las clases y mostrar sus datos
    vehiculos = []
    num_vehiculos = int(input("Cuantos Vehiculos desea insertar: "))

    for i in range(num_vehiculos):
        print(f"\nDatos del automóvil {i + 1}")
        marca = input("Inserte la marca del automóvil: ")
        modelo = input("Inserte el modelo: ")
        numero_ruedas = int(input("Inserte el número de ruedas: "))
        velocidad = int(input("Inserte la velocidad en km/h: "))
        cilindrada = int(input("Inserte el cilindraje en cc: "))
        automovil = Automovil(marca, modelo, numero_ruedas, velocidad, cilindrada)
        vehiculos.append(automovil)
    """
    
    """Parte 2: Crear instancias de las clases y mostrar sus datos
    particular = Particular("Ford", "Fiesta", 4, "180", "500", 5)
    vehiculos.append(particular)
    carga = Carga("Daft Trucks", "G 38", 10, 120, "1000", "20000")
    vehiculos.append(carga)
    bicicleta = Bicicleta("Shimano", "MT Ranger", 2, "Carrera")
    vehiculos.append(bicicleta)
    motocicleta = Motocicleta("BMW", "F800s", 2, "Deportiva", "2T", "Doble Viga", 21)
    vehiculos.append(motocicleta)
    
    

    print("\nImprimiendo por pantalla los Vehículos:\n")
    for i, vehiculo in enumerate(vehiculos, 1):
        print(f"Datos del automóvil {i}: {vehiculo}")
        
        
    # Verificar relaciones de instancia
    print("\nVerificando relaciones de instancia:")
    print("Motocicleta es instancia con relación a Vehículo:", isinstance(motocicleta, Vehiculo))
    print("Motocicleta es instancia con relación a Automovil:", isinstance(motocicleta, Automovil))
    print("Motocicleta es instancia con relación a Particular:", isinstance(motocicleta, Particular))
    print("Motocicleta es instancia con relación a Carga:", isinstance(motocicleta, Carga))
    print("Motocicleta es instancia con relación a Bicicleta:", isinstance(motocicleta, Bicicleta))
    print("Motocicleta es instancia con relación a Motocicleta:", isinstance(motocicleta, Motocicleta))
    """
    
    """Parte 3: Guardar y recuperar datos de un archivo CSV
    automovil = Automovil("Ford", "Fiesta", "4", "180", "500")
    
    guardar("ejemplo.csv", automovil)
    
    automoviles = recuperar("ejemplo.csv")
    
    for automovil in automoviles:
        print(automovil)
    """
    vehiculos = []
    particular = Particular("Ford", "Fiesta", 4, "180", "500", 5)
    vehiculos.append(particular)
    particular2 = Particular("Suzuki", "Swift", 4, "200", "800", 5)
    vehiculos.append(particular2)
    carga = Carga("Daft Trucks", "G 38", 10, 120, "1000", "20000")
    vehiculos.append(carga)
    bicicleta = Bicicleta("Shimano", "MT Ranger", 2, "Carrera")
    vehiculos.append(bicicleta)
    motocicleta = Motocicleta("BMW", "F800s", 2, "Deportiva", "2T", "Doble Viga", 21)
    vehiculos.append(motocicleta)
    
    for vehiculo in vehiculos:
        vehiculo.guardar_datos_csv()
        
    Vehiculo.leer_datos_csv()
    
    
if __name__ == "__main__":
    main()
