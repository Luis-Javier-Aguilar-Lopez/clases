print"Ejercicios"
print"\nRestaurante: \na)Crear una clase llamada Restaurant. El método __init__() debe de aceptar dos atributos: El nombre_restaurant y el tipo_cocina. \nb) Crear un método que se llame describe_restaurant que imprima: El nombre del restaurant es: ------ y El tipo de comida que se sirve es: -------. \nc) Generar"
print"\nTres Restaurantes: Crear tres restaurantes utilizando la clase que se ha definido con anterioridad y llame al método describe_restaurant para cada instancia de la clase."
print("\nRestaurante")
class Restaurant():
  def __init__(self,nombre_restaurant,tipo_cocina):
    self.nombre_restaurant = nombre_restaurant
    self.tipo_cocina = tipo_cocina
  
  def describe_restaurant(self):
    print("El nombre del restaurant es:"+self.nombre_restaurant+" y El tipo de comida que se sirve es: "+self.tipo_cocina)
  def Clientes_Atendidos(self,CA):
    self.CA = CA
    print ("Clientes atendidos:",CA)
  def Aumento_Clientes(self,AC):
    print("Aumento :",AC)
    print("Total de clientes :",self.CA+AC)
mi_restaurante = Restaurant("El tio","chola")
mi_restaurante.describe_restaurant()
mi_restaurante = Restaurant("don tono","Mexicana")
mi_restaurante.describe_restaurant()
mi_restaurante = Restaurant("shotescolares","Americana")
mi_restaurante.describe_restaurant()

print"\nUsuarios: \na) Cree una clase que se llame Usuario. \nb)Cree dos atributos llamados Nombre y Apellido, agregue atributos como CURP,Fecha_Nacimiento, Sexo, Grado_estudios. \nc)Genere un método llamado Saluda_usuario y que despliegue en pantalla algo como Hola Juan Ruiz de Alarcón. \nd)Genere un método que se llame Describe_usuario y que muestre toda la información del usuario. \ne)Genere 5 objetos tipo usuario y ejecute los dos métodos anteriormente descritos."
class usuario():  
  def __init__(self,nombre,apellido,curp,f_nacimiento,sexo,grado_estudios):
    self.nombre = nombre
    self.apellido = apellido
    self.curp = curp
    self.f_nacimiento = f_nacimiento
    self.sexo = sexo
    self.grado_estudios = grado_estudios
  def saluda_usuario(self):
    print"Hola "+self.nombre,self.apellido+"."
  def describe_usuario(self):
    print"Curp :" ,self.curp
    print"Fecha de nacimiento :",self.f_nacimiento
    print"Sexo :",self.sexo
    print"Grado de estudios: ",self.grado_estudios
Sixto = usuario("Maya", "trejo", "LMN87223", "1950","masculino","maestria")
Sixto.saluda_usuario()
Sixto.describe_usuario()    


print "\nClientes atendidos: Retomar la clase de Restaurante que se generó a lo largo de este notebook y agregar un atributo que clientes_atendidos y agregar dos métodos:"
print"\nClientes_Atendidos(self,numero): que pueda modificar el número de clientes \n2.Aumenta_Clientes(self,numero): que pueda aumentar el número de clientes que se han atendido"
mi_restaurante = Restaurant("don tono","Mexicana")
mi_restaurante.describe_restaurant()
mi_restaurante.Clientes_Atendidos(24)
mi_restaurante.Aumento_Clientes(16)

print"\nControl de acceso Acompletar el código de la siguiente celda, que crea una clase Usuario, donde el constructor debe de aceptar el nombre de usuario y la contraseña, cuando se invoque el método ingresar debe de pedir la contraseña del usuario, si la contraseña es correcta, debe de imprimir Bienvenido a su cuenta, si la contraseña se ingresa incorrectamente 3 veces debe de imprimir Cuenta bloquead, intente más tarde y debe de reiniciar la varialbe self.intentosAcceso a cero."
class User():
    def __init__(self,Nickname,password):
        self.Nickname= Nickname
        self.password = password
        self.intentosAcceso = 0        
    def ingresar(self):
        while True :
            cont=raw_input("Ingresa la contrasena: ")
            if cont=="pasemeprof" :
                print"Bienvenido "+self.Nickname
                break
            else:
                print("Contraseña incorrecta")
                self.intentosAcceso = self.intentosAcceso + 1
                if self.intentosAcceso == 3:
                    print("Cuenta bloqueada, intente más tarde")
                    break
nnemalo = User('nene malo','pasemeprof')
nnemalo.ingresar()

class Heladeria(Restaurant):
    def _init_(self,nombre_restaurant,tipo_cocina):
        super()._init_(nombre_restaurant,tipo_cocina)
    sabores=['chocolate','fresa','nuez','limon','sandia','pistache']
    def mostrar_sabores(self):
        sabores=['chocolate','fresa','nuez','limon','sandia','pistache']
        print("tengo helados de "+sabores[0]+ "\n"+ sabores[1]+ "\n"+ sabores[2]+ "\n"+ sabores[3]+ "\n"+ sabores[4]+ "\n"+ sabores[5])
restaurante= Restaurant("chili wily","helados")
restaurante.describe_restaurant()
ninopromedio= Heladeria("chili wily","helados")
ninopromedio.mostrar_sabores()












