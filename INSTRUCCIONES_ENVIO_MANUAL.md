# 📧 INSTRUCCIONES DE ENVÍO MANUAL - TIHARE ARAVENA

**Fecha:** 28 de Abril de 2026  
**Estado:** PDF generado, listo para envío manual  
**Destinatario:** asesor.pac@gmail.com

---

## 🚀 OPCIÓN 1: ENVÍO INMEDIATO (Manual - 30 segundos)

### Pasos:

1. **Abre tu email** (Gmail, Outlook, etc.)

2. **Crea un nuevo email** a: **asesor.pac@gmail.com**

3. **Asunto:**
```
📋 Diagnóstico para Revisión: Transportes Aravena - Tihare Aravena
```

4. **Cuerpo del email:**
```
Hola,

Adjunto encontrarás el diagnóstico de crecimiento para Transportes Aravena.

DATOS DEL CLIENTE:
- Nombre: Tihare Aravena
- Email: tihare.aravena16@gmail.com
- Empresa: Transportes Aravena
- RUT: 78.327.647-K
- Sector: Servicios de Transporte

CONTENIDO DEL INFORME:
✅ Situación actual de la empresa
✅ 3 Oportunidades personalizadas:
   1. Presencia Digital desde Cero (+$2-5M/mes)
   2. Optimización Costos Combustible (+$31.5K/mes)
   3. Beneficios Tributarios (+$3.02M/mes)
✅ Plan de acción integrado 30 días
✅ Proyecciones financieras 90 días

TOTAL POTENCIAL: +$8.17-11.86M mensuales (+39-57%)

ACCIONES REQUERIDAS:
1. Revisar el informe adjunto
2. Validar datos tributarios con RUT
3. Confirmar realismo de proyecciones
4. Enviar al cliente con propuesta de plan

Por favor confirma la recepción.

Saludos,
Sistema ACP
```

5. **Adjunta el archivo:**
```
Diagnostico_Transportes_Aravena_Mejorado_Abril2026.pdf
```

6. **Haz clic en Enviar**

✅ **¡Listo!** El email llegará en segundos a asesor.pac@gmail.com

---

## 🔗 OPCIÓN 2: ENVÍO AUTOMÁTICO (Backend)

Para automatizar el envío en futuras ocasiones, agrega este código al backend Node.js:

### Instalar dependencias (si no están):
```bash
npm install nodemailer nodemailer-sendgrid-transport
```

### Agregar al archivo `app.js` o `routes/emails.js`:

```javascript
const nodemailer = require('nodemailer');
const sgTransport = require('nodemailer-sendgrid-transport');
const fs = require('fs');
const path = require('path');

// Configurar SendGrid
const mailer = nodemailer.createTransport(sgTransport({
  auth: {
    api_key: process.env.SENDGRID_API_KEY
  }
}));

// Endpoint para enviar diagnóstico
app.post('/api/send-diagnostico', async (req, res) => {
  try {
    const {
      para,
      asunto,
      cliente_nombre,
      cliente_email,
      empresa,
      rut,
      pdf_path,
      tipo_email
    } = req.body;

    // Leer archivo PDF
    const pdf_data = fs.readFileSync(pdf_path);

    // Generar HTML
    const html = `
      <html>
        <head>
          <style>
            body { font-family: Arial; color: #333; }
            .container { max-width: 600px; margin: 0 auto; }
            .header { background: linear-gradient(135deg, #1a2d3e 0%, #2a3f52 100%); color: white; padding: 20px; }
            .section { margin: 15px 0; padding: 15px; background: #f9f9f9; }
            table { width: 100%; border-collapse: collapse; }
            td { padding: 8px; border-bottom: 1px solid #ddd; }
          </style>
        </head>
        <body>
          <div class="container">
            <div class="header">
              <h2>📋 Nuevo Diagnóstico para Revisión</h2>
            </div>
            <div class="section">
              <h3>Datos del Cliente</h3>
              <table>
                <tr><td><b>Nombre:</b></td><td>${cliente_nombre}</td></tr>
                <tr><td><b>Email:</b></td><td>${cliente_email}</td></tr>
                <tr><td><b>Empresa:</b></td><td>${empresa}</td></tr>
                <tr><td><b>RUT:</b></td><td>${rut}</td></tr>
              </table>
            </div>
            <div class="section">
              <p>El informe completo está adjunto. Revisar y proceder con envío al cliente.</p>
            </div>
          </div>
        </body>
      </html>
    `;

    // Enviar email con PDF adjunto
    await mailer.sendMail({
      from: process.env.SENDGRID_FROM_EMAIL || 'sistema@acp-diagnosticos.cl',
      to: para,
      subject: asunto,
      html: html,
      attachments: [{
        filename: path.basename(pdf_path),
        content: pdf_data
      }]
    });

    res.json({
      success: true,
      message: 'Email enviado exitosamente'
    });

  } catch (error) {
    console.error('Error:', error);
    res.status(500).json({
      success: false,
      error: error.message
    });
  }
});
```

### Usar el endpoint:
```javascript
// En formulario o script
fetch('https://acp-backend-g3io.onrender.com/api/send-diagnostico', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    para: 'asesor.pac@gmail.com',
    asunto: '📋 Diagnóstico para Revisión: Transportes Aravena - Tihare Aravena',
    cliente_nombre: 'Tihare Aravena',
    cliente_email: 'tihare.aravena16@gmail.com',
    empresa: 'Transportes Aravena',
    rut: '78.327.647-K',
    pdf_path: '/path/to/Diagnostico_Transportes_Aravena_Mejorado_Abril2026.pdf'
  })
})
```

---

## 📍 UBICACIÓN DEL ARCHIVO PDF

**Ruta local (para Patricio):**
```
/sessions/loving-busy-darwin/mnt/Acp y Asociados/Diagnostico_Transportes_Aravena_Mejorado_Abril2026.pdf
```

**Descargar:** El archivo está disponible en tu carpeta de trabajo ACP.

---

## ✅ CHECKLIST DE ENVÍO

- [ ] Abierto email a asesor.pac@gmail.com
- [ ] Copiado asunto: "📋 Diagnóstico para Revisión: Transportes Aravena - Tihare Aravena"
- [ ] Pegado contenido del email
- [ ] Adjuntado archivo PDF
- [ ] Enviado email
- [ ] Confirmado recepción en bandeja de asesor.pac@gmail.com

---

## 🎯 Próximos Pasos (Después del Envío)

### Para el Asesor (asesor.pac@gmail.com):
1. Revisar el informe
2. Validar datos tributarios
3. Confirmar proyecciones
4. Solicitar cambios si es necesario

### Para Envío a Cliente:
1. Esperar aprobación del asesor
2. Enviar a tihare.aravena16@gmail.com
3. Incluir propuesta de plan (Básico $49.900 o Premium $149.900)
4. Enlace a Mercado Pago para pago

---

## 📧 PLANTILLA PARA ENVÍO A CLIENTE (Después)

```
Asunto: Tu Diagnóstico de Crecimiento - Transportes Aravena

Hola Tihare,

Adjunto encontrarás tu diagnóstico personalizado de crecimiento y rentabilidad para Transportes Aravena.

RESUMEN EJECUTIVO:
Se han identificado 3 oportunidades clave que podrían generar entre $8.17 y $11.86 millones adicionales mensuales en los próximos 90 días.

OPORTUNIDADES:
1. Presencia Digital desde Cero (+$2-5M/mes)
2. Optimización de Costos Operacionales (+$31.5K/mes)
3. Beneficios Tributarios (+$3.02M/mes)

PLANES DISPONIBLES:
📦 Plan Básico: $49.900
- Informe diagnóstico completo
- 3 oportunidades detalladas
- Plan de acción 30 días

💎 Plan Premium: $149.900
- Todo lo anterior, más:
- Plan detallado 90 y 180 días
- Seguimiento mensual
- Ajustes según resultados

PRÓXIMOS PASOS:
Puedes seleccionar tu plan aquí: [ENLACE MERCADO PAGO]

Cualquier duda, contáctame directamente.

Saludos,
[Tu nombre]
Sistema ACP
```

---

**Estado Actual:** PDF generado y listo para envío  
**Responsabilidad:** Envío manual a asesor.pac@gmail.com  
**Tiempo estimado:** 30 segundos
