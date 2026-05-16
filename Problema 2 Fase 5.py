# =================================================================
# JOHNATAN SMITH GUIZA MOLINA
# PROGRAMA: Gestión de Precios - Restaurante
# CURSO: Fundamentos de Programación - UNAD
# CODIGO: 213022
# INGENIERÍA DE SISTEMAS
# PROBLEMA 2: Aplicación de promociones en matriz de menú
# =================================================================

# MÓDULO: Función para calcular el precio final
def calcular_precio_final(precio_base, categoria_actual, categoria_objetivo, umbral):
    """
    Aplica un 15% de descuento si el producto coincide con la categoría
    [span_3](start_span)objetivo y supera el umbral de precio definido[span_3](end_span).
    """
    if categoria_actual == categoria_objetivo and precio_base > umbral:
        descuento = precio_base * 0.15
        return precio_base - descuento
    else:
        # [span_4](start_span)Mantiene el precio base si no se cumplen las condiciones[span_4](end_span)
        return precio_base

# PROGRAMA PRINCIPAL
def main():
     # 1. [span_5](start_span)Matriz con al menos 6 productos[span_5](end_span)
     # Estructura: [Nombre del Producto, Categoría, Precio Base]
     menu = [
         ["Pizza Hawaina", "Plato Fuerte", 25000],
         ["Jugo Natural", "Bebida", 7000],
         ["Hamburguesa", "Plato Fuerte", 18000],
         ["Copa Helado", "Postre", 12000],
         ["Lasagna Carne", "Plato Fuerte", 32000],
         ["Agua Botella", "Bebida", 4000]
     ]
 
     # [span_6](start_span)Definición de la lógica de negocio[span_6](end_span)
     categoria_promo = "Plato Fuerte"
     umbral_precio = 20000
 
     print("--- RESULTADOS DEL MENÚ (PROMOCIÓN 15%) ---")
     print(f"{'Producto':<20} | {'Categoría':<15} | {'Base':<10} | {'Final':<10}")
     print("-" * 65)
 
     # 2. [span_7](start_span)Procesamiento de la matriz y salida de datos[span_7](end_span)
     for producto in menu:
         nombre = producto[0]
         categoria = producto[1]
         precio_b = producto[2]
         
         # Llamado al módulo para calcular el precio final
         precio_f = calcular_precio_final(precio_b, categoria, categoria_promo, umbral_precio)
         
         # [span_8](start_span)Mostrar cada producto con su precio base y final[span_8](end_span)
         print(f"{nombre:<20} | {categoria:<15} | ${precio_b:<9} | ${precio_f:<9.0f}")
 
 # Punto de entrada del programa
if __name__ == "__main__":
     main()
