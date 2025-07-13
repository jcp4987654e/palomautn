import streamlit as st

# --- CONFIGURACIÓN DE LA PÁGINA ---
st.set_page_config(
    page_title="Plan de Carrera",
    page_icon="🌸",
    layout="wide"
)

# --- DATOS INICIALES ---
# (Los mismos datos que en la versión HTML)
initial_subjects_data = {
  "1_am1": { "id": "1_am1", "name": "Análisis Matemático I", "credits": 8, "prerequisites": [], "status": 'PENDING' }, "1_aga": { "id": "1_aga", "name": "Álgebra y Geometría Analítica", "credits": 8, "prerequisites": [], "status": 'PENDING' }, "1_qui": { "id": "1_qui", "name": "Química General", "credits": 6, "prerequisites": [], "status": 'PENDING' }, "1_info1": { "id": "1_info1", "name": "Informática I", "credits": 4, "prerequisites": [], "status": 'PENDING' }, "1_ing1": { "id": "1_ing1", "name": "Ingeniería y Sociedad", "credits": 4, "prerequisites": [], "status": 'PENDING' }, "1_fis1": { "id": "1_fis1", "name": "Física I", "credits": 8, "prerequisites": ["1_am1", "1_aga"], "status": 'PENDING' }, "1_sdr": { "id": "1_sdr", "name": "Sistemas de Representación", "credits": 6, "prerequisites": [], "status": 'PENDING' }, "1_info2": { "id": "1_info2", "name": "Informática II", "credits": 4, "prerequisites": ["1_info1"], "status": 'PENDING' }, "1_ing2": { "id": "1_ing2", "name": "Inglés I", "credits": 4, "prerequisites": [], "status": 'PENDING' },
  "2_am2": { "id": "2_am2", "name": "Análisis Matemático II", "credits": 8, "prerequisites": ["1_am1", "1_aga"], "status": 'PENDING' }, "2_fis2": { "id": "2_fis2", "name": "Física II", "credits": 8, "prerequisites": ["1_fis1"], "status": 'PENDING' }, "2_eym": { "id": "2_eym", "name": "Estabilidad y Resistencia de Materiales", "credits": 6, "prerequisites": ["1_fis1"], "status": 'PENDING' }, "2_proba": { "id": "2_proba", "name": "Probabilidad y Estadística", "credits": 6, "prerequisites": ["1_am1", "1_aga"], "status": 'PENDING' }, "2_eco": { "id": "2_eco", "name": "Economía", "credits": 4, "prerequisites": ["1_ing1"], "status": 'PENDING' }, "2_elec": { "id": "2_elec", "name": "Electrotecnia", "credits": 8, "prerequisites": ["2_fis2"], "status": 'PENDING' }, "2_termo": { "id": "2_termo", "name": "Termodinámica y Máquinas Térmicas", "credits": 6, "prerequisites": ["2_fis2"], "status": 'PENDING' }, "2_calcav": { "id": "2_calcav", "name": "Cálculo Avanzado", "credits": 6, "prerequisites": ["2_am2"], "status": 'PENDING' }, "2_ing3": { "id": "2_ing3", "name": "Inglés II", "credits": 4, "prerequisites": ["1_ing2"], "status": 'PENDING' },
  "3_med": { "id": "3_med", "name": "Medidas Eléctricas", "credits": 8, "prerequisites": ["2_elec"], "status": 'PENDING' }, "3_maq1": { "id": "3_maq1", "name": "Máquinas Eléctricas I", "credits": 8, "prerequisites": ["2_elec"], "status": 'PENDING' }, "3_elec1": { "id": "3_elec1", "name": "Electrónica I", "credits": 8, "prerequisites": ["2_elec"], "status": 'PENDING' }, "3_cn": { "id": "3_cn", "name": "Cálculo Numérico", "credits": 6, "prerequisites": ["2_calcav", "1_info2"], "status": 'PENDING' }, "3_leg": { "id": "3_leg", "name": "Legislación", "credits": 4, "prerequisites": ["2_eco"], "status": 'PENDING' }, "3_sys": { "id": "3_sys", "name": "Análisis de Señales y Sistemas", "credits": 8, "prerequisites": ["2_calcav"], "status": 'PENDING' }, "3_inst": { "id": "3_inst", "name": "Instalaciones Eléctricas", "credits": 8, "prerequisites": ["3_med"], "status": 'PENDING' }, "3_tecmat": { "id": "3_tecmat", "name": "Tecnología de los Materiales Eléctricos", "credits": 6, "prerequisites": ["1_qui", "2_fis2"], "status": 'PENDING' },
  "4_maq2": { "id": "4_maq2", "name": "Máquinas Eléctricas II", "credits": 8, "prerequisites": ["3_maq1"], "status": 'PENDING' }, "4_elec2": { "id": "4_elec2", "name": "Electrónica II", "credits": 8, "prerequisites": ["3_elec1"], "status": 'PENDING' }, "4_ctrl": { "id": "4_ctrl", "name": "Sistemas de Control", "credits": 8, "prerequisites": ["3_sys"], "status": 'PENDING' }, "4_cent": { "id": "4_cent", "name": "Centrales Eléctricas", "credits": 8, "prerequisites": ["2_termo", "3_maq1"], "status": 'PENDING' }, "4_redes": { "id": "4_redes", "name": "Líneas de Transmisión y Redes", "credits": 8, "prerequisites": ["3_inst"], "status": 'PENDING' }, "4_com": { "id": "4_com", "name": "Comunicaciones", "credits": 6, "prerequisites": ["3_sys"], "status": 'PENDING' }, "4_sh": { "id": "4_sh", "name": "Seguridad e Higiene Industrial", "credits": 4, "prerequisites": ["3_leg"], "status": 'PENDING' },
  "5_acc": { "id": "5_acc", "name": "Accionamientos Eléctricos", "credits": 8, "prerequisites": ["4_maq2", "4_elec2"], "status": 'PENDING' }, "5_prot": { "id": "5_prot", "name": "Protecciones Eléctricas", "credits": 8, "prerequisites": ["4_redes"], "status": 'PENDING' }, "5_org": { "id": "5_org", "name": "Organización Industrial", "credits": 6, "prerequisites": ["4_sh"], "status": 'PENDING' }, "5_proy": { "id": "5_proy", "name": "Proyecto Final", "credits": 10, "prerequisites": ["4_cent", "4_redes"], "status": 'PENDING' }, "5_elec1": { "id": "5_elec1", "name": "Electiva I", "credits": 6, "prerequisites": [], "status": 'PENDING' }, "5_elec2": { "id": "5_elec2", "name": "Electiva II", "credits": 6, "prerequisites": [], "status": 'PENDING' },
}
initial_semesters_data = [
  { "id": 1, "name": '1º Semestre', "year": 1, "subjectIds": ["1_am1", "1_aga", "1_qui", "1_info1", "1_ing1"] }, { "id": 2, "name": '2º Semestre', "year": 1, "subjectIds": ["1_fis1", "1_sdr", "1_info2", "1_ing2"] },
  { "id": 3, "name": '1º Semestre', "year": 2, "subjectIds": ["2_am2", "2_fis2", "2_eym", "2_proba", "2_eco"] }, { "id": 4, "name": '2º Semestre', "year": 2, "subjectIds": ["2_elec", "2_termo", "2_calcav", "2_ing3"] },
  { "id": 5, "name": '1º Semestre', "year": 3, "subjectIds": ["3_med", "3_maq1", "3_elec1", "3_cn", "3_leg"] }, { "id": 6, "name": '2º Semestre', "year": 3, "subjectIds": ["3_sys", "3_inst", "3_tecmat"] },
  { "id": 7, "name": '1º Semestre', "year": 4, "subjectIds": ["4_maq2", "4_elec2", "4_ctrl", "4_cent"] }, { "id": 8, "name": '2º Semestre', "year": 4, "subjectIds": ["4_redes", "4_com", "4_sh"] },
  { "id": 9, "name": '1º Semestre', "year": 5, "subjectIds": ["5_acc", "5_prot", "5_org", "5_elec1"] }, { "id": 10, "name": '2º Semestre', "year": 5, "subjectIds": ["5_proy", "5_elec2"] },
]

# --- ESTADO DE LA APLICACIÓN (SESSION STATE) ---
if 'subjects' not in st.session_state:
    st.session_state.subjects = initial_subjects_data.copy()
if 'semesters' not in st.session_state:
    st.session_state.semesters = initial_semesters_data.copy()
if 'plan_title' not in st.session_state:
    st.session_state.plan_title = 'Plan de Carrera de Paloma Mariño'

# --- ESTILOS CSS ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700;800&display=swap');
    html, body, [class*="st-"] {
        font-family: 'Nunito', sans-serif;
    }
    /* Ocultar la decoración principal de Streamlit */
    #root > div:nth-child(1) > div > div > div > div > section > div {padding-top: 2rem;}
    header {visibility: hidden;}
    .st-emotion-cache-18ni7ap {
        background: linear-gradient(to bottom right, #f3e8ff, #fee2e2, #e0f2fe);
    }
    /* Estilos para las tarjetas de año */
    .year-column {
        background-color: rgba(233, 213, 255, 0.6);
        border-radius: 1.5rem;
        padding: 1.5rem;
        border: 1px solid #e9d5ff;
        box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1), 0 2px 4px -2px rgb(0 0 0 / 0.1);
    }
    /* Estilos para las tarjetas de materia */
    .subject-card {
        border-radius: 0.75rem;
        padding: 0.75rem;
        text-align: center;
        font-weight: 600;
        color: #374151;
        cursor: pointer;
        transition: all 0.3s;
        position: relative;
    }
    .subject-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1), 0 2px 4px -2px rgb(0 0 0 / 0.1);
    }
    .subject-card-PENDING { background-color: white; }
    .subject-card-IN_PROGRESS { background-color: #bfdbfe; }
    .subject-card-APPROVED { background-color: #bbf7d0; }
    .subject-card-FAILED { background-color: #fecaca; }
</style>
""", unsafe_allow_html=True)


# --- FUNCIONES AUXILIARES ---
def create_circular_progress_svg(value, max_val, size, color):
    """Genera el código SVG para una barra de progreso circular."""
    if max_val == 0:
        percentage = 0
    else:
        percentage = (value / max_val) * 100
    
    radius = 70 if size == 'large' else 52
    stroke = 12 if size == 'large' else 10
    font_size = "2.25rem" if size == 'large' else "1.875rem"
    
    normalized_radius = radius - stroke * 2
    circumference = normalized_radius * 2 * 3.14159
    stroke_dashoffset = circumference - (percentage / 100) * circumference

    return f"""
        <svg height="{radius * 2}" width="{radius * 2}" style="transform: rotate(-90deg);">
            <circle stroke="#e5e7eb" stroke-width="{stroke}" fill="transparent" r="{normalized_radius}" cx="{radius}" cy="{radius}" />
            <circle
                stroke="{color}"
                stroke-width="{stroke}"
                stroke-dasharray="{circumference} {circumference}"
                style="stroke-dashoffset:{stroke_dashoffset}; stroke-linecap: round; transition: stroke-dashoffset 0.5s ease 0s;"
                fill="transparent"
                r="{normalized_radius}"
                cx="{radius}"
                cy="{radius}"
            />
            <text
                fill="#374151"
                x="50%"
                y="50%"
                text-anchor="middle"
                dy=".3em"
                font-size="{font_size}"
                font-weight="bold"
                style="transform: rotate(90deg); transform-origin: center;"
            >
                {round(percentage)}%
            </text>
        </svg>
    """

# --- UI DE LA APLICACIÓN ---

# Header
col1, col2 = st.columns([3, 1])
with col1:
    new_title = st.text_input("Título del Plan", value=st.session_state.plan_title, label_visibility="collapsed")
    if new_title != st.session_state.plan_title:
        st.session_state.plan_title = new_title
    st.caption("Ingeniería Eléctrica - UTN Avellaneda")
with col2:
    if st.button("🗑️ Resetear Datos", use_container_width=True):
        st.session_state.subjects = initial_subjects_data.copy()
        st.session_state.semesters = initial_semesters_data.copy()
        st.session_state.plan_title = 'Plan de Carrera de Paloma Mariño'
        st.rerun()

st.divider()

# Sección de Progreso
st.header("Mi Progreso", anchor=False, divider="rainbow")

total_credits = sum(s['credits'] for s in st.session_state.subjects.values())
total_approved_credits = sum(s['credits'] for s in st.session_state.subjects.values() if s['status'] == 'APPROVED')

# Progreso Total
st.markdown(f"""
<div style="display: flex; justify-content: center; flex-direction: column; align-items: center; gap: 0.5rem;">
    {create_circular_progress_svg(total_approved_credits, total_credits, 'large', '#8b5cf6')}
    <p style="font-weight: 600; color: #4b5563; text-align: center;">Total Carrera</p>
    <p style="font-size: 0.875rem; color: #6b7280;">{total_approved_credits} / {total_credits} créditos</p>
</div>
""", unsafe_allow_html=True)

st.write("") # Espacio

# Progreso por Año
years = sorted(list(set(s['year'] for s in st.session_state.semesters)))
year_cols = st.columns(len(years))

for i, year in enumerate(years):
    with year_cols[i]:
        subject_ids_for_year = [sid for s in st.session_state.semesters if s['year'] == year for sid in s['subjectIds']]
        year_total_credits = sum(st.session_state.subjects[sid]['credits'] for sid in subject_ids_for_year if sid in st.session_state.subjects)
        year_approved_credits = sum(st.session_state.subjects[sid]['credits'] for sid in subject_ids_for_year if sid in st.session_state.subjects and st.session_state.subjects[sid]['status'] == 'APPROVED')
        
        st.markdown(f"""
        <div style="display: flex; justify-content: center; flex-direction: column; align-items: center; gap: 0.5rem;">
            {create_circular_progress_svg(year_approved_credits, year_total_credits, 'small', '#22c55e')}
            <p style="font-weight: 600; color: #4b5563; text-align: center;">Año {year}</p>
            <p style="font-size: 0.875rem; color: #6b7280;">{year_approved_credits} / {year_total_credits} créditos</p>
        </div>
        """, unsafe_allow_html=True)


st.divider()

# Malla Curricular
st.header("Malla Curricular", anchor=False, divider="rainbow")

year_cols_main = st.columns(len(years))
year_names = {1: "Primer", 2: "Segundo", 3: "Tercer", 4: "Cuarto", 5: "Quinto"}

for i, year in enumerate(years):
    with year_cols_main[i]:
        st.markdown(f'<div class="year-column">', unsafe_allow_html=True)
        st.subheader(f"{year_names.get(year, '')} Año", anchor=False)
        
        semesters_in_year = [s for s in st.session_state.semesters if s['year'] == year]
        for semester in semesters_in_year:
            st.markdown(f"**{semester['name']}**")
            for subject_id in semester['subjectIds']:
                if subject_id in st.session_state.subjects:
                    subject = st.session_state.subjects[subject_id]
                    
                    # Chequear correlativas
                    prereqs_met = all(st.session_state.subjects.get(prereq_id, {}).get('status') == 'APPROVED' for prereq_id in subject['prerequisites'])
                    
                    # Mostrar tarjeta de materia
                    if st.button(subject['name'], key=subject_id, use_container_width=True):
                         st.session_state.editing_subject_id = subject_id
                    
                    # Aplicar estilos con markdown
                    st.markdown(f"""
                    <style>
                        div[data-testid*="stButton"] > button[data-st-id="{subject_id}"] {{
                            border-radius: 0.75rem;
                            text-align: center;
                            font-weight: 600;
                            color: #374151;
                            background-color: {'white' if subject['status'] == 'PENDING' else '#bfdbfe' if subject['status'] == 'IN_PROGRESS' else '#bbf7d0' if subject['status'] == 'APPROVED' else '#fecaca'};
                            opacity: {'1' if prereqs_met else '0.6'};
                            border: 1px solid #d1d5db;
                        }}
                    </style>
                    """, unsafe_allow_html=True)

        st.markdown('</div>', unsafe_allow_html=True)


# --- LÓGICA DEL MODAL (DIALOG) ---
if 'editing_subject_id' in st.session_state and st.session_state.editing_subject_id:
    subject_id_to_edit = st.session_state.editing_subject_id
    subject = st.session_state.subjects[subject_id_to_edit]

    @st.dialog("Editar Materia")
    def edit_subject_dialog():
        st.subheader(subject['name'])
        
        # Selector de estado
        status_options = ['PENDING', 'IN_PROGRESS', 'APPROVED', 'FAILED']
        current_status_index = status_options.index(subject['status'])
        new_status = st.radio("Estado", options=status_options, index=current_status_index, horizontal=True)
        if new_status != subject['status']:
            st.session_state.subjects[subject_id_to_edit]['status'] = new_status
            st.rerun()

        # Formulario para editar
        with st.form("edit_form"):
            new_name = st.text_input("Nombre", value=subject['name'])
            new_credits = st.number_input("Créditos", value=subject['credits'], min_value=1)
            
            all_subjects_options = {s_id: s['name'] for s_id, s in st.session_state.subjects.items() if s_id != subject_id_to_edit}
            new_prereqs = st.multiselect(
                "Correlativas",
                options=all_subjects_options.keys(),
                format_func=lambda s_id: all_subjects_options[s_id],
                default=subject['prerequisites']
            )

            submitted = st.form_submit_button("Guardar Cambios")
            if submitted:
                st.session_state.subjects[subject_id_to_edit]['name'] = new_name
                st.session_state.subjects[subject_id_to_edit]['credits'] = new_credits
                st.session_state.subjects[subject_id_to_edit]['prerequisites'] = new_prereqs
                st.session_state.editing_subject_id = None
                st.rerun()
        
        if st.button("Cerrar"):
            st.session_state.editing_subject_id = None
            st.rerun()

    edit_subject_dialog()

