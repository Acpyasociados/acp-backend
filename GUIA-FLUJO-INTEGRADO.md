# Flujo Integrado: Formulario → Informe Personalizado

**Fecha:** 28 Abril 2026  
**Estado:** Operativo

## 📋 Arquitectura del Sistema Mejorado

El sistema ACP ahora funciona como un flujo completamente integrado:

```
Cliente completa formulario mejorado
           ↓
  Datos capturados con campos tributarios/operacionales
           ↓
   Backend procesa y almacena en PostgreSQL
           ↓
   Generador de informes mejorado procesa datos
           ↓
   Informe personalizado generado automáticamente
           ↓
  Cliente recibe diagnóstico con 3 oportunidades adaptadas
```

---

## 📊 Campos Capturados en Formulario

### Información de Contacto (Sin cambios)
- Nombre completo
- Email
- Teléfono

### Información de la Empresa (Mejorada)
- Nombre de la empresa
- **[NUEVO] RUT** - Para validación tributaria
- Rubro/Sector
- Ventas mensuales
- Margen de ganancia
- Cantidad de clientes activos

### Presencia Digital y Operacional (NUEVA SECCIÓN)
- **¿Está en redes sociales?** (Sí/No) → Detecta si necesita crear presencia o potenciar
- **Plataformas activas:** Facebook, Instagram, LinkedIn, Website, WhatsApp Business
- **Consumo mensual de combustible** (Litros) → Calcula proyecciones de Oportunidad 2
- **Nombre del contador** → Referencia para Oportunidad 3 tributaria

### Análisis Financiero (Sin cambios)
- Top 3 costos principales
- Canal principal de adquisición

### Diagnóstico y Objetivos (Sin cambios)
- Problema principal
- Objetivo a 6 meses

### Selección de Plan (Sin cambios)
- Básico: $49.900
- Premium: $149.900

---

## 🎯 Oportunidades Dinámicas

El nuevo generador crea 3 oportunidades adaptadas al cliente:

### Oportunidad 1: Digital (Siempre)
**Si NO tiene redes sociales:**
- Título: "Crear Presencia Digital desde Cero"
- Estrategia: WhatsApp Business → Google My Business → LinkedIn → Outreach

**Si YA tiene presencia:**
- Título: "Potenciar Presencia Digital Existente"
- Estrategia: Optimizar canales actuales + expansión inteligente

### Oportunidad 2: Costos (Adaptada por Sector)
**Si tiene consumo de combustible (transporte, servicios campo):**
- Título: "Optimización de Costos Operacionales (Combustible)"
- Cálculo automático: consumo × precio combustible × mejora%
- Proyección real basada en datos ingresados

**Si NO tiene combustible (servicios/comercio):**
- Título: "Optimización de Márgenes y Procesos"
- Enfoque: Automatización y eficiencia interna
- Proyección: +X% margen basado en margen actual

### Oportunidad 3: Tributaria (Siempre)
- Análisis de régimen fiscal actual
- Referencia al contador específico del cliente
- Proyecciones de ahorro fiscal
- Validación con profesional

---

## 🔄 Flujo de Datos

### 1. Cliente completa formulario (HTML mejorado)
```html
Formulario captura:
✓ RUT de empresa
✓ Estado redes sociales
✓ Plataformas digitales activas
✓ Consumo combustible (si aplica)
✓ Nombre contador
```

### 2. Backend recibe datos
```python
{
  "nombre": "Tihare Aravena",
  "empresa": "Transportes Aravena",
  "rut": "78.327.647-K",
  "sector": "servicios_terreno",
  "redes_sociales": "no",
  "plataformas": "ninguna",
  "consumo_combustible": 500,
  "contador": "Por definir",
  "margen": 15,
  ...otros campos
}
```

### 3. Generador de informes procesa
```python
generar_informe_mejorado(datos_cliente, "output.pdf")
# Automáticamente:
# 1. Detecta sector y datos operacionales
# 2. Genera 3 oportunidades dinámicas
# 3. Crea proyecciones basadas en datos reales
# 4. Personaliza acciones según contexto
```

### 4. Informe personalizado generado
```
Diagnóstico de Transportes Aravena
- Oportunidad 1: Presencia Digital (desde cero)
- Oportunidad 2: Ahorro combustible: +$31.5-37.5K/mes
- Oportunidad 3: Beneficios tributarios PRO PYME
- Plan 4 semanas integrado
- Proyecciones 90 días personalizadas
```

---

## 📁 Archivos del Sistema

### Formulario
- `formulario-cliente.html` - Formulario mejorado con campos tributarios/operacionales

### Generadores de Informes (3 opciones)
- `generador-informe-diagnostico.py` - Original (PDF con reportlab)
- `generador-informe-html.py` - Versión HTML profesional
- `generador-informe-mejorado.py` - NUEVO - Integrado con datos dinámicos

### Almacenamiento
- PostgreSQL en Render - Tabla `leads` con todos los campos
- Schema incluye: nombre, email, rut, sector, redes_sociales, plataformas, consumo_combustible, contador

---

## 🚀 Pasos para Usar el Sistema

### Para Administrador (Patricio)
1. Cliente llena formulario en Netlify
2. Datos se envían a backend en Render
3. Se almacenan en PostgreSQL
4. Email notificación a asesor.pac@gmail.com
5. Ejecutar: `python3 generador-informe-mejorado.py`
6. Informe PDF generado automáticamente
7. Enviar a cliente con propuesta de plan

### Para Cliente
1. Ir a formulario: https://client-diagnostic-app.netlify.app
2. Completar con información real
3. Seleccionar plan (Básico o Premium)
4. Enviar
5. Dentro de 24h recibe diagnóstico personalizado

---

## 💡 Ventajas del Sistema Mejorado

✅ **Dinámico**: Oportunidades adaptadas a datos reales, no genéricas
✅ **Preciso**: Usa información específica del cliente (RUT, combustible, contador)
✅ **Escalable**: Funciona para cualquier sector (transporte, servicios, comercio)
✅ **Automatizado**: Menos trabajo manual, más consistencia
✅ **Profesional**: Datos tributarios y operacionales integrados
✅ **Auditable**: Todos los datos capturados y almacenados

---

## 📝 Ejemplo: Transportes Aravena

**Datos ingresados:**
- RUT: 78.327.647-K
- Sector: Servicios de transporte
- Redes sociales: No
- Consumo combustible: 500 litros/mes
- Contador: Por definir

**Oportunidades generadas automáticamente:**
1. **Presencia Digital desde Cero**
   - Acción: WhatsApp Business → GMB → LinkedIn
   - Proyección: +$4-7M/mes desde 2-3 nuevos clientes

2. **Optimización Combustible**
   - Cálculo: 500L × $68/L × 15% mejora = +$31.5K/mes
   - Acción: Tarjeta COPEC, rutas optimizadas, conducción eficiente

3. **Beneficios Tributarios PRO PYME**
   - Ahorro: 27% → 12.5% IDPC = +$3.02M/mes
   - Validar con contador (campo capturado en formulario)

**Total potencial:** +$8.17-11.86M mensuales en 90 días

---

## 🔧 Próximos Pasos

- [ ] Integrar `generador-informe-mejorado.py` en backend automático
- [ ] Crear webhook que genere PDF al recibir nuevo lead
- [ ] Enviar PDF automáticamente por email (SendGrid)
- [ ] Dashboard para revisar informes generados
- [ ] A/B testing de oportunidades según sector
