def generate_recommendation(sleep_quality_avg):
    if sleep_quality_avg >= 90:
        return "¡Tu sueño es excelente! No necesitas cambios."
    elif 75 <= sleep_quality_avg < 90:
        return "Buen sueño, pero podrías mejorar la consistencia en los horarios."
    elif 60 <= sleep_quality_avg < 75:
        return "Bien, pero puedes mejorar tu higiene del sueño."
    elif 45 <= sleep_quality_avg < 60:
        return "Tu calidad de sueño es baja. Considera evitar pantallas antes de dormir."
    elif 30 <= sleep_quality_avg < 45:
        return "Muy baja calidad de sueño. Intenta crear una rutina de sueño estable."
    else:
        return "Preocupante. Podrías necesitar hablar con un especialista del sueño."

def generate_advanced_recommendation(total_hours, deep_pct, rem_pct, light_pct, awake_count, sleep_quality_avg):
    recommendations = []

    if total_hours < 6:
        recommendations.append("Necesitas dormir más horas.")
    elif total_hours > 9:
        recommendations.append("Estás durmiendo más de lo necesario.")

    if deep_pct < 15:
        recommendations.append("Tu sueño profundo es muy bajo. Considera reducir el estrés antes de dormir.")
    if rem_pct < 20:
        recommendations.append("Tu fase REM es baja. Intenta mantener un horario de sueño más regular.")
    if light_pct > 60:
        recommendations.append("Tienes demasiado sueño ligero. Intenta evitar pantallas antes de dormir.")
    if awake_count > 2:
        recommendations.append("Te despiertas frecuentemente. Revisa factores como ruido o temperatura del ambiente.")

    quality_msg = generate_recommendation(sleep_quality_avg)

    if not recommendations:
        return "¡Buen trabajo! Tus hábitos de sueño parecen saludables."
    return quality_msg + "\nAdemás:\n- " + "\n- ".join(recommendations)
