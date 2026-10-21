from collections import deque
import msvcrt

def main():
    servicios = {
        1: "Contratación de servicio",
        2: "Modificación de datos",
        3: "Indemnización",
        4: "Cancelación del servicio"
    }

    #colas del servicio
    colas_servicios = {num: deque() for num in servicios}

    siguiente_ticket = {num: 1 for num in servicios}

    #menu principal
    while True:
        print("\n==================================================")
        print("   SISTEMA DE ATENCION AL CLIENTE ")
        print("==================================================")
        print("Seleccione un servicio:")
        for num, nombre in servicios.items():
            print(f"  {num}. {nombre}")
        print("  0. Salir del programa")


        opcion = input("\nIngrese el número del servicio: ").strip()

        if opcion == "0":
            print("\nCerrando el sistema. ¡Hasta luego!")
            break

        if not opcion.isdigit() or int(opcion) not in servicios:
            print("  Error: Opción no válida. Seleccione un número de la lista.")
            continue

        num_serv = int(opcion)
        nombre_serv = servicios[num_serv]

        # Menu del servicio
        while True:
            print(f"\n--- SERVICIO: {nombre_serv.upper()} (Servicio {num_serv}) ---")
            print(f"  C{num_serv} : Llegada de nuevo cliente, asignar ticket ")
            print(f"  A{num_serv} : Atender siguiente cliente")
            print(f"  V{num_serv} : Ver cola de espera")
            print("  Esc: Regresar al menú principal(oprima la tecla escape)")
            print("--------------------------------------------------")
            print("\n\nIngrese la accion: ", end="", flush=True)

            print( end="", flush=True)

            #Esc para volver al menu
            buffer = ""
            while True:
                tecla = msvcrt.getch()
                if tecla == b'\x1b':
                    print("\n[Regresando al menú principal...]")
                    break
                elif tecla in (b'\r', b'\n'):
                    print()
                    break
                elif tecla == b'\x08':
                    if len(buffer) > 0:
                        buffer = buffer[:-1]
                        print('\b \b', end='', flush=True)
                else:
                    char = tecla.decode('utf-8', errors='ignore')
                    buffer += char
                    print(char, end='', flush=True)
            if tecla == b'\x1b':
                break

            #llegada de cliente
            comando = buffer.strip().upper()
            if comando == f"C{num_serv}":
                turno = siguiente_ticket[num_serv]
                colas_servicios[num_serv].append(turno)
                print(f"\n[NUEVO CLIENTE] Servicio: {nombre_serv}")
                print(f"                Ticket asignado: {turno}")
                siguiente_ticket[num_serv] += 1

            # salida de cliente
            elif comando == f"A{num_serv}":
                cola = colas_servicios[num_serv]
                if not cola:
                    print(f"\n[!] No hay clientes en espera para {nombre_serv}.")
                else:
                    cliente_atendido = cola.popleft() 
                    print(f"\n[LLAMANDO] Servicio: {nombre_serv}")
                    print(f"                      cliente número: {cliente_atendido}")

            #Ver cola de espera
            elif comando == f"V{num_serv}":
                cola = colas_servicios[num_serv]
                if not cola:
                    print(f"\n[!] No hay clientes en espera para {nombre_serv}.")
                else:
                    print(f"\n[ESTADO] Clientes en espera para {nombre_serv}:")
                    print(f"                    {list(cola)}")

            else:
                print(f"--> Error: Comando no válido. Debe ingresar C{num_serv} o A{num_serv}.")

if __name__ == "__main__":
    main()