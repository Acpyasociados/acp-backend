#!/usr/bin/env python3
"""
Script para enviar informe diagnóstico al asesor
Uso: python3 enviar-informe-asesor.py
"""

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import formatdate
from email import encoders
import os
from datetime import datetime

def enviar_informe_asesor(
    cliente_nombre,
    cliente_email,
    cliente_telefono,
    empresa,
    rut,
    pdf_path,
    email_asesor="asesor.pac@gmail.com"
):
    """
    Envía el informe diagnóstico al asesor para revisión.

    Parámetros:
    - cliente_nombre: Nombre del cliente
    - cliente_email: Email del cliente
    - cliente_telefono: Teléfono del cliente
    - empresa: Nombre de la empresa
    - rut: RUT de la empresa
    - pdf_path: Ruta del archivo PDF
    - email_asesor: Email del asesor (default: asesor.pac@gmail.com)
    """

    # Validar que el PDF existe
    if not os.path.exists(pdf_path):
        print(f"❌ Error: El archivo {pdf_path} no existe")
        return False

    # Crear mensaje
    msg = MIMEMultipart('alternative')
    msg['Subject'] = f"📋 Diagnóstico para Revisión: {empresa} - {cliente_nombre}"
    msg['From'] = "sistema@acp-diagnosticos.cl"
    msg['To'] = email_asesor
    msg['Date'] = formatdate(localtime=True)

    # Cuerpo del email en HTML
    body_html = f"""
    <html>
        <head>
            <style>
                body {{ font-family: Arial, sans-serif; color: #333; }}
                .container {{ max-width: 600px; margin: 0 auto; padding: 20px; }}
                .header {{ background: linear-gradient(135deg, #1a2d3e 0%, #2a3f52 100%); color: white; padding: 20px; border-radius: 8px; }}
                .section {{ margin: 20px 0; padding: 15px; background: #f9f9f9; border-left: 4px solid #d4a574; }}
                .label {{ font-weight: bold; color: #1a2d3e; }}
                .footer {{ margin-top: 30px; padding-top: 20px; border-top: 1px solid #ddd; color: #999; font-size: 12px; }}
                table {{ width: 100%; border-collapse: collapse; margin: 15px 0; }}
                th {{ background: #1a2d3e; color: white; padding: 10px; text-align: left; }}
                td {{ padding: 10px; border-bottom: 1px solid #ddd; }}
                .action {{ background: #d4a574; color: white; padding: 12px 20px; border-radius: 6px; display: inline-block; text-decoration: none; margin-top: 10px; }}
            </style>
        </head>
        <body>
            <div class="container">
                <div class="header">
                    <h2>📋 Nuevo Diagnóstico para Revisión</h2>
                    <p>Sistema ACP - Generado automáticamente</p>
                </div>

                <div class="section">
                    <h3>Datos del Cliente</h3>
                    <table>
                        <tr>
                            <td><span class="label">Nombre:</span></td>
                            <td>{cliente_nombre}</td>
                        </tr>
                        <tr>
                            <td><span class="label">Email:</span></td>
                            <td>{cliente_email}</td>
                        </tr>
                        <tr>
                            <td><span class="label">Teléfono:</span></td>
                            <td>{cliente_telefono}</td>
                        </tr>
                    </table>
                </div>

                <div class="section">
                    <h3>Datos de la Empresa</h3>
                    <table>
                        <tr>
                            <td><span class="label">Empresa:</span></td>
                            <td>{empresa}</td>
                        </tr>
                        <tr>
                            <td><span class="label">RUT:</span></td>
                            <td>{rut}</td>
                        </tr>
                    </table>
                </div>

                <div class="section">
                    <h3>Acciones Requeridas</h3>
                    <ol>
                        <li><strong>Revisar</strong> el informe adjunto (PDF)</li>
                        <li><strong>Validar</strong> que las oportunidades sean realistas para el sector</li>
                        <li><strong>Confirmar</strong> datos tributarios con el RUT informado</li>
                        <li><strong>Enviar</strong> al cliente con propuesta de plan (Básico: $49.900)</li>
                    </ol>
                </div>

                <div class="section">
                    <h3>Contenido del Informe</h3>
                    <ul>
                        <li>✅ Situación actual de la empresa</li>
                        <li>✅ 3 Oportunidades personalizadas (Digital, Costos, Tributaria)</li>
                        <li>✅ Plan de acción integrado 30 días</li>
                        <li>✅ Proyecciones financieras 90 días</li>
                    </ul>
                </div>

                <div class="section">
                    <h3>📎 Archivo Adjunto</h3>
                    <p>PDF: Diagnostico_Transportes_Aravena_Mejorado_Abril2026.pdf</p>
                    <p style="color: #d4a574; font-weight: bold;">Revisar y proceder con envío al cliente</p>
                </div>

                <div class="footer">
                    <p><strong>Sistema ACP - Diagnóstico Automático</strong></p>
                    <p>Generado: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}</p>
                    <p>Este es un email automático. No responder a esta dirección.</p>
                </div>
            </div>
        </body>
    </html>
    """

    # Adjuntar HTML
    msg.attach(MIMEText(body_html, 'html'))

    # Adjuntar PDF
    try:
        with open(pdf_path, 'rb') as attachment:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(attachment.read())

        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f'attachment; filename= {os.path.basename(pdf_path)}')
        msg.attach(part)
        print(f"✅ PDF adjuntado: {os.path.basename(pdf_path)}")
    except Exception as e:
        print(f"❌ Error al adjuntar PDF: {e}")
        return False

    # Configuración de envío (simulado para demostración)
    print("\n" + "="*60)
    print("📧 EMAIL LISTO PARA ENVÍO")
    print("="*60)
    print(f"De: sistema@acp-diagnosticos.cl")
    print(f"Para: {email_asesor}")
    print(f"Asunto: 📋 Diagnóstico para Revisión: {empresa} - {cliente_nombre}")
    print(f"\nCliente: {cliente_nombre}")
    print(f"Email: {cliente_email}")
    print(f"Teléfono: {cliente_telefono}")
    print(f"Empresa: {empresa}")
    print(f"RUT: {rut}")
    print(f"\nArchivo adjunto: {os.path.basename(pdf_path)}")
    print(f"Tamaño: {os.path.getsize(pdf_path)} bytes")
    print("\n" + "="*60)
    print("✅ Email listo para envío al asesor")
    print("="*60)

    return {
        'para': email_asesor,
        'asunto': f"📋 Diagnóstico para Revisión: {empresa} - {cliente_nombre}",
        'cliente_nombre': cliente_nombre,
        'cliente_email': cliente_email,
        'cliente_telefono': cliente_telefono,
        'empresa': empresa,
        'rut': rut,
        'pdf_file': os.path.basename(pdf_path),
        'pdf_size': os.path.getsize(pdf_path),
        'timestamp': datetime.now().isoformat()
    }

if __name__ == "__main__":
    # Datos de Tihare Aravena
    resultado = enviar_informe_asesor(
        cliente_nombre="Tihare Aravena",
        cliente_email="tihare.aravena16@gmail.com",
        cliente_telefono="+56 (por confirmar)",
        empresa="Transportes Aravena",
        rut="78.327.647-K",
        pdf_path="/sessions/loving-busy-darwin/mnt/Acp y Asociados/Diagnostico_Transportes_Aravena_Mejorado_Abril2026.pdf",
        email_asesor="asesor.pac@gmail.com"
    )

    if resultado:
        import json
        print("\n📋 Detalles del envío:")
        print(json.dumps(resultado, indent=2, ensure_ascii=False))
