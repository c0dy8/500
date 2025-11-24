follow = True
register = []
subject = []
assigned_subjects = []
grades_per_subject=[]

while follow:
    print("\n 1. Ingresar datos de estudiante\n 2. Agregar materias\n 3. Asignar(MATERIA-ESTUDIANTE)\n 4. Notas y calificaciones\n 5. Reportes y Estadisticas\n 6. SALIR")
    quest_1 = int(input("\ningrese la opcion que desea realizar: "))

    if quest_1 == 1:
        while follow:
            print("\n===ASIGNACION ESTUDIANTE===")
            print("1. Registrar estudiante\n2. Listar estudiantes\n3. Consultar estudiante por ID\n4. Eliminar estudiante\n5. Volver al menú principal")
            try:
                quest_menu_1 = int(input("\ningrese la opcion que desea realizar: "))
                if quest_menu_1 > 5 or quest_menu_1 <= 0:
                    print("======================================")
                    print("DATO INVALIDO, INGRESE NUMEROS DEL 1-5")
                    print("======================================")

                elif quest_menu_1 == 1:
                    print("------------------")
                    student_repeat = int(input("\ncuantos estudiantes se van a registrar: "))
                    for student in range(student_repeat):
                        c = student + 1
                        print(f"--DATOS ESTUDIANTE {c}--")

                        while follow:
                            try:
                                stud_name = input("Nombre del estudiante: ")
                                stud_age = int(input("Edad del estudiante: "))
                                stud_doc = input("Documento del estudiante: ")
                                doc_exists = False
                                for s in register:
                                    if s['id'] == stud_doc:
                                        print("===============================================")
                                        print("ERROR: El documento ya existe. Intente de nuevo.")
                                        print("===============================================")
                                        doc_exists = True
                                        break
                                if doc_exists:
                                    continue
                                break
                            
                            except ValueError:
                                print("======================================")
                                print("EDAD INVÁLIDA: Ingrese solo números.")
                                print("Por favor, ingrese TODOS los datos de este estudiante de nuevo.")
                                print("======================================")
                                continue
                            
                        registering_students = {
                            'name': stud_name,
                            'age': stud_age,
                            'id': stud_doc
                        }
                        register.append(registering_students)
                elif quest_menu_1 == 2:
                    if not register:
                        print("\n=====================================")
                        print("No hay estudiantes registrados todavía.")
                        print("=====================================")
                    else:
                        for y in register:
                            print(f"\n|Su Estudiante Es: {y['name']} | Su Edad Es: {y['age']} | Su Documento Es: {y['id']}")
                            print("----------------------------------------------------------------------------------")
                elif quest_menu_1 == 3:
                    search_by_id = input("ingresa el numero de documento(ID) del estudiante que deseas buscar: ")
                    found_student = False
                    for s in register:
                        if s['id'] == search_by_id:
                            print("==ESTUDIANTE ENCONTRADO==")
                            print(f" El estudiante {search_by_id} es\n NOMBRE: {s['name']}\n EDAD: {s['age']}\n DOCUMENTO: {s['id']}")
                            found_student = True
                            break
                        
                    if not found_student:
                        print("========================")
                        print("ESTUDIANTE NO ENCONTRADO")
                        print("========================")
                elif quest_menu_1 == 4:
                    while follow:
                        delete_student = input("ingrese el nombre del estudiante que desea eliminar: ")
                        found_student = False
                        for d in (register):
                            if d['name'] == delete_student:
                                register.remove(d)
                                print(f"su estudiante {d['name']} ha sido eliminado")
                                print(f"\nsus estudiantes acutales son: {register}")
                                found_student = True
                                break
                            
                        if found_student:
                            break
                        else:
                            print("======================================")
                            print("NOMBRE NO ENCONTRADO, INTENTE DE NUEVO")
                            print("======================================")
                            q_exit = input("¿Desea volver al menú de estudiantes? (s/n): ")
                            if q_exit.lower() == 's':
                                break
                elif quest_menu_1 == 5:
                    break
            except ValueError:
                print("========================")
                print("SOLO NUMEROS POR FAVOR")
                print("========================")

    elif quest_1 == 2:
        while follow:
            try:
                quest_menu_2 = int(input("\n1. Registrar nueva materia\n2. Listar materias\n3. Consultar materia\n4. Eliminar materia\n5. Volver al menú principal\n\ningrese la opcion que desea realizar: "))
                if quest_menu_2 == 1:
                    while follow:
                        try:
                            print("===================================================")
                            subject_name = input("\ningrese el NOMBRE de la materia: ")
                            print("===================================================")
                            subject_code = input("ingrese el CODIGO de la materia: ")
                            code_exists = False
                            for m in subject:
                                if m['subject_code'] == subject_code:
                                    print("=============================================")
                                    print("ERROR: El código ya existe. Intente de nuevo.")
                                    print("=============================================")
                                    code_exists = True
                                    break
                            if code_exists:
                                continue
                            registering_subjects = {
                                'subject_name': subject_name,
                                'subject_code': subject_code
                            }
                            subject.append(registering_subjects)
                            break
                        except ValueError:
                            print("ingrese un dato valido")
                            
                elif quest_menu_2 == 2:
                    if not subject:
                        print("\n==================================")
                        print("No hay materias registradas todavía.")
                        print("==================================")
                    else:
                        for m in subject:
                            print(f"\n========== ")
                            print(f"materia: {m['subject_name']} | codigo: {m['subject_code']}")
                elif quest_menu_2 == 3:
                    print("===========================")
                    while follow:
                        subject_response = input("\ningrese el codigo de la materia: ")
                        found_subject = False
                        for i in subject:
                            if i['subject_code'] == subject_response:
                                print("===MATERIA ENCONTRADA===")
                                print(f"|la materia es {i['subject_name']}|")
                                found_subject = True
                                break

                        if found_subject:
                            break
                        else:
                            print("======================================")
                            print("MATERIA NO ENCONTRADA, ITENTE DE NUEVO")
                            print("======================================")
                            q_exit = input("¿Desea volver al menú de materias? (s/n): ")
                            if q_exit.lower() == 's':
                                break

                elif quest_menu_2 == 4:
                    while follow:
                        delete_subject = input("ingrese la materia (por NOMBRE) que desea eliminar: ")
                        found_subject = False
                        for p in (subject):
                            if p['subject_name'] == delete_subject:
                                subject.remove(p)
                                print(f"materia {p['subject_name']} ha sido eliminado")
                                print(f"\nsus materias acutales son: {subject}")
                                found_subject = True
                                break

                        if found_subject:
                            break
                        else:
                            print("======================================")
                            print("NOMBRE NO ENCONTRADO, INTENTE DE NUEVO")
                            print("======================================")
                            q_exit = input("¿Desea volver al menú de materias? (s/n): ")
                            if q_exit.lower() == 's':
                                break

                elif quest_menu_2 == 5:
                    break
            except ValueError:
                print("==========================")
                print("INGRESE UNA OPCION DEL 1-5")
                print("==========================")
    elif quest_1 == 3:
        while follow:
            
                quest_menu_3=int(input("\n1. Asignar materia a estudiante\n2. Ver materias de un estudiante\n3. Ver estudiantes por materia\n4. Quitar materia a un estudiante\n5. Volver al menú principal\n\ningrese la ocpion que desea realizar: "))
                if quest_menu_3 <=0 or quest_menu_3 >5:
                    print("====================")
                    print("DATO INVALIDO, INTENTE DE NUEVO")
                
                elif quest_menu_3 == 1:
                    print("============================")
                    validation_student=input("\ningrese el documento del estudiante: ")
                    student_f=False
                    for v in register:
                        if v['id'] == validation_student:
                            student_f=True
                            print("documento ENCONTRADO")
                        
                    print("=========================")
                    validation_subject=input("ingrese el codigo de materia: ")
                    subject_f=False
                    for b in subject:
                        if b['subject_code'] == validation_subject:
                            subject_f=True
                            print("codigo de materia ENCONTRADO")
                    if subject_f == True and student_f == True:
                        validation_dictionary={
                            'validation_student':validation_student,
                            'validation_subject':validation_subject
                        }
                        assigned_subjects.append(validation_dictionary)
                        print(f"\nMateria {validation_subject} asignada al estudiante {validation_student}.")
                    else:
                        print("\n========================================================")
                        print("ERROR: No asignado. Verifique el documento y el código.")
                        if not student_f:
                            print(f" (El estudiante con ID {validation_student} no se encontro)")
                        if not subject_f:
                            print(f" (Materia con código {validation_subject} no se encontro)")
                        print("========================================================")
                        
                elif quest_menu_3 == 2:
                    search_doc = input("\nIngrese el documento del estudiante que desea consultar: ")
                    found_student=False
                    for z in assigned_subjects:
                        if z['validation_student'] == search_doc:
                            print(f"las materias del estudiante {search_doc} son {z['validation_subject']}")
                            found_student=True
                    if found_student==False:
                        print("ERROR: documento no encontrado")
                        
                elif quest_menu_3 == 3:
                    search_subject=input("\nIngrese el codigo de materia que desea consultar: ")
                    found_subject=False
                    for o in assigned_subjects:
                        if o['validation_subject'] == search_subject:
                            print(f"La materia {search_subject} encontrada. Los estudiantes con esta materia son: {o['validation_student']}")
                            found_subject=True        
                    if found_subject == False:
                        print("ERROR: codigo de materia no encontrado")
                        
                elif quest_menu_3 == 4:
                    while follow:
                        search_doc_2=input(" ingrese el documento del estudiante:")
                        search_code_2=input("ingrese el codigo de materia que desea eliminar: ")
                        found=False
                        for h in assigned_subjects:
                            if h['validation_student'] == search_doc_2 and h['validation_subject'] == search_code_2:
                                found=True
                                assigned_subjects.remove(h)
                                print("PERFECTO, materia eliminada")
                            break
                        if found == False:
                            print('\n=============================================')
                            print('ERROR: Asignación no encontrada. Verifique los datos.')
                            print('=============================================')
                elif quest_menu_3 == 5:
                    print("Volviendo al menu principal......")
                    break
    elif quest_1 == 4:
        quest_menu_4 = int(input("\n1. Registrar nota para un estudiante\n2. Ver notas por materia\n3. Ver promedio de un estudiante\n4. Eliminar una nota\n5. Volver al menú principal\n ingrese la opcion que desea realizar: "))


        if quest_menu_4 <=0 or quest_menu_3 >5:
            print("====================")
            print("DATO INVALIDO, INTENTE DE NUEVO")
        elif quest_menu_4 == 1:
            print("==REQUISITOS NOTA==")
            validation_student_1=input("ingrese le documento del estudiante: ")
            student_f=False
            for x in assigned_subjects:
                if x['validation_student'] == validation_student_1:
                    print("DOCUMENTO ENCONTRADO")
                    student_f=True
                    print(f"El estudiante {validation_student_1} tiene las materias {x['validation_subject']}")
                    validation_subject_1=input("\ningrese el codigo de materia a la que se va agreagr la nota: ")
                    subject_f=False
                    if x['validation_subject'] == validation_subject_1:
                        subject_f=True
                        print("CODIGO DE MATERIA ENCONTRADO")
                        grade=float(input(f"ingrese la nota para la materia {validation_subject_1}: "))
                if validation_student_1 == True and validation_subject_1 == True:
                    grade_dictionary={
                        'validation_student':validation_student_1,
                        'validation_subject':validation_subject_1,
                        'grade':grade
                    }
                    grades_per_subject.append(grade_dictionary)

            print(f" tus notas son {grades_per_subject}")

"""
Navegación de directorios
cd <directorio>: Cambia el directorio actual por el especificado.
cd ..: Sube un nivel en la estructura de directorios.
cd /: Te lleva al directorio raíz del sistema.
cd-: Regresa al directorio anterior.
pwd: Muestra la ruta del directorio de trabajo actual. 


Gestión de archivos y directorios

ls: Lista los archivos y directorios en la ubicación actual.
mkdir <nombre_directorio>: Crea un nuevo directorio.
touch <nombre_archivo>: Crea un nuevo archivo vacío.
cp <origen> <destino>: Copia un archivo o directorio.
mv <origen> <destino>: Mueve o renombra un archivo o directorio.
rm <nombre_archivo>: Elimina un archivo.
rm -rf <nombre_directorio>: Elimina un directorio y su contenido de forma recursiva (con precaución).
find: Busca archivos y directorios.
cat <nombre_archivo>: Muestra el contenido completo de un archivo. 

"""