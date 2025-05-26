# entrada_real/analisis_async.py
import asyncio

async def simulate_real_time_input(data):
    for record in data:
        await asyncio.sleep(1)
        print(f"Usuario: {record['user_id']} - Fecha: {record['date']} - Calidad de sueño: {record['sleep_quality']}")
