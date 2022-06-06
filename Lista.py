from zope.interface import implementer
from IDirector import IDirector
from ITesorero import ITesorero
from Interface import Interface
from Nodo import Nodo
from Personal import Personal
from Docente import Docente
from DocenteInvestigador import DocenteInvestigador
from Investigador import Investigador
from Apoyo import Apoyo
@implementer(Interface)
@implementer(ITesorero)
@implementer(IDirector)
class Lista:
    __comienzo=None
    __actual=None
    __indice=0
    __tope=0
    def __init__(self):
        self.__comienzo=None
        self.__actual=None
    def __iter__(self):
        return self
    def __next__(self):
        if self.__indice==self.__tope:
            self.__actual=self.__comienzo
            self.__indice=0
            raise StopIteration
        else:
            self.__indice+=1
            dato=self.__actual.getDato()
            self.__actual=self.__actual.getSiguiente()
            return dato
    def insertarElemento(self,elemento,pos):
        nodo=Nodo(elemento)
        error=False
        if pos==0:
            nodo.setSiguiente(self.__comienzo)
            self.__comienzo=nodo
            self.__actual=self.__comienzo
            self.__tope+=1
        else:
            if self.__comienzo==None:
                error=True
            else:
                i=0
                ant=self.__comienzo
                aux=self.__comienzo
                while aux!=None and i!=pos:
                    ant=aux
                    aux=aux.getSiguiente()
                    i+=1
                if aux==None:
                    error=True
                else:
                    ant.setSiguiente(nodo)
                    nodo.setSiguiente(aux)
                    self.__tope+=1
        if error:
            raise IndexError
    def agregarElemento(self,elemento):
        nodo=Nodo(elemento)
        if self.__comienzo==None:
            self.__comienzo=nodo
            self.__actual=self.__comienzo
        else:
            aux=self.__comienzo
            ant=self.__comienzo
            while aux!=None:
                ant=aux
                aux=aux.getSiguiente()
            ant.setSiguiente(nodo)
        self.__tope+=1
    def mostrarElemento(self,pos):
        error=False
        if self.__comienzo==None:
            error=True
        else:
            i=0
            
            aux=self.__comienzo
            while aux!=None and i!=pos:
                
                aux=aux.getSiguiente()
                i+=1
            if aux==None:
                error=True
            else:
                tipo=''
                if type(aux.getDato())==Docente:
                    tipo='Docente'
                elif type(aux.getDato())==Apoyo:
                    tipo='Personal de Apoyo'
                elif type(aux.getDato())==Investigador:
                    tipo='Investigador'
                else:
                    tipo='Docente Investigador'
                print('El agente almacenado en la posicion:{},es:{}'.format(pos,tipo))
        if error:
            raise IndexError 
    def ordenarPorNombre(self):
        cota=None
        k=None
        while(k!=self.__comienzo):
            k=self.__comienzo
            p=self.__comienzo
            while(p.getSiguiente()!=cota):
                if p.getDato().getNombre()>p.getSiguiente().getDato().getNombre():
                    aux=p.getSiguiente().getDato()
                    p.getSiguiente().setDato(p.getDato())
                    p.setDato(aux)
                    k=p
                p=p.getSiguiente()
            cota=k.getSiguiente()
    def mostrarOrdenadoPorCarrera(self,carrera):
        self.ordenarPorNombre()
        for personal in self:
            if type(personal)==DocenteInvestigador and personal.getCarrera()==carrera:
                personal.mostrarDatos()
    def mostrarPorInvestigacion(self,area):
        contarDI=0
        contarI=0
        for personal in self:
            if isinstance(personal,Investigador) or isinstance(personal,DocenteInvestigador):
                if personal.getArea()==area:
                    if type(personal)==DocenteInvestigador:
                        contarDI+=1
                    elif type(personal)==Investigador:
                        contarI+=1
        print('Cantidad de Investigadores:{}, cantidad de Docentes Investigadores{}'.format(contarI,contarDI))
    def mostrarAgentes(self):
        self.ordenarPorNombre()
        tipo=''
        for personal in self:
            if type(personal)==Docente:
                tipo='Docente'
            elif type(personal)==DocenteInvestigador:
                tipo='Docente Investigador'
            elif type(personal)==Apoyo:
                tipo='Personal de Apoyo'
            elif type(personal)==Investigador:
                tipo='Investigador'
            print('Tipo:{}'.format(tipo))
            personal.mostrarDatosSueldos()
            
            
                
    def toJSON(self):
        d=dict(__class__=self.__class__.__name__,personal=[personal.toJSON() for personal in self])
        return d
    def guardarArchivo(self,objectEncoder):
        diccionario=self.toJSON()
        objectEncoder.guardarJSONArchivo(diccionario,'personal.json')
    def mostrarPorCategoria(self,categoria):
        resultado=0
        for personal in self:
            if type(personal)==DocenteInvestigador:
                if personal.getCategoria()==categoria:
                    
                    resultado+=personal.getImporte()
                    print('{},{},importe:{}'.format(personal.getNombre(),personal.getApellido(),personal.getImporte()))
        print('Total de dinero para solicitar:{}'.format(resultado))
    def gastosSueldoPorEmpleado(self,dni):
        sueldo=0
        bandera=True
        aux=self.__comienzo
        while aux!=None and bandera:
            if aux.getDato().getCuil()==dni:
                sueldo=aux.getDato().calcularSueldo()
                bandera=False
            else:
                aux=aux.getSiguiente()
        if bandera:
            print('No se encontro el empleado.')
        else:
            print('El sueldo del empleado es:',sueldo)
    def modificarBasico(self,dni,basico):
        bandera=True
        aux=self.__comienzo
        while aux!=None and bandera:
            if aux.getDato().getCuil()==dni:
                aux.getDato().setSueldoBasico(basico)
                bandera=False
            else:
                aux=aux.getSiguiente()
        if bandera:
            print('No se encontro el empleado.')
        else:
            print('Se modifico el sueldo basico.')
    def modificarPorcentajeporcargo(self,dni,porcentaje):
        error=None
        bandera=True
        aux=self.__comienzo
        while aux!=None and bandera:
            if aux.getDato().getCuil()==dni:
                if type(aux.getDato())==Docente:
                    aux.getDato().setPorcentaje(porcentaje)
                else:
                    error=-1
                bandera=False
            else:
                aux=aux.getSiguiente()
        if error!=-1:
            if bandera:
                print('No se encontro el empleado.')
            else:
                print('Se modifico el porcentaje por cargo.')
        else:
            print('El DNI no corresponde a un docente.')
    def modificarPorcentajeporcategoría(self,dni,porcentaje):
        error=None
        bandera=True
        aux=self.__comienzo
        while aux!=None and bandera:
            if aux.getDato().getCuil()==dni:
                if type(aux.getDato())==Apoyo:
                    aux.getDato().setPorcentaje(porcentaje)
                else:
                    error=-1
                bandera=False
            else:
                aux=aux.getSiguiente()
        if error!=-1:
            if bandera:
                print('No se encontro el empleado.')
            else:
                print('Se modifico el porcentaje por categoria.')
        else:
            print('El DNI no corresponde a un personal de apoyo.')
    def modificarImporteExtra(self,dni,importe):
        error=None
        bandera=True
        aux=self.__comienzo
        while aux!=None and bandera:
            if aux.getDato().getCuil()==dni:
                if type(aux.getDato())==DocenteInvestigador:
                    aux.getDato().setImporte(importe)
                else:
                    error=-1
                    
                bandera=False
            else:
                aux=aux.getSiguiente()
        if error!=-1:
            if bandera:
                print('No se encontro el empleado.')
            else:
                print('Se modifico el importe extra.')
        else:
            print('El DNI no corresponde a un docente investigador.')