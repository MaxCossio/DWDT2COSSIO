class alumno:
    def __init__(self,nombre,apellido,edad,nota,nacionalidad):
        self.nombreAlumno=nombre
        self.apellidoAlumno=apellido
        self.edadAlumno=edad
        self.notaAlumno=nota
        self.nacionalidadAlumno=nacionalidad
        

    def ingresarNota(self, notaAlumno):
        self.notaAlumno=notaAlumno

if __name__=='__main__':
    alumnosSistema = []
    comandosSistema = ['R','C','P','S','X','M']
    while True:
        comandoInformacion = input("Bienvenido al registro de Notas, ingrese comando : ")
        print(f"El comando ingresado es {comandoInformacion}")
        if comandoInformacion in comandosSistema:
            if comandoInformacion == 'R':
                print("Se registrara un nuevo alumno : ")
                nombreAlumno = input("Ingrese el nombre del alumno : ")
                apellidoAlumno = input("Ingrese el apellido del alumno : ")
                edadAlumno = input("Ingrese edad del alumno : ")
                while 1:
                    notaAlumno = int(input("Ingrese nota del alumno : "))
                    if notaAlumno < 0 or notaAlumno > 20:
                        print("ingrese nota entre 0 y 20")
                    else:
                        break            
                nacionalidadAlumno = input("Ingrese nacionalidad del alumno : ")
                objAlumno = alumno(nombreAlumno,apellidoAlumno,edadAlumno,notaAlumno,nacionalidadAlumno)
                alumnosSistema.append(objAlumno)
            elif comandoInformacion == 'C':
                print("Se calificaran a los alumnos")
                for alumnoInfo in alumnosSistema:
                    if alumnoInfo.notaAlumno == '':
                        notaAlumno = input(f"Ingrese la nota del alumno {alumnoInfo.nombreAlumno} : ")
                        alumnoInfo.ingresarNota(notaAlumno)
            elif comandoInformacion == 'M':
                print("Se mostrara la informacion de los alumnos")
                i = 0
                for alumnoInfo in alumnosSistema:
                    print(f"Mostrando informacion del alumno {i}")
                    print(f"Nombre del alumno : {alumnoInfo.nombreAlumno}")
                    print(f"Apellido del alumno : {alumnoInfo.apellidoAlumno}")
                    print(f"Edad del alumno : {alumnoInfo.edadAlumno}")
                    print(f"Nota del alumno : {alumnoInfo.notaAlumno}")
                    print(f"Nacionalidad del alumno : {alumnoInfo.nacionalidadAlumno}")
                    i = i + 1
                    print("\n")
            elif comandoInformacion == 'P':
                i = 0
                suma =0
                for alumnoInfo in alumnosSistema:
                    suma = alumnoInfo.notaAlumno + suma
                    i = i + 1
                promedio = suma / i
                print("Promedio de Notas para ",i," Alumnos es: ", promedio)
            elif comandoInformacion == 'S':
                i = 0
                suma =0
                for alumnoInfo in alumnosSistema:
                    suma = alumnoInfo.notaAlumno + suma
                    i = i + 1
                print("La suma de notas de ",i," Alumnos es : ", suma)
            else:
                print("Comando de finalizacion")
                break
        else:
            print('Comando incorrecto, vuelva a ingresarlo')