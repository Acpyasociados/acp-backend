#!/usr/bin/env python3
"""
Generador de Informes Diagnósticos Mejorado - ACP
Versión 2.0 - Integra datos tributarios y operacionales
Crea informes personalizados según sector y datos reales del cliente
Uso: python3 generador-informe-mejorado.py
"""

from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
from datetime import datetime

def generar_oportunidades_dinamicas(datos_cliente):
    """
    Genera 3 oportunidades dinámicas basadas en el sector y datos del cliente.

    Retorna dict con estructura:
    {
        'oportunidad_1': {...},
        'oportunidad_2': {...},
        'oportunidad_3': {...}
    }
    """
    sector = datos_cliente.get('sector', 'servicios_profesionales').lower()
    redes = datos_cliente.get('redes_sociales', 'no').lower()
    plataformas = datos_cliente.get('plataformas', '')
    combustible = datos_cliente.get('consumo_combustible', 0)
    margen_actual = float(datos_cliente.get('margen', 20))
    ventas = datos_cliente.get('ventas_mensuales_num', 0)

    oportunidades = {}

    # OPORTUNIDAD 1: DIGITAL (para todos)
    if redes == 'no':
        oportunidad_1_titulo = "Crear Presencia Digital desde Cero"
        oportunidad_1_por_que = "Sin presencia digital pierdes 60-80% de clientes potenciales. No requiere inversión inicial."
    else:
        oportunidad_1_titulo = "Potenciar Presencia Digital Existente"
        oportunidad_1_por_que = f"Ya tienes presencia en {plataformas}. Optimizar genera 30-50% más leads."

    oportunidades['oportunidad_1'] = {
        'titulo': oportunidad_1_titulo,
        'por_que': oportunidad_1_por_que,
        'clientes': 'Nuevos clientes potenciales en línea',
        'acciones': '• Semana 1: Auditar presencia actual o crear perfil<br/>• Semana 2: Optimizar contenido y contacto<br/>• Semana 3: Campaña de alcance<br/>• Semana 4: Análisis de resultados',
        'proyeccion': '+15-25% en leads = +$2-5M mensuales'
    }

    # OPORTUNIDAD 2: COSTOS o SECTOR ESPECÍFICO
    if combustible and combustible > 0:
        # Es una empresa con costos de combustible (transporte, servicios campo, etc)
        ahorro_mensual = int(combustible * 65 * 0.15)  # Estimación: 65 CLP/liter, 15% mejora
        oportunidades['oportunidad_2'] = {
            'titulo': "Optimización de Costos Operacionales (Combustible)",
            'por_que': "Costos de combustible al alza. 15-20% optimización = +margen sin vender más.",
            'clientes': 'Optimización interna',
            'acciones': '• Semana 1: Auditar rutas con GPS<br/>• Semana 2: Implementar tarjeta de combustible<br/>• Semana 3: Capacitación en manejo eficiente<br/>• Semana 4: Medir resultados',
            'proyeccion': f'+${ahorro_mensual:,.0f} mensuales en margen'
        }
    else:
        # Empresa de servicios o comercio sin combustible
        oportunidades['oportunidad_2'] = {
            'titulo': "Optimización de Márgenes y Procesos",
            'por_que': "Mejorar procesos permite vender más rentablemente sin aumentar costos.",
            'clientes': 'Optimización interna',
            'acciones': '• Semana 1: Mapeo de procesos y cuellos de botella<br/>• Semana 2: Implementar mejoras de eficiencia<br/>• Semana 3: Automatización de tareas repetitivas<br/>• Semana 4: Verificación de resultados',
            'proyeccion': f'+{int((margen_actual * 0.2))}% de mejora en margen = +${int(ventas * margen_actual * 0.003):,.0f} mensuales'
        }

    # OPORTUNIDAD 3: TRIBUTARIA
    oportunidades['oportunidad_3'] = {
        'titulo': "Optimización Tributaria y Régimen Fiscal",
        'por_que': "Existen beneficios tributarios según RUT y estructura. Revisar con contador.",
        'clientes': 'Optimización fiscal interna',
        'acciones': f"• Contactar a {datos_cliente.get('contador', 'un contador profesional')}<br/>• Revisar régimen fiscal actual<br/>• Evaluar régimen Pro Pyme o esquemas alternativos<br/>• Implementar optimización fiscal",
        'proyeccion': "$500k-$2M anuales en ahorro potencial"
    }

    return oportunidades

def generar_informe_mejorado(datos_cliente, output_file):
    """
    Genera un informe diagnóstico integrado con datos del formulario mejorado.

    datos_cliente debe incluir:
    - Básicos: nombre, email, empresa, sector, fecha
    - Financieros: ingresos_mensuales, margen, clientes_activos, costos_principales
    - NUEVOS - Tributarios: rut, contador
    - NUEVOS - Operacionales: consumo_combustible
    - NUEVOS - Digital: redes_sociales, plataformas
    - Estratégicos: problema_principal, objetivo_6meses
    """

    # Generar oportunidades dinámicamente
    oportunidades = generar_oportunidades_dinamicas(datos_cliente)
    datos_cliente.update(oportunidades)

    doc = SimpleDocTemplate(
        output_file,
        pagesize=letter,
        rightMargin=0.75*inch,
        leftMargin=0.75*inch,
        topMargin=0.75*inch,
        bottomMargin=0.75*inch
    )

    # Estilos
    styles = getSampleStyleSheet()
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=18,
        textColor=colors.HexColor('#1a2d3e'),
        spaceAfter=6,
        alignment=TA_LEFT,
        bold=True
    )

    heading_style = ParagraphStyle(
        'CustomHeading',
        parent=styles['Heading2'],
        fontSize=13,
        textColor=colors.HexColor('#1a2d3e'),
        spaceAfter=8,
        spaceBefore=12,
        bold=True
    )

    normal_style = ParagraphStyle(
        'CustomNormal',
        parent=styles['Normal'],
        fontSize=10,
        alignment=TA_JUSTIFY,
        spaceAfter=6
    )

    story = []

    # 1. TÍTULO
    story.append(Paragraph("Diagnóstico de Oportunidades", title_style))
    story.append(Paragraph(datos_cliente['sector'], title_style))
    story.append(Spacer(1, 0.1*inch))

    # Información del cliente
    client_info = f"""
    <b>Cliente:</b> {datos_cliente['nombre']} &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
    <b>Email:</b> {datos_cliente['email']}<br/>
    <b>Empresa:</b> {datos_cliente['empresa']} &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
    <b>RUT:</b> {datos_cliente.get('rut', 'N/A')}<br/>
    <b>Fecha Análisis:</b> {datos_cliente['fecha']}
    """
    story.append(Paragraph(client_info, normal_style))
    story.append(Spacer(1, 0.15*inch))

    # 2. ANÁLISIS ACTUAL
    story.append(Paragraph(f"1. Situación Actual - {datos_cliente['empresa']} 2026", heading_style))

    # Datos verificados
    datos_actuales = f"""
    <b>Datos del Cliente:</b><br/>
    ✓ Ventas Mensuales: {datos_cliente.get('ingresos_mensuales', 'N/A')}<br/>
    ✓ Margen de Ganancia: {datos_cliente.get('margen', 'N/A')}%<br/>
    ✓ Clientes Activos: {datos_cliente.get('clientes_activos', 'N/A')}<br/>
    ✓ Costos Principales: {datos_cliente.get('costos_principales', 'N/A')}<br/>
    ✓ Presencia Digital: {datos_cliente.get('redes_sociales', 'No')} ({datos_cliente.get('plataformas', 'ninguna')})<br/>
    """

    if datos_cliente.get('consumo_combustible'):
        datos_actuales += f"✓ Consumo Combustible: {datos_cliente.get('consumo_combustible')} litros/mes<br/>"

    story.append(Paragraph(datos_actuales, normal_style))
    story.append(Spacer(1, 0.1*inch))

    # Problema y objetivo
    desafio_text = f"""
    <b>Desafío Principal:</b> {datos_cliente.get('problema_principal', 'Crecimiento y optimización')}<br/>
    <b>Objetivo 6 Meses:</b> {datos_cliente.get('objetivo_6meses', 'Aumentar ingresos y márgenes')}
    """
    story.append(Paragraph(desafio_text, normal_style))
    story.append(Spacer(1, 0.15*inch))

    # 3. TOP 3 OPORTUNIDADES
    story.append(Paragraph("2. Top 3 Oportunidades Personalizadas", heading_style))

    for i in range(1, 4):
        op_key = f'oportunidad_{i}'
        oport = datos_cliente[op_key]

        story.append(Paragraph(f"<b>Oportunidad #{i}: {oport['titulo']}</b>", heading_style))

        op_text = f"""
        <b>Por qué funciona:</b> {oport['por_que']}<br/><br/>
        <b>Clientes Objetivo:</b> {oport['clientes']}<br/><br/>
        <b>Acciones Concretas:</b><br/>
        {oport['acciones']}<br/><br/>
        <b>Proyección 90 días:</b> {oport['proyeccion']}
        """
        story.append(Paragraph(op_text, normal_style))

        if i < 3:
            story.append(Spacer(1, 0.15*inch))

    story.append(Spacer(1, 0.2*inch))

    # 4. PLAN DE ACCIÓN
    story.append(Paragraph("3. Plan de Acción Integrado - 30 Días", heading_style))

    plan_enfoque = "Digitalización + Optimización + Tributaria"
    plan_text = f"""
    <b>Enfoque Principal:</b> {plan_enfoque}<br/><br/>

    <b>Semana 1:</b> Diagnóstico y planificación<br/>
    • Auditoria de presencia digital actual<br/>
    • Revisión de costos operacionales<br/>
    • Contactar asesor tributario<br/><br/>

    <b>Semana 2:</b> Implementación inicial<br/>
    • Implementar mejoras digitales prioritarias<br/>
    • Iniciar optimización de costos<br/>
    • Análisis de régimen fiscal<br/><br/>

    <b>Semana 3:</b> Ejecución y validación<br/>
    • Campañas digitales en marcha<br/>
    • Procesos de ahorro implementados<br/>
    • Plan tributario definido<br/><br/>

    <b>Semana 4:</b> Medición y ajuste<br/>
    • Análisis de resultados digitales<br/>
    • Validar ahorros en costos<br/>
    • Implementar optimización fiscal<br/><br/>

    <b>Meta Mes 1:</b> Presencia digital mejorada + primeros ahorros visibles + plan tributario ejecutándose
    """
    story.append(Paragraph(plan_text, normal_style))
    story.append(Spacer(1, 0.2*inch))

    # 5. NOTAS IMPORTANTES
    story.append(Paragraph("4. Notas Importantes", heading_style))

    notas = f"""
    ✓ <b>Datos precisos:</b> Este diagnóstico se basa en información real de {datos_cliente['empresa']}<br/>
    ✓ <b>Realista:</b> Proyecciones conservadoras, alcanzables en 90 días<br/>
    ✓ <b>Accionable:</b> Requiere enfoque y esfuerzo, pero sin inversión mayor<br/>
    ✓ <b>Tributario:</b> Validar todas las recomendaciones con {datos_cliente.get('contador', 'asesor tributario profesional')}<br/>
    ✓ <b>Seguimiento:</b> Próxima revisión en 30 días para ajustes
    """
    story.append(Paragraph(notas, normal_style))

    # Construir PDF
    doc.build(story)
    print(f"✅ Informe mejorado generado: {output_file}")

if __name__ == "__main__":
    # Ejemplo de uso con datos del formulario mejorado
    datos = {
        'nombre': 'Tihare Aravena',
        'email': 'tihare.aravena16@gmail.com',
        'empresa': 'Transportes Aravena',
        'rut': '78.327.647-K',
        'sector': 'Servicios de Transporte',
        'fecha': 'Abril 2026',
        'ingresos_mensuales': 'CLP $23.000.000',
        'margen': 15,
        'clientes_activos': 3,
        'costos_principales': 'Combustible, personal, mantención',
        'problema_principal': 'Bajo alcance en mercado, concentración de clientes',
        'objetivo_6meses': 'Diversificar clientes, mejorar márgenes, optimizar costos',
        # Nuevos campos
        'redes_sociales': 'no',
        'plataformas': 'ninguna',
        'consumo_combustible': 500,
        'contador': 'Por definir',
        'ventas_mensuales_num': 23000000,
    }

    generar_informe_mejorado(datos, "diagnostico_mejorado_test.pdf")
