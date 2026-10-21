import os

#clase cola, para la creacion de la cola A y B
class Cola:

  def __init__(self):
    self.elementos = []

  def vacia(self):
    return len(self.elementos) == 0

  def encolar(self, item):
    self.elementos.append(item)

  def desencolar(self):
    if not self.vacia():
      return self.elementos.pop(0)
    return None

  def duplicar(self):
    nueva_cola = Cola()
    for item in self.elementos:
      nueva_cola.encolar(item)
    return nueva_cola

#suma de las 2 colas
def sumar_colas(cola_a: Cola, cola_b: Cola) -> Cola:
  cola_resultado = Cola()
  aux_a = cola_a.duplicar()
  aux_b = cola_b.duplicar()

  while not aux_a.vacia() and not aux_b.vacia():
    suma = aux_a.desencolar() + aux_b.desencolar()
    cola_resultado.encolar(suma)

  return cola_resultado

#limpieza de la consola, para no tener tanta porqueria en pantalla
def limpiar_consola():
  os.system("cls" if os.name == "nt" else "clear")


#graficacion de las colas A y B como tablas
def tabla_colas(cola_a: Cola, cola_b: Cola):
  res = sumar_colas(cola_a, cola_b)

  copia_a = cola_a.duplicar()
  copia_b = cola_b.duplicar()

  print("\n" + "=" * 42)
  print(f"{'Cola A':^12} | {'Cola B':^12} | {'Resultado':^12}")
  print("=" * 42)

  while not copia_a.vacia() and not copia_b.vacia():
    val_a = copia_a.desencolar()
    val_b = copia_b.desencolar()
    val_res = res.desencolar()
    print(f"{val_a:^12} | {val_b:^12} | {val_res:^12}")

  print("=" * 42 + "\n")


#menu dal programa
def menu():
  cola_a = Cola()
  cola_b = Cola()

  while True:
    limpiar_consola()
    print("--- MENÚ ---")
    print("1. Ingresar par de datos (Cola A y Cola B)")
    print("2. Salir")

    opcion = input("Seleccione una opción: ").strip()

    if opcion == "1":
      try:
        print("\n--- Inserción de Datos ---")
        num_a = int(input("Ingrese un número entero para la Cola A: "))
        num_b = int(input("Ingrese un número entero para la Cola B: "))


        cola_a.encolar(num_a)
        cola_b.encolar(num_b)


        limpiar_consola()
        print("¡Datos agregados con éxito!")
        tabla_colas(cola_a, cola_b)

        input("Presione ENTER para regresar al menú principal...")

      except ValueError:
        print("\n[Error]: Debe ingresar números enteros válidos.")

    elif opcion == "2":
      print("\nSaliendo del programa...")
      break
    else:
      print("\n[Error]: Opción no válida.")



if __name__ == "__main__":
  menu()