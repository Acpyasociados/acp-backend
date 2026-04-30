#!/usr/bin/env python3
"""
Script para enviar PDF realmente a asesor.pac@gmail.com
Usa SendGrid API para envío de emails con archivos adjuntos
"""

import os
import base64
from pathlib import Path
from datetime import datetime

def enviar_pdf_sendgrid(
    pdf_path,
    destinatario="asesor.pac@gmail.com",
    remitente="sistema@acp-diagnosticos.cl",
    api_key=None
):
    """
    Envía el PDF usando SendGrid API.

    Requiere:
    - SENDGRID_API_KEY como variable de entorno
    - O pasar api_key como parámetro
    """

    try:
        from sendgrid import SendGridAPIClient
        from sendgrid.helpers.mail import Mail, Attachment, FileContent, FileName, FileType, Disposition
    except ImportError:
        print("❌ SendGrid no está instalado. Instalando...")
        os.system("pip install sendgrid --break-system-packages -q")
        from sendgrid import SendGridAPIClient
        from sendgrid.helpers.mail import Mail, Attachment, FileContent, FileName, FileType, Disposition

    # Obtener API key
    api_key = api_key or os.getenv('SENDGRID_API_KEY')

    if not api_key:
        print("⚠️  SENDGRID_API_KEY no configurada")
        print("Instrucciones para configurar SendGrid:")
        print("1. Ir a https://sendgrid.com")
        print("2. Crear cuenta y obtener API key")
        print("3. Exportar: export SENDGRID_API_KEY='tu_api_key'")
        print("4. Ejecutar este script nuevamente")
        return False

    # Validar archivo
    if not os.path.exists(pdf_path):
        print(f"❌ Archivo no existe: {pdf_path}")
        return False

    try:
        # Leer PDF y codificar en base64
        with open(pdf_path, 'rb') as attachment:
            attachment_data = base64.b64encode(attachment.read()).decode()

        # Crear mensaje
        message = Mail(
            from_email=remitente,
            to_emails=destinatario,
            subject='📋 Diagnóstico para Revisión: Transportes Aravena - Tihare Aravena',
            html_content=generar_html_email()
        )

        # Adjuntar PDF
        attachment = Attachment(
            file_content=FileContent(attachment_data),
            file_name=FileName(os.path.basename(pdf_path)),
            file_type=FileType('application/pdf'),
            disposition=Disposition('attachment')
        )
        message.attachment = attachment

        # Enviar
        sg = SendGridAPIClient(api_key)
        response = sg.send(message)

        print("✅ EMAIL ENVIADO EXITOSAMENTE")
        print(f"Destinatario: {destinatario}")
        print(f"Status: {response.status_code}")
        print(f"ID del mensaje: {response.headers.get('X-Message-Id', 'N/A')}")
        return True

    except Exception as e:
        print(f"❌ Error al enviar: {e}")
        return False

def generar_html_email():
    """Genera el cuerpo HTML del email"""
    return """
    <html>
        <head>
            <style>
                body { font-family: Arial, sans-serif; color: #333; }
                .container { max-width: 600px; margin: 0 auto; padding: 20px; }
                .header { background: linear-gradient(135deg, #1a2d3e 0%, #2a3f52 100%); color: white; padding: 20px; border-radius: 8px; }
                .section { margin: 20px 0; padding: 15px; background: #f9f9f9; border-left: 4px solid #d4a574; }
                .label { font-weight: bold; color: #1a2d3e; }
                table { width: 100%; border-collapse: collapse; margin: 15px 0; }
                th { background: #1a2d3e; color: white; padding: 10px; text-align: left; }
                td { padding: 10px; border-bottom: 1px solid #ddd; }
                .footer { margin-top: 30px; padding-top: 20px; border-top: 1px solid #ddd; color: #999; font-size: 12px; }
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
                            <td>Tihare Aravena</td>
                        </tr>
                        <tr>
                            <td><span class="label">Email:</span></td>
                            <td>tihare.aravena16@gmail.com</td>
                        </tr>
                        <tr>
                            <td><span class="label">Empresa:</span></td>
                            <td>Transportes Aravena</td>
                        </tr>
                        <tr>
                            <td><span class="label">RUT:</span></td>
                            <td>78.327.647-K</td>
                        </tr>
                    </table>
                </div>

                <div class="section">
                    <h3>Contenido del Informe</h3>
                    <ul>
                        <li><strong>Oportunidad 1:</strong> Presencia Digital desde Cero (+$2-5M/mes)</li>
                        <li><strong>Oportunidad 2:</strong> Optimización Combustible (+$31.5K/mes)</li>
                        <li><strong>Oportunidad 3:</strong> Beneficios Tributarios (+$3.02M/mes)</li>
                        <li><strong>Total Potencial:</strong> +$8.17-11.86M mensuales (+39-57%)</li>
                        <li><strong>Plan:</strong> 4 semanas integrado + proyecciones 90 días</li>
                    </ul>
                </div>

                <div class="section">
                    <h3>📎 Archivo Adjunto</h3>
                    <p><strong>Diagnostico_Transportes_Aravena_Mejorado_Abril2026.pdf</strong></p>
                    <p>✅ Revisar y proceder con envío a cliente si todo es correcto</p>
                </div>

                <div class="section">
                    <h3>Acciones Requeridas</h3>
                    <ol>
                        <li>Revisar el informe adjunto</li>
                        <li>Validar datos tributarios con RUT</li>
                        <li>Confirmar realismo de proyecciones</li>
                        <li>Enviar al cliente con propuesta de plan</li>
                    </ol>
                </div>

                <div class="footer">
                    <p><strong>Sistema ACP - Diagnóstico Automático</strong></p>
                    <p>Generado: """ + datetime.now().strftime('%d/%m/%Y %H:%M:%S') + """</p>
                </div>
            </div>
        </body>
    </html>
    """

def main():
    pdf_path = "/sessions/loving-busy-darwin/mnt/Acp y Asociados/Diagnostico_Transportes_Aravena_Mejorado_Abril2026.pdf"

    print("📧 INICIANDO ENVÍO DE EMAIL CON PDF")
    print("="*60)
    print(f"PDF: {os.path.basename(pdf_path)}")
    print(f"Destinatario: asesor.pac@gmail.com")
    print("="*60 + "\n")

    # Intentar enviar
    resultado = enviar_pdf_sendgrid(pdf_path)

    if resultado:
        print("\n✅ EMAIL ENVIADO EXITOSAMENTE A ASESOR")
        print("El PDF ya debería estar en la bandeja de entrada de asesor.pac@gmail.com")
    else:
        print("\n⚠️  No se pudo enviar automáticamente")
        print("\nOpciones:")
        print("1. Configurar SENDGRID_API_KEY y reintentar")
        print("2. Usar backend de Render para envío automático")
        print("3. Enviar manualmente adjuntando el PDF")

if __name__ == "__main__":
    main()
