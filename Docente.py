from Personal import Personal
class Docente(Personal):
    __carrera=''
    __cargo=''
    __catedra=''
    __porcentajeCargo=None
    def __init__(self,cuil='',apellido='',nombre='',sueldoBasico=0,antiguedad=0,carrera='',cargo='',catedra='',areaInvestigacion='',tipoInvestigacion=''):
        super(). __init__(cuil,apellido,nombre,sueldoBasico,antiguedad,carrera,cargo,catedra,areaInvestigacion,tipoInvestigacion)
        self.__carrera=carrera
        self.__cargo=cargo
        self.__catedra=catedra
        self.__porcentajeCargo=None
    def getCarrera(self):
        return self.__carrera
    def getCargo(self):
        return self.__cargo
    def getCatedra(self):
        return self.__catedra
    def setPorcentaje(self,porcentaje):
        self.__porcentajeCargo=porcentaje
    def calcularSueldo(self):
        resultado=0
        if self.__porcentajeCargo==None:
            porcentaje=0
            sueldoCargo=0
            if self.__cargo=='simple':
                porcentaje+=10
            elif self.__cargo=='semiexclusivo':
                porcentaje+=20
            elif self.__cargo=='exclusivo':
                porcentaje+=50
            sueldoCargo=(self.getSueldo()*porcentaje)/100
            resultado=self.getSueldo()+self.calcularSueldoPorAnt()+sueldoCargo
        else:
            resultado=self.getSueldo()+self.calcularSueldoPorAnt()+self.__porcentajeCargo
        return resultado
    def toJSON(self):
        d=dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(super().toJSON(),carrera=self.__carrera,cargo=self.__cargo,catedra=self.__catedra)
        )
        return d