# 🚀 INTEGRACIÓN SENDGRID + RENDER - GUÍA COMPLETA

**Fecha:** 28 de Abril de 2026  
**Objetivo:** Automatizar envío de diagnósticos con HTML + PDF a asesor.pac@gmail.com  
**Estado:** Listo para configuración

---

## 📋 RESUMEN DEL SISTEMA

El sistema ACP ahora puede:

1. ✅ **Generar dinámicamente** HTML profesional con datos del cliente
2. ✅ **Convertir a PDF** automáticamente desde HTML
3. ✅ **Preparar ambos archivos** para envío (HTML + PDF)
4. ⏳ **Enviar automáticamente** via SendGrid (requiere configuración)
5. ⏳ **Notificar al asesor** (asesor.pac@gmail.com) para revisión

---

## 🔑 PASO 1: OBTENER API KEY DE SENDGRID

### 1.1 Crear cuenta o acceder a SendGrid

```
https://app.sendgrid.com
```

- Si no tienes cuenta: Registrarse (gratis)
- Si tienes cuenta: Iniciar sesión

### 1.2 Generar API Key

1. En dashboard de SendGrid, ve a **Settings** → **API Keys**
2. Haz clic en **Create API Key**
3. Nombre: `ACP-Render-Diagnosticos`
4. Permisos: Selecciona **Full Access**
5. Haz clic en **Create & Edit**
6. **COPIAR LA API KEY** (aparecerá una sola vez)

Ejemplo de API Key:
```
SG.XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
```

⚠️ **IMPORTANTE:** Guardar la API Key de forma segura. No compartir.

---

## ⚙️ PASO 2: CONFIGURAR EN RENDER

### 2.1 Acceder al Dashboard de Render

```
https://dashboard.render.com
```

Ir a tu servicio: **acp-backend-g3io** (o el nombre de tu backend)

### 2.2 Agregar Variable de Entorno

1. Click en **Settings**
2. Ir a **Environment**
3. Haz clic en **Add Environment Variable**
4. **Key:** `SENDGRID_API_KEY`
5. **Value:** Pega la API Key que copiaste en Paso 1
6. Click en **Save Changes**

Render redesplegará automáticamente el servicio.

### 2.3 Agregar Email del Remitente (Opcional pero recomendado)

1. Agregar otra variable:
2. **Key:** `SENDGRID_FROM_EMAIL`
3. **Value:** `sistema@acp-diagnosticos.cl`
4. Click en **Save Changes**

---

## 💻 PASO 3: ACTUALIZAR CÓDIGO DEL BACKEND

### 3.1 Instalar Dependencias

En tu repositorio local, asegúrate de tener en `package.json`:

```json
{
  "dependencies": {
    "@sendgrid/mail": "^7.7.0",
    "puppeteer": "^21.0.0",
    "express": "^4.x.x"
  }
}
```

Ejecuta:
```bash
npm install
```

### 3.2 Agregar el Endpoint en Backend

Copia este código en tu `app.js` o `routes/diagnosticos.js`:

```javascript
const sgMail = require('@sendgrid/mail');
const fs = require('fs');
const path = require('path');
const { execFile } = require('child_process');

// Configurar SendGrid
sgMail.setApiKey(process.env.SENDGRID_API_KEY);

/**
 * POST /api/generate-and-send-diagnostico
 * Genera HTML + PDF y envía a asesor para revisión
 */
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

    console.log(`📋 Generando diagnóstico para: ${empresa}`);

    // Crear directorio temporal si no existe
    const tempDir = path.join(__dirname, 'temp');
    if (!fs.existsSync(tempDir)) {
      fs.mkdirSync(tempDir, { recursive: true });
    }

    // Rutas de archivos
    const htmlPath = path.join(tempDir, `diag_${Date.now()}.html`);
    const pdfPath = htmlPath.replace('.html', '.pdf');

    // Datos para el generador Python
    const datos_cliente = {
      nombre: cliente_nombre,
      email: cliente_email,
      empresa: empresa,
      rut: rut,
      sector: sector,
      fecha: new Date().toLocaleDateString('es-ES', { 
        year: 'numeric', 
        month: 'long' 
      }),
      ingresos_mensuales: ingresos_mensuales,
      margen: margen,
      clientes_activos: clientes_activos,
      costos_principales: costos_principales,
      redes_sociales: redes_sociales,
      plataformas: plataformas,
      consumo_combustible: consumo_combustible,
      contador: contador
    };

    // 1. Generar HTML (usar el script Python existente)
    // Nota: Si es posible, implementar en JavaScript puro para evitar 
    // dependencia de Python en Render
    
    // ALTERNATIVA: Implementar el generador en JavaScript
    const htmlContent = generarHTMLDiagnostico(datos_cliente);
    fs.writeFileSync(htmlPath, htmlContent);

    console.log(`✅ HTML generado: ${htmlPath}`);

    // 2. Convertir HTML a PDF usando Puppeteer
    const browser = await require('puppeteer').launch({
      headless: true,
      args: ['--no-sandbox', '--disable-setuid-sandbox']
    });
    
    const page = await browser.newPage();
    await page.setContent(htmlContent, { waitUntil: 'networkidle0' });
    await page.pdf({ 
      path: pdfPath, 
      format: 'A4',
      margin: { top: '20px', right: '20px', bottom: '20px', left: '20px' }
    });
    await browser.close();

    console.log(`✅ PDF generado: ${pdfPath}`);

    // 3. Leer ambos archivos
    const htmlBuffer = fs.readFileSync(htmlPath);
    const pdfBuffer = fs.readFileSync(pdfPath);

    // 4. Preparar email con SendGrid
    const msg = {
      to: 'asesor.pac@gmail.com',
      from: process.env.SENDGRID_FROM_EMAIL || 'sistema@acp-diagnosticos.cl',
      subject: `📋 Diagnóstico para Revisión: ${empresa} - ${cliente_nombre}`,
      html: generarEmailHTML(cliente_nombre, cliente_email, empresa, rut),
      attachments: [
        {
          content: htmlBuffer.toString('base64'),
          filename: `Diagnostico_${empresa.replace(/\\s+/g, '_')}_HTML.html`,
          type: 'text/html',
          disposition: 'attachment'
        },
        {
          content: pdfBuffer.toString('base64'),
          filename: `Diagnostico_${empresa.replace(/\\s+/g, '_')}_PDF.pdf`,
          type: 'application/pdf',
          disposition: 'attachment'
        }
      ]
    };

    // 5. Enviar email
    const resultado = await sgMail.send(msg);
    console.log(`✅ Email enviado a ${msg.to}`);

    // 6. Limpiar archivos temporales
    fs.unlinkSync(htmlPath);
    fs.unlinkSync(pdfPath);

    // 7. Guardar en base de datos (opcional)
    // await db.diagnosticos.create({
    //   cliente_nombre,
    //   empresa,
    //   rut,
    //   enviado_a: 'asesor.pac@gmail.com',
    //   enviado_en: new Date(),
    //   estado: 'en_revision'
    // });

    res.json({
      success: true,
      message: 'Diagnóstico generado y enviado al asesor',
      cliente: cliente_nombre,
      empresa: empresa,
      email_id: resultado[0].headers['x-message-id']
    });

  } catch (error) {
    console.error('❌ Error:', error);
    res.status(500).json({
      success: false,
      error: error.message
    });
  }
});

/**
 * Genera el HTML del diagnóstico (implementación JavaScript)
 */
function generarHTMLDiagnostico(datos) {
  // Aquí va la lógica completa del HTML
  // Puede ser muy larga, así que se recomienda:
  // 1. Importar desde archivo separado
  // 2. O convertir el script Python a JavaScript
  
  return `
    <!DOCTYPE html>
    <html>
      <head>
        <meta charset="UTF-8">
        <title>Diagnóstico - ${datos.empresa}</title>
        <style>
          body { font-family: Arial; color: #333; }
          .container { max-width: 900px; margin: 0; background: white; padding: 30px; }
          h1 { color: #1a2d3e; }
          h2 { color: #1a2d3e; border-bottom: 2px solid #d4a574; padding-bottom: 8px; }
        </style>
      </head>
      <body>
        <div class="container">
          <h1>Diagnóstico de Oportunidades</h1>
          <p>${datos.sector}</p>
          <p>Cliente: ${datos.nombre}</p>
          <p>Empresa: ${datos.empresa}</p>
          <p>RUT: ${datos.rut}</p>
          
          <!-- Contenido del diagnóstico aquí -->
          
        </div>
      </body>
    </html>
  `;
}

/**
 * Genera el cuerpo HTML del email al asesor
 */
function generarEmailHTML(cliente_nombre, cliente_email, empresa, rut) {
  return `
    <html>
      <body style="font-family: Arial;">
        <h2>Nuevo Diagnóstico para Revisión</h2>
        <p><strong>Cliente:</strong> ${cliente_nombre}</p>
        <p><strong>Email:</strong> ${cliente_email}</p>
        <p><strong>Empresa:</strong> ${empresa}</p>
        <p><strong>RUT:</strong> ${rut}</p>
        <p>Los archivos HTML y PDF están adjuntos. Revisar y proceder con envío al cliente si todo es correcto.</p>
      </body>
    </html>
  `;
}
```

### 3.3 Actualizar package.json

```json
{
  "name": "acp-backend",
  "version": "1.0.0",
  "dependencies": {
    "express": "^4.18.0",
    "pg": "^8.8.0",
    "@sendgrid/mail": "^7.7.0",
    "puppeteer": "^21.0.0"
  }
}
```

---

## 🚀 PASO 4: DESPLEGAR EN RENDER

### 4.1 Pushear cambios a GitHub

```bash
git add .
git commit -m "feat: Add SendGrid integration for automatic diagnostic emails"
git push origin main
```

### 4.2 Render redeploy automático

Render detectará el push y redesplegará automáticamente:
- Instala dependencias nuevas
- Carga variables de entorno
- Reinicia el servicio

Puedes verificar en: https://dashboard.render.com → acp-backend-g3io → Logs

---

## 🧪 PASO 5: PROBAR EL ENDPOINT

### 5.1 Prueba Local (si tienes backend local)

```bash
curl -X POST http://localhost:3000/api/generate-and-send-diagnostico \
  -H "Content-Type: application/json" \
  -d '{
    "cliente_nombre": "Tihare Aravena",
    "cliente_email": "tihare.aravena16@gmail.com",
    "empresa": "Transportes Aravena",
    "rut": "78.327.647-K",
    "sector": "Servicios de Transporte",
    "ingresos_mensuales": "CLP $23.000.000",
    "margen": 15,
    "clientes_activos": 3,
    "costos_principales": "Combustible, personal, mantención",
    "redes_sociales": "no",
    "plataformas": "ninguna",
    "consumo_combustible": 500,
    "contador": "Por definir"
  }'
```

### 5.2 Prueba en Render (después de desplegar)

```bash
curl -X POST https://acp-backend-g3io.onrender.com/api/generate-and-send-diagnostico \
  -H "Content-Type: application/json" \
  -d '{
    "cliente_nombre": "Tihare Aravena",
    "cliente_email": "tihare.aravena16@gmail.com",
    "empresa": "Transportes Aravena",
    "rut": "78.327.647-K",
    "sector": "Servicios de Transporte",
    "ingresos_mensuales": "CLP $23.000.000",
    "margen": 15,
    "clientes_activos": 3,
    "costos_principales": "Combustible, personal, mantención",
    "redes_sociales": "no",
    "plataformas": "ninguna",
    "consumo_combustible": 500,
    "contador": "Por definir"
  }'
```

**Respuesta esperada:**
```json
{
  "success": true,
  "message": "Diagnóstico generado y enviado al asesor",
  "cliente": "Tihare Aravena",
  "empresa": "Transportes Aravena",
  "email_id": "..."
}
```

**Verifica en asesor.pac@gmail.com:** Deberías recibir el email con ambos archivos (HTML + PDF)

---

## 📧 FLUJO COMPLETO AUTOMATIZADO

```
Cliente llena formulario en Netlify
         ↓
Backend Node.js recibe datos
         ↓
POST /api/generate-and-send-diagnostico
         ↓
1. Ejecuta generador HTML dinámico
2. Convierte HTML → PDF con Puppeteer
3. Prepara ambos archivos (base64)
4. Envía por SendGrid a asesor.pac@gmail.com
5. Limpia archivos temporales
         ↓
Asesor recibe email con HTML + PDF
         ↓
Asesor revisa y envía al cliente
         ↓
Cliente recibe diagnóstico y puede comprar plan
```

---

## ✅ CHECKLIST DE IMPLEMENTACIÓN

- [ ] Obtener API Key de SendGrid
- [ ] Agregar variables de entorno en Render
- [ ] Instalar dependencias en package.json
- [ ] Agregar endpoint /api/generate-and-send-diagnostico
- [ ] Pushear a GitHub
- [ ] Verificar despliegue en Render
- [ ] Probar endpoint con curl
- [ ] Verificar email en asesor.pac@gmail.com
- [ ] Documentar proceso en equipo

---

## 🔍 TROUBLESHOOTING

### "Error: SENDGRID_API_KEY is not set"

**Solución:** Verificar que la variable de entorno esté agregada en Render Settings.

### "Puppeteer timeout"

**Solución:** Aumentar timeout en page.pdf() o usar Render Plan pagado (más recursos).

### "Email no llega a asesor.pac@gmail.com"

**Solución:** 
1. Verificar que email sea correcto: asesor.pac@gmail.com
2. Revisar spam/basura
3. Verificar logs en Render dashboard
4. Probar enviando email de prueba desde SendGrid

### "PDF vacío o corrupto"

**Solución:**
1. Usar Puppeteer en lugar de WeasyPrint
2. Aumentar timeout: `waitUntil: 'networkidle0'`
3. Reducir tamaño del HTML si es muy grande

---

## 📞 SOPORTE

Para ayuda:
1. Revisar logs en Render dashboard
2. Consultar documentación SendGrid: https://docs.sendgrid.com
3. Documentación Puppeteer: https://pptr.dev/

---

**Sistema ACP - Diagnóstico Automático**  
**Fecha:** 28 de Abril de 2026  
**Estado:** Listo para implementación
