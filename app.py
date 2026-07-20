import streamlit as st
import streamlit.components.v1 as components

# Configuración de página completa en Streamlit
st.set_page_config(
    page_title="Plataforma Integrada de Salud Menopáusica",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Renderizado del HTML/CSS/JS completo
html_code = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Plataforma Integrada de Salud Menopáusica - Dr. Ronald & Gemini AI</title>
    <!-- Tailwind CSS -->
    <script src="https://cdn.tailwindcss.com"></script>
    <!-- FontAwesome Iconos -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <!-- html2pdf.js -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/html2pdf.js/0.10.1/html2pdf.bundle.min.js"></script>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
    <style>
        body { font-family: 'Inter', sans-serif; }
        ::-webkit-scrollbar { width: 8px; }
        ::-webkit-scrollbar-track { background: #f1f5f9; }
        ::-webkit-scrollbar-thumb { background: #cbd5e1; border-radius: 4px; }
        ::-webkit-scrollbar-thumb:hover { background: #94a3b8; }
        .tab-btn.active {
            border-bottom-color: #6366f1;
            color: #4f46e5;
            background-color: #ffffff;
        }
    </style>
</head>
<body class="bg-slate-100 text-slate-800 min-h-screen pb-12">

    <!-- BARRA DE NAVEGACIÓN PRINCIPAL (PESTAÑAS) -->
    <header class="bg-slate-900 text-white sticky top-0 z-50 shadow-md">
        <div class="max-w-7xl mx-auto px-4 flex flex-col sm:flex-row justify-between items-center gap-2">
            <div class="py-3 flex items-center gap-3">
                <span class="bg-indigo-600 text-white text-xs font-bold px-2.5 py-1 rounded-md uppercase tracking-wider">Suite Clínica v2.0</span>
                <h1 class="font-extrabold text-base md:text-lg tracking-tight">Evaluación Integral en Menopausia</h1>
            </div>
            
            <nav class="flex space-x-2 text-xs md:text-sm font-semibold">
                <button id="btn-tab-thm" onclick="switchTab('thm')" class="tab-btn active px-4 py-3 border-b-4 border-transparent transition-all flex items-center gap-2 text-slate-300 hover:text-white">
                    <i class="fa-solid fa-notes-medical"></i> 1. Protocolo THM (MRS / Riesgos)
                </button>
                <button id="btn-tab-fsfi" onclick="switchTab('fsfi')" class="tab-btn px-4 py-3 border-b-4 border-transparent transition-all flex items-center gap-2 text-slate-300 hover:text-white">
                    <i class="fa-solid fa-heart-pulse"></i> 2. Test FSFI (TDSH / Testosterona)
                </button>
            </nav>
        </div>
    </header>

    <div class="max-w-7xl mx-auto px-4 py-6">

        <!-- MÓDULO 1: PROTOCOLO RONALD V2.0 - EVALUACIÓN THM -->
        <main id="tab-thm" class="block space-y-6">
            <div class="bg-gradient-to-r from-slate-900 via-indigo-950 to-slate-900 text-white rounded-2xl p-6 shadow-xl border border-indigo-500/20">
                <div class="flex flex-col md:flex-row justify-between items-center gap-4">
                    <div>
                        <div class="flex items-center gap-3">
                            <span class="bg-indigo-600 text-white text-xs font-bold px-3 py-1 rounded-full uppercase tracking-wider">v2.0 Actualizada</span>
                            <span class="text-xs text-indigo-300"><i class="fa-solid fa-microchip mr-1"></i> Powered by Gemini AI</span>
                        </div>
                        <h2 class="text-2xl md:text-3xl font-extrabold tracking-tight mt-2 text-white">PROTOCOLO RONALD v2.0</h2>
                        <p class="text-xs md:text-sm text-slate-300 mt-1">Evaluación Clínica Digitalizada de Terapia Hormonal Menopáusica (THM)</p>
                    </div>
                    <div class="text-right border-l-0 md:border-l border-indigo-800 pl-0 md:pl-6 text-xs text-slate-400 hidden sm:block">
                        <p class="font-semibold text-indigo-200">Co-Desarrollo Clínico - Tecnológico</p>
                        <p class="mt-0.5"><i class="fa-solid fa-user-doctor text-indigo-400 mr-1"></i> Autor: Dr. Ronald</p>
                        <p><i class="fa-solid fa-brain text-purple-400 mr-1"></i> Motor Clínico: Gemini AI Collaborator</p>
                    </div>
                </div>
            </div>

            <form id="appForm" class="space-y-6">
                <!-- PASO 1 -->
                <div class="bg-white rounded-xl shadow-md p-6 border border-slate-200">
                    <h3 class="text-base font-bold text-slate-900 flex items-center gap-2 mb-4 pb-2 border-b">
                        <i class="fa-solid fa-address-card text-indigo-600"></i> PASO 1: Confirmar Etapa Reproductiva
                    </h3>
                    <div class="grid grid-cols-1 md:grid-cols-4 gap-4 text-sm">
                        <div>
                            <label class="block font-semibold text-slate-700 mb-1">Nombre Completo</label>
                            <input type="text" id="nombre" placeholder="Nombre de la paciente" required class="w-full border border-slate-300 rounded-lg p-2.5 focus:ring-2 focus:ring-indigo-500 focus:outline-none">
                        </div>
                        <div>
                            <label class="block font-semibold text-slate-700 mb-1">Edad (Años)</label>
                            <input type="number" id="edad" placeholder="Ej. 52" required class="w-full border border-slate-300 rounded-lg p-2.5 focus:ring-2 focus:ring-indigo-500 focus:outline-none">
                        </div>
                        <div>
                            <label class="block font-semibold text-slate-700 mb-1">FUR (Fecha Última Regla)</label>
                            <input type="text" id="fur" placeholder="DD/MM/AAAA" class="w-full border border-slate-300 rounded-lg p-2.5 focus:ring-2 focus:ring-indigo-500 focus:outline-none">
                        </div>
                        <div>
                            <label class="block font-semibold text-slate-700 mb-1">Etapa Reproductiva</label>
                            <select id="etapa" class="w-full border border-slate-300 rounded-lg p-2.5 focus:ring-2 focus:ring-indigo-500 focus:outline-none bg-white">
                                <option value="Premenopausia">Premenopausia</option>
                                <option value="Perimenopausia">Perimenopausia</option>
                                <option value="Posmenopausia <10 años">Posmenopausia &lt; 10 años</option>
                                <option value="Posmenopausia ≥10 años">Posmenopausia &ge; 10 años</option>
                            </select>
                        </div>
                    </div>
                </div>

                <!-- PASO 2 -->
                <div class="bg-white rounded-xl shadow-md p-6 border border-slate-200">
                    <div class="flex justify-between items-center mb-4 pb-2 border-b">
                        <h3 class="text-base font-bold text-slate-900 flex items-center gap-2">
                            <i class="fa-solid fa-chart-simple text-indigo-600"></i> PASO 2: Escala MRS Completa (Validada)
                        </h3>
                        <span class="text-xs text-slate-500 font-medium">0 = Sin molestia | 4 = Muy severo</span>
                    </div>

                    <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
                        <div class="bg-amber-50/50 rounded-xl p-4 border border-amber-200/60">
                            <h4 class="text-xs font-bold uppercase tracking-wider text-amber-900 mb-3 flex items-center justify-between">
                                <span>Dominio Somático</span>
                                <span class="text-amber-700 bg-amber-100 px-2 py-0.5 rounded text-[10px]">Máx 16 pts</span>
                            </h4>
                            <div class="space-y-3 text-xs">
                                <div><label class="block text-slate-700 font-medium mb-1">1. Bochornos / Sofocos</label><select class="mrs-s w-full border border-amber-200 rounded-lg p-2 bg-white"><option value="0">0 - Ausente</option><option value="1">1 - Leve</option><option value="2">2 - Moderado</option><option value="3">3 - Severo</option><option value="4">4 - Muy severo</option></select></div>
                                <div><label class="block text-slate-700 font-medium mb-1">2. Trastornos del sueño</label><select class="mrs-s w-full border border-amber-200 rounded-lg p-2 bg-white"><option value="0">0 - Ausente</option><option value="1">1 - Leve</option><option value="2">2 - Moderado</option><option value="3">3 - Severo</option><option value="4">4 - Muy severo</option></select></div>
                                <div><label class="block text-slate-700 font-medium mb-1">3. Dolores osteomusculares</label><select class="mrs-s w-full border border-amber-200 rounded-lg p-2 bg-white"><option value="0">0 - Ausente</option><option value="1">1 - Leve</option><option value="2">2 - Moderado</option><option value="3">3 - Severo</option><option value="4">4 - Muy severo</option></select></div>
                                <div><label class="block text-slate-700 font-medium mb-1">4. Cansancio / Fatiga</label><select class="mrs-s w-full border border-amber-200 rounded-lg p-2 bg-white"><option value="0">0 - Ausente</option><option value="1">1 - Leve</option><option value="2">2 - Moderado</option><option value="3">3 - Severo</option><option value="4">4 - Muy severo</option></select></div>
                            </div>
                        </div>

                        <div class="bg-blue-50/50 rounded-xl p-4 border border-blue-200/60">
                            <h4 class="text-xs font-bold uppercase tracking-wider text-blue-900 mb-3 flex items-center justify-between">
                                <span>Dominio Psicológico</span>
                                <span class="text-blue-700 bg-blue-100 px-2 py-0.5 rounded text-[10px]">Máx 12 pts</span>
                            </h4>
                            <div class="space-y-3 text-xs">
                                <div><label class="block text-slate-700 font-medium mb-1">5. Depresión / Tristeza</label><select class="mrs-p w-full border border-blue-200 rounded-lg p-2 bg-white"><option value="0">0 - Ausente</option><option value="1">1 - Leve</option><option value="2">2 - Moderado</option><option value="3">3 - Severo</option><option value="4">4 - Muy severo</option></select></div>
                                <div><label class="block text-slate-700 font-medium mb-1">6. Irritabilidad / Mal humor</label><select class="mrs-p w-full border border-blue-200 rounded-lg p-2 bg-white"><option value="0">0 - Ausente</option><option value="1">1 - Leve</option><option value="2">2 - Moderado</option><option value="3">3 - Severo</option><option value="4">4 - Muy severo</option></select></div>
                                <div><label class="block text-slate-700 font-medium mb-1">7. Ansiedad / Tensión</label><select class="mrs-p w-full border border-blue-200 rounded-lg p-2 bg-white"><option value="0">0 - Ausente</option><option value="1">1 - Leve</option><option value="2">2 - Moderado</option><option value="3">3 - Severo</option><option value="4">4 - Muy severo</option></select></div>
                            </div>
                        </div>

                        <div class="bg-purple-50/50 rounded-xl p-4 border border-purple-200/60">
                            <h4 class="text-xs font-bold uppercase tracking-wider text-purple-900 mb-3 flex items-center justify-between">
                                <span>Dominio Urogenital</span>
                                <span class="text-purple-700 bg-purple-100 px-2 py-0.5 rounded text-[10px]">Máx 12 pts</span>
                            </h4>
                            <div class="space-y-3 text-xs">
                                <div><label class="block text-slate-700 font-medium mb-1">8. Sequedad vaginal</label><select class="mrs-u w-full border border-purple-200 rounded-lg p-2 bg-white"><option value="0">0 - Ausente</option><option value="1">1 - Leve</option><option value="2">2 - Moderado</option><option value="3">3 - Severo</option><option value="4">4 - Muy severo</option></select></div>
                                <div><label class="block text-slate-700 font-medium mb-1">9. Disfunción sexual</label><select class="mrs-u w-full border border-purple-200 rounded-lg p-2 bg-white"><option value="0">0 - Ausente</option><option value="1">1 - Leve</option><option value="2">2 - Moderado</option><option value="3">3 - Severo</option><option value="4">4 - Muy severo</option></select></div>
                                <div><label class="block text-slate-700 font-medium mb-1">10. Síntomas urinarios</label><select class="mrs-u w-full border border-purple-200 rounded-lg p-2 bg-white"><option value="0">0 - Ausente</option><option value="1">1 - Leve</option><option value="2">2 - Moderado</option><option value="3">3 - Severo</option><option value="4">4 - Muy severo</option></select></div>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- PASO 3 Y PASO 4 -->
                <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                    <div class="bg-white rounded-xl shadow-md p-6 border border-slate-200">
                        <h3 class="text-base font-bold text-slate-900 flex items-center gap-2 mb-4 pb-2 border-b">
                            <i class="fa-solid fa-fire text-orange-500"></i> PASO 3: Evaluación de Bochornos
                        </h3>
                        <div class="space-y-4 text-xs">
                            <div class="grid grid-cols-2 gap-3">
                                <div><label class="block font-semibold text-slate-700 mb-1">Episodios / día</label><input type="number" id="bochornos-dia" value="0" class="w-full border border-slate-300 rounded-lg p-2"></div>
                                <div><label class="block font-semibold text-slate-700 mb-1">Impacto (0 al 10)</label><input type="number" id="bochornos-impacto" min="0" max="10" value="0" class="w-full border border-slate-300 rounded-lg p-2"></div>
                            </div>
                            <div class="bg-slate-50 p-3 rounded-lg border border-slate-200 space-y-2">
                                <p class="font-bold text-slate-600 uppercase text-[10px]">Síntomas Asociados</p>
                                <div class="grid grid-cols-2 gap-2">
                                    <label class="flex items-center gap-2"><input type="checkbox" id="sint-sudor" class="rounded text-indigo-600"> <span>Sudoración</span></label>
                                    <label class="flex items-center gap-2"><input type="checkbox" id="sint-noche" class="rounded text-indigo-600"> <span>Despierta de noche</span></label>
                                    <label class="flex items-center gap-2"><input type="checkbox" id="sint-act" class="rounded text-indigo-600"> <span>Interrumpe rutina</span></label>
                                    <label class="flex items-center gap-2"><input type="checkbox" id="sint-ropa" class="rounded text-indigo-600"> <span>Cambia de ropa</span></label>
                                </div>
                            </div>
                        </div>
                    </div>

                    <div class="bg-red-50/40 rounded-xl shadow-md p-6 border border-red-200">
                        <h3 class="text-base font-bold text-red-900 flex items-center gap-2 mb-3 pb-2 border-b border-red-200">
                            <i class="fa-solid fa-ban text-red-600"></i> PASO 4: Contraindicaciones
                        </h3>
                        <p class="text-[11px] text-red-700 mb-3 font-medium">Marcar cualquiera detendrá automáticamente la indicación de THM sistémica:</p>
                        <div class="space-y-2 text-xs">
                            <label class="flex items-start gap-2 text-slate-800"><input type="checkbox" class="cx-absoluta mt-0.5 rounded text-red-600"> <span>Cáncer de mama (activo o previo)</span></label>
                            <label class="flex items-start gap-2 text-slate-800"><input type="checkbox" class="cx-absoluta mt-0.5 rounded text-red-600"> <span>Sangrado uterino no estudiado</span></label>
                            <label class="flex items-start gap-2 text-slate-800"><input type="checkbox" class="cx-absoluta mt-0.5 rounded text-red-600"> <span>TVP / TEP activa o reciente</span></label>
                            <label class="flex items-start gap-2 text-slate-800"><input type="checkbox" class="cx-absoluta mt-0.5 rounded text-red-600"> <span>IAM / ACV / AIT reciente (&lt; 6 meses)</span></label>
                            <label class="flex items-start gap-2 text-slate-800"><input type="checkbox" class="cx-absoluta mt-0.5 rounded text-red-600"> <span>Enfermedad hepática grave descompensada</span></label>
                            <label class="flex items-start gap-2 text-slate-800"><input type="checkbox" class="cx-absoluta mt-0.5 rounded text-red-600"> <span>Hiperplasia endometrial atípica no tratada</span></label>
                        </div>
                        <div class="mt-3 pt-2 border-t border-red-200/80 text-xs">
                            <label class="flex items-center gap-2 font-semibold text-slate-800"><input type="checkbox" id="cx-coronaria" class="rounded text-amber-600"> <span>⚠️ Relativa: Enfermedad coronaria activa</span></label>
                        </div>
                    </div>
                </div>

                <!-- PASO 5 -->
                <div class="bg-white rounded-xl shadow-md p-6 border border-slate-200">
                    <h3 class="text-base font-bold text-slate-900 flex items-center gap-2 mb-4 pb-2 border-b">
                        <i class="fa-solid fa-triangle-exclamation text-amber-500"></i> PASO 5: Factores de Riesgo (Ponderados)
                    </h3>
                    <div class="grid grid-cols-1 md:grid-cols-3 gap-4 text-xs">
                        <div class="bg-slate-50 p-3 rounded-lg border border-slate-200">
                            <h4 class="font-bold text-slate-800 border-b pb-1 mb-2">A. Cardiovascular</h4>
                            <div class="space-y-1.5">
                                <label class="flex items-center justify-between"><span>HTA no controlada (+2)</span><input type="checkbox" value="2" class="rf-cardio rounded text-indigo-600"></label>
                                <label class="flex items-center justify-between"><span>Diabetes (+1)</span><input type="checkbox" value="1" class="rf-cardio rounded text-indigo-600"></label>
                                <label class="flex items-center justify-between"><span>Dislipidemia (+1)</span><input type="checkbox" value="1" class="rf-cardio rounded text-indigo-600"></label>
                                <label class="flex items-center justify-between"><span>IMC &ge; 30 (+2)</span><input type="checkbox" value="2" class="rf-cardio rounded text-indigo-600"></label>
                                <label class="flex items-center justify-between"><span>Tabaquismo activo (+2)</span><input type="checkbox" value="2" class="rf-cardio rounded text-indigo-600"></label>
                                <label class="flex items-center justify-between"><span>Enfermedad CV (+1)</span><input type="checkbox" value="1" class="rf-cardio rounded text-indigo-600"></label>
                            </div>
                        </div>
                        <div class="bg-slate-50 p-3 rounded-lg border border-slate-200">
                            <h4 class="font-bold text-slate-800 border-b pb-1 mb-2">B. Tromboembólico</h4>
                            <div class="space-y-1.5">
                                <label class="flex items-center justify-between"><span>TVP / TEP previa (+3)</span><input type="checkbox" value="3" class="rf-trombo rounded text-indigo-600"></label>
                                <label class="flex items-center justify-between"><span>Trombofilia conocida (+3)</span><input type="checkbox" value="3" class="rf-trombo rounded text-indigo-600"></label>
                                <label class="flex items-center justify-between"><span>IMC &ge; 30 (+2)</span><input type="checkbox" value="2" class="rf-trombo rounded text-indigo-600"></label>
                                <label class="flex items-center justify-between"><span>Várices importantes (+1)</span><input type="checkbox" value="1" class="rf-trombo rounded text-indigo-600"></label>
                                <label class="flex items-center justify-between"><span>Fam. 1er grado Trombosis (+1)</span><input type="checkbox" value="1" class="rf-trombo rounded text-indigo-600"></label>
                            </div>
                        </div>
                        <div class="bg-slate-50 p-3 rounded-lg border border-slate-200">
                            <h4 class="font-bold text-slate-800 border-b pb-1 mb-2">C. Cáncer de Mama</h4>
                            <div class="space-y-1.5">
                                <label class="flex items-center justify-between"><span>Antecedente personal (+3)</span><input type="checkbox" value="3" class="rf-mama rounded text-indigo-600"></label>
                                <label class="flex items-center justify-between"><span>BRCA 1/2 (+3)</span><input type="checkbox" value="3" class="rf-mama rounded text-indigo-600"></label>
                                <label class="flex items-center justify-between"><span>Familiar 1er grado (+2)</span><input type="checkbox" value="2" class="rf-mama rounded text-indigo-600"></label>
                                <label class="flex items-center justify-between"><span>Hiperplasia atípica (+3)</span><input type="checkbox" value="3" class="rf-mama rounded text-indigo-600"></label>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- PASO 6 Y 7 -->
                <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                    <div class="bg-white rounded-xl shadow-md p-6 border border-slate-200">
                        <h3 class="text-base font-bold text-slate-900 flex items-center gap-2 mb-3 pb-2 border-b">
                            <i class="fa-solid fa-sliders text-indigo-600"></i> PASO 6: Individualización
                        </h3>
                        <div class="grid grid-cols-2 gap-2 text-xs">
                            <label class="flex items-center gap-1.5"><input type="checkbox" value="Endometriosis" class="sit-esp rounded"> <span>Endometriosis</span></label>
                            <label class="flex items-center gap-1.5"><input type="checkbox" value="Adenomiosis" class="sit-esp rounded"> <span>Adenomiosis</span></label>
                            <label class="flex items-center gap-1.5"><input type="checkbox" value="Miomas" class="sit-esp rounded"> <span>Miomas</span></label>
                            <label class="flex items-center gap-1.5"><input type="checkbox" value="Migraña con aura" class="sit-esp rounded" id="se-migrana"> <span>Migraña con aura</span></label>
                            <label class="flex items-center gap-1.5"><input type="checkbox" value="Lupus" class="sit-esp rounded"> <span>Lupus</span></label>
                            <label class="flex items-center gap-1.5"><input type="checkbox" value="Artritis reumatoide" class="sit-esp rounded"> <span>Artritis reumatoide</span></label>
                            <label class="flex items-center gap-1.5"><input type="checkbox" value="Osteoporosis" class="sit-esp rounded" id="se-osteo"> <span>Osteoporosis</span></label>
                            <label class="flex items-center gap-1.5"><input type="checkbox" value="Menopausia precoz" class="sit-esp rounded" id="se-precoz"> <span>Menopausia precoz</span></label>
                        </div>
                    </div>
                    <div class="bg-white rounded-xl shadow-md p-6 border border-slate-200">
                        <h3 class="text-base font-bold text-slate-900 flex items-center gap-2 mb-3 pb-2 border-b">
                            <i class="fa-solid fa-comments text-indigo-600"></i> PASO 7: Preferencia Paciente
                        </h3>
                        <div class="text-xs space-y-3">
                            <label class="block font-medium text-slate-700">Deseo expreso de la paciente:</label>
                            <select id="preferencia" class="w-full border border-slate-300 rounded-lg p-2.5 bg-white font-medium">
                                <option value="Desea THM">Desea THM</option>
                                <option value="No desea THM">No desea THM</option>
                                <option value="Indecisa">Indecisa</option>
                            </select>
                        </div>
                    </div>
                </div>

                <div class="text-center pt-2">
                    <button type="button" onclick="generarInformeApp()" class="bg-gradient-to-r from-indigo-700 to-slate-800 hover:from-indigo-800 hover:to-slate-900 text-white font-bold py-4 px-10 rounded-xl shadow-lg hover:shadow-xl transition duration-200 flex items-center justify-center gap-3 mx-auto text-sm">
                        <i class="fa-solid fa-wand-magic-sparkles"></i> GENERAR INFORME CLÍNICO AUTOMÁTICO
                    </button>
                </div>
            </form>

            <section id="seccion-resultado" class="hidden mt-10 space-y-4">
                <div class="flex flex-wrap justify-between items-center gap-3 bg-white p-4 rounded-xl border border-slate-200 shadow-sm">
                    <h3 class="text-lg font-bold text-slate-800 flex items-center gap-2">
                        <i class="fa-solid fa-file-medical text-emerald-600"></i> Informe Generado
                    </h3>
                    <div class="flex items-center gap-2">
                        <button onclick="copiarTextoInforme()" class="bg-slate-700 hover:bg-slate-800 text-white text-xs font-semibold py-2.5 px-4 rounded-lg shadow transition flex items-center gap-2">
                            <i class="fa-solid fa-copy"></i> Copiar Texto
                        </button>
                        <button onclick="exportarPDF()" class="bg-red-600 hover:bg-red-700 text-white text-xs font-semibold py-2.5 px-4 rounded-lg shadow transition flex items-center gap-2">
                            <i class="fa-solid fa-file-pdf"></i> Descargar PDF
                        </button>
                    </div>
                </div>
                <textarea id="rawTextInforme" class="hidden"></textarea>
                <div id="pdfView" class="bg-white p-8 rounded-xl border border-slate-300 shadow-md font-mono text-xs text-slate-900 leading-relaxed space-y-4"></div>
            </section>
        </main>

        <!-- MÓDULO 2: EVALUADOR FSFI -->
        <main id="tab-fsfi" class="hidden space-y-6">
            <div class="bg-gradient-to-r from-teal-800 to-cyan-900 rounded-2xl p-6 md:p-8 text-white shadow-xl border border-teal-900/20">
                <div class="flex flex-col md:flex-row justify-between items-start md:items-center gap-6">
                    <div>
                        <span class="bg-teal-500/30 text-teal-200 text-xs font-bold px-3 py-1 rounded-full uppercase tracking-wider">Cuestionario Oficial e Interactivo</span>
                        <h2 class="text-3xl md:text-4xl font-extrabold mt-2 tracking-tight">Índice de Función Sexual Femenina (FSFI)</h2>
                        <p class="text-teal-100 text-sm md:text-base mt-2 max-w-2xl">
                            Evaluación científica autoadministrada de 19 ítems para el diagnóstico del TDSH y candidatura a terapia con Testosterona.
                        </p>
                    </div>
                    <div class="bg-white/10 backdrop-blur-md p-4 rounded-xl border border-white/10 text-xs text-left md:text-right shrink-0">
                        <p class="font-medium text-teal-200 uppercase tracking-wider">Herramienta Clínica Diseñada por:</p>
                        <p class="font-bold text-white text-base mt-0.5">Dr. Ronald</p>
                        <p class="text-teal-100/70 text-xs">Ginecología y Obstetricia</p>
                        <div class="border-t border-white/15 my-2"></div>
                        <p class="text-teal-200 font-medium">Soporte Tecnológico:</p>
                        <p class="font-semibold text-white">Gemini AI • 2026</p>
                    </div>
                </div>
            </div>

            <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-start">
                <div class="lg:col-span-7 space-y-6">
                    <div class="bg-white p-5 rounded-2xl border border-slate-200 shadow-sm space-y-4">
                        <h3 class="text-xs font-bold uppercase tracking-wider text-teal-700 flex items-center gap-2">
                            <span class="p-1 rounded-md bg-teal-50 text-teal-700">📋</span> 1. Criterios Clínicos del Consenso Global 2019
                        </h3>
                        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                            <label class="flex items-start gap-3 p-3 bg-slate-50 rounded-xl border border-slate-200 hover:border-teal-500 cursor-pointer transition-all">
                                <input type="checkbox" id="chk-postmenopause" class="mt-1 h-5 w-5 rounded border-slate-300 text-teal-600 focus:ring-teal-500" checked>
                                <span class="text-xs text-slate-700 leading-normal">La paciente es <strong>posmenopáusica</strong> (natural, quirúrgica o inducida).</span>
                            </label>
                            <label class="flex items-start gap-3 p-3 bg-slate-50 rounded-xl border border-slate-200 hover:border-teal-500 cursor-pointer transition-all">
                                <input type="checkbox" id="chk-distress" class="mt-1 h-5 w-5 rounded border-slate-300 text-teal-600 focus:ring-teal-500" checked>
                                <span class="text-xs text-slate-700 leading-normal">La baja del deseo le genera un <strong>malestar o angustia clínicamente significativa</strong>.</span>
                            </label>
                        </div>
                    </div>

                    <div class="bg-white p-4 rounded-xl border border-slate-200 shadow-sm flex items-center justify-between gap-4">
                        <div class="w-full bg-slate-100 rounded-full h-2.5">
                            <div id="progress-bar" class="bg-teal-600 h-2.5 rounded-full transition-all duration-300" style="width: 0%"></div>
                        </div>
                        <span id="progress-text" class="text-xs font-bold text-teal-800 whitespace-nowrap bg-teal-50 px-2.5 py-1 rounded-full">0 / 19 Respondidas</span>
                    </div>

                    <div id="questions-form" class="space-y-6"></div>
                </div>

                <div class="lg:col-span-5 space-y-6 lg:sticky lg:top-20">
                    <div class="bg-slate-900 text-white p-6 rounded-2xl shadow-xl border border-slate-800 space-y-6">
                        <div class="flex justify-between items-center">
                            <h3 class="text-xs font-bold uppercase tracking-widest text-teal-400">Análisis FSFI en Tiempo Real</h3>
                            <button onclick="resetAll()" class="text-xs text-slate-400 hover:text-white underline transition-colors">Reiniciar Test</button>
                        </div>

                        <div class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-2 gap-3">
                            <div class="bg-slate-800/80 p-3 rounded-xl border border-slate-700/50 flex flex-col justify-between">
                                <div><div class="flex justify-between items-center"><span class="text-xs font-semibold text-slate-300">1. Deseo</span><span class="text-[9px] text-teal-400 font-mono">Factor x0.6</span></div><p id="score-desire" class="text-xl font-bold text-white mt-1">0.00</p></div>
                                <span id="badge-desire" class="text-[9px] mt-1.5 px-2 py-0.5 rounded font-bold bg-slate-700/50 text-slate-400 w-fit">Pendiente</span>
                            </div>
                            <div class="bg-slate-800/80 p-3 rounded-xl border border-slate-700/50 flex flex-col justify-between">
                                <div><div class="flex justify-between items-center"><span class="text-xs font-semibold text-slate-300">2. Excitación</span><span class="text-[9px] text-teal-400 font-mono">Factor x0.3</span></div><p id="score-arousal" class="text-xl font-bold text-white mt-1">0.00</p></div>
                                <span id="badge-arousal" class="text-[9px] mt-1.5 px-2 py-0.5 rounded font-bold bg-slate-700/50 text-slate-400 w-fit">Pendiente</span>
                            </div>
                            <div class="bg-slate-800/80 p-3 rounded-xl border border-slate-700/50 flex flex-col justify-between">
                                <div><div class="flex justify-between items-center"><span class="text-xs font-semibold text-slate-300">3. Lubricación</span><span class="text-[9px] text-teal-400 font-mono">Factor x0.3</span></div><p id="score-lubrication" class="text-xl font-bold text-white mt-1">0.00</p></div>
                                <span id="badge-lubrication" class="text-[9px] mt-1.5 px-2 py-0.5 rounded font-bold bg-slate-700/50 text-slate-400 w-fit">Pendiente</span>
                            </div>
                            <div class="bg-slate-800/80 p-3 rounded-xl border border-slate-700/50 flex flex-col justify-between">
                                <div><div class="flex justify-between items-center"><span class="text-xs font-semibold text-slate-300">4. Orgasmo</span><span class="text-[9px] text-teal-400 font-mono">Factor x0.4</span></div><p id="score-orgasm" class="text-xl font-bold text-white mt-1">0.00</p></div>
                                <span id="badge-orgasm" class="text-[9px] mt-1.5 px-2 py-0.5 rounded font-bold bg-slate-700/50 text-slate-400 w-fit">Pendiente</span>
                            </div>
                            <div class="bg-slate-800/80 p-3 rounded-xl border border-slate-700/50 flex flex-col justify-between">
                                <div><div class="flex justify-between items-center"><span class="text-xs font-semibold text-slate-300">5. Satisfacción</span><span class="text-[9px] text-teal-400 font-mono">Factor x0.4</span></div><p id="score-satisfaction" class="text-xl font-bold text-white mt-1">0.00</p></div>
                                <span id="badge-satisfaction" class="text-[9px] mt-1.5 px-2 py-0.5 rounded font-bold bg-slate-700/50 text-slate-400 w-fit">Pendiente</span>
                            </div>
                            <div class="bg-slate-800/80 p-3 rounded-xl border border-slate-700/50 flex flex-col justify-between">
                                <div><div class="flex justify-between items-center"><span class="text-xs font-semibold text-slate-300">6. Dolor Coital</span><span class="text-[9px] text-teal-400 font-mono">Factor x0.4</span></div><p id="score-pain" class="text-xl font-bold text-white mt-1">0.00</p></div>
                                <span id="badge-pain" class="text-[9px] mt-1.5 px-2 py-0.5 rounded font-bold bg-slate-700/50 text-slate-400 w-fit">Pendiente</span>
                            </div>
                        </div>

                        <div class="bg-slate-800 p-4 rounded-xl border border-slate-700 text-center">
                            <p class="text-xs text-slate-400 uppercase tracking-widest font-bold">PUNTAJE GLOBAL FSFI</p>
                            <p id="score-total" class="text-5xl font-extrabold text-white mt-1.5">0.00</p>
                            <p class="text-[11px] text-teal-300 mt-1.5">Disfunción Sexual si es ≤ 26.55 puntos</p>
                        </div>

                        <div id="verdict-card" class="p-4 rounded-xl border text-center transition-all duration-300 bg-slate-800 text-slate-300 border-slate-700">
                            <p class="text-xs uppercase tracking-wider font-bold" id="verdict-title">Evaluando Datos...</p>
                            <p class="text-sm font-semibold mt-1" id="verdict-body">Por favor, complete las 19 preguntas del test.</p>
                        </div>
                    </div>

                    <div class="bg-white p-5 rounded-2xl border border-slate-200 shadow-sm space-y-4">
                        <div class="flex justify-between items-center">
                            <h3 class="text-xs font-bold uppercase tracking-wider text-slate-500 flex items-center gap-1.5">
                                <span>📝</span> Nota Clínica para Historia
                            </h3>
                            <button onclick="copyClinicalNote()" class="text-xs bg-teal-50 hover:bg-teal-100 text-teal-700 font-semibold px-2.5 py-1.5 rounded-lg border border-teal-200 flex items-center gap-1 transition-colors">
                                <span>Copiar nota</span>
                            </button>
                        </div>
                        <textarea id="clinical-note" rows="6" class="w-full bg-slate-50 border border-slate-200 rounded-xl p-3 text-[11px] font-mono text-slate-600 focus:outline-none focus:ring-1 focus:ring-teal-500 cursor-text" readonly></textarea>
                        <p id="copy-success-msg" class="text-xs text-emerald-600 font-semibold text-center hidden">¡Nota clínica copiada con éxito!</p>
                    </div>
                </div>
            </div>
        </main>

        <footer class="mt-12 text-center text-xs text-slate-500 space-y-1 border-t border-slate-200 pt-6">
            <p class="font-semibold text-slate-600">Plataforma Integrada Menopausia &copy; 2026 — Algoritmos de Decisión Clínica</p>
            <p class="text-[11px] text-slate-400">Co-diseñado e implementado por Dr. Ronald & Gemini AI Collaborator</p>
        </footer>
    </div>

    <script>
        function switchTab(tab) {
            const tabThm = document.getElementById('tab-thm');
            const tabFsfi = document.getElementById('tab-fsfi');
            const btnThm = document.getElementById('btn-tab-thm');
            const btnFsfi = document.getElementById('btn-tab-fsfi');

            if (tab === 'thm') {
                tabThm.classList.remove('hidden');
                tabFsfi.classList.add('hidden');
                btnThm.classList.add('active');
                btnFsfi.classList.remove('active');
            } else {
                tabFsfi.classList.remove('hidden');
                tabThm.classList.add('hidden');
                btnFsfi.classList.add('active');
                btnThm.classList.remove('active');
            }
        }

        let nombrePacienteGlobal = "Paciente";

        function generarInformeApp() {
            const nombre = document.getElementById('nombre').value || 'Paciente No Registrada';
            nombrePacienteGlobal = nombre.replace(/ /g, "_");
            const edad = parseInt(document.getElementById('edad').value) || '__';
            const fur = document.getElementById('fur').value || '//_____';
            const etapa = document.getElementById('etapa').value;

            let somatico = 0; [...document.querySelectorAll('.mrs-s')].forEach(i => somatico += parseInt(i.value));
            let psicologico = 0; [...document.querySelectorAll('.mrs-p')].forEach(i => psicologico += parseInt(i.value));
            let urogenital = 0; [...document.querySelectorAll('.mrs-u')].forEach(i => urogenital += parseInt(i.value));
            let totalMRS = somatico + psicologico + urogenital;

            let interpS = somatico <= 4 ? 'Leve' : (somatico <= 8 ? 'Moderado' : 'Severo');
            let interpP = psicologico <= 3 ? 'Leve' : (psicologico <= 6 ? 'Moderado' : 'Severo');
            let interpU = urogenital <= 3 ? 'Leve' : (urogenital <= 6 ? 'Moderado' : 'Severo');

            let interpTotalMRS = 'Leves';
            if (totalMRS >= 9 && totalMRS <= 14) interpTotalMRS = 'Moderados leves';
            else if (totalMRS >= 15 && totalMRS <= 20) interpTotalMRS = 'Moderados severos';
            else if (totalMRS > 20) interpTotalMRS = 'Severos';

            let pctS = Math.round((somatico / 16) * 100) || 0;
            let pctP = Math.round((psicologico / 12) * 100) || 0;
            let pctU = Math.round((urogenital / 12) * 100) || 0;

            let maxPct = Math.max(pctS, pctP, pctU);
            let domPred = "Ninguno";
            let analisisDom = "Sin prevalencia marcada.";

            if (maxPct > 0) {
                if (maxPct === pctS) { domPred = "Somático"; analisisDom = "SINTOMATOLOGÍA VASOMOTORA Y OSTEOMUSCULAR PREDOMINANTE. Indicación preferente de THM sistémica."; }
                else if (maxPct === pctP) { domPred = "Psicológico"; analisisDom = "Afectación anímica prevalente. Descartar origen psicógeno independiente de la transición."; }
                else if (maxPct === pctU) { domPred = "Urogenital"; analisisDom = "SÍNDROME GENITOURINARIO (SGUM) DOMINANTE. Evaluar THM tópica o sistémica según severidad."; }
            }

            const bDia = parseInt(document.getElementById('bochornos-dia').value) || 0;
            const bImp = parseInt(document.getElementById('bochornos-impacto').value) || 0;
            let interpImp = bImp <= 3 ? 'Leve' : (bImp <= 6 ? 'Moderado' : 'Severo');

            const sudor = document.getElementById('sint-sudor').checked ? 'Sí' : 'No';
            const noche = document.getElementById('sint-noche').checked ? 'Sí' : 'No';
            const act = document.getElementById('sint-act').checked ? 'Sí' : 'No';
            const ropa = document.getElementById('sint-ropa').checked ? 'Sí' : 'No';

            let absCount = 0; [...document.querySelectorAll('.cx-absoluta')].forEach(c => { if(c.checked) absCount++; });
            const absText = absCount > 0 ? 'ALERTA: Contraindicación absoluta presente.' : 'Ninguna';
            const relText = document.getElementById('cx-coronaria').checked ? 'Enfermedad coronaria activa (Evaluación por Cardiología)' : 'Ninguna';

            let rCardio = 0; [...document.querySelectorAll('.rf-cardio')].forEach(c => { if(c.checked) rCardio += parseInt(c.value); });
            let rTrombo = 0; [...document.querySelectorAll('.rf-trombo')].forEach(c => { if(c.checked) rTrombo += parseInt(c.value); });
            let rMama = 0; [...document.querySelectorAll('.rf-mama')].forEach(c => { if(c.checked) rMama += parseInt(c.value); });
            let rTotal = rCardio + rTrombo + rMama;
            let interpRiesgo = rTotal <= 2 ? 'RIESGO BAJO' : (rTotal <= 5 ? 'RIESGO INTERMEDIO' : 'RIESGO ALTO');

            let sitEsp = []; [...document.querySelectorAll('.sit-esp')].forEach(c => { if(c.checked) sitEsp.push(c.value); });
            let sitEspText = sitEsp.length > 0 ? sitEsp.join(', ') : 'Ninguna';
            const pref = document.getElementById('preferencia').value;

            let indPuntos = 0;
            if (edad < 60 || etapa === 'Posmenopausia <10 años') indPuntos++;
            if (totalMRS >= 9) indPuntos++;
            if (bDia >= 3) indPuntos++;
            if (bImp >= 4) indPuntos++;
            if (absCount === 0) indPuntos++;
            if (interpRiesgo === 'RIESGO BAJO' || interpRiesgo === 'RIESGO INTERMEDIO') indPuntos++;
            if (document.getElementById('se-osteo').checked) indPuntos++;
            if (document.getElementById('se-precoz').checked || (edad > 0 && edad < 40)) indPuntos++;

            let interpInd = 'NO HORMONAL';
            let recFinal = 'Priorizar manejo no hormonal y modificaciones de estilo de vida.';

            if (indPuntos >= 7) { interpInd = 'CANDIDATA IDEAL a THM'; recFinal = 'Indicar THM sistémica. Los beneficios superan ampliamente a los riesgos.'; }
            else if (indPuntos >= 5) { interpInd = 'CANDIDATA CLARA a THM'; recFinal = 'Indicar THM. Evaluar idoneidad de tipo y vía según comorbilidades.'; }
            else if (indPuntos >= 3) { interpInd = 'INDIVIDUALIZAR'; recFinal = 'Ponderar minuciosamente relación riesgo/beneficio con la paciente.'; }

            if (absCount > 0) {
                interpInd = 'NO HORMONAL (CONTRAINDICACIÓN ABSOLUTA)';
                recFinal = 'CRÍTICO: THM Sistémica totalmente CONTRAINDICADA. Preferir alternativas no hormonales o estrógenos locales si se limita a síntomas genitourinarios.';
            } else {
                if (document.getElementById('se-migrana').checked) recFinal += '\\n* Paciente con Migraña con aura: Prescribir exclusivamente VÍA TRANSDÉRMICA.';
                if (sitEsp.includes('Endometriosis') || sitEsp.includes('Adenomiosis')) recFinal += '\\n* Antecedente de Endometriosis/Adenomiosis: Utilizar ESQUEMA COMBINADO CONTINUO o DIU Mirena.';
            }

            const informeTexto = `===========================================================
INFORME DE EVALUACIÓN MENOPÁUSICA - Protocolo Ronald v2.0
Desarrollo Clínico: Dr. Ronald | Motor: Gemini AI
===========================================================
Paciente: ${nombre} | Edad: ${edad} años | FUR: ${fur}
Etapa: ${etapa}

1. ESCALA MRS COMPLETA
   Dominio Somático: ${somatico}/16 → ${interpS}
   Dominio Psicológico: ${psicologico}/12 → ${interpP}
   Dominio Urogenital: ${urogenital}/12 → ${interpU}
   Puntaje TOTAL: ${totalMRS}/40 → ${interpTotalMRS}

2. ANÁLISIS POR DOMINIO
   ${domPred === 'Somático' ? '[X]' : '[ ]'} Somático predominante (${pctS}% del máx): ${domPred === 'Somático' ? analisisDom : 'No prevalente.'}
   ${domPred === 'Psicológico' ? '[X]' : '[ ]'} Psicológico predominante (${pctP}% del máx): ${domPred === 'Psicológico' ? analisisDom : 'No prevalente.'}
   ${domPred === 'Urogenital' ? '[X]' : '[ ]'} Urogenital predominante (${pctU}% del máx): ${domPred === 'Urogenital' ? analisisDom : 'No prevalente.'}

3. BOCHORNOS
   Episodios/día: ${bDia} | Impacto: ${bImp}/10 → ${interpImp}
   Sudoración: ${sudor}              | Despierta por noche: ${noche}
   Interrumpe actividades: ${act}  | Debe cambiarse de ropa: ${ropa}

4. CONTRANDICACIONES
   Absolutas: ${absText}
   Relativas: ${relText}

5. RIESGOS PONDERADOS
   Cardiovascular: ${rCardio} pts
   Tromboembólico: ${rTrombo} pts
   Cáncer mama: ${rMama} pts
   RIESGO TOTAL: ${rTotal} pts → ${interpRiesgo}

6. SITUACIONES ESPECIALES
   ${sitEspText}

7. PREFERENCIA DE LA PACIENTE
   ${pref}

8. PUNTAJE DE INDICACIÓN (8 criterios)
   Puntaje: ${indPuntos}/8 → ${interpInd}
===========================================================
RECOMENDACIÓN FINAL:
${recFinal}
===========================================================`;

            document.getElementById('rawTextInforme').value = informeTexto;
            document.getElementById('pdfView').innerHTML = informeTexto.replace(/\\n/g, '<br>').replace(/ /g, '&nbsp;');
            document.getElementById('seccion-resultado').classList.remove('hidden');
            document.getElementById('seccion-resultado').scrollIntoView({ behavior: 'smooth' });
        }

        function copiarTextoInforme() {
            const raw = document.getElementById('rawTextInforme');
            raw.select();
            document.execCommand('copy');
            alert('¡Informe copiado al portapapeles!');
        }

        function exportarPDF() {
            const el = document.getElementById('pdfView');
            const opt = {
                margin:       12,
                filename:     `Protocolo_Ronald_${nombrePacienteGlobal}.pdf`,
                image:        { type: 'jpeg', quality: 0.98 },
                html2canvas:  { scale: 2 },
                jsPDF:        { unit: 'mm', format: 'letter', orientation: 'portrait' }
            };
            html2pdf().set(opt).from(el).save();
        }

        const DOMAINS_SPEC = [
            { id: "desire", name: "Deseo", questions: [1, 2], factor: 0.6 },
            { id: "arousal", name: "Excitación", questions: [3, 4, 5, 6], factor: 0.3 },
            { id: "lubrication", name: "Lubricación", questions: [7, 8, 9, 10], factor: 0.3 },
            { id: "orgasm", name: "Orgasmo", questions: [11, 12, 13], factor: 0.4 },
            { id: "satisfaction", name: "Satisfacción", questions: [14, 15, 16], factor: 0.4 },
            { id: "pain", name: "Dolor Coital", questions: [17, 18, 19], factor: 0.4 }
        ];

        const QUESTIONS_DATABASE = [
            { id: 1, domain: "desire", question: "1. ¿Con qué frecuencia sintió deseo o interés sexual?", options: [{value:5,label:"Casi siempre o siempre"},{value:4,label:"La mayoría de las veces"},{value:3,label:"A veces"},{value:2,label:"Pocas veces"},{value:1,label:"Casi nunca o nunca"}] },
            { id: 2, domain: "desire", question: "2. ¿Cómo calificaría su nivel de deseo o interés sexual?", options: [{value:5,label:"Muy alto"},{value:4,label:"Alto"},{value:3,label:"Moderado"},{value:2,label:"Bajo"},{value:1,label:"Muy bajo o nulo"}] },
            { id: 3, domain: "arousal", question: "3. ¿Con qué frecuencia se sintió sexualmente excitada durante la actividad sexual?", options: [{value:0,label:"No hubo actividad sexual"},{value:5,label:"Casi siempre o siempre"},{value:4,label:"La mayoría de las veces"},{value:3,label:"A veces"},{value:2,label:"Pocas veces"},{value:1,label:"Casi nunca o nunca"}] },
            { id: 4, domain: "arousal", question: "4. ¿Cómo calificaría su nivel de excitación sexual durante la actividad sexual?", options: [{value:0,label:"No hubo actividad sexual"},{value:5,label:"Muy alto"},{value:4,label:"Alto"},{value:3,label:"Moderado"},{value:2,label:"Bajo"},{value:1,label:"Muy bajo o nulo"}] },
            { id: 5, domain: "arousal", question: "5. ¿Con qué frecuencia se sintió satisfecha con su nivel de excitación durante la actividad sexual?", options: [{value:0,label:"No hubo actividad sexual"},{value:5,label:"Casi siempre o siempre"},{value:4,label:"La mayoría de las veces"},{value:3,label:"A veces"},{value:2,label:"Pocas veces"},{value:1,label:"Casi nunca o nunca"}] },
            { id: 6, domain: "arousal", question: "6. ¿Con qué frecuencia se sintió confiada en lograr la excitación sexual durante la actividad sexual?", options: [{value:0,label:"No hubo actividad sexual"},{value:5,label:"Casi siempre o siempre"},{value:4,label:"La mayoría de las veces"},{value:3,label:"A veces"},{value:2,label:"Pocas veces"},{value:1,label:"Casi nunca o nunca"}] },
            { id: 7, domain: "lubrication", question: "7. ¿Con qué frecuencia se lubricó ('se mojó') durante la actividad sexual?", options: [{value:0,label:"No hubo actividad sexual"},{value:5,label:"Casi siempre o siempre"},{value:4,label:"La mayoría de las veces"},{value:3,label:"A veces"},{value:2,label:"Pocas veces"},{value:1,label:"Casi nunca o nunca"}] },
            { id: 8, domain: "lubrication", question: "8. ¿Cómo calificaría su dificultad para lograr la lubricación durante la actividad sexual?", options: [{value:0,label:"No hubo actividad sexual"},{value:1,label:"Mucho o extremadamente difícil"},{value:2,label:"Muy difícil"},{value:3,label:"Difícil"},{value:4,label:"Un poco difícil"},{value:5,label:"Nada difícil"}] },
            { id: 9, domain: "lubrication", question: "9. ¿Con qué frecuencia mantuvo la lubricación hasta el final de la actividad sexual?", options: [{value:0,label:"No hubo actividad sexual"},{value:5,label:"Casi siempre o siempre"},{value:4,label:"La mayoría de las veces"},{value:3,label:"A veces"},{value:2,label:"Pocas veces"},{value:1,label:"Casi nunca o nunca"}] },
            { id: 10, domain: "lubrication", question: "10. ¿Cómo calificaría su dificultad para mantener la lubricación hasta el final de la actividad sexual?", options: [{value:0,label:"No hubo actividad sexual"},{value:1,label:"Mucho o extremadamente difícil"},{value:2,label:"Muy difícil"},{value:3,label:"Difícil"},{value:4,label:"Un poco difícil"},{value:5,label:"Nada difícil"}] },
            { id: 11, domain: "orgasm", question: "11. ¿Con qué frecuencia llegó al orgasmo (clímax) durante la actividad sexual?", options: [{value:0,label:"No hubo actividad sexual"},{value:5,label:"Casi siempre o siempre"},{value:4,label:"La mayoría de las veces"},{value:3,label:"A veces"},{value:2,label:"Pocas veces"},{value:1,label:"Casi nunca o nunca"}] },
            { id: 12, domain: "orgasm", question: "12. ¿Cómo calificaría su dificultad para alcanzar el orgasmo durante la actividad sexual?", options: [{value:0,label:"No hubo actividad sexual"},{value:1,label:"Mucho o extremadamente difícil"},{value:2,label:"Muy difícil"},{value:3,label:"Difícil"},{value:4,label:"Un poco difícil"},{value:5,label:"Nada difícil"}] },
            { id: 13, domain: "orgasm", question: "13. ¿Qué tan satisfecha estuvo con su capacidad para alcanzar el orgasmo durante la actividad sexual?", options: [{value:0,label:"No hubo actividad sexual"},{value:5,label:"Muy satisfecha"},{value:4,label:"Moderadamente satisfecha"},{value:3,label:"Ni satisfecha ni insatisfecha"},{value:2,label:"Moderadamente insatisfecha"},{value:1,label:"Muy insatisfecha"}] },
            { id: 14, domain: "satisfaction", question: "14. ¿Qué tan satisfecha estuvo con la cercanía emocional entre usted y su pareja durante la actividad sexual?", options: [{value:0,label:"No hubo actividad sexual"},{value:5,label:"Muy satisfecha"},{value:4,label:"Moderadamente satisfecha"},{value:3,label:"Ni satisfecha ni insatisfecha"},{value:2,label:"Moderadamente insatisfecha"},{value:1,label:"Muy insatisfecha"}] },
            { id: 15, domain: "satisfaction", question: "15. ¿Qué tan satisfecha estuvo con su relación sexual con su pareja?", options: [{value:5,label:"Muy satisfecha"},{value:4,label:"Moderadamente satisfecha"},{value:3,label:"Ni satisfecha ni insatisfecha"},{value:2,label:"Moderadamente insatisfecha"},{value:1,label:"Muy insatisfecha"}] },
            { id: 16, domain: "satisfaction", question: "16. ¿Qué tan satisfecha estuvo con su vida sexual en general?", options: [{value:5,label:"Muy satisfecha"},{value:4,label:"Moderadamente satisfecha"},{value:3,label:"Ni satisfecha ni insatisfecha"},{value:2,label:"Moderadamente insatisfecha"},{value:1,label:"Muy insatisfecha"}] },
            { id: 17, domain: "pain", question: "17. ¿Con qué frecuencia experimentó dolor o malestar durante la penetración vaginal?", options: [{value:0,label:"No hubo penetración"},{value:1,label:"Casi siempre o siempre"},{value:2,label:"La mayoría de las veces"},{value:3,label:"A veces"},{value:4,label:"Pocas veces"},{value:5,label:"Casi nunca o nunca"}] },
            { id: 18, domain: "pain", question: "18. ¿Con qué frecuencia experimentó dolor o malestar después de la penetración vaginal?", options: [{value:0,label:"No hubo penetración"},{value:1,label:"Casi siempre o siempre"},{value:2,label:"La mayoría de las veces"},{value:3,label:"A veces"},{value:4,label:"Pocas veces"},{value:5,label:"Casi nunca o nunca"}] },
            { id: 19, domain: "pain", question: "19. ¿Cómo calificaría el nivel de dolor o malestar durante o después de la penetración vaginal?", options: [{value:0,label:"No hubo penetración"},{value:1,label:"Muy alto o insoportable"},{value:2,label:"Alto"},{value:3,label:"Moderado"},{value:4,label:"Bajo"},{value:5,label:"Muy bajo o nulo"}] }
        ];

        let state = { responses: {}, postmenopause: true, distress: true };

        function renderQuestions() {
            const formContainer = document.getElementById('questions-form');
            formContainer.innerHTML = '';

            DOMAINS_SPEC.forEach(domain => {
                const domainQuestions = QUESTIONS_DATABASE.filter(q => q.domain === domain.id);
                const domainCard = document.createElement('div');
                domainCard.className = "bg-white rounded-2xl border border-slate-200 shadow-sm overflow-hidden mb-6";
                
                const cardHeader = document.createElement('div');
                cardHeader.className = "bg-slate-50 border-b border-slate-200 p-4 flex justify-between items-center";
                cardHeader.innerHTML = `
                    <div class="flex items-center gap-2">
                        <span class="w-2.5 h-2.5 rounded-full bg-teal-600"></span>
                        <h4 class="font-bold text-slate-800 text-sm md:text-base">Dominio: ${domain.name}</h4>
                    </div>
                    <span class="text-[10px] bg-teal-50 text-teal-700 font-bold px-2 py-0.5 rounded-md uppercase tracking-wider">Peso: x${domain.factor}</span>
                `;
                domainCard.appendChild(cardHeader);

                const cardBody = document.createElement('div');
                cardBody.className = "p-4 md:p-6 space-y-6";

                domainQuestions.forEach(q => {
                    const qElement = document.createElement('div');
                    qElement.className = "space-y-3";
                    qElement.innerHTML = `
                        <p class="text-xs md:text-sm font-semibold text-slate-700 leading-relaxed">${q.question}</p>
                        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-1 xl:grid-cols-2 gap-2" id="options-group-${q.id}"></div>
                    `;
                    const optionsGroup = qElement.querySelector(`#options-group-${q.id}`);
                    
                    q.options.forEach(opt => {
                        const optButton = document.createElement('button');
                        optButton.type = "button";
                        optButton.id = `q-${q.id}-opt-${opt.value}`;
                        optButton.className = "flex items-center justify-between p-3 rounded-xl border border-slate-200 text-left text-xs hover:border-teal-500 hover:bg-slate-50 transition-all focus:outline-none focus:ring-2 focus:ring-teal-500";
                        optButton.innerHTML = `
                            <span class="text-slate-600 font-medium">${opt.label}</span>
                            <span class="bg-slate-100 text-slate-500 font-bold text-[10px] px-2 py-1 rounded-md shrink-0 ml-2">Puntos: ${opt.value}</span>
                        `;
                        optButton.addEventListener('click', () => selectOption(q.id, opt.value));
                        optionsGroup.appendChild(optButton);
                    });
                    cardBody.appendChild(qElement);
                });
                domainCard.appendChild(cardBody);
                formContainer.appendChild(domainCard);
            });
        }

        function selectOption(questionId, value) {
            state.responses[questionId] = value;
            const questionData = QUESTIONS_DATABASE.find(q => q.id === questionId);
            
            questionData.options.forEach(opt => {
                const btn = document.getElementById(`q-${questionId}-opt-${opt.value}`);
                if (btn) {
                    btn.className = "flex items-center justify-between p-3 rounded-xl border border-slate-200 text-left text-xs hover:border-teal-500 hover:bg-slate-50 transition-all focus:outline-none focus:ring-2 focus:ring-teal-500";
                    const badge = btn.querySelector('span:last-child');
                    if (badge) badge.className = "bg-slate-100 text-slate-500 font-bold text-[10px] px-2 py-1 rounded-md shrink-0 ml-2";
                }
            });

            const activeBtn = document.getElementById(`q-${questionId}-opt-${value}`);
            if (activeBtn) {
                activeBtn.className = "flex items-center justify-between p-3 rounded-xl border-2 border-teal-600 bg-teal-50/40 text-left text-xs transition-all focus:outline-none focus:ring-2 focus:ring-teal-500";
                const badge = activeBtn.querySelector('span:last-child');
                if (badge) badge.className = "bg-teal-600 text-white font-bold text-[10px] px-2 py-1 rounded-md shrink-0 ml-2";
            }
            calculateResults();
        }

        function calculateResults() {
            let totalWeightedScore = 0;
            let answeredCount = 0;
            const domainScores = {};

            DOMAINS_SPEC.forEach(domain => {
                let domainSum = 0;
                let domainAnswered = 0;

                domain.questions.forEach(qId => {
                    if (state.responses[qId] !== undefined) {
                        domainSum += state.responses[qId];
                        domainAnswered++;
                    }
                });

                const isDomainComplete = domainAnswered === domain.questions.length;
                const weighted = domainSum * domain.factor;
                domainScores[domain.id] = { sum: domainSum, weighted: weighted, isComplete: isDomainComplete };

                if (isDomainComplete) {
                    answeredCount += domainAnswered;
                    totalWeightedScore += weighted;
                }

                const scoreEl = document.getElementById(`score-${domain.id}`);
                const badgeEl = document.getElementById(`badge-${domain.id}`);
                
                if (scoreEl && badgeEl) {
                    scoreEl.textContent = weighted.toFixed(2);
                    if (isDomainComplete) {
                        if (domain.id === 'desire') {
                            badgeEl.textContent = weighted <= 3.3 ? "Deseo Bajo (TDSH)" : "Deseo Normal";
                            badgeEl.className = weighted <= 3.3 ? "text-[9px] mt-1.5 px-2 py-0.5 rounded font-bold bg-rose-500/20 text-rose-300 w-fit" : "text-[9px] mt-1.5 px-2 py-0.5 rounded font-bold bg-emerald-500/20 text-emerald-300 w-fit";
                        } else if (domain.id === 'pain') {
                            badgeEl.textContent = weighted <= 4.0 ? "Dispareunia Activa" : "Sin dolor limitante";
                            badgeEl.className = weighted <= 4.0 ? "text-[9px] mt-1.5 px-2 py-0.5 rounded font-bold bg-amber-500/20 text-amber-300 w-fit" : "text-[9px] mt-1.5 px-2 py-0.5 rounded font-bold bg-emerald-500/20 text-emerald-300 w-fit";
                        } else {
                            badgeEl.textContent = "Completo";
                            badgeEl.className = "text-[9px] mt-1.5 px-2 py-0.5 rounded font-bold bg-teal-500/20 text-teal-300 w-fit";
                        }
                    } else {
                        scoreEl.textContent = "0.00";
                        badgeEl.textContent = "Incompleto";
                        badgeEl.className = "text-[9px] mt-1.5 px-2 py-0.5 rounded font-bold bg-slate-700/50 text-slate-400 w-fit";
                    }
                }
            });

            const totalQuestionsCount = QUESTIONS_DATABASE.length;
            const progressPct = (answeredCount / totalQuestionsCount) * 100;
            document.getElementById('progress-bar').style.width = `${progressPct}%`;
            document.getElementById('progress-text').textContent = `${answeredCount} / ${totalQuestionsCount} Respondidas`;

            const scoreTotalEl = document.getElementById('score-total');
            if (scoreTotalEl) scoreTotalEl.textContent = totalWeightedScore.toFixed(2);

            const isPostmenopause = document.getElementById('chk-postmenopause').checked;
            const hasDistress = document.getElementById('chk-distress').checked;
            
            const verdictCard = document.getElementById('verdict-card');
            const verdictTitle = document.getElementById('verdict-title');
            const verdictBody = document.getElementById('verdict-body');

            const isAllAnswered = answeredCount === totalQuestionsCount;

            if (!isAllAnswered) {
                verdictCard.className = "p-4 rounded-xl border text-center transition-all duration-300 bg-slate-800 text-slate-300 border-slate-700";
                verdictTitle.textContent = "Evaluando Datos...";
                verdictBody.textContent = `Por favor, complete las ${totalQuestionsCount - answeredCount} preguntas pendientes.`;
            } else {
                const desireScore = domainScores['desire'].weighted;
                const painScore = domainScores['pain'].weighted;

                if (!isPostmenopause || !hasDistress) {
                    verdictCard.className = "p-4 rounded-xl border text-center transition-all duration-300 bg-rose-950/40 text-rose-300 border-rose-900";
                    verdictTitle.textContent = "No Candidata (Requisitos Excluidos)";
                    verdictBody.textContent = "La terapia con testosterona solo se indica bajo el Consenso Global en pacientes posmenopáusicas con malestar clínico manifiesto.";
                } else if (painScore <= 4.0) {
                    verdictCard.className = "p-4 rounded-xl border text-center transition-all duration-300 bg-amber-950/40 text-amber-300 border-amber-900";
                    verdictTitle.textContent = "Tratar Dispareunia Primero";
                    verdictBody.textContent = `La paciente tiene dolor coital significativo (${painScore.toFixed(2)} pts). Priorice resolver la atrofia con estrógenos tópicos locales antes de evaluar testosterona.`;
                } else if (desireScore > 3.3) {
                    verdictCard.className = "p-4 rounded-xl border text-center transition-all duration-300 bg-rose-950/40 text-rose-300 border-rose-900";
                    verdictTitle.textContent = "No Candidata (Deseo Conservado)";
                    verdictBody.textContent = `El subtotal de deseo (${desireScore.toFixed(2)} pts) es mayor al límite diagnóstico de ≤ 3.3. No califica para TDSH.`;
                } else {
                    verdictCard.className = "p-4 rounded-xl border text-center transition-all duration-300 bg-emerald-950/40 text-emerald-300 border-emerald-900";
                    verdictTitle.textContent = "✓ Candidata Apta para Testosterona";
                    verdictBody.textContent = `Cumple criterios: Deseo bajo (${desireScore.toFixed(2)} pts), sin dolor coital limitante y estatus posmenopáusico con malestar. Solicitar laboratorios pre-tratamiento.`;
                }
            }

            generateClinicalNote(domainScores, totalWeightedScore, isAllAnswered, isPostmenopause, hasDistress);
        }

        function generateClinicalNote(domainScores, totalScore, isComplete, isPostmenopause, hasDistress) {
            const noteEl = document.getElementById('clinical-note');
            if (!noteEl) return;

            if (!isComplete) {
                noteEl.value = "Complete el test completo con la paciente para estructurar la nota médica automática.";
                return;
            }

            const dateStr = new Date().toLocaleDateString('es-ES');
            const desireVal = domainScores['desire'].weighted;
            const arousalVal = domainScores['arousal'].weighted;
            const lubVal = domainScores['lubrication'].weighted;
            const orgVal = domainScores['orgasm'].weighted;
            const satVal = domainScores['satisfaction'].weighted;
            const painVal = domainScores['pain'].weighted;

            let conclusionStr = "";
            if (!isPostmenopause || !hasDistress) {
                conclusionStr = "No candidata a terapia androgénica (No cumple criterios basales de posmenopausia y distress).";
            } else if (painVal <= 4.0) {
                conclusionStr = "No apta para testosterona en este momento. Se sospecha dispareunia / atrofia urogenital severa como causa de la pérdida del deseo. Tratar primero la mucosa local.";
            } else if (desireVal > 3.3) {
                conclusionStr = "No cumple criterios de TDSH (Deseo sexual conservado según FSFI).";
            } else {
                conclusionStr = "Apta para terapia con Testosterona Transdérmica Femenina (1/10 dosis de varón). Solicitar testosterona total, SHBG, perfil hepático y mamografía vigente antes de iniciar.";
            }

            noteEl.value = `REPORTE CLÍNICO - ÍNDICE DE FUNCIÓN SEXUAL FEMENINA (FSFI)
======================================================
Fecha de Evaluación: ${dateStr}
Criterio Clínico Basal: ${isPostmenopause ? 'Posmenopáusica' : 'Premenopáusica'} | Distress Sexual: ${hasDistress ? 'SÍ' : 'NO'}

SUBTOTALES DE DOMINIOS FSFI:
------------------------------------------------------
- DESEO: ${desireVal.toFixed(2)} pts  (Umbral de sospecha TDSH: <= 3.3)
- EXCITACIÓN: ${arousalVal.toFixed(2)} pts
- LUBRICACIÓN: ${lubVal.toFixed(2)} pts
- ORGASMO: ${orgVal.toFixed(2)} pts
- SATISFACCIÓN: ${satVal.toFixed(2)} pts
- DOLOR COITAL: ${painVal.toFixed(2)} pts  (Disfunción por dispareunia: <= 4.0)

PUNTAJE GLOBAL FSFI: ${totalScore.toFixed(2)} pts  (Disfunción si <= 26.55)

DIAGNÓSTICO Y PLAN DE MANEJO RECOMENDADO:
------------------------------------------------------
${conclusionStr}

------------------------------------------------------
Co-diseñado para la práctica clínica por:
Dr. Ronald (Ginecología y Obstetricia) & Gemini AI`;
        }

        function copyClinicalNote() {
            const textarea = document.getElementById('clinical-note');
            textarea.select();
            textarea.setSelectionRange(0, 99999);
            try {
                document.execCommand('copy');
                const msg = document.getElementById('copy-success-msg');
                msg.classList.remove('hidden');
                setTimeout(() => msg.classList.add('hidden'), 3000);
            } catch (err) {
                console.error("Error al copiar nota: ", err);
            }
        }

        function resetAll() {
            state.responses = {};
            document.getElementById('chk-postmenopause').checked = true;
            document.getElementById('chk-distress').checked = true;
            renderQuestions();
            calculateResults();
            window.scrollTo({ top: 0, behavior: 'smooth' });
        }

        window.onload = function() {
            renderQuestions();
            document.getElementById('chk-postmenopause').addEventListener('change', calculateResults);
            document.getElementById('chk-distress').addEventListener('change', calculateResults);
            calculateResults();
        };
    </script>
</body>
</html>
"""

# Renderizar en la aplicación Streamlit
components.html(html_code, height=1800, scrolling=True)
import streamlit.components.v1 as components

# Configuración de página completa en Streamlit
st.set_page_config(
    page_title="Plataforma Integrada de Salud Menopáusica",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Renderizado del HTML/CSS/JS completo
html_code = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Plataforma Integrada de Salud Menopáusica - Dr. Ronald & Gemini AI</title>
    <!-- Tailwind CSS -->
    <script src="https://cdn.tailwindcss.com"></script>
    <!-- FontAwesome Iconos -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <!-- html2pdf.js -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/html2pdf.js/0.10.1/html2pdf.bundle.min.js"></script>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
    <style>
        body { font-family: 'Inter', sans-serif; }
        ::-webkit-scrollbar { width: 8px; }
        ::-webkit-scrollbar-track { background: #f1f5f9; }
        ::-webkit-scrollbar-thumb { background: #cbd5e1; border-radius: 4px; }
        ::-webkit-scrollbar-thumb:hover { background: #94a3b8; }
        .tab-btn.active {
            border-bottom-color: #6366f1;
            color: #4f46e5;
            background-color: #ffffff;
        }
    </style>
</head>
<body class="bg-slate-100 text-slate-800 min-h-screen pb-12">

    <!-- BARRA DE NAVEGACIÓN PRINCIPAL (PESTAÑAS) -->
    <header class="bg-slate-900 text-white sticky top-0 z-50 shadow-md">
        <div class="max-w-7xl mx-auto px-4 flex flex-col sm:flex-row justify-between items-center gap-2">
            <div class="py-3 flex items-center gap-3">
                <span class="bg-indigo-600 text-white text-xs font-bold px-2.5 py-1 rounded-md uppercase tracking-wider">Suite Clínica v2.0</span>
                <h1 class="font-extrabold text-base md:text-lg tracking-tight">Evaluación Integral en Menopausia</h1>
            </div>
            
            <nav class="flex space-x-2 text-xs md:text-sm font-semibold">
                <button id="btn-tab-thm" onclick="switchTab('thm')" class="tab-btn active px-4 py-3 border-b-4 border-transparent transition-all flex items-center gap-2 text-slate-300 hover:text-white">
                    <i class="fa-solid fa-notes-medical"></i> 1. Protocolo THM (MRS / Riesgos)
                </button>
                <button id="btn-tab-fsfi" onclick="switchTab('fsfi')" class="tab-btn px-4 py-3 border-b-4 border-transparent transition-all flex items-center gap-2 text-slate-300 hover:text-white">
                    <i class="fa-solid fa-heart-pulse"></i> 2. Test FSFI (TDSH / Testosterona)
                </button>
            </nav>
        </div>
    </header>

    <div class="max-w-7xl mx-auto px-4 py-6">

        <!-- MÓDULO 1: PROTOCOLO RONALD V2.0 - EVALUACIÓN THM -->
        <main id="tab-thm" class="block space-y-6">
            <div class="bg-gradient-to-r from-slate-900 via-indigo-950 to-slate-900 text-white rounded-2xl p-6 shadow-xl border border-indigo-500/20">
                <div class="flex flex-col md:flex-row justify-between items-center gap-4">
                    <div>
                        <div class="flex items-center gap-3">
                            <span class="bg-indigo-600 text-white text-xs font-bold px-3 py-1 rounded-full uppercase tracking-wider">v2.0 Actualizada</span>
                            <span class="text-xs text-indigo-300"><i class="fa-solid fa-microchip mr-1"></i> Powered by Gemini AI</span>
                        </div>
                        <h2 class="text-2xl md:text-3xl font-extrabold tracking-tight mt-2 text-white">PROTOCOLO RONALD v2.0</h2>
                        <p class="text-xs md:text-sm text-slate-300 mt-1">Evaluación Clínica Digitalizada de Terapia Hormonal Menopáusica (THM)</p>
                    </div>
                    <div class="text-right border-l-0 md:border-l border-indigo-800 pl-0 md:pl-6 text-xs text-slate-400 hidden sm:block">
                        <p class="font-semibold text-indigo-200">Co-Desarrollo Clínico - Tecnológico</p>
                        <p class="mt-0.5"><i class="fa-solid fa-user-doctor text-indigo-400 mr-1"></i> Autor: Dr. Ronald</p>
                        <p><i class="fa-solid fa-brain text-purple-400 mr-1"></i> Motor Clínico: Gemini AI Collaborator</p>
                    </div>
                </div>
            </div>

            <form id="appForm" class="space-y-6">
                <!-- PASO 1 -->
                <div class="bg-white rounded-xl shadow-md p-6 border border-slate-200">
                    <h3 class="text-base font-bold text-slate-900 flex items-center gap-2 mb-4 pb-2 border-b">
                        <i class="fa-solid fa-address-card text-indigo-600"></i> PASO 1: Confirmar Etapa Reproductiva
                    </h3>
                    <div class="grid grid-cols-1 md:grid-cols-4 gap-4 text-sm">
                        <div>
                            <label class="block font-semibold text-slate-700 mb-1">Nombre Completo</label>
                            <input type="text" id="nombre" placeholder="Nombre de la paciente" required class="w-full border border-slate-300 rounded-lg p-2.5 focus:ring-2 focus:ring-indigo-500 focus:outline-none">
                        </div>
                        <div>
                            <label class="block font-semibold text-slate-700 mb-1">Edad (Años)</label>
                            <input type="number" id="edad" placeholder="Ej. 52" required class="w-full border border-slate-300 rounded-lg p-2.5 focus:ring-2 focus:ring-indigo-500 focus:outline-none">
                        </div>
                        <div>
                            <label class="block font-semibold text-slate-700 mb-1">FUR (Fecha Última Regla)</label>
                            <input type="text" id="fur" placeholder="DD/MM/AAAA" class="w-full border border-slate-300 rounded-lg p-2.5 focus:ring-2 focus:ring-indigo-500 focus:outline-none">
                        </div>
                        <div>
                            <label class="block font-semibold text-slate-700 mb-1">Etapa Reproductiva</label>
                            <select id="etapa" class="w-full border border-slate-300 rounded-lg p-2.5 focus:ring-2 focus:ring-indigo-500 focus:outline-none bg-white">
                                <option value="Premenopausia">Premenopausia</option>
                                <option value="Perimenopausia">Perimenopausia</option>
                                <option value="Posmenopausia <10 años">Posmenopausia &lt; 10 años</option>
                                <option value="Posmenopausia ≥10 años">Posmenopausia &ge; 10 años</option>
                            </select>
                        </div>
                    </div>
                </div>

                <!-- PASO 2 -->
                <div class="bg-white rounded-xl shadow-md p-6 border border-slate-200">
                    <div class="flex justify-between items-center mb-4 pb-2 border-b">
                        <h3 class="text-base font-bold text-slate-900 flex items-center gap-2">
                            <i class="fa-solid fa-chart-simple text-indigo-600"></i> PASO 2: Escala MRS Completa (Validada)
                        </h3>
                        <span class="text-xs text-slate-500 font-medium">0 = Sin molestia | 4 = Muy severo</span>
                    </div>

                    <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
                        <div class="bg-amber-50/50 rounded-xl p-4 border border-amber-200/60">
                            <h4 class="text-xs font-bold uppercase tracking-wider text-amber-900 mb-3 flex items-center justify-between">
                                <span>Dominio Somático</span>
                                <span class="text-amber-700 bg-amber-100 px-2 py-0.5 rounded text-[10px]">Máx 16 pts</span>
                            </h4>
                            <div class="space-y-3 text-xs">
                                <div><label class="block text-slate-700 font-medium mb-1">1. Bochornos / Sofocos</label><select class="mrs-s w-full border border-amber-200 rounded-lg p-2 bg-white"><option value="0">0 - Ausente</option><option value="1">1 - Leve</option><option value="2">2 - Moderado</option><option value="3">3 - Severo</option><option value="4">4 - Muy severo</option></select></div>
                                <div><label class="block text-slate-700 font-medium mb-1">2. Trastornos del sueño</label><select class="mrs-s w-full border border-amber-200 rounded-lg p-2 bg-white"><option value="0">0 - Ausente</option><option value="1">1 - Leve</option><option value="2">2 - Moderado</option><option value="3">3 - Severo</option><option value="4">4 - Muy severo</option></select></div>
                                <div><label class="block text-slate-700 font-medium mb-1">3. Dolores osteomusculares</label><select class="mrs-s w-full border border-amber-200 rounded-lg p-2 bg-white"><option value="0">0 - Ausente</option><option value="1">1 - Leve</option><option value="2">2 - Moderado</option><option value="3">3 - Severo</option><option value="4">4 - Muy severo</option></select></div>
                                <div><label class="block text-slate-700 font-medium mb-1">4. Cansancio / Fatiga</label><select class="mrs-s w-full border border-amber-200 rounded-lg p-2 bg-white"><option value="0">0 - Ausente</option><option value="1">1 - Leve</option><option value="2">2 - Moderado</option><option value="3">3 - Severo</option><option value="4">4 - Muy severo</option></select></div>
                            </div>
                        </div>

                        <div class="bg-blue-50/50 rounded-xl p-4 border border-blue-200/60">
                            <h4 class="text-xs font-bold uppercase tracking-wider text-blue-900 mb-3 flex items-center justify-between">
                                <span>Dominio Psicológico</span>
                                <span class="text-blue-700 bg-blue-100 px-2 py-0.5 rounded text-[10px]">Máx 12 pts</span>
                            </h4>
                            <div class="space-y-3 text-xs">
                                <div><label class="block text-slate-700 font-medium mb-1">5. Depresión / Tristeza</label><select class="mrs-p w-full border border-blue-200 rounded-lg p-2 bg-white"><option value="0">0 - Ausente</option><option value="1">1 - Leve</option><option value="2">2 - Moderado</option><option value="3">3 - Severo</option><option value="4">4 - Muy severo</option></select></div>
                                <div><label class="block text-slate-700 font-medium mb-1">6. Irritabilidad / Mal humor</label><select class="mrs-p w-full border border-blue-200 rounded-lg p-2 bg-white"><option value="0">0 - Ausente</option><option value="1">1 - Leve</option><option value="2">2 - Moderado</option><option value="3">3 - Severo</option><option value="4">4 - Muy severo</option></select></div>
                                <div><label class="block text-slate-700 font-medium mb-1">7. Ansiedad / Tensión</label><select class="mrs-p w-full border border-blue-200 rounded-lg p-2 bg-white"><option value="0">0 - Ausente</option><option value="1">1 - Leve</option><option value="2">2 - Moderado</option><option value="3">3 - Severo</option><option value="4">4 - Muy severo</option></select></div>
                            </div>
                        </div>

                        <div class="bg-purple-50/50 rounded-xl p-4 border border-purple-200/60">
                            <h4 class="text-xs font-bold uppercase tracking-wider text-purple-900 mb-3 flex items-center justify-between">
                                <span>Dominio Urogenital</span>
                                <span class="text-purple-700 bg-purple-100 px-2 py-0.5 rounded text-[10px]">Máx 12 pts</span>
                            </h4>
                            <div class="space-y-3 text-xs">
                                <div><label class="block text-slate-700 font-medium mb-1">8. Sequedad vaginal</label><select class="mrs-u w-full border border-purple-200 rounded-lg p-2 bg-white"><option value="0">0 - Ausente</option><option value="1">1 - Leve</option><option value="2">2 - Moderado</option><option value="3">3 - Severo</option><option value="4">4 - Muy severo</option></select></div>
                                <div><label class="block text-slate-700 font-medium mb-1">9. Disfunción sexual</label><select class="mrs-u w-full border border-purple-200 rounded-lg p-2 bg-white"><option value="0">0 - Ausente</option><option value="1">1 - Leve</option><option value="2">2 - Moderado</option><option value="3">3 - Severo</option><option value="4">4 - Muy severo</option></select></div>
                                <div><label class="block text-slate-700 font-medium mb-1">10. Síntomas urinarios</label><select class="mrs-u w-full border border-purple-200 rounded-lg p-2 bg-white"><option value="0">0 - Ausente</option><option value="1">1 - Leve</option><option value="2">2 - Moderado</option><option value="3">3 - Severo</option><option value="4">4 - Muy severo</option></select></div>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- PASO 3 Y PASO 4 -->
                <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                    <div class="bg-white rounded-xl shadow-md p-6 border border-slate-200">
                        <h3 class="text-base font-bold text-slate-900 flex items-center gap-2 mb-4 pb-2 border-b">
                            <i class="fa-solid fa-fire text-orange-500"></i> PASO 3: Evaluación de Bochornos
                        </h3>
                        <div class="space-y-4 text-xs">
                            <div class="grid grid-cols-2 gap-3">
                                <div><label class="block font-semibold text-slate-700 mb-1">Episodios / día</label><input type="number" id="bochornos-dia" value="0" class="w-full border border-slate-300 rounded-lg p-2"></div>
                                <div><label class="block font-semibold text-slate-700 mb-1">Impacto (0 al 10)</label><input type="number" id="bochornos-impacto" min="0" max="10" value="0" class="w-full border border-slate-300 rounded-lg p-2"></div>
                            </div>
                            <div class="bg-slate-50 p-3 rounded-lg border border-slate-200 space-y-2">
                                <p class="font-bold text-slate-600 uppercase text-[10px]">Síntomas Asociados</p>
                                <div class="grid grid-cols-2 gap-2">
                                    <label class="flex items-center gap-2"><input type="checkbox" id="sint-sudor" class="rounded text-indigo-600"> <span>Sudoración</span></label>
                                    <label class="flex items-center gap-2"><input type="checkbox" id="sint-noche" class="rounded text-indigo-600"> <span>Despierta de noche</span></label>
                                    <label class="flex items-center gap-2"><input type="checkbox" id="sint-act" class="rounded text-indigo-600"> <span>Interrumpe rutina</span></label>
                                    <label class="flex items-center gap-2"><input type="checkbox" id="sint-ropa" class="rounded text-indigo-600"> <span>Cambia de ropa</span></label>
                                </div>
                            </div>
                        </div>
                    </div>

                    <div class="bg-red-50/40 rounded-xl shadow-md p-6 border border-red-200">
                        <h3 class="text-base font-bold text-red-900 flex items-center gap-2 mb-3 pb-2 border-b border-red-200">
                            <i class="fa-solid fa-ban text-red-600"></i> PASO 4: Contraindicaciones
                        </h3>
                        <p class="text-[11px] text-red-700 mb-3 font-medium">Marcar cualquiera detendrá automáticamente la indicación de THM sistémica:</p>
                        <div class="space-y-2 text-xs">
                            <label class="flex items-start gap-2 text-slate-800"><input type="checkbox" class="cx-absoluta mt-0.5 rounded text-red-600"> <span>Cáncer de mama (activo o previo)</span></label>
                            <label class="flex items-start gap-2 text-slate-800"><input type="checkbox" class="cx-absoluta mt-0.5 rounded text-red-600"> <span>Sangrado uterino no estudiado</span></label>
                            <label class="flex items-start gap-2 text-slate-800"><input type="checkbox" class="cx-absoluta mt-0.5 rounded text-red-600"> <span>TVP / TEP activa o reciente</span></label>
                            <label class="flex items-start gap-2 text-slate-800"><input type="checkbox" class="cx-absoluta mt-0.5 rounded text-red-600"> <span>IAM / ACV / AIT reciente (&lt; 6 meses)</span></label>
                            <label class="flex items-start gap-2 text-slate-800"><input type="checkbox" class="cx-absoluta mt-0.5 rounded text-red-600"> <span>Enfermedad hepática grave descompensada</span></label>
                            <label class="flex items-start gap-2 text-slate-800"><input type="checkbox" class="cx-absoluta mt-0.5 rounded text-red-600"> <span>Hiperplasia endometrial atípica no tratada</span></label>
                        </div>
                        <div class="mt-3 pt-2 border-t border-red-200/80 text-xs">
                            <label class="flex items-center gap-2 font-semibold text-slate-800"><input type="checkbox" id="cx-coronaria" class="rounded text-amber-600"> <span>⚠️ Relativa: Enfermedad coronaria activa</span></label>
                        </div>
                    </div>
                </div>

                <!-- PASO 5 -->
                <div class="bg-white rounded-xl shadow-md p-6 border border-slate-200">
                    <h3 class="text-base font-bold text-slate-900 flex items-center gap-2 mb-4 pb-2 border-b">
                        <i class="fa-solid fa-triangle-exclamation text-amber-500"></i> PASO 5: Factores de Riesgo (Ponderados)
                    </h3>
                    <div class="grid grid-cols-1 md:grid-cols-3 gap-4 text-xs">
                        <div class="bg-slate-50 p-3 rounded-lg border border-slate-200">
                            <h4 class="font-bold text-slate-800 border-b pb-1 mb-2">A. Cardiovascular</h4>
                            <div class="space-y-1.5">
                                <label class="flex items-center justify-between"><span>HTA no controlada (+2)</span><input type="checkbox" value="2" class="rf-cardio rounded text-indigo-600"></label>
                                <label class="flex items-center justify-between"><span>Diabetes (+1)</span><input type="checkbox" value="1" class="rf-cardio rounded text-indigo-600"></label>
                                <label class="flex items-center justify-between"><span>Dislipidemia (+1)</span><input type="checkbox" value="1" class="rf-cardio rounded text-indigo-600"></label>
                                <label class="flex items-center justify-between"><span>IMC &ge; 30 (+2)</span><input type="checkbox" value="2" class="rf-cardio rounded text-indigo-600"></label>
                                <label class="flex items-center justify-between"><span>Tabaquismo activo (+2)</span><input type="checkbox" value="2" class="rf-cardio rounded text-indigo-600"></label>
                                <label class="flex items-center justify-between"><span>Enfermedad CV (+1)</span><input type="checkbox" value="1" class="rf-cardio rounded text-indigo-600"></label>
                            </div>
                        </div>
                        <div class="bg-slate-50 p-3 rounded-lg border border-slate-200">
                            <h4 class="font-bold text-slate-800 border-b pb-1 mb-2">B. Tromboembólico</h4>
                            <div class="space-y-1.5">
                                <label class="flex items-center justify-between"><span>TVP / TEP previa (+3)</span><input type="checkbox" value="3" class="rf-trombo rounded text-indigo-600"></label>
                                <label class="flex items-center justify-between"><span>Trombofilia conocida (+3)</span><input type="checkbox" value="3" class="rf-trombo rounded text-indigo-600"></label>
                                <label class="flex items-center justify-between"><span>IMC &ge; 30 (+2)</span><input type="checkbox" value="2" class="rf-trombo rounded text-indigo-600"></label>
                                <label class="flex items-center justify-between"><span>Várices importantes (+1)</span><input type="checkbox" value="1" class="rf-trombo rounded text-indigo-600"></label>
                                <label class="flex items-center justify-between"><span>Fam. 1er grado Trombosis (+1)</span><input type="checkbox" value="1" class="rf-trombo rounded text-indigo-600"></label>
                            </div>
                        </div>
                        <div class="bg-slate-50 p-3 rounded-lg border border-slate-200">
                            <h4 class="font-bold text-slate-800 border-b pb-1 mb-2">C. Cáncer de Mama</h4>
                            <div class="space-y-1.5">
                                <label class="flex items-center justify-between"><span>Antecedente personal (+3)</span><input type="checkbox" value="3" class="rf-mama rounded text-indigo-600"></label>
                                <label class="flex items-center justify-between"><span>BRCA 1/2 (+3)</span><input type="checkbox" value="3" class="rf-mama rounded text-indigo-600"></label>
                                <label class="flex items-center justify-between"><span>Familiar 1er grado (+2)</span><input type="checkbox" value="2" class="rf-mama rounded text-indigo-600"></label>
                                <label class="flex items-center justify-between"><span>Hiperplasia atípica (+3)</span><input type="checkbox" value="3" class="rf-mama rounded text-indigo-600"></label>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- PASO 6 Y 7 -->
                <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                    <div class="bg-white rounded-xl shadow-md p-6 border border-slate-200">
                        <h3 class="text-base font-bold text-slate-900 flex items-center gap-2 mb-3 pb-2 border-b">
                            <i class="fa-solid fa-sliders text-indigo-600"></i> PASO 6: Individualización
                        </h3>
                        <div class="grid grid-cols-2 gap-2 text-xs">
                            <label class="flex items-center gap-1.5"><input type="checkbox" value="Endometriosis" class="sit-esp rounded"> <span>Endometriosis</span></label>
                            <label class="flex items-center gap-1.5"><input type="checkbox" value="Adenomiosis" class="sit-esp rounded"> <span>Adenomiosis</span></label>
                            <label class="flex items-center gap-1.5"><input type="checkbox" value="Miomas" class="sit-esp rounded"> <span>Miomas</span></label>
                            <label class="flex items-center gap-1.5"><input type="checkbox" value="Migraña con aura" class="sit-esp rounded" id="se-migrana"> <span>Migraña con aura</span></label>
                            <label class="flex items-center gap-1.5"><input type="checkbox" value="Lupus" class="sit-esp rounded"> <span>Lupus</span></label>
                            <label class="flex items-center gap-1.5"><input type="checkbox" value="Artritis reumatoide" class="sit-esp rounded"> <span>Artritis reumatoide</span></label>
                            <label class="flex items-center gap-1.5"><input type="checkbox" value="Osteoporosis" class="sit-esp rounded" id="se-osteo"> <span>Osteoporosis</span></label>
                            <label class="flex items-center gap-1.5"><input type="checkbox" value="Menopausia precoz" class="sit-esp rounded" id="se-precoz"> <span>Menopausia precoz</span></label>
                        </div>
                    </div>
                    <div class="bg-white rounded-xl shadow-md p-6 border border-slate-200">
                        <h3 class="text-base font-bold text-slate-900 flex items-center gap-2 mb-3 pb-2 border-b">
                            <i class="fa-solid fa-comments text-indigo-600"></i> PASO 7: Preferencia Paciente
                        </h3>
                        <div class="text-xs space-y-3">
                            <label class="block font-medium text-slate-700">Deseo expreso de la paciente:</label>
                            <select id="preferencia" class="w-full border border-slate-300 rounded-lg p-2.5 bg-white font-medium">
                                <option value="Desea THM">Desea THM</option>
                                <option value="No desea THM">No desea THM</option>
                                <option value="Indecisa">Indecisa</option>
                            </select>
                        </div>
                    </div>
                </div>

                <div class="text-center pt-2">
                    <button type="button" onclick="generarInformeApp()" class="bg-gradient-to-r from-indigo-700 to-slate-800 hover:from-indigo-800 hover:to-slate-900 text-white font-bold py-4 px-10 rounded-xl shadow-lg hover:shadow-xl transition duration-200 flex items-center justify-center gap-3 mx-auto text-sm">
                        <i class="fa-solid fa-wand-magic-sparkles"></i> GENERAR INFORME CLÍNICO AUTOMÁTICO
                    </button>
                </div>
            </form>

            <section id="seccion-resultado" class="hidden mt-10 space-y-4">
                <div class="flex flex-wrap justify-between items-center gap-3 bg-white p-4 rounded-xl border border-slate-200 shadow-sm">
                    <h3 class="text-lg font-bold text-slate-800 flex items-center gap-2">
                        <i class="fa-solid fa-file-medical text-emerald-600"></i> Informe Generado
                    </h3>
                    <div class="flex items-center gap-2">
                        <button onclick="copiarTextoInforme()" class="bg-slate-700 hover:bg-slate-800 text-white text-xs font-semibold py-2.5 px-4 rounded-lg shadow transition flex items-center gap-2">
                            <i class="fa-solid fa-copy"></i> Copiar Texto
                        </button>
                        <button onclick="exportarPDF()" class="bg-red-600 hover:bg-red-700 text-white text-xs font-semibold py-2.5 px-4 rounded-lg shadow transition flex items-center gap-2">
                            <i class="fa-solid fa-file-pdf"></i> Descargar PDF
                        </button>
                    </div>
                </div>
                <textarea id="rawTextInforme" class="hidden"></textarea>
                <div id="pdfView" class="bg-white p-8 rounded-xl border border-slate-300 shadow-md font-mono text-xs text-slate-900 leading-relaxed space-y-4"></div>
            </section>
        </main>

        <!-- MÓDULO 2: EVALUADOR FSFI -->
        <main id="tab-fsfi" class="hidden space-y-6">
            <div class="bg-gradient-to-r from-teal-800 to-cyan-900 rounded-2xl p-6 md:p-8 text-white shadow-xl border border-teal-900/20">
                <div class="flex flex-col md:flex-row justify-between items-start md:items-center gap-6">
                    <div>
                        <span class="bg-teal-500/30 text-teal-200 text-xs font-bold px-3 py-1 rounded-full uppercase tracking-wider">Cuestionario Oficial e Interactivo</span>
                        <h2 class="text-3xl md:text-4xl font-extrabold mt-2 tracking-tight">Índice de Función Sexual Femenina (FSFI)</h2>
                        <p class="text-teal-100 text-sm md:text-base mt-2 max-w-2xl">
                            Evaluación científica autoadministrada de 19 ítems para el diagnóstico del TDSH y candidatura a terapia con Testosterona.
                        </p>
                    </div>
                    <div class="bg-white/10 backdrop-blur-md p-4 rounded-xl border border-white/10 text-xs text-left md:text-right shrink-0">
                        <p class="font-medium text-teal-200 uppercase tracking-wider">Herramienta Clínica Diseñada por:</p>
                        <p class="font-bold text-white text-base mt-0.5">Dr. Ronald</p>
                        <p class="text-teal-100/70 text-xs">Ginecología y Obstetricia</p>
                        <div class="border-t border-white/15 my-2"></div>
                        <p class="text-teal-200 font-medium">Soporte Tecnológico:</p>
                        <p class="font-semibold text-white">Gemini AI • 2026</p>
                    </div>
                </div>
            </div>

            <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-start">
                <div class="lg:col-span-7 space-y-6">
                    <div class="bg-white p-5 rounded-2xl border border-slate-200 shadow-sm space-y-4">
                        <h3 class="text-xs font-bold uppercase tracking-wider text-teal-700 flex items-center gap-2">
                            <span class="p-1 rounded-md bg-teal-50 text-teal-700">📋</span> 1. Criterios Clínicos del Consenso Global 2019
                        </h3>
                        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                            <label class="flex items-start gap-3 p-3 bg-slate-50 rounded-xl border border-slate-200 hover:border-teal-500 cursor-pointer transition-all">
                                <input type="checkbox" id="chk-postmenopause" class="mt-1 h-5 w-5 rounded border-slate-300 text-teal-600 focus:ring-teal-500" checked>
                                <span class="text-xs text-slate-700 leading-normal">La paciente es <strong>posmenopáusica</strong> (natural, quirúrgica o inducida).</span>
                            </label>
                            <label class="flex items-start gap-3 p-3 bg-slate-50 rounded-xl border border-slate-200 hover:border-teal-500 cursor-pointer transition-all">
                                <input type="checkbox" id="chk-distress" class="mt-1 h-5 w-5 rounded border-slate-300 text-teal-600 focus:ring-teal-500" checked>
                                <span class="text-xs text-slate-700 leading-normal">La baja del deseo le genera un <strong>malestar o angustia clínicamente significativa</strong>.</span>
                            </label>
                        </div>
                    </div>

                    <div class="bg-white p-4 rounded-xl border border-slate-200 shadow-sm flex items-center justify-between gap-4">
                        <div class="w-full bg-slate-100 rounded-full h-2.5">
                            <div id="progress-bar" class="bg-teal-600 h-2.5 rounded-full transition-all duration-300" style="width: 0%"></div>
                        </div>
                        <span id="progress-text" class="text-xs font-bold text-teal-800 whitespace-nowrap bg-teal-50 px-2.5 py-1 rounded-full">0 / 19 Respondidas</span>
                    </div>

                    <div id="questions-form" class="space-y-6"></div>
                </div>

                <div class="lg:col-span-5 space-y-6 lg:sticky lg:top-20">
                    <div class="bg-slate-900 text-white p-6 rounded-2xl shadow-xl border border-slate-800 space-y-6">
                        <div class="flex justify-between items-center">
                            <h3 class="text-xs font-bold uppercase tracking-widest text-teal-400">Análisis FSFI en Tiempo Real</h3>
                            <button onclick="resetAll()" class="text-xs text-slate-400 hover:text-white underline transition-colors">Reiniciar Test</button>
                        </div>

                        <div class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-2 gap-3">
                            <div class="bg-slate-800/80 p-3 rounded-xl border border-slate-700/50 flex flex-col justify-between">
                                <div><div class="flex justify-between items-center"><span class="text-xs font-semibold text-slate-300">1. Deseo</span><span class="text-[9px] text-teal-400 font-mono">Factor x0.6</span></div><p id="score-desire" class="text-xl font-bold text-white mt-1">0.00</p></div>
                                <span id="badge-desire" class="text-[9px] mt-1.5 px-2 py-0.5 rounded font-bold bg-slate-700/50 text-slate-400 w-fit">Pendiente</span>
                            </div>
                            <div class="bg-slate-800/80 p-3 rounded-xl border border-slate-700/50 flex flex-col justify-between">
                                <div><div class="flex justify-between items-center"><span class="text-xs font-semibold text-slate-300">2. Excitación</span><span class="text-[9px] text-teal-400 font-mono">Factor x0.3</span></div><p id="score-arousal" class="text-xl font-bold text-white mt-1">0.00</p></div>
                                <span id="badge-arousal" class="text-[9px] mt-1.5 px-2 py-0.5 rounded font-bold bg-slate-700/50 text-slate-400 w-fit">Pendiente</span>
                            </div>
                            <div class="bg-slate-800/80 p-3 rounded-xl border border-slate-700/50 flex flex-col justify-between">
                                <div><div class="flex justify-between items-center"><span class="text-xs font-semibold text-slate-300">3. Lubricación</span><span class="text-[9px] text-teal-400 font-mono">Factor x0.3</span></div><p id="score-lubrication" class="text-xl font-bold text-white mt-1">0.00</p></div>
                                <span id="badge-lubrication" class="text-[9px] mt-1.5 px-2 py-0.5 rounded font-bold bg-slate-700/50 text-slate-400 w-fit">Pendiente</span>
                            </div>
                            <div class="bg-slate-800/80 p-3 rounded-xl border border-slate-700/50 flex flex-col justify-between">
                                <div><div class="flex justify-between items-center"><span class="text-xs font-semibold text-slate-300">4. Orgasmo</span><span class="text-[9px] text-teal-400 font-mono">Factor x0.4</span></div><p id="score-orgasm" class="text-xl font-bold text-white mt-1">0.00</p></div>
                                <span id="badge-orgasm" class="text-[9px] mt-1.5 px-2 py-0.5 rounded font-bold bg-slate-700/50 text-slate-400 w-fit">Pendiente</span>
                            </div>
                            <div class="bg-slate-800/80 p-3 rounded-xl border border-slate-700/50 flex flex-col justify-between">
                                <div><div class="flex justify-between items-center"><span class="text-xs font-semibold text-slate-300">5. Satisfacción</span><span class="text-[9px] text-teal-400 font-mono">Factor x0.4</span></div><p id="score-satisfaction" class="text-xl font-bold text-white mt-1">0.00</p></div>
                                <span id="badge-satisfaction" class="text-[9px] mt-1.5 px-2 py-0.5 rounded font-bold bg-slate-700/50 text-slate-400 w-fit">Pendiente</span>
                            </div>
                            <div class="bg-slate-800/80 p-3 rounded-xl border border-slate-700/50 flex flex-col justify-between">
                                <div><div class="flex justify-between items-center"><span class="text-xs font-semibold text-slate-300">6. Dolor Coital</span><span class="text-[9px] text-teal-400 font-mono">Factor x0.4</span></div><p id="score-pain" class="text-xl font-bold text-white mt-1">0.00</p></div>
                                <span id="badge-pain" class="text-[9px] mt-1.5 px-2 py-0.5 rounded font-bold bg-slate-700/50 text-slate-400 w-fit">Pendiente</span>
                            </div>
                        </div>

                        <div class="bg-slate-800 p-4 rounded-xl border border-slate-700 text-center">
                            <p class="text-xs text-slate-400 uppercase tracking-widest font-bold">PUNTAJE GLOBAL FSFI</p>
                            <p id="score-total" class="text-5xl font-extrabold text-white mt-1.5">0.00</p>
                            <p class="text-[11px] text-teal-300 mt-1.5">Disfunción Sexual si es ≤ 26.55 puntos</p>
                        </div>

                        <div id="verdict-card" class="p-4 rounded-xl border text-center transition-all duration-300 bg-slate-800 text-slate-300 border-slate-700">
                            <p class="text-xs uppercase tracking-wider font-bold" id="verdict-title">Evaluando Datos...</p>
                            <p class="text-sm font-semibold mt-1" id="verdict-body">Por favor, complete las 19 preguntas del test.</p>
                        </div>
                    </div>

                    <div class="bg-white p-5 rounded-2xl border border-slate-200 shadow-sm space-y-4">
                        <div class="flex justify-between items-center">
                            <h3 class="text-xs font-bold uppercase tracking-wider text-slate-500 flex items-center gap-1.5">
                                <span>📝</span> Nota Clínica para Historia
                            </h3>
                            <button onclick="copyClinicalNote()" class="text-xs bg-teal-50 hover:bg-teal-100 text-teal-700 font-semibold px-2.5 py-1.5 rounded-lg border border-teal-200 flex items-center gap-1 transition-colors">
                                <span>Copiar nota</span>
                            </button>
                        </div>
                        <textarea id="clinical-note" rows="6" class="w-full bg-slate-50 border border-slate-200 rounded-xl p-3 text-[11px] font-mono text-slate-600 focus:outline-none focus:ring-1 focus:ring-teal-500 cursor-text" readonly></textarea>
                        <p id="copy-success-msg" class="text-xs text-emerald-600 font-semibold text-center hidden">¡Nota clínica copiada con éxito!</p>
                    </div>
                </div>
            </div>
        </main>

        <footer class="mt-12 text-center text-xs text-slate-500 space-y-1 border-t border-slate-200 pt-6">
            <p class="font-semibold text-slate-600">Plataforma Integrada Menopausia &copy; 2026 — Algoritmos de Decisión Clínica</p>
            <p class="text-[11px] text-slate-400">Co-diseñado e implementado por Dr. Ronald & Gemini AI Collaborator</p>
        </footer>
    </div>

    <script>
        function switchTab(tab) {
            const tabThm = document.getElementById('tab-thm');
            const tabFsfi = document.getElementById('tab-fsfi');
            const btnThm = document.getElementById('btn-tab-thm');
            const btnFsfi = document.getElementById('btn-tab-fsfi');

            if (tab === 'thm') {
                tabThm.classList.remove('hidden');
                tabFsfi.classList.add('hidden');
                btnThm.classList.add('active');
                btnFsfi.classList.remove('active');
            } else {
                tabFsfi.classList.remove('hidden');
                tabThm.classList.add('hidden');
                btnFsfi.classList.add('active');
                btnThm.classList.remove('active');
            }
        }

        let nombrePacienteGlobal = "Paciente";

        function generarInformeApp() {
            const nombre = document.getElementById('nombre').value || 'Paciente No Registrada';
            nombrePacienteGlobal = nombre.replace(/ /g, "_");
            const edad = parseInt(document.getElementById('edad').value) || '__';
            const fur = document.getElementById('fur').value || '//_____';
            const etapa = document.getElementById('etapa').value;

            let somatico = 0; [...document.querySelectorAll('.mrs-s')].forEach(i => somatico += parseInt(i.value));
            let psicologico = 0; [...document.querySelectorAll('.mrs-p')].forEach(i => psicologico += parseInt(i.value));
            let urogenital = 0; [...document.querySelectorAll('.mrs-u')].forEach(i => urogenital += parseInt(i.value));
            let totalMRS = somatico + psicologico + urogenital;

            let interpS = somatico <= 4 ? 'Leve' : (somatico <= 8 ? 'Moderado' : 'Severo');
            let interpP = psicologico <= 3 ? 'Leve' : (psicologico <= 6 ? 'Moderado' : 'Severo');
            let interpU = urogenital <= 3 ? 'Leve' : (urogenital <= 6 ? 'Moderado' : 'Severo');

            let interpTotalMRS = 'Leves';
            if (totalMRS >= 9 && totalMRS <= 14) interpTotalMRS = 'Moderados leves';
            else if (totalMRS >= 15 && totalMRS <= 20) interpTotalMRS = 'Moderados severos';
            else if (totalMRS > 20) interpTotalMRS = 'Severos';

            let pctS = Math.round((somatico / 16) * 100) || 0;
            let pctP = Math.round((psicologico / 12) * 100) || 0;
            let pctU = Math.round((urogenital / 12) * 100) || 0;

            let maxPct = Math.max(pctS, pctP, pctU);
            let domPred = "Ninguno";
            let analisisDom = "Sin prevalencia marcada.";

            if (maxPct > 0) {
                if (maxPct === pctS) { domPred = "Somático"; analisisDom = "SINTOMATOLOGÍA VASOMOTORA Y OSTEOMUSCULAR PREDOMINANTE. Indicación preferente de THM sistémica."; }
                else if (maxPct === pctP) { domPred = "Psicológico"; analisisDom = "Afectación anímica prevalente. Descartar origen psicógeno independiente de la transición."; }
                else if (maxPct === pctU) { domPred = "Urogenital"; analisisDom = "SÍNDROME GENITOURINARIO (SGUM) DOMINANTE. Evaluar THM tópica o sistémica según severidad."; }
            }

            const bDia = parseInt(document.getElementById('bochornos-dia').value) || 0;
            const bImp = parseInt(document.getElementById('bochornos-impacto').value) || 0;
            let interpImp = bImp <= 3 ? 'Leve' : (bImp <= 6 ? 'Moderado' : 'Severo');

            const sudor = document.getElementById('sint-sudor').checked ? 'Sí' : 'No';
            const noche = document.getElementById('sint-noche').checked ? 'Sí' : 'No';
            const act = document.getElementById('sint-act').checked ? 'Sí' : 'No';
            const ropa = document.getElementById('sint-ropa').checked ? 'Sí' : 'No';

            let absCount = 0; [...document.querySelectorAll('.cx-absoluta')].forEach(c => { if(c.checked) absCount++; });
            const absText = absCount > 0 ? 'ALERTA: Contraindicación absoluta presente.' : 'Ninguna';
            const relText = document.getElementById('cx-coronaria').checked ? 'Enfermedad coronaria activa (Evaluación por Cardiología)' : 'Ninguna';

            let rCardio = 0; [...document.querySelectorAll('.rf-cardio')].forEach(c => { if(c.checked) rCardio += parseInt(c.value); });
            let rTrombo = 0; [...document.querySelectorAll('.rf-trombo')].forEach(c => { if(c.checked) rTrombo += parseInt(c.value); });
            let rMama = 0; [...document.querySelectorAll('.rf-mama')].forEach(c => { if(c.checked) rMama += parseInt(c.value); });
            let rTotal = rCardio + rTrombo + rMama;
            let interpRiesgo = rTotal <= 2 ? 'RIESGO BAJO' : (rTotal <= 5 ? 'RIESGO INTERMEDIO' : 'RIESGO ALTO');

            let sitEsp = []; [...document.querySelectorAll('.sit-esp')].forEach(c => { if(c.checked) sitEsp.push(c.value); });
            let sitEspText = sitEsp.length > 0 ? sitEsp.join(', ') : 'Ninguna';
            const pref = document.getElementById('preferencia').value;

            let indPuntos = 0;
            if (edad < 60 || etapa === 'Posmenopausia <10 años') indPuntos++;
            if (totalMRS >= 9) indPuntos++;
            if (bDia >= 3) indPuntos++;
            if (bImp >= 4) indPuntos++;
            if (absCount === 0) indPuntos++;
            if (interpRiesgo === 'RIESGO BAJO' || interpRiesgo === 'RIESGO INTERMEDIO') indPuntos++;
            if (document.getElementById('se-osteo').checked) indPuntos++;
            if (document.getElementById('se-precoz').checked || (edad > 0 && edad < 40)) indPuntos++;

            let interpInd = 'NO HORMONAL';
            let recFinal = 'Priorizar manejo no hormonal y modificaciones de estilo de vida.';

            if (indPuntos >= 7) { interpInd = 'CANDIDATA IDEAL a THM'; recFinal = 'Indicar THM sistémica. Los beneficios superan ampliamente a los riesgos.'; }
            else if (indPuntos >= 5) { interpInd = 'CANDIDATA CLARA a THM'; recFinal = 'Indicar THM. Evaluar idoneidad de tipo y vía según comorbilidades.'; }
            else if (indPuntos >= 3) { interpInd = 'INDIVIDUALIZAR'; recFinal = 'Ponderar minuciosamente relación riesgo/beneficio con la paciente.'; }

            if (absCount > 0) {
                interpInd = 'NO HORMONAL (CONTRAINDICACIÓN ABSOLUTA)';
                recFinal = 'CRÍTICO: THM Sistémica totalmente CONTRAINDICADA. Preferir alternativas no hormonales o estrógenos locales si se limita a síntomas genitourinarios.';
            } else {
                if (document.getElementById('se-migrana').checked) recFinal += '\\n* Paciente con Migraña con aura: Prescribir exclusivamente VÍA TRANSDÉRMICA.';
                if (sitEsp.includes('Endometriosis') || sitEsp.includes('Adenomiosis')) recFinal += '\\n* Antecedente de Endometriosis/Adenomiosis: Utilizar ESQUEMA COMBINADO CONTINUO o DIU Mirena.';
            }

            const informeTexto = `===========================================================
INFORME DE EVALUACIÓN MENOPÁUSICA - Protocolo Ronald v2.0
Desarrollo Clínico: Dr. Ronald | Motor: Gemini AI
===========================================================
Paciente: ${nombre} | Edad: ${edad} años | FUR: ${fur}
Etapa: ${etapa}

1. ESCALA MRS COMPLETA
   Dominio Somático: ${somatico}/16 → ${interpS}
   Dominio Psicológico: ${psicologico}/12 → ${interpP}
   Dominio Urogenital: ${urogenital}/12 → ${interpU}
   Puntaje TOTAL: ${totalMRS}/40 → ${interpTotalMRS}

2. ANÁLISIS POR DOMINIO
   ${domPred === 'Somático' ? '[X]' : '[ ]'} Somático predominante (${pctS}% del máx): ${domPred === 'Somático' ? analisisDom : 'No prevalente.'}
   ${domPred === 'Psicológico' ? '[X]' : '[ ]'} Psicológico predominante (${pctP}% del máx): ${domPred === 'Psicológico' ? analisisDom : 'No prevalente.'}
   ${domPred === 'Urogenital' ? '[X]' : '[ ]'} Urogenital predominante (${pctU}% del máx): ${domPred === 'Urogenital' ? analisisDom : 'No prevalente.'}

3. BOCHORNOS
   Episodios/día: ${bDia} | Impacto: ${bImp}/10 → ${interpImp}
   Sudoración: ${sudor}              | Despierta por noche: ${noche}
   Interrumpe actividades: ${act}  | Debe cambiarse de ropa: ${ropa}

4. CONTRANDICACIONES
   Absolutas: ${absText}
   Relativas: ${relText}

5. RIESGOS PONDERADOS
   Cardiovascular: ${rCardio} pts
   Tromboembólico: ${rTrombo} pts
   Cáncer mama: ${rMama} pts
   RIESGO TOTAL: ${rTotal} pts → ${interpRiesgo}

6. SITUACIONES ESPECIALES
   ${sitEspText}

7. PREFERENCIA DE LA PACIENTE
   ${pref}

8. PUNTAJE DE INDICACIÓN (8 criterios)
   Puntaje: ${indPuntos}/8 → ${interpInd}
===========================================================
RECOMENDACIÓN FINAL:
${recFinal}
===========================================================`;

            document.getElementById('rawTextInforme').value = informeTexto;
            document.getElementById('pdfView').innerHTML = informeTexto.replace(/\\n/g, '<br>').replace(/ /g, '&nbsp;');
            document.getElementById('seccion-resultado').classList.remove('hidden');
            document.getElementById('seccion-resultado').scrollIntoView({ behavior: 'smooth' });
        }

        function copiarTextoInforme() {
            const raw = document.getElementById('rawTextInforme');
            raw.select();
            document.execCommand('copy');
            alert('¡Informe copiado al portapapeles!');
        }

        function exportarPDF() {
            const el = document.getElementById('pdfView');
            const opt = {
                margin:       12,
                filename:     `Protocolo_Ronald_${nombrePacienteGlobal}.pdf`,
                image:        { type: 'jpeg', quality: 0.98 },
                html2canvas:  { scale: 2 },
                jsPDF:        { unit: 'mm', format: 'letter', orientation: 'portrait' }
            };
            html2pdf().set(opt).from(el).save();
        }

        const DOMAINS_SPEC = [
            { id: "desire", name: "Deseo", questions: [1, 2], factor: 0.6 },
            { id: "arousal", name: "Excitación", questions: [3, 4, 5, 6], factor: 0.3 },
            { id: "lubrication", name: "Lubricación", questions: [7, 8, 9, 10], factor: 0.3 },
            { id: "orgasm", name: "Orgasmo", questions: [11, 12, 13], factor: 0.4 },
            { id: "satisfaction", name: "Satisfacción", questions: [14, 15, 16], factor: 0.4 },
            { id: "pain", name: "Dolor Coital", questions: [17, 18, 19], factor: 0.4 }
        ];

        const QUESTIONS_DATABASE = [
            { id: 1, domain: "desire", question: "1. ¿Con qué frecuencia sintió deseo o interés sexual?", options: [{value:5,label:"Casi siempre o siempre"},{value:4,label:"La mayoría de las veces"},{value:3,label:"A veces"},{value:2,label:"Pocas veces"},{value:1,label:"Casi nunca o nunca"}] },
            { id: 2, domain: "desire", question: "2. ¿Cómo calificaría su nivel de deseo o interés sexual?", options: [{value:5,label:"Muy alto"},{value:4,label:"Alto"},{value:3,label:"Moderado"},{value:2,label:"Bajo"},{value:1,label:"Muy bajo o nulo"}] },
            { id: 3, domain: "arousal", question: "3. ¿Con qué frecuencia se sintió sexualmente excitada durante la actividad sexual?", options: [{value:0,label:"No hubo actividad sexual"},{value:5,label:"Casi siempre o siempre"},{value:4,label:"La mayoría de las veces"},{value:3,label:"A veces"},{value:2,label:"Pocas veces"},{value:1,label:"Casi nunca o nunca"}] },
            { id: 4, domain: "arousal", question: "4. ¿Cómo calificaría su nivel de excitación sexual durante la actividad sexual?", options: [{value:0,label:"No hubo actividad sexual"},{value:5,label:"Muy alto"},{value:4,label:"Alto"},{value:3,label:"Moderado"},{value:2,label:"Bajo"},{value:1,label:"Muy bajo o nulo"}] },
            { id: 5, domain: "arousal", question: "5. ¿Con qué frecuencia se sintió satisfecha con su nivel de excitación durante la actividad sexual?", options: [{value:0,label:"No hubo actividad sexual"},{value:5,label:"Casi siempre o siempre"},{value:4,label:"La mayoría de las veces"},{value:3,label:"A veces"},{value:2,label:"Pocas veces"},{value:1,label:"Casi nunca o nunca"}] },
            { id: 6, domain: "arousal", question: "6. ¿Con qué frecuencia se sintió confiada en lograr la excitación sexual durante la actividad sexual?", options: [{value:0,label:"No hubo actividad sexual"},{value:5,label:"Casi siempre o siempre"},{value:4,label:"La mayoría de las veces"},{value:3,label:"A veces"},{value:2,label:"Pocas veces"},{value:1,label:"Casi nunca o nunca"}] },
            { id: 7, domain: "lubrication", question: "7. ¿Con qué frecuencia se lubricó ('se mojó') durante la actividad sexual?", options: [{value:0,label:"No hubo actividad sexual"},{value:5,label:"Casi siempre o siempre"},{value:4,label:"La mayoría de las veces"},{value:3,label:"A veces"},{value:2,label:"Pocas veces"},{value:1,label:"Casi nunca o nunca"}] },
            { id: 8, domain: "lubrication", question: "8. ¿Cómo calificaría su dificultad para lograr la lubricación durante la actividad sexual?", options: [{value:0,label:"No hubo actividad sexual"},{value:1,label:"Mucho o extremadamente difícil"},{value:2,label:"Muy difícil"},{value:3,label:"Difícil"},{value:4,label:"Un poco difícil"},{value:5,label:"Nada difícil"}] },
            { id: 9, domain: "lubrication", question: "9. ¿Con qué frecuencia mantuvo la lubricación hasta el final de la actividad sexual?", options: [{value:0,label:"No hubo actividad sexual"},{value:5,label:"Casi siempre o siempre"},{value:4,label:"La mayoría de las veces"},{value:3,label:"A veces"},{value:2,label:"Pocas veces"},{value:1,label:"Casi nunca o nunca"}] },
            { id: 10, domain: "lubrication", question: "10. ¿Cómo calificaría su dificultad para mantener la lubricación hasta el final de la actividad sexual?", options: [{value:0,label:"No hubo actividad sexual"},{value:1,label:"Mucho o extremadamente difícil"},{value:2,label:"Muy difícil"},{value:3,label:"Difícil"},{value:4,label:"Un poco difícil"},{value:5,label:"Nada difícil"}] },
            { id: 11, domain: "orgasm", question: "11. ¿Con qué frecuencia llegó al orgasmo (clímax) durante la actividad sexual?", options: [{value:0,label:"No hubo actividad sexual"},{value:5,label:"Casi siempre o siempre"},{value:4,label:"La mayoría de las veces"},{value:3,label:"A veces"},{value:2,label:"Pocas veces"},{value:1,label:"Casi nunca o nunca"}] },
            { id: 12, domain: "orgasm", question: "12. ¿Cómo calificaría su dificultad para alcanzar el orgasmo durante la actividad sexual?", options: [{value:0,label:"No hubo actividad sexual"},{value:1,label:"Mucho o extremadamente difícil"},{value:2,label:"Muy difícil"},{value:3,label:"Difícil"},{value:4,label:"Un poco difícil"},{value:5,label:"Nada difícil"}] },
            { id: 13, domain: "orgasm", question: "13. ¿Qué tan satisfecha estuvo con su capacidad para alcanzar el orgasmo durante la actividad sexual?", options: [{value:0,label:"No hubo actividad sexual"},{value:5,label:"Muy satisfecha"},{value:4,label:"Moderadamente satisfecha"},{value:3,label:"Ni satisfecha ni insatisfecha"},{value:2,label:"Moderadamente insatisfecha"},{value:1,label:"Muy insatisfecha"}] },
            { id: 14, domain: "satisfaction", question: "14. ¿Qué tan satisfecha estuvo con la cercanía emocional entre usted y su pareja durante la actividad sexual?", options: [{value:0,label:"No hubo actividad sexual"},{value:5,label:"Muy satisfecha"},{value:4,label:"Moderadamente satisfecha"},{value:3,label:"Ni satisfecha ni insatisfecha"},{value:2,label:"Moderadamente insatisfecha"},{value:1,label:"Muy insatisfecha"}] },
            { id: 15, domain: "satisfaction", question: "15. ¿Qué tan satisfecha estuvo con su relación sexual con su pareja?", options: [{value:5,label:"Muy satisfecha"},{value:4,label:"Moderadamente satisfecha"},{value:3,label:"Ni satisfecha ni insatisfecha"},{value:2,label:"Moderadamente insatisfecha"},{value:1,label:"Muy insatisfecha"}] },
            { id: 16, domain: "satisfaction", question: "16. ¿Qué tan satisfecha estuvo con su vida sexual en general?", options: [{value:5,label:"Muy satisfecha"},{value:4,label:"Moderadamente satisfecha"},{value:3,label:"Ni satisfecha ni insatisfecha"},{value:2,label:"Moderadamente insatisfecha"},{value:1,label:"Muy insatisfecha"}] },
            { id: 17, domain: "pain", question: "17. ¿Con qué frecuencia experimentó dolor o malestar durante la penetración vaginal?", options: [{value:0,label:"No hubo penetración"},{value:1,label:"Casi siempre o siempre"},{value:2,label:"La mayoría de las veces"},{value:3,label:"A veces"},{value:4,label:"Pocas veces"},{value:5,label:"Casi nunca o nunca"}] },
            { id: 18, domain: "pain", question: "18. ¿Con qué frecuencia experimentó dolor o malestar después de la penetración vaginal?", options: [{value:0,label:"No hubo penetración"},{value:1,label:"Casi siempre o siempre"},{value:2,label:"La mayoría de las veces"},{value:3,label:"A veces"},{value:4,label:"Pocas veces"},{value:5,label:"Casi nunca o nunca"}] },
            { id: 19, domain: "pain", question: "19. ¿Cómo calificaría el nivel de dolor o malestar durante o después de la penetración vaginal?", options: [{value:0,label:"No hubo penetración"},{value:1,label:"Muy alto o insoportable"},{value:2,label:"Alto"},{value:3,label:"Moderado"},{value:4,label:"Bajo"},{value:5,label:"Muy bajo o nulo"}] }
        ];

        let state = { responses: {}, postmenopause: true, distress: true };

        function renderQuestions() {
            const formContainer = document.getElementById('questions-form');
            formContainer.innerHTML = '';

            DOMAINS_SPEC.forEach(domain => {
                const domainQuestions = QUESTIONS_DATABASE.filter(q => q.domain === domain.id);
                const domainCard = document.createElement('div');
                domainCard.className = "bg-white rounded-2xl border border-slate-200 shadow-sm overflow-hidden mb-6";
                
                const cardHeader = document.createElement('div');
                cardHeader.className = "bg-slate-50 border-b border-slate-200 p-4 flex justify-between items-center";
                cardHeader.innerHTML = `
                    <div class="flex items-center gap-2">
                        <span class="w-2.5 h-2.5 rounded-full bg-teal-600"></span>
                        <h4 class="font-bold text-slate-800 text-sm md:text-base">Dominio: ${domain.name}</h4>
                    </div>
                    <span class="text-[10px] bg-teal-50 text-teal-700 font-bold px-2 py-0.5 rounded-md uppercase tracking-wider">Peso: x${domain.factor}</span>
                `;
                domainCard.appendChild(cardHeader);

                const cardBody = document.createElement('div');
                cardBody.className = "p-4 md:p-6 space-y-6";

                domainQuestions.forEach(q => {
                    const qElement = document.createElement('div');
                    qElement.className = "space-y-3";
                    qElement.innerHTML = `
                        <p class="text-xs md:text-sm font-semibold text-slate-700 leading-relaxed">${q.question}</p>
                        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-1 xl:grid-cols-2 gap-2" id="options-group-${q.id}"></div>
                    `;
                    const optionsGroup = qElement.querySelector(`#options-group-${q.id}`);
                    
                    q.options.forEach(opt => {
                        const optButton = document.createElement('button');
                        optButton.type = "button";
                        optButton.id = `q-${q.id}-opt-${opt.value}`;
                        optButton.className = "flex items-center justify-between p-3 rounded-xl border border-slate-200 text-left text-xs hover:border-teal-500 hover:bg-slate-50 transition-all focus:outline-none focus:ring-2 focus:ring-teal-500";
                        optButton.innerHTML = `
                            <span class="text-slate-600 font-medium">${opt.label}</span>
                            <span class="bg-slate-100 text-slate-500 font-bold text-[10px] px-2 py-1 rounded-md shrink-0 ml-2">Puntos: ${opt.value}</span>
                        `;
                        optButton.addEventListener('click', () => selectOption(q.id, opt.value));
                        optionsGroup.appendChild(optButton);
                    });
                    cardBody.appendChild(qElement);
                });
                domainCard.appendChild(cardBody);
                formContainer.appendChild(domainCard);
            });
        }

        function selectOption(questionId, value) {
            state.responses[questionId] = value;
            const questionData = QUESTIONS_DATABASE.find(q => q.id === questionId);
            
            questionData.options.forEach(opt => {
                const btn = document.getElementById(`q-${questionId}-opt-${opt.value}`);
                if (btn) {
                    btn.className = "flex items-center justify-between p-3 rounded-xl border border-slate-200 text-left text-xs hover:border-teal-500 hover:bg-slate-50 transition-all focus:outline-none focus:ring-2 focus:ring-teal-500";
                    const badge = btn.querySelector('span:last-child');
                    if (badge) badge.className = "bg-slate-100 text-slate-500 font-bold text-[10px] px-2 py-1 rounded-md shrink-0 ml-2";
                }
            });

            const activeBtn = document.getElementById(`q-${questionId}-opt-${value}`);
            if (activeBtn) {
                activeBtn.className = "flex items-center justify-between p-3 rounded-xl border-2 border-teal-600 bg-teal-50/40 text-left text-xs transition-all focus:outline-none focus:ring-2 focus:ring-teal-500";
                const badge = activeBtn.querySelector('span:last-child');
                if (badge) badge.className = "bg-teal-600 text-white font-bold text-[10px] px-2 py-1 rounded-md shrink-0 ml-2";
            }
            calculateResults();
        }

        function calculateResults() {
            let totalWeightedScore = 0;
            let answeredCount = 0;
            const domainScores = {};

            DOMAINS_SPEC.forEach(domain => {
                let domainSum = 0;
                let domainAnswered = 0;

                domain.questions.forEach(qId => {
                    if (state.responses[qId] !== undefined) {
                        domainSum += state.responses[qId];
                        domainAnswered++;
                    }
                });

                const isDomainComplete = domainAnswered === domain.questions.length;
                const weighted = domainSum * domain.factor;
                domainScores[domain.id] = { sum: domainSum, weighted: weighted, isComplete: isDomainComplete };

                if (isDomainComplete) {
                    answeredCount += domainAnswered;
                    totalWeightedScore += weighted;
                }

                const scoreEl = document.getElementById(`score-${domain.id}`);
                const badgeEl = document.getElementById(`badge-${domain.id}`);
                
                if (scoreEl && badgeEl) {
                    scoreEl.textContent = weighted.toFixed(2);
                    if (isDomainComplete) {
                        if (domain.id === 'desire') {
                            badgeEl.textContent = weighted <= 3.3 ? "Deseo Bajo (TDSH)" : "Deseo Normal";
                            badgeEl.className = weighted <= 3.3 ? "text-[9px] mt-1.5 px-2 py-0.5 rounded font-bold bg-rose-500/20 text-rose-300 w-fit" : "text-[9px] mt-1.5 px-2 py-0.5 rounded font-bold bg-emerald-500/20 text-emerald-300 w-fit";
                        } else if (domain.id === 'pain') {
                            badgeEl.textContent = weighted <= 4.0 ? "Dispareunia Activa" : "Sin dolor limitante";
                            badgeEl.className = weighted <= 4.0 ? "text-[9px] mt-1.5 px-2 py-0.5 rounded font-bold bg-amber-500/20 text-amber-300 w-fit" : "text-[9px] mt-1.5 px-2 py-0.5 rounded font-bold bg-emerald-500/20 text-emerald-300 w-fit";
                        } else {
                            badgeEl.textContent = "Completo";
                            badgeEl.className = "text-[9px] mt-1.5 px-2 py-0.5 rounded font-bold bg-teal-500/20 text-teal-300 w-fit";
                        }
                    } else {
                        scoreEl.textContent = "0.00";
                        badgeEl.textContent = "Incompleto";
                        badgeEl.className = "text-[9px] mt-1.5 px-2 py-0.5 rounded font-bold bg-slate-700/50 text-slate-400 w-fit";
                    }
                }
            });

            const totalQuestionsCount = QUESTIONS_DATABASE.length;
            const progressPct = (answeredCount / totalQuestionsCount) * 100;
            document.getElementById('progress-bar').style.width = `${progressPct}%`;
            document.getElementById('progress-text').textContent = `${answeredCount} / ${totalQuestionsCount} Respondidas`;

            const scoreTotalEl = document.getElementById('score-total');
            if (scoreTotalEl) scoreTotalEl.textContent = totalWeightedScore.toFixed(2);

            const isPostmenopause = document.getElementById('chk-postmenopause').checked;
            const hasDistress = document.getElementById('chk-distress').checked;
            
            const verdictCard = document.getElementById('verdict-card');
            const verdictTitle = document.getElementById('verdict-title');
            const verdictBody = document.getElementById('verdict-body');

            const isAllAnswered = answeredCount === totalQuestionsCount;

            if (!isAllAnswered) {
                verdictCard.className = "p-4 rounded-xl border text-center transition-all duration-300 bg-slate-800 text-slate-300 border-slate-700";
                verdictTitle.textContent = "Evaluando Datos...";
                verdictBody.textContent = `Por favor, complete las ${totalQuestionsCount - answeredCount} preguntas pendientes.`;
            } else {
                const desireScore = domainScores['desire'].weighted;
                const painScore = domainScores['pain'].weighted;

                if (!isPostmenopause || !hasDistress) {
                    verdictCard.className = "p-4 rounded-xl border text-center transition-all duration-300 bg-rose-950/40 text-rose-300 border-rose-900";
                    verdictTitle.textContent = "No Candidata (Requisitos Excluidos)";
                    verdictBody.textContent = "La terapia con testosterona solo se indica bajo el Consenso Global en pacientes posmenopáusicas con malestar clínico manifiesto.";
                } else if (painScore <= 4.0) {
                    verdictCard.className = "p-4 rounded-xl border text-center transition-all duration-300 bg-amber-950/40 text-amber-300 border-amber-900";
                    verdictTitle.textContent = "Tratar Dispareunia Primero";
                    verdictBody.textContent = `La paciente tiene dolor coital significativo (${painScore.toFixed(2)} pts). Priorice resolver la atrofia con estrógenos tópicos locales antes de evaluar testosterona.`;
                } else if (desireScore > 3.3) {
                    verdictCard.className = "p-4 rounded-xl border text-center transition-all duration-300 bg-rose-950/40 text-rose-300 border-rose-900";
                    verdictTitle.textContent = "No Candidata (Deseo Conservado)";
                    verdictBody.textContent = `El subtotal de deseo (${desireScore.toFixed(2)} pts) es mayor al límite diagnóstico de ≤ 3.3. No califica para TDSH.`;
                } else {
                    verdictCard.className = "p-4 rounded-xl border text-center transition-all duration-300 bg-emerald-950/40 text-emerald-300 border-emerald-900";
                    verdictTitle.textContent = "✓ Candidata Apta para Testosterona";
                    verdictBody.textContent = `Cumple criterios: Deseo bajo (${desireScore.toFixed(2)} pts), sin dolor coital limitante y estatus posmenopáusico con malestar. Solicitar laboratorios pre-tratamiento.`;
                }
            }

            generateClinicalNote(domainScores, totalWeightedScore, isAllAnswered, isPostmenopause, hasDistress);
        }

        function generateClinicalNote(domainScores, totalScore, isComplete, isPostmenopause, hasDistress) {
            const noteEl = document.getElementById('clinical-note');
            if (!noteEl) return;

            if (!isComplete) {
                noteEl.value = "Complete el test completo con la paciente para estructurar la nota médica automática.";
                return;
            }

            const dateStr = new Date().toLocaleDateString('es-ES');
            const desireVal = domainScores['desire'].weighted;
            const arousalVal = domainScores['arousal'].weighted;
            const lubVal = domainScores['lubrication'].weighted;
            const orgVal = domainScores['orgasm'].weighted;
            const satVal = domainScores['satisfaction'].weighted;
            const painVal = domainScores['pain'].weighted;

            let conclusionStr = "";
            if (!isPostmenopause || !hasDistress) {
                conclusionStr = "No candidata a terapia androgénica (No cumple criterios basales de posmenopausia y distress).";
            } else if (painVal <= 4.0) {
                conclusionStr = "No apta para testosterona en este momento. Se sospecha dispareunia / atrofia urogenital severa como causa de la pérdida del deseo. Tratar primero la mucosa local.";
            } else if (desireVal > 3.3) {
                conclusionStr = "No cumple criterios de TDSH (Deseo sexual conservado según FSFI).";
            } else {
                conclusionStr = "Apta para terapia con Testosterona Transdérmica Femenina (1/10 dosis de varón). Solicitar testosterona total, SHBG, perfil hepático y mamografía vigente antes de iniciar.";
            }

            noteEl.value = `REPORTE CLÍNICO - ÍNDICE DE FUNCIÓN SEXUAL FEMENINA (FSFI)
======================================================
Fecha de Evaluación: ${dateStr}
Criterio Clínico Basal: ${isPostmenopause ? 'Posmenopáusica' : 'Premenopáusica'} | Distress Sexual: ${hasDistress ? 'SÍ' : 'NO'}

SUBTOTALES DE DOMINIOS FSFI:
------------------------------------------------------
- DESEO: ${desireVal.toFixed(2)} pts  (Umbral de sospecha TDSH: <= 3.3)
- EXCITACIÓN: ${arousalVal.toFixed(2)} pts
- LUBRICACIÓN: ${lubVal.toFixed(2)} pts
- ORGASMO: ${orgVal.toFixed(2)} pts
- SATISFACCIÓN: ${satVal.toFixed(2)} pts
- DOLOR COITAL: ${painVal.toFixed(2)} pts  (Disfunción por dispareunia: <= 4.0)

PUNTAJE GLOBAL FSFI: ${totalScore.toFixed(2)} pts  (Disfunción si <= 26.55)

DIAGNÓSTICO Y PLAN DE MANEJO RECOMENDADO:
------------------------------------------------------
${conclusionStr}

------------------------------------------------------
Co-diseñado para la práctica clínica por:
Dr. Ronald (Ginecología y Obstetricia) & Gemini AI`;
        }

        function copyClinicalNote() {
            const textarea = document.getElementById('clinical-note');
            textarea.select();
            textarea.setSelectionRange(0, 99999);
            try {
                document.execCommand('copy');
                const msg = document.getElementById('copy-success-msg');
                msg.classList.remove('hidden');
                setTimeout(() => msg.classList.add('hidden'), 3000);
            } catch (err) {
                console.error("Error al copiar nota: ", err);
            }
        }

        function resetAll() {
            state.responses = {};
            document.getElementById('chk-postmenopause').checked = true;
            document.getElementById('chk-distress').checked = true;
            renderQuestions();
            calculateResults();
            window.scrollTo({ top: 0, behavior: 'smooth' });
        }

        window.onload = function() {
            renderQuestions();
            document.getElementById('chk-postmenopause').addEventListener('change', calculateResults);
            document.getElementById('chk-distress').addEventListener('change', calculateResults);
            calculateResults();
        };
    </script>
</body>
</html>
"""

# Renderizar en la aplicación Streamlit
components.html(html_code, height=1800, scrolling=True)
