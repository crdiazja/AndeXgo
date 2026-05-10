# AndeXgo — Sitio listo para producción

## Archivos en este paquete
- `index.html` — la página principal (Variante "Red")
- `robots.txt` — instrucciones para Google
- `sitemap.xml` — mapa del sitio para SEO
- `og-image.jpg` — **falta agregar** (1200×630px) para WhatsApp/redes

## Cómo subir a GoDaddy + Netlify (gratis, recomendado)

### 1. Subir a Netlify
1. Andá a https://app.netlify.com (creá cuenta gratis con GitHub o email)
2. **Add new site → Deploy manually**
3. Arrastrá esta carpeta `production` completa a la zona de drop
4. Tu sitio queda vivo en `<algo>.netlify.app` en 30 segundos

### 2. Conectar el dominio andexgo.com
1. En Netlify: **Domain settings → Add custom domain → `andexgo.com`**
2. Netlify te muestra los **nameservers** (4 direcciones tipo `dns1.p01.nsone.net`)
3. Copialos
4. En GoDaddy: **My Products → andexgo.com → DNS → Nameservers → Change → I'll use my own nameservers**
5. Pegá los 4 nameservers de Netlify
6. Save. Esperá 1–24 horas para propagación.

### 3. Activar HTTPS (gratis)
Netlify lo activa solo. En 1 hora aprox tu sitio anda en `https://www.andexgo.com`.

## Cómo actualizar el sitio
Cada vez que cambies algo, simplemente arrastrás la carpeta de nuevo a Netlify (en la pestaña "Deploys") y se publica al toque.

## Pendientes para optimizar después
- [ ] Crear imagen `og-image.jpg` (1200×630) para previews en WhatsApp/LinkedIn
- [ ] Reemplazar fotos placeholder con fotos reales de cargadores
- [ ] Agregar página `/contacto` con formulario real (Netlify Forms es gratis)
- [ ] Google Analytics o Plausible para métricas
- [ ] Conectar el botón "Encontrar cargador" a un mapa real
