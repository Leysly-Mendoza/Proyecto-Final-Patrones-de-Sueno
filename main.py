import pandas as pd
from models.modelo_sueno import SleepAnalyzer
from process.functional_tools import filter_low_quality, average_deep_sleep
from utils.recomendador import generate_recommendation
import asyncio
from entrada_real.analisis_async import simulate_real_time_input

# Leer el archivo CSV con pandas
df = pd.read_csv("data/sleep_dataset.csv")

# Mostrar usuarios disponibles
usuarios = df['user_id'].unique()
#print("Usuarios disponibles:", ", ".join(usuarios))
print("Usuarios disponibles:", ", ".join(str(u) for u in usuarios))

# Solicitar el user_id
try:
    user_input = int(input("Ingrese el ID del usuario que desea analizar: ").strip())
except ValueError:
    print("Entrada inválida. Debe ser un número.")
    exit()

# Verificar si el usuario existe
if user_input not in usuarios:
    print(f"Usuario '{user_input}' no encontrado.")
    exit()
else:
    # Filtrar los datos del usuario seleccionado
    user_data = df[df['user_id'] == user_input].to_dict(orient="records")

    session = SleepAnalyzer(user_input, user_data)
    print("\n--- ANÁLISIS DEL SUEÑO ---")
    print("Horas promedio de sueño:", session.average_sleep_hours())
    print("Problemas detectados:", session.detect_problems())

    baja_calidad = filter_low_quality(user_data)
    print("Noches de baja calidad:", baja_calidad)

    promedio_deep = average_deep_sleep(user_data)
    print("Promedio de sueño profundo:", promedio_deep)

    promedio_calidad = sum(d['sleep_quality'] for d in user_data) / len(user_data)
    print(generate_recommendation(promedio_calidad))

    # Ejecutar simulación en tiempo real
    # mprint("\n--- SIMULACIÓN EN TIEMPO REAL ---")
    # asyncio.run(simulate_real_time_input(user_data))
