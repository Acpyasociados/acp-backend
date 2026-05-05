#!/usr/bin/env python3
"""
Script para enviar PDF a través del backend de Render
El backend ya tiene SendGrid configurado y credenciales válidas
"""

import requests
import json
import base64
import os
from datetime import datetime

BACKEND_URL = "https://acp-backend-g3io.onrender.com"

def enviar_via_backend(
    pdf_path,
    destinatario="asesor.pac@gmail.com",
    cliente_nombre="Tihare Aravena",
    cliente_email="tihare.aravena16@gmail.com",
    empresa="Transportes Aravena"
):
    """
    Envía email con PDF a través del endpoint del backend.
    El backend maneja SendGrid automáticamente.
    """

    # Validar archivo
    if not os.path.exists(pdf_path):
        print(f"❌ Archivo no existe: {pdf_path}")
        return False

    try:
        # Leer PDF y codificar en base64
        with open(pdf_path, 'rb') as f:
            pdf_data = base64.b64encode(f.read()).decode('utf-8')

        # Preparar payload
        payload = {
            "para": destinatario,
            "asunto": f"📋 Diagnóstico para Revisión: {empresa} - {cliente_nombre}",
            "cliente_nombre": cliente_nombre,
            "cliente_email": cliente_email,
            "empresa": empresa,
            "rut": "78.327.647-K",
            "pdf_base64": pdf_data,
            "pdf_filename": os.path.basename(pdf_path),
            "tipo_email": "diagnostico_asesor"
        }

        print("\n📧 ENVIANDO A TRAVÉS DEL BACKEND")
        print("="*60)
        print(f"Backend: {BACKEND_URL}")
        print(f"Destinatario: {destinatario}")
        print(f"Cliente: {cliente_nombre}")
        print(f"Empresa: {empresa}")
        print("="*60)

        # Hacer request al backend
        response = requests.post(
            f"{BACKEND_URL}/api/send-email",
            json=payload,
            timeout=30
        )

        if response.status_code == 200:
            resultado = response.json()
            print("\n✅ EMAIL ENVIADO EXITOSAMENTE")
            print(f"Status: {response.status_code}")
            print(f"Mensaje: {resultado.get('message', 'OK')}")
            print(f"Email ID: {resultado.get('email_id', 'N/A')}")
            return True
        else:
            print(f"\n⚠️  Error en backend: {response.status_code}")
            print(f"Respuesta: {response.text}")
            return False

    except requests.exceptions.ConnectionError:
        print(f"\n❌ No se puede conectar al backend: {BACKEND_URL}")
        print("El backend de Render puede estar en hibernación.")
        print("\nAlternativas:")
        print("1. Esperar 1-2 minutos y reintentar (backend se activa)")
        print("2. Usar SendGrid directamente con API key")
        print("3. Enviar manualmente el PDF adjunto")
        return False
    except Exception as e:
        print(f"\n❌ Error: {e}")
        return False

def crear_endpoint_backend():
    """
    Código para agregar al backend Node.js (acp-backend-g3io.onrender.com)
    Copiar en app.js o routes/emails.js
    """
    codigo = '''
// Agregar esta ruta al backend Node.js

const nodemailer = require('nodemailer');
const sgTransport = require('nodemailer-sendgrid-transport');

// Configurar SendGrid
const mailer = nodemailer.createTransport(sgTransport({
  auth: {
    api_key: process.env.SENDGRID_API_KEY
  }
}));

app.post('/api/send-email', async (req, res) => {
  try {
    const {
      para,
      asunto,
      cliente_nombre,
      cliente_email,
      empresa,
      rut,
      pdf_base64,
      pdf_filename,
      tipo_email
    } = req.body;

    // Decodificar PDF
    const pdf_buffer = Buffer.from(pdf_base64, 'base64');

    // Generar HTML del email
    const html = `
      <html>
        <body style="font-family: Arial;">
          <h2>Nuevo Diagnóstico para Revisión</h2>
          <p><strong>Cliente:</strong> ${cliente_nombre}</p>
          <p><strong>Email:</strong> ${cliente_email}</p>
          <p><strong>Empresa:</strong> ${empresa}</p>
          <p><strong>RUT:</strong> ${rut}</p>
          <p>El informe completo está adjunto en PDF.</p>
        </body>
      </html>
    `;

    // Enviar email
    const resultado = await mailer.sendMail({
      from: process.env.SENDGRID_FROM_EMAIL,
      to: para,
      subject: asunto,
      html: html,
      attachments: [{
        filename: pdf_filename,
        content: pdf_buffer,
        contentType: 'application/pdf'
      }]
    });

    res.json({
      success: true,
      message: 'Email enviado',
      email_id: resultado.response
    });

  } catch (error) {
    console.error('Error enviando email:', error);
    res.status(500).json({
      success: false,
      error: error.message
    });
  }
});
    '''
    return codigo

if __name__ == "__main__":
    pdf_path = "/sessions/loving-busy-darwin/mnt/Acp y Asociados/Diagnostico_Transportes_Aravena_Mejorado_Abril2026.pdf"

    print("\n" + "="*60)
    print("ENVÍO DE PDF A ASESOR.PAC@GMAIL.COM")
    print("="*60)

    resultado = enviar_via_backend(pdf_path)

    if not resultado:
        print("\n" + "="*60)
        print("CÓDIGO PARA AGREGAR AL BACKEND")
        print("="*60)
        print("\nSi quieres automatizar esto, agrega este endpoint al backend Node.js:")
        print(crear_endpoint_backend())
