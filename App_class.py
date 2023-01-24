from tkinter import *
from PIL import Image, ImageTk
import cv2
import imutils
import numpy as np
from tkinter import messagebox
from app_area import Area_Saludable
from Base_datos import *


class Planta():
    def __init__ (self):
        self.inicio()

    def inicio (self):
        self.cap = None
        self.n = 0
        self.lista = []
        self.contador_general = 0
        self.contador_update = 0
        self.contador_color = 0
        self.contador_color_Putr = 0
        self.plantas = Sistema()
        # self.crear_botones()

    # def crear_botones(self):
    #     # -----------------------------------Sliders---------------------------------


    #     # Color H
    #     self.H_MIN = H_MIN
    #     self.H_MAX = H_MAX
    #     # Color S
    #     self.S_MIN = S_MIN
    #     self.S_MAX = S_MAX
    #     # Color V
    #     textoV.place(x = 30, y = 220)
    #     self.V_MIN = V_MIN
    #     self.V_MAX = V_MAX

    #     # Color H
    #     self.H_MIN_Putr = H_MIN_Putr
    #     self.H_MAX_Putr = H_MAX_Putr
    #     # Color S
    #     self.S_MIN_Putr = S_MIN_Putr
    #     self.S_MAX_Putr = S_MAX_Putr
    #     # Color V
    #     self.V_MIN_Putr = V_MIN_Putr
    #     self.V_MAX_Putr = V_MAX_Putr



    def iniciar(self):
        self.contador_general = 1
        self.cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        self.visualizar()

    def finalizar(self):
        ventana.withdraw() 

    def visualizar(self):
            # Leemos la videocaptura
        if self.cap is not None:
            self.ret, self.frame = self.cap.read()

            # Si es correcta
            if self.ret == True:

                self.frame = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)


                # Rendimensionamos el video
                self.frame = imutils.resize(self.frame, width=640)

                # Convertimos el video
                im = Image.fromarray(self.frame)
                img = ImageTk.PhotoImage(image=im)

                # Mostramos en el GUI
                lblVideo.configure(image=img)
                lblVideo.image = img
                lblVideo.after(10, self.visualizar)

            else:
                self.cap.release()
        
    def Det_Color(self):
            self.var =  clicked2.get()

            if (self.var == "New") or (self.contador_color == 1):
                # Extraemos el sliders H
                self.Tmin = H_MIN.get()
                self.Tmax = H_MAX.get()
                #print(Tmin, Tmax)
                # Extraemos el sliders S
                self.Pmin = S_MIN.get()
                self.Pmax = S_MAX.get()
                #print(Pmin, Pmax)
                # Extraemos el sliders V
                self.Lmin = V_MIN.get()
                self.Lmax = V_MAX.get()
            else: 
                param_data = self.plantas.getParams(self.var)
                self.contador_color = 1

                #------V = (H,S,V)---------
                
                param_data_VS_MIN = param_data[1].replace('(', '')
                param_data_VS_MIN2 = param_data_VS_MIN.replace(')', '')

                VS_MIN = list(param_data_VS_MIN2.split(sep = ','))
                
                self.Tmin = int(VS_MIN[0])
                self.Pmin = int(VS_MIN[1])
                self.Lmin = int(VS_MIN[2])
                
                H_MIN.set(self.Tmin)
                S_MIN.set(self.Pmin)
                V_MIN.set(self.Lmin)


                param_data_VS_MAX = param_data[2].replace('(', '')
                param_data_VS_MAX2 = param_data_VS_MAX.replace(')', '')

                VS_MAX = list(param_data_VS_MAX2.split(sep = ','))

                self.Tmax = int(VS_MAX[0])
                self.Pmax = int(VS_MAX[1])
                self.Lmax = int(VS_MAX[2])

                H_MAX.set(self.Tmax)
                S_MAX.set(self.Pmax)
                V_MAX.set(self.Lmax)

    def colores(self):
        self.detcolor = 1
        self.Det_Color()

        if self.contador_general == 0:
            messagebox.showwarning("Error", "Haga click en iniciar")

        # Deteccion de color
        if self.detcolor == 1:
            # Deteccion de color
            hsv = cv2.cvtColor(self.frame, cv2.COLOR_BGR2HSV)

            # Establecemos el rango minimo y maximo para la codificacion HSV
            self.color_oscuro = np.array([self.Tmin, self.Pmin, self.Lmin])
            self.color_brilla = np.array([self.Tmax, self.Pmax, self.Lmax])

            # Detectamos los pixeles que esten dentro de los rangos
            self.mascara = cv2.inRange(hsv, self.color_oscuro, self.color_brilla)

            # Mascara
            mask = cv2.bitwise_and(self.frame, self.frame, mask=self.mascara)

            mask = imutils.resize(mask, width=360)

            # Convertimos el video
            im2 = Image.fromarray(mask)
            img2 = ImageTk.PhotoImage(image=im2)

            # Mostramos en el GUI
            lblVideo2.configure(image=img2)
            lblVideo2.image = img2
            lblVideo2.after(10, self.colores)
            lblVideo2. place(x = 970, y = 30)
    
    def Det_Putrefaccion(self):
        self.var =  clicked2.get()
        if (self.var == "New") or (self.contador_color_Putr == 1) :
                # Extraemos el sliders H
                self.Tmin_Putr = H_MIN_Putr.get()
                self.Tmax_Putr = H_MAX_Putr.get()
                #print(Tmin, Tmax)
                # Extraemos el sliders S
                self.Pmin_Putr = S_MIN_Putr.get()
                self.Pmax_Putr = S_MAX_Putr.get()
                #print(Pmin, Pmax)
                # Extraemos el sliders V
                self.Lmin_Putr = V_MIN_Putr.get()
                self.Lmax_Putr = V_MAX_Putr.get()
        else: 
            param_data = self.plantas.getParams(self.var)
            self.contador_color_Putr = 1
            #------V = (H,S,V)---------
            
            param_data_VP_MIN = param_data[3].replace('(', '')
            param_data_VP_MIN2 = param_data_VP_MIN.replace(')', '')

            VP_MIN = list(param_data_VP_MIN2.split(sep = ','))
            
            self.Tmin_Putr = int(VP_MIN[0])
            self.Pmin_Putr = int(VP_MIN[1])
            self.Lmin_Putr = int(VP_MIN[2])
            
            H_MIN_Putr.set(self.Tmin_Putr)
            S_MIN_Putr.set(self.Pmin_Putr)
            V_MIN_Putr.set(self.Lmin_Putr)


            param_data_VP_MAX = param_data[4].replace('(', '')
            param_data_VP_MAX2 = param_data_VP_MAX.replace(')', '')

            VP_MAX = list(param_data_VP_MAX2.split(sep = ','))

            self.Tmax_Putr = int(VP_MAX[0])
            self.Pmax_Putr = int(VP_MAX[1])
            self.Lmax_Putr = int(VP_MAX[2])

            H_MAX_Putr.set(self.Tmax_Putr)
            S_MAX_Putr.set(self.Pmax_Putr)
            V_MAX_Putr.set(self.Lmax_Putr)

    def Putrefaccion(self):
        self.Det_Putrefaccion()

        # Activamos deteccion de color
        self.detcolor_Putr = 1
        

        #print(Lmin, Lmax)
        # Kx = Kernel_X.get()
        # Ky = Kernel_Y.get()
        if self.contador_general == 0:
            messagebox.showwarning("Error", "Haga click en iniciar")    
        # Deteccion de color
        if self.detcolor_Putr == 1:
            # Deteccion de color
            hsv2 = cv2.cvtColor(self.frame, cv2.COLOR_BGR2HSV)

            # Establecemos el rango minimo y maximo para la codificacion HSV
            self.color_oscuro_Putr = np.array([self.Tmin_Putr, self.Pmin_Putr, self.Lmin_Putr])
            self.color_brilla_Putr = np.array([self.Tmax_Putr, self.Pmax_Putr, self.Lmax_Putr])

            # Detectamos los pixeles que esten dentro de los rangos
            self.mascara_Putr = cv2.inRange(hsv2, self.color_oscuro_Putr, self.color_brilla_Putr)

            # Mascara
            mask_Putr = cv2.bitwise_and(self.frame, self.frame, mask=self.mascara_Putr)

            mask_Putr = imutils.resize(mask_Putr, width=360)

            # Convertimos el video
            im3 = Image.fromarray(mask_Putr)
            img3 = ImageTk.PhotoImage(image=im3)

            # Mostramos en el GUI
            lblVideo3.configure(image=img3)
            lblVideo3.image = img3
            lblVideo3.after(10, self.Putrefaccion)
            lblVideo3. place(x = 970, y = 330)
    
    def Subir_datos(self):
        self.contador_update = self.contador_update + 1
        if self.contador_general == 0:
            messagebox.showwarning("Error", "Haga click en iniciar")
        
        area_saludable = Area_Saludable(self.ret, self.frame, self.color_oscuro, self.color_brilla, self.mascara )
        area_podrida = Area_Saludable(self.ret, self.frame, self.color_oscuro_Putr, self.color_brilla_Putr, self.mascara_Putr )

        if area_podrida > 100:
            Estado = "Poco podrida"
            if area_podrida >= area_saludable:
                Estado = "Muy podrida"
            if area_saludable == 0:
                Estado = "Podrida"
        if area_podrida <= 100:
            Estado = "Saludable"


        if self.contador_update == 1 or self.contador_update == 0:
            area_saludable2 = Label(ventana, text = f'El área detectada saludable es: {area_saludable}')
            area_saludable2.place(x = 470, y = 600)
            area_podrida2 = Label(ventana, text = f'El área detectada podrida es: {area_podrida}')
            area_podrida2.place(x = 470, y = 620)

            Estado_planta = Label(ventana, text = f'El estado de la planta es: {Estado}')
            Estado_planta.place(x = 470, y = 650)

        if contador_update == 2:
            contador_update = 0
            area_saludable2.destroy()
            area_podrida2.destroy()
            Estado_planta.destroy()

        VS_Min = "(" + str(self.Tmin) + "," + str(self.Pmin) + "," +  str(self.Lmin) + ")"
        VS_Max = "(" + str(self.Tmax) + "," + str(self.Pmax) + "," +  str(self.Lmax) + ")"

        VP_Min = "(" + str(self.Tmin_Putr) + "," + str(self.Pmin_Putr) + "," +  str(self.Lmin_Putr) + ")"
        VP_Max = "(" + str(self.Tmax_Putr) + "," + str(self.Pmax_Putr) + "," +  str(self.Lmax_Putr) + ")" 

        var2 =  clicked2.get()

        if var2 == "New":
            self.planta.Subir_Parametros(VS_Min, VS_Max, VP_Min, VP_Max, Estado)
        else:
            self.planta.Modificar_Parametros(var2, VS_Min, VS_Max, VP_Min, VP_Max, Estado)



        


ventana = Tk()
ventana.title("Hidroponia")
#ventana.geometry("1280x720")
altura_pantalla = ventana.winfo_screenheight()-int(50)
ancho_pantalla = ventana.winfo_screenwidth()
ventana.geometry(f'{ancho_pantalla}x{altura_pantalla}')

#ventana.attributes('-fullscreen', True)
ventana.iconbitmap('./iconos/logo.ico')

Fondo = PhotoImage(file = r'./iconos/Fondo.png')
background = Label(image = Fondo, text = "Fondo")
background.place(x = 0, y = 0, relwidth = 1, relheight = 1)

# Interfaz
texto1 = Label(ventana, text="VIDEO EN TIEMPO REAL: ")
texto1.place(x = 580, y = 10)

# texto2 = Label(ventana, text="CONVERSION DE COLOR: ")
# texto2.place(x = 1010, y = 100)

texto3 = Label(ventana, text="DETECCION DE COLOR: ")
texto3.place(x = 110, y = 50)

texto4 = Label(ventana, text = "DETECCIÓN DE PUTREFACCIÓN:")
texto4.place(x = 82, y = 350)
#----------------------------Botones----------------------------------------

plantas2 = Planta()


# Iniciar Video
imagenBI = PhotoImage(file = r'./iconos/Inicio.png')
inicio = Button(ventana, text="Iniciar", image=imagenBI, height="40", width="200", command = plantas2.iniciar)
inicio.place(x = 100, y = 600)

# Finalizar Video
imagenBF = PhotoImage(file = r'./iconos/Finalizar.png')
fin = Button(ventana, text="Finalizar", image= imagenBF, height="40", width="200", command = ventana.quit)
fin.place(x = 980, y = 600)

# Colores
imagenBC = PhotoImage(file = r'./iconos/Colores.png')
color = Button(ventana, text="Colores", image= imagenBC, height="40", width="200", command = plantas2.colores)
color.place(x = 82, y = 250)

#Putrefaccion
Putrefaccion_boton = Button(ventana, text="Putrefaccion", image= imagenBC, height="40", width="200", command = plantas2.Putrefaccion)
Putrefaccion_boton.place(x = 82, y = 550)

#Subir datos
imagenBU = PhotoImage(file = r'./iconos/Update.png')
Update = Button(ventana, text="Subir datos", image= imagenBU, height="40", width="200", command = plantas2.Subir_datos)
Update.place(x = 470, y = 550)

# # ESCOGER CAMARA

# text_camara = Label(ventana, text = "Eliga su cámara")

# clicked = StringVar()
# clicked.set(lista[0])

# camaras = OptionMenu(ventana, clicked, *lista)
# camaras.place(x = 560, y = 520)
# text_camara.place(x = 470, y = 520)

# ESCOGER SISTEMA
text_sistema = Label(ventana, text = "Eliga el sistema")
clicked2 = StringVar()
lista_sistemas2 = list(lista_sistemas)
clicked2.set(lista_sistemas2[0])

sistemas2 = OptionMenu(ventana, clicked2, *lista_sistemas2)
sistemas2.place(x = 740, y = 520)
text_sistema.place(x = 650, y = 520)

# -----------------------------------Sliders---------------------------------
#------------------------------COLOR-----------------
# Max y min
texto_Max = Label(ventana, text="Min Value")
texto_Max.place(x = 100, y = 80)
texto_Min = Label(ventana, text="Max Value")
texto_Min.place(x = 210, y = 80)

# Color H
textoH = Label(ventana, text="H value: ")
textoH.place(x = 30, y = 120)
H_MIN = Scale(ventana, from_ = 0, to = 255, orient=HORIZONTAL)
H_MIN.place(x = 80, y = 100)
H_MAX = Scale(ventana, from_ = 0, to = 255, orient=HORIZONTAL)
H_MAX.place(x = 190, y = 100)
# Color S
textoS = Label(ventana, text="S value: ")
textoS.place(x = 30, y = 170)
S_MIN = Scale(ventana, from_ = 0, to = 255, orient=HORIZONTAL)
S_MIN.place(x = 80, y = 150)
S_MAX = Scale(ventana, from_ = 0, to = 255, orient=HORIZONTAL)
S_MAX.place(x = 190, y = 150)
# Color V
textoV = Label(ventana, text="V value: ")
textoV.place(x = 30, y = 220)
V_MIN = Scale(ventana, from_ = 0, to = 255, orient=HORIZONTAL)
V_MIN.place(x = 80, y = 200)
V_MAX = Scale(ventana, from_ = 0, to = 255, orient=HORIZONTAL)
V_MAX.place(x = 190, y = 200)

#-----------------PUTREFACCION----------------
texto_Max_Putr = Label(ventana, text="Min Value")
texto_Max_Putr.place(x = 100, y = 380)
texto_Min_Putr = Label(ventana, text="Max Value")
texto_Min_Putr.place(x = 210, y = 380)
# Color H
textoH_Putr = Label(ventana, text="H value: ")
textoH_Putr.place(x = 30, y = 420)
H_MIN_Putr = Scale(ventana, from_ = 0, to = 255, orient=HORIZONTAL)
H_MIN_Putr.place(x = 80, y = 400)
H_MAX_Putr = Scale(ventana, from_ = 0, to = 255, orient=HORIZONTAL)
H_MAX_Putr.place(x = 190, y = 400)
# Color S
textoS_Putr = Label(ventana, text="S value: ")
textoS_Putr.place(x = 30, y = 470)
S_MIN_Putr = Scale(ventana, from_ = 0, to = 255, orient=HORIZONTAL)
S_MIN_Putr.place(x = 80, y = 450)
S_MAX_Putr = Scale(ventana, from_ = 0, to = 255, orient=HORIZONTAL)
S_MAX_Putr.place(x = 190, y = 450)
# Color V
textoV_Putr = Label(ventana, text="V value: ")
textoV_Putr.place(x = 30, y = 520)
V_MIN_Putr = Scale(ventana, from_ = 0, to = 255, orient=HORIZONTAL)
V_MIN_Putr.place(x = 80, y = 500)
V_MAX_Putr = Scale(ventana, from_ = 0, to = 255, orient=HORIZONTAL)
V_MAX_Putr.place(x = 190, y = 500)


# Video
lblVideo = Label(ventana)
lblVideo.place(x = 320, y = 30)

lblVideo2 = Label(ventana)
lblVideo2.place(x = 470, y = 500)

lblVideo3 = Label(ventana)
lblVideo3.place(x = 470, y = 800)

ventana.mainloop()