#!/usr/bin/env python3
"""
Generador de Informes HTML - ACP
Crea pre-informes profesionales en HTML para revisión
"""

def generar_informe_html(datos_cliente, output_file):
    """
    Genera un informe diagnóstico en HTML profesional.
    """

    html = f"""
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Diagnóstico - {datos_cliente['empresa']}</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}

        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            color: #333;
            background-color: #f5f5f5;
            padding: 20px;
        }}

        .container {{
            max-width: 900px;
            margin: 0 auto;
            background-color: white;
            padding: 50px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            border-radius: 8px;
        }}

        .header {{
            border-bottom: 3px solid #1a2d3e;
            padding-bottom: 30px;
            margin-bottom: 30px;
        }}

        h1 {{
            font-size: 28px;
            color: #1a2d3e;
            margin-bottom: 5px;
            font-weight: 700;
        }}

        .subtitle {{
            font-size: 16px;
            color: #d4a574;
            font-weight: 600;
            margin-bottom: 20px;
        }}

        .client-info {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 15px;
            font-size: 13px;
            color: #666;
        }}

        .client-info-item {{
            padding: 8px 0;
        }}

        .client-info-label {{
            font-weight: 600;
            color: #1a2d3e;
        }}

        h2 {{
            font-size: 20px;
            color: #1a2d3e;
            margin-top: 35px;
            margin-bottom: 20px;
            padding-bottom: 10px;
            border-bottom: 2px solid #d4a574;
            font-weight: 700;
        }}

        h3 {{
            font-size: 14px;
            color: #1a2d3e;
            margin-top: 25px;
            margin-bottom: 12px;
            font-weight: 700;
        }}

        .section {{
            margin-bottom: 25px;
            line-height: 1.7;
        }}

        .datos-actuales {{
            background-color: #f9f9f9;
            padding: 15px;
            border-left: 4px solid #d4a574;
            margin: 15px 0;
            font-size: 13px;
        }}

        .datos-actuales p {{
            margin: 8px 0;
        }}

        .checkmark {{
            color: #27ae60;
            font-weight: bold;
            margin-right: 5px;
        }}

        .oportunidad {{
            background-color: #f0f8ff;
            padding: 20px;
            margin: 20px 0;
            border-radius: 6px;
            border-left: 4px solid #1a2d3e;
        }}

        .oportunidad h3 {{
            color: #1a2d3e;
            margin-top: 0;
        }}

        .oportunidad p {{
            margin: 10px 0;
            font-size: 13px;
            line-height: 1.7;
        }}

        .oportunidad strong {{
            color: #1a2d3e;
        }}

        .acciones {{
            background-color: white;
            padding: 12px;
            margin: 10px 0;
            border-radius: 4px;
            font-size: 13px;
            line-height: 1.8;
        }}

        .acciones ul {{
            list-style: none;
            padding-left: 20px;
        }}

        .acciones li {{
            margin: 6px 0;
        }}

        .acciones li:before {{
            content: "• ";
            color: #d4a574;
            font-weight: bold;
            margin-right: 8px;
        }}

        .plan {{
            background-color: #fffbf0;
            padding: 15px;
            margin: 15px 0;
            border-radius: 6px;
            font-size: 13px;
        }}

        .semana {{
            background-color: white;
            padding: 12px;
            margin: 10px 0;
            border-radius: 4px;
            border-left: 3px solid #d4a574;
        }}

        .semana strong {{
            color: #1a2d3e;
        }}

        .semana ul {{
            list-style: none;
            padding-left: 20px;
            margin-top: 8px;
        }}

        .semana li {{
            margin: 5px 0;
            font-size: 13px;
        }}

        .semana li:before {{
            content: "• ";
            color: #1a2d3e;
            margin-right: 8px;
        }}

        table {{
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
            font-size: 13px;
        }}

        thead {{
            background-color: #1a2d3e;
            color: white;
        }}

        th {{
            padding: 12px;
            text-align: left;
            font-weight: 600;
        }}

        td {{
            padding: 12px;
            border-bottom: 1px solid #ddd;
        }}

        tbody tr:nth-child(even) {{
            background-color: #f9f9f9;
        }}

        .notas {{
            background-color: #fff3cd;
            padding: 15px;
            border-radius: 6px;
            margin-top: 20px;
            font-size: 13px;
            border-left: 4px solid #d4a574;
        }}

        .notas ul {{
            list-style: none;
            padding-left: 20px;
            margin-top: 10px;
        }}

        .notas li {{
            margin: 8px 0;
        }}

        .notas li:before {{
            content: "✓ ";
            color: #27ae60;
            font-weight: bold;
            margin-right: 8px;
        }}

        .footer {{
            margin-top: 50px;
            padding-top: 20px;
            border-top: 1px solid #ddd;
            text-align: center;
            font-size: 12px;
            color: #999;
        }}

        .print-button {{
            position: fixed;
            top: 20px;
            right: 20px;
            padding: 10px 20px;
            background-color: #1a2d3e;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-weight: 600;
            font-size: 14px;
            z-index: 1000;
        }}

        .print-button:hover {{
            background-color: #d4a574;
        }}

        @media print {{
            body {{
                padding: 0;
                background-color: white;
            }}
            .container {{
                box-shadow: none;
                padding: 20px;
            }}
            .print-button {{
                display: none;
            }}
        }}

        @media (max-width: 768px) {{
            .container {{
                padding: 20px;
            }}

            .client-info {{
                grid-template-columns: 1fr;
            }}

            h1 {{
                font-size: 22px;
            }}
        }}
    </style>
</head>
<body>
    <button class="print-button" onclick="window.print()">🖨️ Imprimir / PDF</button>

    <div class="container">
        <!-- HEADER -->
        <div class="header">
            <h1>Diagnóstico de Oportunidades</h1>
            <p class="subtitle">{datos_cliente['sector']}</p>

            <div class="client-info">
                <div class="client-info-item">
                    <span class="client-info-label">Cliente:</span>
                    <span>{datos_cliente['nombre']}</span>
                </div>
                <div class="client-info-item">
                    <span class="client-info-label">Email:</span>
                    <span>{datos_cliente['email']}</span>
                </div>
                <div class="client-info-item">
                    <span class="client-info-label">Empresa:</span>
                    <span>{datos_cliente['empresa']}</span>
                </div>
                <div class="client-info-item">
                    <span class="client-info-label">Fecha Análisis:</span>
                    <span>{datos_cliente['fecha']}</span>
                </div>
            </div>
        </div>

        <!-- SECCIÓN 1: ANÁLISIS ACTUAL -->
        <h2>1. Situación Actual - {datos_cliente['empresa']} 2026</h2>

        <div class="section">
            <h3>Datos Verificados</h3>
            <div class="datos-actuales">
                <p><span class="checkmark">✓</span> <strong>Ventas Mensuales:</strong> {datos_cliente['ingresos_mensuales']}</p>
                <p><span class="checkmark">✓</span> <strong>Margen de Ganancia:</strong> {datos_cliente['margen']}</p>
                <p><span class="checkmark">✓</span> <strong>Clientes Activos:</strong> {datos_cliente['clientes_activos']}</p>
                <p><span class="checkmark">✓</span> <strong>Costos Principales:</strong> {datos_cliente['costos_principales']}</p>
                <p><span class="checkmark">✓</span> <strong>Principal Desafío:</strong> {datos_cliente['desafio_principal']}</p>
            </div>
        </div>

        <div class="section">
            <h3>Análisis del Mercado</h3>
            <p>{datos_cliente['analisis']}</p>
        </div>

        <!-- SECCIÓN 2: TOP 3 OPORTUNIDADES -->
        <h2>2. Top 3 Oportunidades Realistas</h2>

        <div class="oportunidad">
            <h3>Oportunidad #1: {datos_cliente['oportunidad_1']['titulo']}</h3>

            <p><strong>Por qué funciona:</strong></p>
            <p>{datos_cliente['oportunidad_1']['por_que']}</p>

            <p><strong>Clientes Objetivo:</strong></p>
            <p>{datos_cliente['oportunidad_1']['clientes']}</p>

            <p><strong>Acciones Concretas:</strong></p>
            <div class="acciones">
                {datos_cliente['oportunidad_1']['acciones']}
            </div>

            <p><strong style="color: #27ae60;">Proyección 90 días:</strong></p>
            <p style="color: #27ae60; font-weight: 600;">{datos_cliente['oportunidad_1']['proyeccion']}</p>
        </div>

        <div class="oportunidad">
            <h3>Oportunidad #2: {datos_cliente['oportunidad_2']['titulo']}</h3>

            <p><strong>Por qué funciona:</strong></p>
            <p>{datos_cliente['oportunidad_2']['por_que']}</p>

            <p><strong>Clientes Objetivo:</strong></p>
            <p>{datos_cliente['oportunidad_2']['clientes']}</p>

            <p><strong>Acciones Concretas:</strong></p>
            <div class="acciones">
                {datos_cliente['oportunidad_2']['acciones']}
            </div>

            <p><strong style="color: #27ae60;">Proyección 90 días:</strong></p>
            <p style="color: #27ae60; font-weight: 600;">{datos_cliente['oportunidad_2']['proyeccion']}</p>
        </div>

        <div class="oportunidad">
            <h3>Oportunidad #3: {datos_cliente['oportunidad_3']['titulo']}</h3>

            <p><strong>Por qué funciona:</strong></p>
            <p>{datos_cliente['oportunidad_3']['por_que']}</p>

            <p><strong>Clientes Objetivo:</strong></p>
            <p>{datos_cliente['oportunidad_3']['clientes']}</p>

            <p><strong>Acciones Concretas:</strong></p>
            <div class="acciones">
                {datos_cliente['oportunidad_3']['acciones']}
            </div>

            <p><strong style="color: #27ae60;">Proyección 90 días:</strong></p>
            <p style="color: #27ae60; font-weight: 600;">{datos_cliente['oportunidad_3']['proyeccion']}</p>
        </div>

        <!-- SECCIÓN 3: PLAN DE ACCIÓN -->
        <h2>3. Plan de Acción Integrado - 30 Días</h2>

        <div class="plan">
            <p><strong style="color: #1a2d3e;">Enfoque Principal:</strong></p>
            <p>{datos_cliente['plan_enfoque']}</p>

            <div class="semana">
                <strong>Semana 1</strong>
                <ul>
                    {datos_cliente['plan_semana_1']}
                </ul>
            </div>

            <div class="semana">
                <strong>Semana 2</strong>
                <ul>
                    {datos_cliente['plan_semana_2']}
                </ul>
            </div>

            <div class="semana">
                <strong>Semana 3</strong>
                <ul>
                    {datos_cliente['plan_semana_3']}
                </ul>
            </div>

            <div class="semana">
                <strong>Semana 4</strong>
                <ul>
                    {datos_cliente['plan_semana_4']}
                </ul>
            </div>

            <p style="margin-top: 15px;"><strong style="color: #1a2d3e;">Meta Mes 1:</strong></p>
            <p>{datos_cliente['plan_meta']}</p>
        </div>

        <!-- SECCIÓN 4: PROYECCIONES -->
        <h2>4. Proyecciones Financieras - 90 Días</h2>

        <table>
            <thead>
                <tr>
                    <th>Período</th>
                    <th>Ingresos</th>
                    <th>Margen %</th>
                    <th>Ganancia Neta</th>
                    <th>Métrica Key</th>
                </tr>
            </thead>
            <tbody>
"""

    for proj in datos_cliente['proyecciones']:
        html += f"""
                <tr>
                    <td><strong>{proj['periodo']}</strong></td>
                    <td>{proj['ingresos']}</td>
                    <td>{proj['margen']}</td>
                    <td><strong style="color: #27ae60;">{proj['ganancia']}</strong></td>
                    <td>{proj['metrica']}</td>
                </tr>
"""

    html += f"""
            </tbody>
        </table>

        <div class="notas">
            <strong>Notas Importantes:</strong>
            <ul>
                {datos_cliente['notas_importantes']}
            </ul>
        </div>

        <div class="footer">
            <p>Diagnóstico preparado por ACP Diagnóstico y Consultoría</p>
            <p>Este documento contiene análisis confidencial y específico para {datos_cliente['empresa']}</p>
        </div>
    </div>
</body>
</html>
"""

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html)

    print(f"✅ Informe HTML generado: {output_file}")


if __name__ == "__main__":
    # Ejemplo de uso
    datos = {
        'nombre': 'Tihare aravena',
        'email': 'Tihare.aravena16@gmail.com',
        'empresa': 'Transportes Aravena',
        'sector': 'Servicios de Transporte en Ruta',
        'fecha': 'Abril 2026',
        'ingresos_mensuales': 'CLP $23.000.000',
        'margen': '15%',
        'clientes_activos': 3,
        'costos_principales': 'Combustible, personal, mantención camiones',
        'desafio_principal': 'Bajo alcance en mercado (3 clientes = concentración del riesgo)',
        'analisis': 'El segmento de servicios de transporte en ruta tiene alta demanda pero está fragmentado. Las empresas pequeñas como Transportes Aravena compiten principalmente en agilidad operativa, confiabilidad y relaciones cercanas. La principal limitación es el bajo alcance comercial (3 clientes), lo que genera vulnerabilidad y dificulta el crecimiento.',

        'oportunidad_1': {
            'titulo': 'Expansión Digital y Marketing Especializado',
            'por_que': 'La mayoría de transportistas pequeños NO tienen presencia digital efectiva. Empresas medianas buscan proveedores confiables online. Presencia en LinkedIn, sitio web y Google My Business genera leads sin inversión comercial directa.',
            'clientes': 'Distribuidoras de alimentos | Empresas de logística | E-commerce | Proveedores de servicios',
            'acciones': '<li>Semana 1: Crear perfil LinkedIn, Google My Business, WhatsApp Business</li><li>Semana 2: Propuesta de valor clara y presupuesto</li><li>Semana 3: Contactar 15-20 empresas vía LinkedIn</li><li>Semana 4: Seguimiento y cierre</li>',
            'proyeccion': '2-3 nuevos clientes medianos = +$4-7M en ingresos mensuales'
        },

        'oportunidad_2': {
            'titulo': 'Optimización de Costos Operativos (Margen +5-8%)',
            'por_que': 'Con ventas estables, la optimización de costos es el apalancamiento más directo. Reducción de combustible y mantención en 5-8% genera $1.15M-1.84M en ganancias adicionales sin aumentar ventas.',
            'clientes': 'Interno - mejora de márgenes propios',
            'acciones': '<li>Auditoría de rutas: Optimizar kilómetros recorridos</li><li>Mantenimiento preventivo: Reducir reparaciones de emergencia</li><li>Negociación de combustible con tarjeta corporativa</li><li>Capacitación en manejo eficiente</li>',
            'proyeccion': 'Margen mejora de 15% a 20-23% = +$1.15M-1.84M mensuales en resultado neto'
        },

        'oportunidad_3': {
            'titulo': 'Formalización Tributaria y Beneficios Pyme',
            'por_que': 'Transportes Aravena genera $3.45M netos mensuales (~$41.4M anuales). Existen beneficios tributarios para Pymes: tasa reducida (19% vs 27%), deducciones adicionales y acceso a financiamiento preferencial.',
            'clientes': 'Interno - optimización tributaria',
            'acciones': '<li>Revisar estructura fiscal actual</li><li>Evaluar cambio a régimen Pyme si es viable</li><li>Optimizar deducciones: combustible, mantención, seguros</li><li>Acceso a créditos Pyme con tasa preferencial</li>',
            'proyeccion': 'Ahorro tributario estimado: $800k-1.2M anuales = +$66k-100k/mes'
        },

        'plan_enfoque': 'Expansión Digital + Optimización de Costos',
        'plan_semana_1': '<li>Crear presencia digital (LinkedIn, Google My Business, WhatsApp Business)</li><li>Iniciar auditoría de rutas y consumo de combustible</li><li>Consultar con contador sobre beneficios tributarios Pyme</li>',
        'plan_semana_2': '<li>Contactar 10 empresas potenciales vía LinkedIn</li><li>Implementar primera ronda de optimización de rutas</li><li>Solicitar presupuesto para tarjeta corporativa de combustible</li>',
        'plan_semana_3': '<li>Seguimiento a contactos y envío de propuestas</li><li>Capacitación interna en manejo eficiente</li><li>Análisis de impacto tributario de posibles cambios</li>',
        'plan_semana_4': '<li>Cierre de negociaciones con clientes potenciales</li><li>Revisión de resultados de optimización de rutas</li><li>Plan de implementación tributaria</li>',
        'plan_meta': '1 nuevo cliente + mejora de margen a 17% + plan tributario definido',

        'proyecciones': [
            {'periodo': 'Mes 1 (Actual)', 'ingresos': 'CLP $23.0M', 'margen': '15%', 'ganancia': 'CLP $3.45M', 'metrica': '3 clientes'},
            {'periodo': 'Mes 2 (+Digital)', 'ingresos': 'CLP $27.0M', 'margen': '17%', 'ganancia': 'CLP $4.59M', 'metrica': '4-5 clientes'},
            {'periodo': 'Mes 3 (+Optimización)', 'ingresos': 'CLP $30.0M', 'margen': '20%', 'ganancia': 'CLP $6.00M', 'metrica': '5-6 clientes'},
        ],

        'notas_importantes': '<li>Proyecciones conservadoras basadas en mercado actual</li><li>Requieren esfuerzo enfocado en expansión digital</li><li>Beneficios tributarios son inmediatos sin inversión operativa</li><li>Potencial neto: +$2.55M/mes (+74% en 90 días)</li>'
    }

    generar_informe_html(datos, "Diagnostico_Transportes_Aravena.html")
