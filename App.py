from tkinter import *
from PIL import Image, ImageTk
import cv2
import imutils
import numpy as np
from tkinter import messagebox
from app_area import Area_Saludable
from Base_datos import *

#----------VARIABLES-----------
contador_general = 0
contador_update = 0
contador_color = 0
contador_color_Putr = 0

#---------FUNCIONES--------------

# Funcion Visualizar
def visualizar():
    global ventana, frame, Tmin, Tmax, Pmin, Pmax, Lmin, Lmax, ret
    # Leemos la videocaptura
    if cap is not None:
        ret, frame = cap.read()

        # Si es correcta
        if ret == True:

            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)


            # Rendimensionamos el video
            frame = imutils.resize(frame, width=640)

            # Convertimos el video
            im = Image.fromarray(frame)
            img = ImageTk.PhotoImage(image=im)

            # Mostramos en el GUI
            lblVideo.configure(image=img)
            lblVideo.image = img
            lblVideo.after(10, visualizar)

        else:
            cap.release()


# Colores

def Det_Color():
    global Tmin, Tmax, Pmin, Pmax, Lmin, Lmax, contador_color
    var =  clicked2.get()

    if (var == "New") or (contador_color == 1):
        # Extraemos el sliders H
        Tmin = H_MIN.get()
        Tmax = H_MAX.get()
        #print(Tmin, Tmax)
        # Extraemos el sliders S
        Pmin = S_MIN.get()
        Pmax = S_MAX.get()
        #print(Pmin, Pmax)
        # Extraemos el sliders V
        Lmin = V_MIN.get()
        Lmax = V_MAX.get()
    else: 
        plantas = Sistema()
        param_data = plantas.getParams(var)
        contador_color = 1

        #------V = (H,S,V)---------
        
        param_data_VS_MIN = param_data[1].replace('(', '')
        param_data_VS_MIN2 = param_data_VS_MIN.replace(')', '')

        VS_MIN = list(param_data_VS_MIN2.split(sep = ','))
        
        Tmin = int(VS_MIN[0])
        Pmin = int(VS_MIN[1])
        Lmin = int(VS_MIN[2])
        
        H_MIN.set(Tmin)
        S_MIN.set(Pmin)
        V_MIN.set(Lmin)


        param_data_VS_MAX = param_data[2].replace('(', '')
        param_data_VS_MAX2 = param_data_VS_MAX.replace(')', '')

        VS_MAX = list(param_data_VS_MAX2.split(sep = ','))

        Tmax = int(VS_MAX[0])
        Pmax = int(VS_MAX[1])
        Lmax = int(VS_MAX[2])

        H_MAX.set(Tmax)
        S_MAX.set(Pmax)
        V_MAX.set(Lmax)
    
    return Tmin, Pmin, Lmin, Tmax, Pmax, Lmax



def colores():
    global H_MIN, H_MAX, S_MIN, S_MAX, V_MAX, Kx, Ky, detcolor
    global color_brilla, color_oscuro, mascara


    # Activamos deteccion de color
    detcolor = 1

    Det_Color()

    if contador_general == 0:
        messagebox.showwarning("Error", "Haga click en iniciar")

    # Deteccion de color
    if detcolor == 1:
        # Deteccion de color
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # Establecemos el rango minimo y maximo para la codificacion HSV
        color_oscuro = np.array([Tmin, Pmin, Lmin])
        color_brilla = np.array([Tmax, Pmax, Lmax])

        # Detectamos los pixeles que esten dentro de los rangos
        mascara = cv2.inRange(hsv, color_oscuro, color_brilla)

        # Mascara
        mask = cv2.bitwise_and(frame, frame, mask=mascara)

        mask = imutils.resize(mask, width=360)

        # Convertimos el video
        im2 = Image.fromarray(mask)
        img2 = ImageTk.PhotoImage(image=im2)

        # Mostramos en el GUI
        lblVideo2.configure(image=img2)
        lblVideo2.image = img2
        lblVideo2.after(10, colores)
        lblVideo2. place(x = 970, y = 30)

# PUTREFACCION
def Det_Putrefaccion():
    global Tmin_Putr, Tmax_Putr, Pmin_Putr, Pmax_Putr, Lmin_Putr, Lmax_Putr, contador_color_Putr
    var =  clicked2.get()

    if (var == "New") or (contador_color_Putr == 1) :
        # Extraemos el sliders H
        Tmin_Putr = H_MIN_Putr.get()
        Tmax_Putr = H_MAX_Putr.get()
        # Extraemos el sliders S
        Pmin_Putr = S_MIN_Putr.get()
        Pmax_Putr = S_MAX_Putr.get()
        # Extraemos el sliders V
        Lmin_Putr = V_MIN_Putr.get()
        Lmax_Putr = V_MAX_Putr.get()
    else: 
        plantas = Sistema()
        param_data = plantas.getParams(var)
        contador_color_Putr = 1
        #------V = (H,S,V)---------
        
        param_data_VP_MIN = param_data[3].replace('(', '')
        param_data_VP_MIN2 = param_data_VP_MIN.replace(')', '')

        VP_MIN = list(param_data_VP_MIN2.split(sep = ','))
        
        Tmin_Putr = int(VP_MIN[0])
        Pmin_Putr = int(VP_MIN[1])
        Lmin_Putr = int(VP_MIN[2])
        
        H_MIN_Putr.set(Tmin_Putr)
        S_MIN_Putr.set(Pmin_Putr)
        V_MIN_Putr.set(Lmin_Putr)


        param_data_VP_MAX = param_data[4].replace('(', '')
        param_data_VP_MAX2 = param_data_VP_MAX.replace(')', '')

        VP_MAX = list(param_data_VP_MAX2.split(sep = ','))

        Tmax_Putr = int(VP_MAX[0])
        Pmax_Putr = int(VP_MAX[1])
        Lmax_Putr = int(VP_MAX[2])

        H_MAX_Putr.set(Tmax_Putr)
        S_MAX_Putr.set(Pmax_Putr)
        V_MAX_Putr.set(Lmax_Putr)
    
    return Tmin_Putr, Pmin_Putr, Lmin_Putr, Tmax_Putr, Pmax_Putr, Lmax_Putr



def Putrefaccion():
    global H_MIN_Putr, H_MAX_Putr, S_MIN_Putr, S_MAX_Putr, V_MAX_Putr, detcolor_Putr
    global color_brilla_Putr, color_oscuro_Putr, mascara_Putr

    Det_Putrefaccion()

    # Activamos deteccion de color
    detcolor_Putr = 1
    

    if contador_general == 0:
        messagebox.showwarning("Error", "Haga click en iniciar")    
    # Deteccion de color
    if detcolor_Putr == 1:
        # Deteccion de color
        hsv2 = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # Establecemos el rango minimo y maximo para la codificacion HSV
        color_oscuro_Putr = np.array([Tmin_Putr, Pmin_Putr, Lmin_Putr])
        color_brilla_Putr = np.array([Tmax_Putr, Pmax_Putr, Lmax_Putr])

        # Detectamos los pixeles que esten dentro de los rangos
        mascara_Putr = cv2.inRange(hsv2, color_oscuro_Putr, color_brilla_Putr)

        # Mascara
        mask_Putr = cv2.bitwise_and(frame, frame, mask=mascara_Putr)

        mask_Putr = imutils.resize(mask_Putr, width=360)

        # Convertimos el video
        im3 = Image.fromarray(mask_Putr)
        img3 = ImageTk.PhotoImage(image=im3)

        # Mostramos en el GUI
        lblVideo3.configure(image=img3)
        lblVideo3.image = img3
        lblVideo3.after(10, Putrefaccion)
        lblVideo3. place(x = 970, y = 330)

# SUBIR DATOS
def Subir_datos():
    global contador_update, Estado, area_saludable2, area_podrida2, Estado_planta
    contador_update = contador_update + 1
    if contador_general == 0:
        messagebox.showwarning("Error", "Haga click en iniciar")
    
    area_saludable = Area_Saludable(ret, frame, color_oscuro, color_brilla, mascara )
    area_podrida = Area_Saludable(ret, frame, color_oscuro_Putr, color_brilla_Putr, mascara_Putr )

    if area_podrida > 100:
        Estado = "Poco podrida"
        if area_podrida >= area_saludable:
            Estado = "Muy podrida"
        if area_saludable == 0:
            Estado = "Podrida"
    if area_podrida <= 100:
        Estado = "Saludable"


    if contador_update == 1 or contador_update == 0:
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
    
    VS_Min = "(" + str(Tmin) + "," + str(Pmin) + "," +  str(Lmin) + ")"
    VS_Max = "(" + str(Tmax) + "," + str(Pmax) + "," +  str(Lmax) + ")"

    VP_Min = "(" + str(Tmin_Putr) + "," + str(Pmin_Putr) + "," +  str(Lmin_Putr) + ")"
    VP_Max = "(" + str(Tmax_Putr) + "," + str(Pmax_Putr) + "," +  str(Lmax_Putr) + ")" 

    var2 =  clicked2.get()
    planta = Sistema()
    if var2 == "New":
        planta = Sistema()
        planta.Subir_Parametros(VS_Min, VS_Max, VP_Min, VP_Max, Estado)
    else:
        planta.Modificar_Parametros(var2, VS_Min, VS_Max, VP_Min, VP_Max, Estado)


# Funcion iniciar
def iniciar():
    global cap, contador_general
    # Elegimos la camara
    contador_general = 1
    # cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    cap = cv2.VideoCapture("http://192.168.159.241:8080/video")
    visualizar()

# Funcion finalizar
def finalizar():
    ventana.withdraw()


# Variables
cap = None


ventana = Tk()
ventana.title("Hidroponia")
#ventana.geometry("1280x720")
altura_pantalla = ventana.winfo_screenheight()-int(50)
ancho_pantalla = ventana.winfo_screenwidth()
ventana.geometry(f'{ancho_pantalla}x{altura_pantalla}')

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

# Iniciar Video
imagenBI = PhotoImage(file = r'./iconos/Inicio.png')
inicio = Button(ventana, text="Iniciar", image=imagenBI, height="40", width="200", command=iniciar)
inicio.place(x = 100, y = 600)

# Finalizar Video
imagenBF = PhotoImage(file = r'./iconos/Finalizar.png')
fin = Button(ventana, text="Finalizar", image= imagenBF, height="40", width="200", command=ventana.quit)
fin.place(x = 980, y = 600)

# Colores
imagenBC = PhotoImage(file = r'./iconos/Colores.png')
color = Button(ventana, text="Colores", image= imagenBC, height="40", width="200", command=colores)
color.place(x = 82, y = 250)

#Putrefaccion
Putrefaccion_boton = Button(ventana, text="Putrefaccion", image= imagenBC, height="40", width="200", command=Putrefaccion)
Putrefaccion_boton.place(x = 82, y = 550)

#Subir datos
imagenBU = PhotoImage(file = r'./iconos/Update.png')
Update = Button(ventana, text="Subir datos", image= imagenBU, height="40", width="200", command=Subir_datos)
Update.place(x = 470, y = 550)

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
H_MAX.set(255)
# Color S
textoS = Label(ventana, text="S value: ")
textoS.place(x = 30, y = 170)
S_MIN = Scale(ventana, from_ = 0, to = 255, orient=HORIZONTAL)
S_MIN.place(x = 80, y = 150)
S_MAX = Scale(ventana, from_ = 0, to = 255, orient=HORIZONTAL)
S_MAX.place(x = 190, y = 150)
S_MAX.set(255)
# Color V
textoV = Label(ventana, text="V value: ")
textoV.place(x = 30, y = 220)
V_MIN = Scale(ventana, from_ = 0, to = 255, orient=HORIZONTAL)
V_MIN.place(x = 80, y = 200)
V_MAX = Scale(ventana, from_ = 0, to = 255, orient=HORIZONTAL)
V_MAX.place(x = 190, y = 200)
V_MAX.set(255)

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
H_MAX_Putr.set(255)
# Color S
textoS_Putr = Label(ventana, text="S value: ")
textoS_Putr.place(x = 30, y = 470)
S_MIN_Putr = Scale(ventana, from_ = 0, to = 255, orient=HORIZONTAL)
S_MIN_Putr.place(x = 80, y = 450)
S_MAX_Putr = Scale(ventana, from_ = 0, to = 255, orient=HORIZONTAL)
S_MAX_Putr.place(x = 190, y = 450)
S_MAX_Putr.set(255)
# Color V
textoV_Putr = Label(ventana, text="V value: ")
textoV_Putr.place(x = 30, y = 520)
V_MIN_Putr = Scale(ventana, from_ = 0, to = 255, orient=HORIZONTAL)
V_MIN_Putr.place(x = 80, y = 500)
V_MAX_Putr = Scale(ventana, from_ = 0, to = 255, orient=HORIZONTAL)
V_MAX_Putr.place(x = 190, y = 500)
V_MAX_Putr.set(255)

# Video
lblVideo = Label(ventana)
lblVideo.place(x = 320, y = 30)

lblVideo2 = Label(ventana)
lblVideo2.place(x = 470, y = 500)

lblVideo3 = Label(ventana)
lblVideo3.place(x = 470, y = 800)

ventana.mainloop()
