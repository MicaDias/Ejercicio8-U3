class MenuDirector:
    __opciones={}
    def __init__(self):
        self.__opciones={
            1:self.opcion1,
            2:self.opcion2,
            3:self.opcion3,
            4:self.opcion4,
            5:self.salir
        }
    def lanzarMenu(self,lista):
        #Menu opciones
        i=len(self.__opciones)
        opcion=0
        while(i!=opcion):
            print('Menu:')
            print('-Ingrese 1: Modificar el sueldo básico.')
            print('-Ingrese 2: Modificar el porcentaje que se paga por cargo.')
            print('-Ingrese 3: Modificar el porcentaje que se paga por categoría.')
            print('-Ingrese 4: Modificar el importe extra.')
            print('-Ingrese 5: para salir.')
            opcion=self.cargarNumeroEntero('Ingrese opcion:')
            ejecutar=self.__opciones.get(opcion,self.error)
            if opcion>0 and opcion<5:
                ejecutar(lista)
            else:
                ejecutar()
    def opcion1(self,lista):
        dni=input('Ingrese el DNI:')
        nuevoBasico=self.cargarFlotante('Ingrese sueldo basico:')
        lista.modificarBasico(dni,nuevoBasico)
    def opcion2(self,lista):
        dni=input('Ingrese el DNI:')
        nuevoPorcentaje=self.cargarFlotante('Ingrese el nuevo porcentaje del docente:')
        lista.modificarPorcentajeporcargo(dni,nuevoPorcentaje)
    def opcion3(self,lista):
        dni=input('Ingrese el DNI:')
        nuevoPorcentaje=self.cargarFlotante('Ingrese el nuevo porcentaje del personal de apoyo:')
        lista.modificarPorcentajeporcategoría(dni,nuevoPorcentaje)
    def opcion4(self,lista):
        dni=input('Ingrese el DNI:')
        nuevoImporteExtra=self.cargarFlotante('Ingrese el nuevo importe extra:')
        lista.modificarImporteExtra(dni, nuevoImporteExtra)
    def cargarNumeroEntero(self,mensaje='Ingrese valor:'):
        numero=None
        bandera=True
        while bandera:
            try:
                numero=int(input(mensaje))
            except ValueError:
                print('ERROR: Se debe ingresar un numero entero.')
            else:
                bandera=False
        return numero
    def cargarFlotante(self,mensaje='Ingrese valor:'):
        numero=None
        bandera=True
        while bandera:
            try:
                numero=int(input(mensaje))
            except ValueError:
                print('ERROR: Se admiten numeros enteros y punto ,por ejemplo:500 o 500.50')
            else:
                bandera=False
        return numero
    def error(self):
        #Mensaje cuando ingresa opcion incorrecta
        print('Opción incorrecta')
    def salir(self):
        #Mensaje cuando decide salir
        print('Se cerro el menú')