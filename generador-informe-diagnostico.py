#!/usr/bin/env python3
"""
Generador de Informes Diagnósticos - ACP
Crea informes siguiendo la plantilla estándar
Uso: python3 generador-informe-diagnostico.py
"""

from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
from datetime import datetime

def generar_informe(datos_cliente, output_file):
    """
    Genera un informe diagnóstico basado en los datos del cliente.

    datos_cliente = {
        'nombre': str,
        'email': str,
        'empresa': str,
        'sector': str,
        'ubicacion': str,
        'fecha': str,
        'ingresos_mensuales': str,
        'margen': str,
        'clientes_activos': int,
        'costos_principales': str,
        'desafio_principal': str,
        'analisis': str,
        'oportunidad_1': {
            'titulo': str,
            'por_que': str,
            'clientes': str,
            'acciones': str,
            'proyeccion': str
        },
        'oportunidad_2': {...},
        'oportunidad_3': {...},
        'plan_enfoque': str,
        'plan_semana_1': str,
        'plan_semana_2': str,
        'plan_semana_3': str,
        'plan_semana_4': str,
        'plan_meta': str,
        'proyecciones': [
            {'periodo': str, 'ingresos': str, 'margen': str, 'ganancia': str, 'metrica': str},
            ...
        ],
        'notas_importantes': str
    }
    """

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
    <b>Fecha Análisis:</b> {datos_cliente['fecha']}
    """
    story.append(Paragraph(client_info, normal_style))
    story.append(Spacer(1, 0.15*inch))

    # 2. ANÁLISIS ACTUAL
    story.append(Paragraph(f"1. Situación Actual - {datos_cliente['empresa']} 2026", heading_style))

    datos_actuales = f"""
    <b>Datos Verificados:</b><br/>
    ✓ Ventas Mensuales: {datos_cliente['ingresos_mensuales']}<br/>
    ✓ Margen de Ganancia: {datos_cliente['margen']}<br/>
    ✓ Clientes Activos: {datos_cliente['clientes_activos']}<br/>
    ✓ Costos Principales: {datos_cliente['costos_principales']}<br/>
    ✓ Principal Desafío: {datos_cliente['desafio_principal']}<br/>
    """
    story.append(Paragraph(datos_actuales, normal_style))
    story.append(Spacer(1, 0.1*inch))

    story.append(Paragraph(f"<b>Análisis del Mercado:</b><br/>{datos_cliente['analisis']}", normal_style))
    story.append(Spacer(1, 0.15*inch))

    # 3. TOP 3 OPORTUNIDADES
    story.append(Paragraph("2. Top 3 Oportunidades Realistas", heading_style))

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

    plan_text = f"""
    <b>Enfoque Principal:</b> {datos_cliente['plan_enfoque']}<br/><br/>

    <b>Semana 1:</b><br/>
    {datos_cliente['plan_semana_1']}<br/><br/>

    <b>Semana 2:</b><br/>
    {datos_cliente['plan_semana_2']}<br/><br/>

    <b>Semana 3:</b><br/>
    {datos_cliente['plan_semana_3']}<br/><br/>

    <b>Semana 4:</b><br/>
    {datos_cliente['plan_semana_4']}<br/><br/>

    <b>Meta Mes 1:</b> {datos_cliente['plan_meta']}
    """
    story.append(Paragraph(plan_text, normal_style))
    story.append(Spacer(1, 0.2*inch))

    # 5. PROYECCIONES
    story.append(Paragraph("4. Proyecciones Financieras - 90 Días", heading_style))

    # Construir tabla de proyecciones
    tabla_data = [['Período', 'Ingresos', 'Margen %', 'Ganancia Neta', 'Métrica']]
    for proj in datos_cliente['proyecciones']:
        tabla_data.append([
            proj['periodo'],
            proj['ingresos'],
            proj['margen'],
            proj['ganancia'],
            proj['metrica']
        ])

    table = Table(tabla_data, colWidths=[1.3*inch, 1.2*inch, 1*inch, 1.4*inch, 1*inch])
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#1a2d3e')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 10),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.HexColor('#f0f0f0')),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))

    story.append(table)
    story.append(Spacer(1, 0.2*inch))

    story.append(Paragraph(f"<b>Importante:</b><br/>{datos_cliente['notas_importantes']}", normal_style))

    # Construir PDF
    doc.build(story)
    print(f"✅ Informe generado: {output_file}")

if __name__ == "__main__":
    # Ejemplo de uso
    datos = {
        'nombre': 'Tihare aravena',
        'email': 'Tihare.aravena16@gmail.com',
        'empresa': 'Transportes Aravena',
        'sector': 'Servicios de Transporte en Ruta',
        'ubicacion': 'Región Metropolitana',
        'fecha': 'Abril 2026',
        'ingresos_mensuales': 'CLP $23.000.000',
        'margen': '15%',
        'clientes_activos': 3,
        'costos_principales': 'Combustible, personal, mantención camiones',
        'desafio_principal': 'Bajo alcance en mercado (3 clientes = concentración del riesgo)',
        'analisis': 'El segmento de servicios de transporte en ruta tiene alta demanda pero está fragmentado.',
        'oportunidad_1': {
            'titulo': 'Expansión Digital y Marketing Especializado',
            'por_que': 'La mayoría de transportistas pequeños NO tienen presencia digital efectiva.',
            'clientes': 'Distribuidoras de alimentos | Empresas de logística | E-commerce',
            'acciones': '• Semana 1: Crear LinkedIn, Google My Business<br/>• Semana 2: Propuesta de valor<br/>• Semana 3: Contactar 15-20 empresas<br/>• Semana 4: Seguimiento',
            'proyeccion': '2-3 nuevos clientes = +$4-7M en ingresos mensuales'
        },
        'oportunidad_2': {
            'titulo': 'Optimización de Costos Operativos (Margen +5-8%)',
            'por_que': 'Optimizar costos genera más ganancias sin aumentar ventas.',
            'clientes': 'Interno - mejora de márgenes propios',
            'acciones': '• Auditoría de rutas con GPS<br/>• Mantenimiento preventivo<br/>• Negociación de combustible<br/>• Capacitación en manejo eficiente',
            'proyeccion': 'Margen mejora a 20-23% = +$1.15M-1.84M mensuales'
        },
        'oportunidad_3': {
            'titulo': 'Formalización Tributaria y Beneficios Pyme',
            'por_que': 'Existen beneficios tributarios: tasa reducida 19% vs 27%.',
            'clientes': 'Interno - optimización tributaria',
            'acciones': '• Revisar estructura fiscal<br/>• Evaluar cambio a régimen Pyme<br/>• Optimizar deducciones<br/>• Acceso a créditos Pyme',
            'proyeccion': 'Ahorro tributario: $800k-1.2M anuales = +$66k-100k/mes'
        },
        'plan_enfoque': 'Expansión Digital + Optimización de Costos',
        'plan_semana_1': '• Crear presencia digital<br/>• Iniciar auditoría de rutas<br/>• Consultar beneficios tributarios',
        'plan_semana_2': '• Contactar 10 empresas potenciales<br/>• Implementar optimización de rutas<br/>• Solicitar presupuesto combustible',
        'plan_semana_3': '• Seguimiento comercial<br/>• Capacitación en manejo eficiente<br/>• Análisis impacto tributario',
        'plan_semana_4': '• Cierre de negociaciones<br/>• Revisión de resultados<br/>• Plan tributario definido',
        'plan_meta': '1 nuevo cliente + mejora de margen a 17% + plan tributario definido',
        'proyecciones': [
            {'periodo': 'Mes 1 (Actual)', 'ingresos': 'CLP $23.0M', 'margen': '15%', 'ganancia': 'CLP $3.45M', 'metrica': '3 clientes'},
            {'periodo': 'Mes 2 (+Digital)', 'ingresos': 'CLP $27.0M', 'margen': '17%', 'ganancia': 'CLP $4.59M', 'metrica': '4-5 clientes'},
            {'periodo': 'Mes 3 (+Optimización)', 'ingresos': 'CLP $30.0M', 'margen': '20%', 'ganancia': 'CLP $6.00M', 'metrica': '5-6 clientes'},
        ],
        'notas_importantes': '✓ Proyecciones conservadoras<br/>✓ Requieren esfuerzo enfocado<br/>✓ Beneficios inmediatos<br/>✓ Potencial neto: +$2.55M/mes (+74% en 90 días)'
    }

    generar_informe(datos, "diagnostico_test.pdf")
