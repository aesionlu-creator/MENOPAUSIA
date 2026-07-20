import streamlit

# Configuración de la página
st.set_page_config(
    page_title="Protocolo Ronald v2.0 - Suite Médica Menopausia",
    page_icon="🩺",
    layout="wide"
)

# Estilos personalizados
st.markdown("""
    <style>
    .main-header {
        background: linear-gradient(90deg, #0f172a 0%, #1e1b4b 50%, #0f172a 100%);
        padding: 20px;
        border-radius: 12px;
        color: white;
        margin-bottom: 25px;
    }
    .sub-text {
        font-size: 0.85rem;
        color: #cbd5e1;
    }
    </style>
""", unsafe_allow_html=True)

# Menú lateral para seleccionar la herramienta
st.sidebar.title("🩺 Panel Médico")
modulo = st.sidebar.radio(
    "Seleccione el módulo clínico:",
    ["Protocolo Ronald v2.0 (Evaluación THM)", "Índice FSFI (Función Sexual / TDSH)"]
)

st.sidebar.markdown("---")
st.sidebar.caption("Dr. Ronald - Ginecología y Obstetricia")
st.sidebar.caption("Powered by Gemini AI Collaborator (2026)")

# ==========================================
# MÓDULO 1: PROTOCOLO RONALD v2.0 (THM)
# ==========================================
if modulo == "Protocolo Ronald v2.0 (Evaluación THM)":
    
    st.markdown("""
        <div class="main-header">
            <span style="background-color: #4f46e5; padding: 2px 8px; border-radius: 10px; font-size: 11px; font-weight: bold;">v2.0 Actualizada</span>
            <h1 style="margin: 5px 0 0 0; font-size: 24px;">PROTOCOLO RONALD v2.0</h1>
            <p class="sub-text">Evaluación Clínica Digitalizada de Terapia Hormonal Menopáusica (THM)</p>
        </div>
    """, unsafe_allow_html=True)

    st.subheader("PASO 1: Confirmar Etapa Reproductiva")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        nombre = st.text_input("Nombre Completo", placeholder="Nombre de la paciente")
    with col2:
        edad = st.number_input("Edad (Años)", min_value=18, max_value=100, value=52)
    with col3:
        fur = st.text_input("FUR (Fecha Última Regla)", placeholder="DD/MM/AAAA")
    with col4:
        etapa = st.selectbox("Etapa Reproductiva", [
            "Premenopausia", "Perimenopausia", "Posmenopausia <10 años", "Posmenopausia ≥10 años"
        ])

    st.markdown("---")
    st.subheader("PASO 2: Escala MRS Completa (Validada)")
    st.caption("0 = Sin molestia | 4 = Muy severo")

    col_s, col_p, col_u = st.columns(3)

    with col_s:
        st.markdown("**Dominio Somático (Máx 16 pts)**")
        s1 = st.selectbox("1. Bochornos / Sofocos", [0, 1, 2, 3, 4])
        s2 = st.selectbox("2. Trastornos del sueño", [0, 1, 2, 3, 4])
        s3 = st.selectbox("3. Dolores osteomusculares", [0, 1, 2, 3, 4])
        s4 = st.selectbox("4. Cansancio / Fatiga", [0, 1, 2, 3, 4])

    with col_p:
        st.markdown("**Dominio Psicológico (Máx 12 pts)**")
        p5 = st.selectbox("5. Depresión / Tristeza", [0, 1, 2, 3, 4])
        p6 = st.selectbox("6. Irritabilidad / Mal humor", [0, 1, 2, 3, 4])
        p7 = st.selectbox("7. Ansiedad / Tensión", [0, 1, 2, 3, 4])

    with col_u:
        st.markdown("**Dominio Urogenital (Máx 12 pts)**")
        u8 = st.selectbox("8. Sequedad vaginal", [0, 1, 2, 3, 4])
        u9 = st.selectbox("9. Disfunción sexual", [0, 1, 2, 3, 4])
        u10 = st.selectbox("10. Síntomas urinarios", [0, 1, 2, 3, 4])

    st.markdown("---")
    col_b, col_cx = st.columns(2)

    with col_b:
        st.subheader("PASO 3: Evaluación de Bochornos")
        b_dia = st.number_input("Episodios / día", min_value=0, value=0)
        b_imp = st.slider("Impacto (0 al 10)", 0, 10, 0)
        
        st.write("**Síntomas Asociados:**")
        sudor = st.checkbox("Sudoración")
        noche = st.checkbox("Despierta de noche")
        act = st.checkbox("Interrumpe rutina")
        ropa = st.checkbox("Cambia de ropa")

    with col_cx:
        st.subheader("PASO 4: Contraindicaciones")
        st.error("Marcar cualquiera detendrá la indicación de THM sistémica:")
        cx1 = st.checkbox("Cáncer de mama (activo o previo)")
        cx2 = st.checkbox("Sangrado uterino no estudiado")
        cx3 = st.checkbox("TVP / TEP activa o reciente")
        cx4 = st.checkbox("IAM / ACV / AIT reciente (< 6 meses)")
        cx5 = st.checkbox("Enfermedad hepática grave descompensada")
        cx6 = st.checkbox("Hiperplasia endometrial atípica no tratada")
        cx_coronaria = st.checkbox("⚠️ Relativa: Enfermedad coronaria activa")

    st.markdown("---")
    st.subheader("PASO 5: Factores de Riesgo (Ponderados)")
    col_rc, col_rt, col_rm = st.columns(3)

    with col_rc:
        st.markdown("**Cardiovascular**")
        rc1 = st.checkbox("HTA no controlada (+2)", value=False)
        rc2 = st.checkbox("Diabetes (+1)", value=False)
        rc3 = st.checkbox("Dislipidemia (+1)", value=False)
        rc4 = st.checkbox("IMC ≥ 30 (+2)", value=False)
        rc5 = st.checkbox("Tabaquismo activo (+2)", value=False)
        rc6 = st.checkbox("Enfermedad CV (+1)", value=False)

    with col_rt:
        st.markdown("**Tromboembólico**")
        rt1 = st.checkbox("TVP / TEP previa (+3)", value=False)
        rt2 = st.checkbox("Trombofilia conocida (+3)", value=False)
        rt3 = st.checkbox("IMC ≥ 30 (+2)", key="rt_imc", value=False)
        rt4 = st.checkbox("Várices importantes (+1)", value=False)
        rt5 = st.checkbox("Fam. 1er grado Trombosis (+1)", value=False)

    with col_rm:
        st.markdown("**Cáncer de Mama**")
        rm1 = st.checkbox("Antecedente personal (+3)", value=False)
        rm2 = st.checkbox("BRCA 1/2 (+3)", value=False)
        rm3 = st.checkbox("Familiar 1er grado (+2)", value=False)
        rm4 = st.checkbox("Hiperplasia atípica (+3)", key="rm_hip", value=False)

    st.markdown("---")
    col_esp, col_pref = st.columns(2)

    with col_esp:
        st.subheader("PASO 6: Individualización")
        se_endo = st.checkbox("Endometriosis")
        se_adeno = st.checkbox("Adenomiosis")
        se_mio = st.checkbox("Miomas")
        se_migrana = st.checkbox("Migraña con aura")
        se_lupus = st.checkbox("Lupus")
        se_art = st.checkbox("Artritis reumatoide")
        se_osteo = st.checkbox("Osteoporosis")
        se_precoz = st.checkbox("Menopausia precoz")

    with col_pref:
        st.subheader("PASO 7: Preferencia Paciente")
        preferencia = st.selectbox("Deseo expreso de la paciente:", ["Desea THM", "No desea THM", "Indecisa"])

    if st.button("🧙‍♂️ GENERAR INFORME CLÍNICO AUTOMÁTICO", type="primary", use_container_width=True):
        somatico = s1 + s2 + s3 + s4
        psicologico = p5 + p6 + p7
        urogenital = u8 + u9 + u10
        totalMRS = somatico + psicologico + urogenital

        interpS = "Leve" if somatico <= 4 else ("Moderado" if somatico <= 8 else "Severo")
        interpP = "Leve" if psicologico <= 3 else ("Moderado" if psicologico <= 6 else "Severo")
        interpU = "Leve" if urogenital <= 3 else ("Moderado" if urogenital <= 6 else "Severo")

        interpTotalMRS = "Leves"
        if 9 <= totalMRS <= 14: interpTotalMRS = "Moderados leves"
        elif 15 <= totalMRS <= 20: interpTotalMRS = "Moderados severos"
        elif totalMRS > 20: interpTotalMRS = "Severos"

        pctS = round((somatico / 16) * 100)
        pctP = round((psicologico / 12) * 100)
        pctU = round((urogenital / 12) * 100)
        maxPct = max(pctS, pctP, pctU)

        domPred = "Ninguno"
        analisisDom = "Sin prevalencia marcada."
        if maxPct > 0:
            if maxPct == pctS:
                domPred = "Somático"
                analisisDom = "SINTOMATOLOGÍA VASOMOTORA Y OSTEOMUSCULAR PREDOMINANTE. Indicación preferente de THM sistémica."
            elif maxPct == pctP:
                domPred = "Psicológico"
                analisisDom = "Afectación anímica prevalente. Descartar origen psicógeno independiente de la transición."
            elif maxPct == pctU:
                domPred = "Urogenital"
                analisisDom = "SÍNDROME GENITOURINARIO (SGUM) DOMINANTE. Evaluar THM tópica o sistémica según severidad."

        absCount = sum([cx1, cx2, cx3, cx4, cx5, cx6])
        absText = "ALERTA: Contraindicación absoluta presente." if absCount > 0 else "Ninguna"
        relText = "Enfermedad coronaria activa (Evaluación por Cardiología)" if cx_coronaria else "Ninguna"

        rCardio = (2 if rc1 else 0) + (1 if rc2 else 0) + (1 if rc3 else 0) + (2 if rc4 else 0) + (2 if rc5 else 0) + (1 if rc6 else 0)
        rTrombo = (3 if rt1 else 0) + (3 if rt2 else 0) + (2 if rt3 else 0) + (1 if rt4 else 0) + (1 if rt5 else 0)
        rMama = (3 if rm1 else 0) + (3 if rm2 else 0) + (2 if rm3 else 0) + (3 if rm4 else 0)
        rTotal = rCardio + rTrombo + rMama
        interpRiesgo = "RIESGO BAJO" if rTotal <= 2 else ("RIESGO INTERMEDIO" if rTotal <= 5 else "RIESGO ALTO")

        sitEspList = []
        if se_endo: sitEspList.append("Endometriosis")
        if se_adeno: sitEspList.append("Adenomiosis")
        if se_mio: sitEspList.append("Miomas")
        if se_migrana: sitEspList.append("Migraña con aura")
        if se_lupus: sitEspList.append("Lupus")
        if se_art: sitEspList.append("Artritis reumatoide")
        if se_osteo: sitEspList.append("Osteoporosis")
        if se_precoz: sitEspList.append("Menopausia precoz")
        sitEspText = ", ".join(sitEspList) if sitEspList else "Ninguna"

        indPuntos = 0
        if edad < 60 or etapa == "Posmenopausia <10 años": indPuntos += 1
        if totalMRS >= 9: indPuntos += 1
        if b_dia >= 3: indPuntos += 1
        if b_imp >= 4: indPuntos += 1
        if absCount == 0: indPuntos += 1
        if interpRiesgo in ["RIESGO BAJO", "RIESGO INTERMEDIO"]: indPuntos += 1
        if se_osteo: indPuntos += 1
        if se_precoz or edad < 40: indPuntos += 1

        interpInd = "NO HORMONAL"
        recFinal = "Priorizar manejo no hormonal y modificaciones de estilo de vida."

        if indPuntos >= 7:
            interpInd = "CANDIDATA IDEAL a THM"
            recFinal = "Indicar THM sistémica. Los beneficios superan ampliamente a los riesgos."
        elif indPuntos >= 5:
            interpInd = "CANDIDATA CLARA a THM"
            recFinal = "Indicar THM. Evaluar idoneidad de tipo y vía según comorbilidades."
        elif indPuntos >= 3:
            interpInd = "INDIVIDUALIZAR"
            recFinal = "Ponderar minuciosamente relación riesgo/beneficio con la paciente."

        if absCount > 0:
            interpInd = "NO HORMONAL (CONTRAINDICACIÓN ABSOLUTA)"
            recFinal = "CRÍTICO: THM Sistémica totalmente CONTRAINDICADA. Preferir alternativas no hormonales o estrógenos locales si se limita a síntomas genitourinarios."
        else:
            if se_migrana: recFinal += "\n* Paciente con Migraña con aura: Prescribir exclusivamente VÍA TRANSDÉRMICA."
            if "Endometriosis" in sitEspList or "Adenomiosis" in sitEspList:
                recFinal += "\n* Antecedente de Endometriosis/Adenomiosis: Utilizar ESQUEMA COMBINADO CONTINUO o DIU Mirena."

        informeTexto = f"""===========================================================
INFORME DE EVALUACIÓN MENOPÁUSICA - Protocolo Ronald v2.0
Desarrollo Clínico: Protocolo Ronald | Motor: Gemini AI
===========================================================
Paciente: {nombre if nombre else 'No indicada'} | Edad: {edad} años | FUR: {fur}
Etapa: {etapa}

1. ESCALA MRS COMPLETA
   Dominio Somático: {somatico}/16 → {interpS}
   Dominio Psicológico: {psicologico}/12 → {interpP}
   Dominio Urogenital: {urogenital}/12 → {interpU}
   Puntaje TOTAL: {totalMRS}/40 → {interpTotalMRS}

2. ANÁLISIS POR DOMINIO
   {'[X]' if domPred == 'Somático' else '[ '] Somático predominante ({pctS}% del máx): {analisisDom if domPred == 'Somático' else 'No prevalente.'}
   {'[X]' if domPred == 'Psicológico' else '[ '] Psicológico predominante ({pctP}% del máx): {analisisDom if domPred == 'Psicológico' else 'No prevalente.'}
   {'[X]' if domPred == 'Urogenital' else '[ '] Urogenital predominante ({pctU}% del máx): {analisisDom if domPred == 'Urogenital' else 'No prevalente.'}

3. BOCHORNOS
   Episodios/día: {b_dia} | Impacto: {b_imp}/10
   Sudoración: {'Sí' if sudor else 'No'} | Despierta noche: {'Sí' if noche else 'No'}

4. CONTRAINDICACIONES
   Absolutas: {absText}
   Relativas: {relText}

5. RIESGOS PONDERADOS
   Cardiovascular: {rCardio} pts | Tromboembólico: {rTrombo} pts | Cáncer mama: {rMama} pts
   RIESGO TOTAL: {rTotal} pts → {interpRiesgo}

6. SITUACIONES ESPECIALES: {sitEspText}
7. PREFERENCIA PACIENTE: {preferencia}
8. PUNTAJE DE INDICACIÓN: {indPuntos}/8 → {interpInd}
===========================================================
RECOMENDACIÓN FINAL:
{recFinal}
===========================================================
"""
        st.subheader("📋 Informe Clínico Generado")
        st.code(informeTexto, language="text")

# ==========================================
# MÓDULO 2: EVALUADOR FSFI (FUNCIÓN SEXUAL)
# ==========================================
else:
    st.markdown("""
        <div class="main-header" style="background: linear-gradient(90deg, #115e59 0%, #0f766e 100%);">
            <span style="background-color: #2dd4bf; color: #0f766e; padding: 2px 8px; border-radius: 10px; font-size: 11px; font-weight: bold;">Cuestionario Oficial</span>
            <h1 style="margin: 5px 0 0 0; font-size: 24px;">Índice de Función Sexual Femenina (FSFI)</h1>
            <p class="sub-text">Evaluación del TDSH y candidatura a terapia con Testosterona</p>
        </div>
    """, unsafe_allow_html=True)

    criterio_post = st.checkbox("La paciente es posmenopáusica (natural, quirúrgica o inducida).", value=True)
    criterio_distress = st.checkbox("La baja del deseo le genera un malestar o angustia clínicamente significativa.", value=True)

    st.markdown("---")
    st.subheader("Cuestionario de 19 Ítems")

    # 1. Deseo
    st.markdown("### 1. Deseo (Factor x0.6)")
    q1 = st.radio("1. ¿Con qué frecuencia sintió deseo o interés sexual?", [5, 4, 3, 2, 1], format_func=lambda x: {5:"5 - Casi siempre/siempre", 4:"4 - Mayoría de veces", 3:"3 - A veces", 2:"2 - Pocas veces", 1:"1 - Casi nunca/nunca"}[x], index=3)
    q2 = st.radio("2. ¿Cómo calificaría su nivel de deseo o interés sexual?", [5, 4, 3, 2, 1], format_func=lambda x: {5:"5 - Muy alto", 4:"4 - Alto", 3:"3 - Moderado", 2:"2 - Bajo", 1:"1 - Muy bajo o nulo"}[x], index=3)

    # 2. Excitación
    st.markdown("### 2. Excitación (Factor x0.3)")
    q3 = st.selectbox("3. Frecuencia de excitación durante la actividad sexual", [0, 5, 4, 3, 2, 1], index=3)
    q4 = st.selectbox("4. Nivel de excitación durante la actividad sexual", [0, 5, 4, 3, 2, 1], index=3)
    q5 = st.selectbox("5. Satisfacción con el nivel de excitación", [0, 5, 4, 3, 2, 1], index=4)
    q6 = st.selectbox("6. Confianza en lograr la excitación sexual", [0, 5, 4, 3, 2, 1], index=3)

    # 3. Lubricación
    st.markdown("### 3. Lubricación (Factor x0.3)")
    q7 = st.selectbox("7. Frecuencia de lubricación", [0, 5, 4, 3, 2, 1], index=2)
    q8 = st.selectbox("8. Dificultad para lograr lubricación", [0, 1, 2, 3, 4, 5], index=4)
    q9 = st.selectbox("9. Mantener la lubricación hasta el final", [0, 5, 4, 3, 2, 1], index=2)
    q10 = st.selectbox("10. Dificultad para mantener la lubricación", [0, 1, 2, 3, 4, 5], index=4)

    # 4. Orgasmo
    st.markdown("### 4. Orgasmo (Factor x0.4)")
    q11 = st.selectbox("11. Frecuencia al llegar al orgasmo", [0, 5, 4, 3, 2, 1], index=3)
    q12 = st.selectbox("12. Dificultad para alcanzar el orgasmo", [0, 1, 2, 3, 4, 5], index=3)
    q13 = st.selectbox("13. Satisfacción con capacidad orgásmica", [0, 5, 4, 3, 2, 1], index=3)

    # 5. Satisfacción
    st.markdown("### 5. Satisfacción (Factor x0.4)")
    q14 = st.selectbox("14. Cercanía emocional con pareja", [0, 5, 4, 3, 2, 1], index=3)
    q15 = st.selectbox("15. Satisfacción con relación sexual", [5, 4, 3, 2, 1], index=2)
    q16 = st.selectbox("16. Satisfacción con vida sexual en general", [5, 4, 3, 2, 1], index=3)

    # 6. Dolor
    st.markdown("### 6. Dolor Coital (Factor x0.4)")
    q17 = st.selectbox("17. Frecuencia de dolor durante penetración", [0, 1, 2, 3, 4, 5], index=5)
    q18 = st.selectbox("18. Frecuencia de dolor después de penetración", [0, 1, 2, 3, 4, 5], index=5)
    q19 = st.selectbox("19. Nivel de dolor durante/después", [0, 1, 2, 3, 4, 5], index=5)

    if st.button("📊 CALCULAR PUNTAJE FSFI", type="primary", use_container_width=True):
        score_desire = (q1 + q2) * 0.6
        score_arousal = (q3 + q4 + q5 + q6) * 0.3
        score_lubrication = (q7 + q8 + q9 + q10) * 0.3
        score_orgasm = (q11 + q12 + q13) * 0.4
        score_satisfaction = (q14 + q15 + q16) * 0.4
        score_pain = (q17 + q18 + q19) * 0.4

        score_total = score_desire + score_arousal + score_lubrication + score_orgasm + score_satisfaction + score_pain

        st.markdown("---")
        st.subheader("Resultados de la Evaluación")

        c1, c2, c3 = st.columns(3)
        c1.metric("1. Deseo", f"{score_desire:.2f} pts", "≤ 3.3 = TDSH" if score_desire <= 3.3 else "Normal")
        c2.metric("2. Excitación", f"{score_arousal:.2f} pts")
        c3.metric("3. Lubricación", f"{score_lubrication:.2f} pts")

        c4, c5, c6 = st.columns(3)
        c4.metric("4. Orgasmo", f"{score_orgasm:.2f} pts")
        c5.metric("5. Satisfacción", f"{score_satisfaction:.2f} pts")
        c6.metric("6. Dolor Coital", f"{score_pain:.2f} pts", "≤ 4.0 = Dispareunia" if score_pain <= 4.0 else "Sin dolor")

        st.subheader(f"PUNTAJE GLOBAL FSFI: {score_total:.2f} pts")

        if not criterio_post or not criterio_distress:
            st.error("❌ **No Candidata a Testosterona:** No cumple los criterios basales de posmenopausia y malestar manifiesto.")
        elif score_pain <= 4.0:
            st.warning("⚠️ **Tratar Dispareunia Primero:** Paciente presenta dolor coital significativo. Tratar atrofia local con estrógenos antes de evaluar testosterona.")
        elif score_desire > 3.3:
            st.info("ℹ️ **No Candidata a TDSH:** Subtotal de deseo > 3.3 (Deseo conservado).")
        else:
            st.success("✅ **Candidata Apta para Testosterona:** Cumple criterios de TDSH (Deseo ≤ 3.3) sin dolor limitante. Solicitar laboratorios previos.")
