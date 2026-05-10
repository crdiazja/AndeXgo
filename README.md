# AndeXgo — Sitio listo para producción

Sitio web operativo para **www.andexgo.com** con mapa en vivo de la red LATAM y buscador de cargadores cercanos.

## Archivos en este paquete

| Archivo | Descripción |
|---|---|
| `index.html` | Página principal — single page con mapa, catálogo, casos de uso, API y CTA |
| `logo-andexgo.png` | Logo de la marca (header + footer) |
| `favicon.png` | Ícono que aparece en la pestaña del navegador |
| `robots.txt` | Le dice a Google qué puede indexar |
| `sitemap.xml` | Mapa del sitio para SEO |
| `og-image.jpg` | **Falta agregar** (1200×630px) — preview en WhatsApp / LinkedIn / Twitter |

## Funcionalidades del sitio

### 🗺️ Mapa operativo en vivo
- 13 estaciones reales en Colombia, Ecuador, Perú, Bolivia y Chile
- Tiles oscuros de CartoDB sobre OpenStreetMap (no requiere API key)
- Pin animado por estación con popup detallado: dirección, potencia, tipo, número de puertos
- Zoom + scroll wheel + controles de navegación

### 🔍 Buscador "Encontrar cargador más cercano"
Disponible desde **3 botones** (nav, hero y CTA final). Abre un drawer superior con:
- **Geolocalización** — usa la ubicación actual del navegador con un click
- **Búsqueda por dirección** — autocompletado contextual usando Nominatim (OpenStreetMap), gratis y sin API key
- **Sugerencias inteligentes** — prioriza resultados cerca de la ubicación del usuario
- **Filtro por distancia** — solo muestra estaciones a ≤ 20 km del punto buscado
- **Lista ordenada** por distancia con km exactos

### 📍 Popup de cada estación
- Nombre y dirección completa
- Potencia (kW) y tipo (DC FAST / AC + DC)
- Distancia desde el punto buscado
- **Botones de navegación**:
  - 🗺️ Abrir en Google Maps
  - 📍 Abrir en Waze (con navegación activa)
  - 📋 Copiar dirección al portapapeles

### 🎨 Diseño responsive
- Mobile-first con breakpoints en 500px, 700px, 768px, 900px
- Tipografía IBM Plex Sans + Mono (Google Fonts)
- Paleta verde neón sobre fondo dark naval

---

## Cómo subir a GoDaddy + Netlify (gratis)

### 1. Subir a Netlify
1. Andá a https://app.netlify.com (creá cuenta gratis con GitHub o email)
2. **Add new site → Deploy manually**
3. Arrastrá la carpeta `production` completa a la zona de drop
4. Tu sitio queda vivo en `<algo>.netlify.app` en 30 segundos

### 2. Conectar el dominio andexgo.com
1. En Netlify: **Domain settings → Add custom domain → `andexgo.com`**
2. Netlify te muestra 4 **nameservers** (tipo `dns1.p01.nsone.net`)
3. En GoDaddy: **My Products → andexgo.com → DNS → Nameservers → Change → I'll use my own nameservers**
4. Pegá los 4 nameservers de Netlify y guardá
5. Esperá 1–24 horas para propagación

### 3. HTTPS automático
Netlify activa SSL/HTTPS solo. En ~1 hora `https://www.andexgo.com` está vivo.

---

## Cómo actualizar el sitio
Editá los archivos localmente y arrastrá la carpeta de nuevo a Netlify (pestaña **Deploys**). Se publica al instante.

---

## Permisos del navegador

Para que **"Usar mi ubicación actual"** funcione, el navegador pide permiso de geolocalización. Esto **solo funciona sobre HTTPS** — es decir, una vez que el sitio está vivo en Netlify (no funciona abriendo el archivo `index.html` localmente).

---

## Servicios externos (todos gratis, sin API key)

- **OpenStreetMap + CartoDB** — tiles del mapa
- **Nominatim** — geocoding (dirección → lat/lng) y autocompletado
- **Leaflet 1.9.4** — librería del mapa (CDN unpkg)
- **Google Fonts** — IBM Plex Sans / Mono

> ⚠️ Nominatim tiene un rate limit de 1 request/segundo. Para tráfico alto (>10k búsquedas/día), considerá migrar a Mapbox Geocoding o Google Places.

---

## Pendientes para después

- [ ] Crear imagen `og-image.jpg` (1200×630) para previews en redes
- [ ] Reemplazar imágenes placeholder por fotos reales de cargadores
- [ ] Agregar página `/contacto` con formulario (Netlify Forms es gratis)
- [ ] Google Analytics o Plausible para métricas de uso
- [ ] Página `/estaciones` con detalle por estación (nombre amigable en URL)
- [ ] Conectar API real `/v1/stations/nearby` a la grilla del dashboard (hoy son números fijos)
- [ ] Verificar el sitio en Google Search Console y enviar `sitemap.xml`
