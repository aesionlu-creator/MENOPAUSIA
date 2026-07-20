import streamlit as st

# ---------------------------------------------------------
# 1. CONFIGURACIÓN DE PÁGINA Y TÍTULO
# ---------------------------------------------------------
st.set_page_config(
    page_title="Evaluación Salud Femenina | TDSH y Menopausia",
    page_icon="🩺",
    layout="centered"
)

# ---------------------------------------------------------
# 2. BARRA LATERAL - NAVEGACIÓN Y MONETIZACIÓN / APOYO
# ---------------------------------------------------------
st.sidebar.title("Navegación Médica")
opcion = st.sidebar.radio(
    "Seleccione el módulo:",
    [
        "📌 Inicio y Aspectos Legales", 
        "🩺 Módulo TDSH (DSDS)", 
        "🌸 Módulo Menopausia (MRS)",
        "📚 Evidencia y Referencias"
    ]
)

st.sidebar.markdown("---")
st.sidebar.subheader("💡 Apoya esta Plataforma")
st.sidebar.caption(
    "Si esta herramienta facilita tu práctica clínica diaria, puedes apoyar su mantenimiento e investigación continua."
)
# Puedes reemplazar el enlace por tu enlace de PayPal, BuyMeACoffee o número Yape/Plin
st.sidebar.markdown("[☕ Invitar un café / Donar al proyecto](https://www.buymeacoffee.com)")

# ---------------------------------------------------------
# MÓDULO 0: INICIO Y DISCLAIMER OBLIGATORIO
# ---------------------------------------------------------
if opcion == "📌 Inicio y Aspectos Legales":
    st.title("🩺 Plataforma de Apoyo a la Decisión Clínica")
    st.subheader("Evaluación Integral de TDSH y Síndromes Climatéricos")
    
    st.markdown("---")
    
    st.warning("⚠️ **AVISO LEGAL Y DESCARGO DE RESPONSABILIDAD (DISCLAIMER):**\n\n"
               "• **Uso exclusivo para profesionales de la salud:** Esta herramienta digital interactiva está "
               "diseñada únicamente como guía y soporte de consulta rápida.\n"
               "• **Juicio clínico:** Las recomendaciones, puntajes y algoritmos mostrados no constituyen "
               "un diagnóstico definitivo ni sustituyen el criterio médico individualizado.\n"
               "• **Privacidad y Protección de Datos:** Esta aplicación **no recopila, almacena ni transmite** "
               "ningún dato de identificación personal de pacientes.")
    
    st.info("💡 **Instrucciones:** Utilice el menú desplegable a la izquierda para cambiar entre las escalas validadas.")

# ---------------------------------------------------------
# MÓDULO 1: ALGORITMO TDSH (DSDS)
# ---------------------------------------------------------
elif opcion == "🩺 Módulo TDSH (DSDS)":
    st.title("🩺 Módulo de Evaluación: TDSH")
    st.caption("Cuestionario de Pesquisa de Deseo Sexual Disminuido (**DSDS**, Rosen et al., **2008**).")
    
    st.markdown("---")
    st.subheader("Algoritmo de Pesquisa Rápida (DSDS)")
    
    q1 = st.checkbox("1. ¿Ha habido una disminución en su nivel de deseo o interés sexual?")
    q2 = st.checkbox("2. ¿Esta disminución le produce molestia, frustración o angustia (distress)?")
    q3 = st.checkbox("3. ¿Le gustaría que su nivel de deseo fuera mayor?")
    
    if q1 and q2 and q3:
        st.subheader("Descarte de Causas Secundarias:")
        c_med = st.checkbox("¿Se debe a una condición médica preexistente u otra disfunción sexual principal?")
        c_far = st.checkbox("¿Se debe al uso de algún medicamento/fármaco?")
        c_rel = st.checkbox("¿Se debe principalmente a problemas de pareja o estrés ambiental severo?")
        
        st.markdown("---")
        if not (c_med or c_far or c_rel):
            st.error("🚨 **Resultado Compatible con Criterios de TDSH Generalizado / Primario.**")
            st.write("Se sugiere evaluar opciones de abordaje multidisciplinario y/o tratamiento farmacológico según guías vigentes.")
        else:
            st.warning("⚠️ **Resultado Compatible con TDSH Secundario / Multifactorial.**")
            st.write("Se recomienda abordar primero los factores secundarios (ajuste farmacológico, terapia de pareja o manejo de comorbilidad).")
    else:
        st.success("✅ **Criterios de TDSH no completados.**")

# ---------------------------------------------------------
# MÓDULO 2: MENOPAUSIA Y ESCALA MRS
# ---------------------------------------------------------
elif opcion == "🌸 Módulo Menopausia (MRS)":
    st.title("🌸 Módulo de Evaluación: Menopausia")
    st.caption("Escala de Valoración de la Menopausia (**MRS - Menopause Rating Scale**, Heinemann et al., **2004**).")
    
    st.markdown("---")
    st.subheader("Evaluación de Síntomas")
    
    col1, col2 = st.columns(2)
    
    with col1:
        s_vaso = st.slider("Bochornos / Sudoración (Sint. Vasomotores)", 0, 4, 0)
        s_card = st.slider("Molestias cardíacas / Palpitaciones", 0, 4, 0)
        s_sue = st.slider("Trastornos del sueño / Insomnio", 0, 4, 0)
        s_anx = st.slider("Estado de ánimo depresivo / Ansiedad", 0, 4, 0)
        
    with col2:
        s_fat = st.slider("Cansancio físico y mental", 0, 4, 0)
        s_sex = st.slider("Problemas sexuales / Sequedad vaginal", 0, 4, 0)
        s_uri = st.slider("Molestias urinarias", 0, 4, 0)
        s_art = st.slider("Molestias articulares y musculares", 0, 4, 0)
        
    total_mrs = s_vaso + s_card + s_sue + s_anx + s_fat + s_sex + s_uri + s_art
    
    st.markdown("---")
    st.metric("Puntaje Total MRS", f"{total_mrs} pts")
    
    if total_mrs < 5:
        st.success("Sintomatología Leve / Ausente.")
    elif 5 <= total_mrs <= 14:
        st.warning("Sintomatología Moderada.")
    else:
        st.error("Sintomatología Severa. Evaluar indicación de Terapia de Reemplazo Hormonal (THM) u otras alternativas.")

# ---------------------------------------------------------
# MÓDULO 3: EVIDENCIA Y MARCOS MODERNOS
# ---------------------------------------------------------
elif opcion == "📚 Evidencia y Referencias":
    st.title("📚 Respaldo Científico y Marcos Modernos")
    st.write("Esta herramienta integra escalas validadas alineadas con los consensos y guías ginecológicas internacionales más recientes:")
    
    st.markdown("---")
    
    st.markdown("### 1. Trastorno de Deseo Sexual Hipoactivo (TDSH / FSIAD)")
    st.markdown("• **Guía de Práctica Clínica ISSWSH (2020):** *International Society for the Study of Women's Sexual Health Clinical Practice Guideline for the Assessment and Treatment of HSDD in Women* (J Sex Med, 2020).")
    st.markdown("• **Consenso Global sobre Testosterona (2019):** *Global Consensus Position Statement on the Use of Testosterone Therapy for Women* (J Clin Endocrinol Metab, 2019).")
    st.markdown("• **Clasificación CIE-11 (OMS, 2022) / DSM-5-TR (2022):** Diagnóstico diferencial entre TDSH primario vs. secundario.")
    
    st.markdown("---")
    
    st.markdown("### 2. Síndromes Climatéricos y Salud Holística en la Menopausia")
    st.markdown("• **Posicionamiento The Menopause Society / NAMS (2022/2023):** *The 2022 Hormone Therapy Position Statement of The North American Menopause Society* (Menopause, 2022).")
    st.markdown("• **Criterios STRAW+10:** Clasificación de la etapa reproductiva y climaterio basada en patrones menstruales y biomarcadores.")
    st.markdown("• **Escala MRS (Estandarización Continua):** Instrumento de medición de severidad validado internacionalmente para monitoreo de respuesta a tratamiento.")

# ---------------------------------------------------------
# PIE DE PÁGINA COMÚN
# ---------------------------------------------------------
st.markdown("---")
st.caption("👨‍⚕️ *Herramienta desarrollada para consulta rápida de profesionales de la salud.*")