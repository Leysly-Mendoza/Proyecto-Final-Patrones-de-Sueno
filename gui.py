import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
import asyncio
import threading

from models.modelo_sueno import AdvancedSleepAnalyzer
from utils.recomendador import generate_advanced_recommendation
from process.functional_tools import filter_low_quality, average_deep_sleep
from entrada_real.analisis_async import simulate_real_time_input

# Cargar dataset
df = pd.read_csv("data/sleep_dataset.csv")
usuarios = df['user_id'].unique()

# Función para análisis completo
def analizar_usuario():
    try:
        uid = int(combo_usuario.get())
        datos_usuario = df[df['user_id'] == uid].to_dict(orient="records")

        session = AdvancedSleepAnalyzer(uid, datos_usuario)

        horas_prom = session.average_sleep_hours()
        problemas = session.detect_problems()
        prom_deep = average_deep_sleep(datos_usuario)
        calidad_avg = sum(d['sleep_quality'] for d in datos_usuario) / len(datos_usuario)
        rem_avg = sum(d['rem_pct'] for d in datos_usuario) / len(datos_usuario)
        light_avg = sum(d['light_pct'] for d in datos_usuario) / len(datos_usuario)
        awake_avg = sum(d['awake_count'] for d in datos_usuario) / len(datos_usuario)
        total_hours_avg = sum(d['total_sleep_hours'] for d in datos_usuario) / len(datos_usuario)

        recomendacion = generate_advanced_recommendation(
            total_hours=total_hours_avg,
            deep_pct=prom_deep,
            rem_pct=rem_avg,
            light_pct=light_avg,
            awake_count=awake_avg,
            sleep_quality_avg=calidad_avg
        )

        resultado.set(f"\n📊 Promedio de horas: {horas_prom:.2f}\n\n"
                      f"🚩 Problemas detectados: {len(problemas)}\n\n"
                      f"📈 Promedio sueño profundo: {prom_deep:.2f}%\n\n"
                      f"🧠 Recomendación personalizada:\n\n{recomendacion}")

    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error: {e}")

# Función para ejecutar asyncio en hilo aparte
def simular_entrada():
    try:
        uid = int(combo_usuario.get())
        datos_usuario = df[df['user_id'] == uid].to_dict(orient="records")
        threading.Thread(target=lambda: asyncio.run(simulate_real_time_input(datos_usuario))).start()
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo iniciar la simulación: {e}")

# Crear ventana
root = tk.Tk()
root.title("🛌 Analizador de Sueño")
root.geometry("700x600")
root.configure(bg="#EAF2F8")  # Azul claro moderno

# Estilos modernos
style = ttk.Style()
style.theme_use("clam")
style.configure("TLabel", background="#EAF2F8", font=("Segoe UI", 11))
style.configure("TButton", font=("Segoe UI", 10, "bold"), foreground="#ffffff", background="#3498DB")
style.map("TButton", background=[("active", "#5DADE2")])
style.configure("TCombobox", font=("Segoe UI", 10))

# Título
title_label = ttk.Label(root, text="🛌 Analizador de Patrones de Sueño", font=("Segoe UI", 18, "bold"), foreground="#2E86C1")
title_label.pack(pady=20)

# Selector de usuario
frame_input = ttk.Frame(root)
frame_input.pack(pady=10)

label_usuario = ttk.Label(frame_input, text="Selecciona un ID de usuario:", foreground="#1B4F72")
label_usuario.pack(side="left", padx=10)
combo_usuario = ttk.Combobox(frame_input, values=list(usuarios), state="readonly", width=10)
combo_usuario.pack(side="left")

# Botones
frame_btns = ttk.Frame(root)
frame_btns.pack(pady=10)

btn_analizar = ttk.Button(frame_btns, text="🔍 Analizar Usuario", command=analizar_usuario)
btn_analizar.grid(row=0, column=0, padx=10)

btn_simular = ttk.Button(frame_btns, text="🔁 Simular Entrada", command=simular_entrada)
btn_simular.grid(row=0, column=1, padx=10)

# Tarjeta de resultados
card_frame = tk.Frame(root, bg="#D6EAF8", bd=2, relief="ridge")
card_frame.pack(pady=20, padx=20, fill="both", expand=True)

resultado = tk.StringVar()
label_resultado = ttk.Label(card_frame, textvariable=resultado, wraplength=650, justify="left", background="#D6EAF8")
label_resultado.pack(pady=20, padx=20)

# Ejecutar ventana
root.mainloop()
