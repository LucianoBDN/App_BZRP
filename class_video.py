from datetime import datetime


class Video:
    def __init__(self, titulo: str, vistas: int, tiempo: int, url_youtube: str, fecha_lanzamiento: str):
        self.titulo = titulo
        self.vistas = vistas
        self.tiempo = tiempo
        self.url_youtube = url_youtube
        self.fecha_lanzamiento = fecha_lanzamiento
        self.sesion = None
        self.colaborador = None
        self.codigo_url = None
        
    def mostrar_tema(self):
        #Agregar los datos pertinentes para que a la hora de mostrar se vean los datos completos del video
        print(f"Titulo: {self.titulo}")
        print(f"Colaborador: {self.colaborador}")
        print(self.codigo_url)
        print(f"Session #: {self.sesion}")
        print(f"Vistas: {self.vistas}")
        print(f"Duración: {self.tiempo} segundos")
        print(f"URL de YouTube: {self.url_youtube}")
        print(f"Fecha de Lanzamiento: {self.fecha_lanzamiento.strftime("%d-%m-%Y")}")
        print("*"*30)

    def dividir_titulo(self):
        titulo_dividido = self.titulo.split("|")
        self.colaborador = " ".join(titulo_dividido[0].split()).strip()
      
        sesion = titulo_dividido[1].split("#")
        self.sesion = int(sesion[1].strip())
       
        #Debe setear el atributo sesion y colaborador con los datos obtenidos del 
        #titulo del video
        #eto ya ta
        
        
    
    def obtener_codigo_url(self):
        #Debe setear el atributo codigo_url con el codigo obtenido del atributo url_youtube
        #Por ej: si la url es https://www.youtube.com/watch?v=nicki13 
        #el codigo seria nicki13
        separador = self.url_youtube.split("=")
        self.codigo_url = separador[1]

        
    
    def formatear_fecha(self):
        #Necesitamos que la fecha de lanzamiento sea un objeto de la clase datetime (investigar).
        #Para ello deberan dividir la fecha (en formato string) en dia, mes y año y a partir de 
        #esos datos, crear la nueva fecha. 
        separador = self.fecha_lanzamiento.split("-")
        año = separador[0]
        año = int(año)
        mes = separador[1]
        mes = int(mes)
        dia = separador[2]
        dia = int(dia)
        
        self.fecha_lanzamiento = datetime(año, mes, dia)
        
    @staticmethod
    def normaliza_elemtos(lista_videos: list["Video"]):
        for tema in lista_videos:
            tema.dividir_titulo()
            tema.obtener_codigo_url()
            tema.formatear_fecha()

    @staticmethod

    def mostrar_lista_videos(lista_videos: list["Video"]):
        for tema in lista_videos:
            tema.mostrar_tema()
    
    @staticmethod

    def promedio_sesion(lista_videos: list["Video"]) -> float:
        acumulador_vistas = 0

        for tema in lista_videos:
            acumulador_vistas += tema.vistas
        
        promedio_vistas = (acumulador_vistas / len(lista_videos)) * 1000

        return promedio_vistas
    
    @staticmethod
        
    def buscar_por_codigo(lista_videos: list["Video"], codigo: str):

        for tema in lista_videos:
            if tema.codigo_url == codigo:
                tema.mostrar_tema()
                break
    
    @staticmethod
    
    def buscar_por_nombre(lista_videos: list["Video"], colaborador: str):

        for tema in lista_videos:
            if tema.colaborador == colaborador:
                tema.mostrar_tema()
                break
    
    @staticmethod
                
    def ordenar_menor_a_mayor(lista_videos: list["Video"]):
        
        for i in range(1, len(lista_videos)):
            key = lista_videos[i]
            j = i - 1

            while j >=0 and key.sesion < lista_videos[j].sesion:
                lista_videos[j + 1] = lista_videos[j]
                j -= 1
            
            lista_videos[j + 1] = key
            
        return lista_videos

    @staticmethod

    def mas_vistos(lista_videos: list["Video"]):
        
        for i in range(1, len(lista_videos)):
            key = lista_videos[i]
            j = i - 1

            while j >=0 and key.vistas > lista_videos[j].vistas:
                lista_videos[j + 1] = lista_videos[j]
                j -= 1
            
            lista_videos[j + 1] = key
            
        return lista_videos[:3]