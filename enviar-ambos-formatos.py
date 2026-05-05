#!/usr/bin/env python3
"""
Script para enviar HTML + PDF a asesor.pac@gmail.com
Genera PDF desde HTML y envía ambos archivos
"""

import os
import base64
from pathlib import Path
from datetime import datetime

def convertir_html_a_pdf(html_path, pdf_output_path):
    """Convierte HTML a PDF usando WeasyPrint"""
    try:
        from weasyprint import HTML
        HTML(html_path).write_pdf(pdf_output_path)
        print(f"✅ PDF generado desde HTML: {pdf_output_path}")
        return True
    except Exception as e:
        print(f"⚠️  Error al generar PDF: {e}")
        return False

def preparar_envio_sendgrid(
    html_path,
    pdf_path,
    destinatario="asesor.pac@gmail.com",
    cliente_nombre="Tihare Aravena",
    cliente_email="tihare.aravena16@gmail.com",
    empresa="Transportes Aravena",
    rut="78.327.647-K"
):
    """
    Prepara el envío de ambos archivos vía SendGrid
    Retorna estructura lista para usar en backend
    """

    # Validar archivos
    if not os.path.exists(html_path):
        print(f"❌ Archivo HTML no existe: {html_path}")
        return None

    if not os.path.exists(pdf_path):
        print(f"❌ Archivo PDF no existe: {pdf_path}")
        return None

    try:
        # Leer archivos
        with open(html_path, 'rb') as f:
            html_data = base64.b64encode(f.read()).decode('utf-8')

        with open(pdf_path, 'rb') as f:
            pdf_data = base64.b64encode(f.read()).decode('utf-8')

        # Preparar payload para SendGrid
        payload = {
            "personalizations": [{
                "to": [{"email": destinatario}],
                "subject": f"📋 Diagnóstico para Revisión: {empresa} - {cliente_nombre}"
            }],
            "from": {
                "email": "sistema@acp-diagnosticos.cl",
                "name": "Sistema ACP"
            },
            "reply_to": {
                "email": "asesor.pac@gmail.com"
            },
            "content": [{
                "type": "text/html",
                "value": generar_html_email(cliente_nombre, cliente_email, empresa, rut)
            }],
            "attachments": [
                {
                    "content": html_data,
                    "type": "text/html",
                    "filename": os.path.basename(html_path),
                    "disposition": "attachment"
                },
                {
                    "content": pdf_data,
                    "type": "application/pdf",
                    "filename": os.path.basename(pdf_path),
                    "disposition": "attachment"
                }
            ]
        }

        return payload

    except Exception as e:
        print(f"❌ Error preparando envío: {e}")
        return None

def generar_html_email(cliente_nombre, cliente_email, empresa, rut):
    """Genera el cuerpo HTML del email"""
    return f"""
    <html>
        <head>
            <style>
                body {{ font-family: Arial, sans-serif; color: #333; }}
                .container {{ max-width: 600px; margin: 0 auto; padding: 20px; }}
                .header {{ background: linear-gradient(135deg, #1a2d3e 0%, #2a3f52 100%); color: white; padding: 20px; border-radius: 8px; }}
                .section {{ margin: 20px 0; padding: 15px; background: #f9f9f9; border-left: 4px solid #d4a574; }}
                .label {{ font-weight: bold; color: #1a2d3e; }}
                table {{ width: 100%; border-collapse: collapse; margin: 15px 0; }}
                th {{ background: #1a2d3e; color: white; padding: 10px; text-align: left; }}
                td {{ padding: 10px; border-bottom: 1px solid #ddd; }}
                .footer {{ margin-top: 30px; padding-top: 20px; border-top: 1px solid #ddd; color: #999; font-size: 12px; }}
            </style>
        </head>
        <body>
            <div class="container">
                <div class="header">
                    <h2>📋 Nuevo Diagnóstico para Revisión</h2>
                    <p>Sistema ACP - Diagnóstico Automático</p>
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
                    <h3>📎 Archivos Adjuntos</h3>
                    <ul>
                        <li><strong>Diagnostico_Transportes_Aravena_HTML_Final.html</strong> - Versión HTML (visualización en navegador)</li>
                        <li><strong>Diagnostico_Transportes_Aravena_PDF_Final.pdf</strong> - Versión PDF (impresión y archivo)</li>
                    </ul>
                </div>

                <div class="section">
                    <h3>3 Oportunidades Personalizadas</h3>
                    <ul>
                        <li><strong>Oportunidad 1:</strong> Presencia Digital desde Cero (+$2-5M/mes)</li>
                        <li><strong>Oportunidad 2:</strong> Optimización Costos Operacionales (+$31.5K/mes)</li>
                        <li><strong>Oportunidad 3:</strong> Beneficios Tributarios (+$3.02M/mes)</li>
                    </ul>
                    <p><strong>Total Potencial: +$8.17-11.86M mensuales (+39-57%)</strong></p>
                </div>

                <div class="section">
                    <h3>Acciones Requeridas</h3>
                    <ol>
                        <li>Revisar los archivos adjuntos (HTML o PDF, son idénticos)</li>
                        <li>Validar datos tributarios con el RUT informado</li>
                        <li>Confirmar realismo de proyecciones</li>
                        <li>Enviar al cliente con propuesta de plan (Básico $49.900 o Premium $149.900)</li>
                    </ol>
                </div>

                <div class="footer">
                    <p><strong>Sistema ACP - Diagnóstico Automático</strong></p>
                    <p>Generado: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}</p>
                    <p>Enviado desde: Sistema automático ACP</p>
                </div>
            </div>
        </body>
    </html>
    """

def mostrar_codigo_backend():
    """Muestra el código para integrar en el backend Node.js"""
    return """
// CÓDIGO PARA AGREGAR AL BACKEND NODE.js (app.js o routes/diagnosticos.js)

const sgMail = require('@sendgrid/mail');
sgMail.setApiKey(process.env.SENDGRID_API_KEY);
const fs = require('fs');
const path = require('path');
const { execFile } = require('child_process');
const puppeteer = require('puppeteer');

// Endpoint para generar y enviar diagnóstico
app.post('/api/generate-and-send-diagnostico', async (req, res) => {
  try {
    const {
      cliente_nombre,
      cliente_email,
      empresa,
      rut,
      sector,
      ingresos_mensuales,
      margen,
      clientes_activos,
      costos_principales,
      redes_sociales,
      plataformas,
      consumo_combustible,
      contador
    } = req.body;

    // 1. Generar HTML dinámicamente (desde Python o JavaScript)
    const datos_cliente = {
      nombre: cliente_nombre,
      email: cliente_email,
      empresa: empresa,
      rut: rut,
      sector: sector,
      fecha: new Date().toLocaleDateString('es-ES', { year: 'numeric', month: 'long' }),
      ingresos_mensuales: ingresos_mensuales,
      margen: margen,
      clientes_activos: clientes_activos,
      costos_principales: costos_principales,
      redes_sociales: redes_sociales,
      plataformas: plataformas,
      consumo_combustible: consumo_combustible,
      contador: contador
    };

    // 2. Ejecutar script Python para generar HTML
    const htmlPath = path.join(__dirname, `./temp/diagnostico_${rut}.html`);

    // Ejecutar: python3 generador-informe-html-mejorado.py
    await new Promise((resolve, reject) => {
      execFile('python3', [
        path.join(__dirname, './scripts/generador-informe-html-mejorado.py'),
        '--output', htmlPath,
        '--data', JSON.stringify(datos_cliente)
      ], (error, stdout, stderr) => {
        if (error) reject(error);
        else resolve();
      });
    });

    // 3. Convertir HTML a PDF (usando Puppeteer o WeasyPrint)
    const pdfPath = htmlPath.replace('.html', '.pdf');
    const browser = await puppeteer.launch();
    const page = await browser.newPage();
    await page.goto(`file://${htmlPath}`, { waitUntil: 'networkidle0' });
    await page.pdf({ path: pdfPath, format: 'A4' });
    await browser.close();

    // 4. Leer ambos archivos
    const htmlContent = fs.readFileSync(htmlPath);
    const pdfContent = fs.readFileSync(pdfPath);

    // 5. Enviar por SendGrid con ambos adjuntos
    const msg = {
      to: 'asesor.pac@gmail.com',
      from: process.env.SENDGRID_FROM_EMAIL || 'sistema@acp-diagnosticos.cl',
      subject: `📋 Diagnóstico para Revisión: ${empresa} - ${cliente_nombre}`,
      html: generarEmailHTML(cliente_nombre, cliente_email, empresa, rut),
      attachments: [
        {
          content: Buffer.from(htmlContent).toString('base64'),
          filename: `Diagnostico_${empresa.replace(/\\s+/g, '_')}_HTML_Final.html`,
          type: 'text/html',
          disposition: 'attachment'
        },
        {
          content: Buffer.from(pdfContent).toString('base64'),
          filename: `Diagnostico_${empresa.replace(/\\s+/g, '_')}_PDF_Final.pdf`,
          type: 'application/pdf',
          disposition: 'attachment'
        }
      ]
    };

    await sgMail.send(msg);

    // 6. Limpiar archivos temporales
    fs.unlinkSync(htmlPath);
    fs.unlinkSync(pdfPath);

    res.json({
      success: true,
      message: 'Diagnóstico generado y enviado a asesor.pac@gmail.com',
      cliente: cliente_nombre,
      empresa: empresa
    });

  } catch (error) {
    console.error('Error:', error);
    res.status(500).json({
      success: false,
      error: error.message
    });
  }
});

// Función auxiliar para generar HTML del email
function generarEmailHTML(cliente_nombre, cliente_email, empresa, rut) {
  return `
    <html>
      <body style="font-family: Arial;">
        <h2>Nuevo Diagnóstico para Revisión</h2>
        <p><strong>Cliente:</strong> ${cliente_nombre}</p>
        <p><strong>Email:</strong> ${cliente_email}</p>
        <p><strong>Empresa:</strong> ${empresa}</p>
        <p><strong>RUT:</strong> ${rut}</p>
        <p>Los archivos HTML y PDF están adjuntos. Revisar y proceder con envío al cliente.</p>
      </body>
    </html>
  `;
}
"""

def main():
    print("\n" + "="*60)
    print("GENERADOR Y ENVÍO DE DIAGNÓSTICOS - SISTEMA ACP")
    print("="*60 + "\n")

    html_path = "/sessions/loving-busy-darwin/mnt/Acp y Asociados/Diagnostico_Transportes_Aravena_HTML_Final.html"
    pdf_output = "/sessions/loving-busy-darwin/mnt/Acp y Asociados/Diagnostico_Transportes_Aravena_PDF_Final.pdf"

    # Paso 1: Generar PDF desde HTML
    print("📄 PASO 1: Generando PDF desde HTML...")
    if convertir_html_a_pdf(html_path, pdf_output):
        print(f"✅ PDF creado: {pdf_output}\n")
    else:
        print("⚠️  No se pudo generar PDF\n")
        return

    # Paso 2: Preparar estructura para SendGrid
    print("📧 PASO 2: Preparando estructura para SendGrid...")
    payload = preparar_envio_sendgrid(html_path, pdf_output)

    if payload:
        print("✅ Estructura preparada\n")
        print(f"Destinatario: asesor.pac@gmail.com")
        print(f"Asunto: 📋 Diagnóstico para Revisión: Transportes Aravena - Tihare Aravena")
        print(f"Adjuntos:")
        print(f"  - Diagnostico_Transportes_Aravena_HTML_Final.html")
        print(f"  - Diagnostico_Transportes_Aravena_PDF_Final.pdf")
        print("\n")
    else:
        print("❌ Error preparando estructura\n")
        return

    # Paso 3: Mostrar instrucciones de integración
    print("="*60)
    print("🔧 PASO 3: INTEGRACIÓN CON BACKEND (Render)")
    print("="*60 + "\n")

    print("Para automatizar esto en el backend Node.js, agregar este código:\n")
    print(mostrar_codigo_backend())

    # Paso 4: Instrucciones de configuración
    print("\n" + "="*60)
    print("⚙️  CONFIGURACIÓN REQUERIDA EN RENDER")
    print("="*60 + "\n")

    print("""
1. INSTALAR DEPENDENCIAS (en backend):
   npm install @sendgrid/mail puppeteer

2. CONFIGURAR VARIABLES DE ENTORNO (Render Dashboard):
   - SENDGRID_API_KEY: Tu API key de SendGrid
   - SENDGRID_FROM_EMAIL: sistema@acp-diagnosticos.cl

3. OBTENER API KEY DE SENDGRID:
   a) Ir a https://app.sendgrid.com
   b) Settings → API Keys
   c) Create API Key (Full Access)
   d) Copiar y guardar en Render

4. COPIAR SCRIPTS PYTHON AL BACKEND:
   - generador-informe-html-mejorado.py
   - Asegurar que Python 3 está disponible en Render

5. DESPLEGAR CAMBIOS:
   git add .
   git commit -m "feat: Add automatic diagnostico generation and SendGrid integration"
   git push origin main
   (Render redeploy automático)

6. PROBAR ENDPOINT:
   curl -X POST https://acp-backend-g3io.onrender.com/api/generate-and-send-diagnostico \\
     -H "Content-Type: application/json" \\
     -d '{
       "cliente_nombre": "Test Cliente",
       "cliente_email": "test@example.com",
       "empresa": "Test Empresa",
       "rut": "12.345.678-K",
       ...otros campos...
     }'
""")

    print("\n" + "="*60)
    print("✅ ESTADO ACTUAL")
    print("="*60)
    print("""
✅ HTML generado: Diagnostico_Transportes_Aravena_HTML_Final.html
✅ PDF generado: Diagnostico_Transportes_Aravena_PDF_Final.pdf
✅ Estructura SendGrid preparada
✅ Código backend documentado
⏳ Pendiente: Obtener API key de SendGrid
⏳ Pendiente: Integrar en backend Node.js
⏳ Pendiente: Desplegar en Render

Una vez completado, los diagnósticos se generarán automáticamente.
""")

if __name__ == "__main__":
    main()
