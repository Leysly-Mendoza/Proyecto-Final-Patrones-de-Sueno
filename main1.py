from models.modelo_sueno import SleepAnalyzer
from process.functional_tools import filter_low_quality, average_deep_sleep
from utils.recomendador import generate_recommendation
import asyncio
from entrada_real.analisis_async import simulate_real_time_input
from models.modelo_sueno import AdvancedSleepAnalyzer 

# Simulación de dataset cargado
data = [
    {'user_id': 'u01', 'date': '2025-05-01', 'total_sleep_hours': 6.5, 'deep_pct': 15, 'rem_pct': 25, 'light_pct': 50, 'awake_count': 4, 'sleep_quality': 45},
    {'user_id': 'u01', 'date': '2025-05-02', 'total_sleep_hours': 7.2, 'deep_pct': 20, 'rem_pct': 22, 'light_pct': 48, 'awake_count': 2, 'sleep_quality': 65},
]

session = AdvancedSleepAnalyzer("u01", data)
print("Horas promedio de sueño:", session.average_sleep_hours())
print("Problemas detectados:", session.detect_problems())

baja_calidad = filter_low_quality(data)
print("Noches de baja calidad:", baja_calidad)

promedio_deep = average_deep_sleep(data)
print("Promedio de sueño profundo:", promedio_deep)

print(generate_recommendation(sum(d['sleep_quality'] for d in data) / len(data)))

# Ejecutar simulación en tiempo real
asyncio.run(simulate_real_time_input(data))
