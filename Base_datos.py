import mysql.connector
from mysql.connector import Error

class Parametro_Sistema():
    def __init__(self):
        self.sist_ID = 0
        self.sist_VS_MIN = ""
        self.sist_VS_MAX = ""
        self.sist_VP_MIN = ""
        self.sist_VP_MAX = ""
        self.sist_Estado = ""
    
    def setParametros(self, ID, VS_MIN, VS_MAX, VP_MIN,VP_MAX, ESTADO):
        self.sist_ID = ID
        self.sist_VS_MIN = VS_MIN
        self.sist_VS_MAX = VS_MAX
        self.sist_VP_MIN = VP_MIN
        self.sist_VP_MAX = VP_MAX
        self.sist_Estado = ESTADO
    def __str__(self):
        return f"ID:{self.sist_ID}, VP_MIN:{self.sist_VP_MIN}"

class Sistema:
    def __init__(self):
        self.param_sistem = dict()
        self.contador = 0
        self.sistemas = ["New"]
        
    def reportParametros(self):
        print(f"REPORTE DE SISTEMA")
        print(f"-------------------")
        for clave in self.param_sistem:
            print(self.param_sistem[clave])
    def reportIds(self):
        self.loadAllParams()
        for clave in self.param_sistem:
            self.sistemas.append(clave)
        return self.sistemas
        
    def loadAllParams(self):
        idx = {
            "ID":0,
            "VS_MIN":1,
            "VS_MAX":2,
            "VP_MIN":3,
            "VP_MAX":4,
            "ESTADO_PLANTA":5
        }
        
        try:
            
            connection = mysql.connector.connect(host='localhost', user= 'root', passwd='groot', db='hidroponia' )
            cur = connection.cursor()
            cur.execute( "SELECT * FROM parametro_colores" )
            for registro in cur.fetchall():
                plant = Parametro_Sistema()
                ID = registro[idx["ID"]]
                VS_MIN = registro[idx["VS_MIN"]]
                VS_MAX = registro[idx["VS_MAX"]]
                VP_MIN = registro[idx["VP_MIN"]]
                VP_MAX = registro[idx["VP_MAX"]]
                ESTADO_PLANTA = registro[idx["ESTADO_PLANTA"]]
                plant.setParametros(ID, VS_MIN, VS_MAX, VP_MIN,VP_MAX,ESTADO_PLANTA)
                self.contador = self.contador + 1
                self.param_sistem[ID]=plant
                
        except Error as error:
            print("Error al ejecutar el procedimiento: {}".format(error))
        finally:
            if (connection.is_connected()):
                cur.close()
                connection.close()
                print("Los parámetros de colores se han cargado exitosamente...")
    
    def getParams(self,ID):
        connection = mysql.connector.connect(host='localhost', user= 'root', passwd='groot', db='hidroponia' )
        cur = connection.cursor()
        getParams = "SELECT * FROM parametro_colores WHERE idPARAMETRO_COLORES = {}".format(ID)
        cur.execute(getParams)
        datos = cur.fetchone()
        cur.close()
        return datos


    def Subir_Parametros(self, VS_MIN, VS_MAX, VP_MIN, VP_MAX, ESTADO_PLANTA):
        #self.loadAllParams()
        
        connection = mysql.connector.connect(host='localhost', user= 'root', passwd='groot', db='hidroponia' )
        cur = connection.cursor()
        addFunction = "INSERT INTO parametro_colores (VS_MIN, VS_MAX, VP_MIN, VP_MAX, ESTADO_PLANTA) VALUES (%s, %s, %s, %s, %s)"
        cur.execute( addFunction, (VS_MIN ,VS_MAX, VP_MIN ,VP_MAX, ESTADO_PLANTA))
        
        connection.commit()
        cur.close()
    
    def Modificar_Parametros(self, ID, VS_MIN, VS_MAX, VP_MIN, VP_MAX, ESTADO_PLANTA):
        connection = mysql.connector.connect(host='localhost', user= 'root', passwd='groot', db='hidroponia' )
        cur = connection.cursor()
        putFunction = "UPDATE parametro_colores SET VS_MIN='{}', VS_MAX='{}', VP_MIN='{}', VP_MAX='{}', ESTADO_PLANTA='{}' WHERE idPARAMETRO_COLORES='{}'".format(VS_MIN, VS_MAX, VP_MIN, VP_MAX, ESTADO_PLANTA, ID)
        cur.execute(putFunction)

        connection.commit()
        cur.close()

    def Modificar_Estado(self, ID, ESTADO_PLANTA):
        connection = mysql.connector.connect(host='localhost', user= 'root', passwd='groot', db='hidroponia' )
        cur = connection.cursor()
        putFunction2 = "UPDATE parametro_colores SET ESTADO_PLANTA='{}' WHERE idPARAMETRO_COLORES='{}'".format(ESTADO_PLANTA, ID)
        cur.execute(putFunction2)

        connection.commit()
        cur.close()

plantas = Sistema()
lista_sistemas = plantas.reportIds()
