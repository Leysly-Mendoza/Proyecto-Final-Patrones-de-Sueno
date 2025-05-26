# utils/recomendador.py
def generate_recommendation(quality):
    if quality >= 80:
        return "¡Excelente! Sigue con esa rutina."
    elif quality >= 60:
        return "Bien, pero puedes mejorar tu higiene del sueño."
    else:
        return "Considera mejorar tu ambiente de descanso y evitar pantallas antes de dormir."
