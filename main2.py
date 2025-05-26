import pandas as pd
from models.modelo_sueno import SleepAnalyzer
from process.functional_tools import filter_low_quality, average_deep_sleep
from utils.recomendador import generate_advanced_recommendation  # Asegúrate de tener esta función
import asyncio
from entrada_real.analisis_async import simulate_real_time_input

# Leer el archivo CSV
df = pd.read_csv("data/sleep_dataset.csv")

# Mostrar usuarios disponibles
usuarios = df['user_id'].unique()
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
   
    # Calcular promedios para recomendaciones avanzadas
    total_hours_avg = sum(d['total_sleep_hours'] for d in user_data) / len(user_data)
    deep_pct_avg = sum(d['deep_pct'] for d in user_data) / len(user_data)
    rem_pct_avg = sum(d['rem_pct'] for d in user_data) / len(user_data)
    light_pct_avg = sum(d['light_pct'] for d in user_data) / len(user_data)
    awake_avg = sum(d['awake_count'] for d in user_data) / len(user_data)
    sleep_quality_avg = sum(d['sleep_quality'] for d in user_data) / len(user_data)

    print("\n--- RECOMENDACIÓN PERSONALIZADA ---")
    print(generate_advanced_recommendation(
        total_hours=total_hours_avg,
        deep_pct=deep_pct_avg,
        rem_pct=rem_pct_avg,
        light_pct=light_pct_avg,
        awake_count=awake_avg,
        sleep_quality_avg=sleep_quality_avg
    ))

    # Simulación (opcional)
    # print("\n--- SIMULACIÓN EN TIEMPO REAL ---")
    # asyncio.run(simulate_real_time_input(user_data))
