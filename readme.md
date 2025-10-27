┌─────────────────────────────────┐
│  Navegador (tu PC/móvil)        │
└──────────────┬──────────────────┘
               │ HTTP
┌──────────────▼──────────────────┐
│  Nginx (puerto 80/443)          │
│  - Sirve interfaz web           │
│  - Redirige /api a Flask        │
└──────────────┬──────────────────┘
               │ localhost:5000
┌──────────────▼──────────────────┐
│  Docker Container               │
│  ├─ Gunicorn (WSGI server)      │
│  ├─ Flask (tu API)              │
│  └─ SQLite (datos)              │
└─────────────────────────────────┘
```

## Stack final recomendado

- **OS**: Raspberry Pi OS Lite 64-bit
- **Contenedor**: Docker + docker-compose
- **Backend**: Flask + Gunicorn
- **BD**: SQLite (migrando de JSON)
- **Proxy**: Nginx (si quieres interfaz web)
- **Monitoreo**: systemctl (para reiniciar automáticamente)

## Cambios mínimos para producción

Si quieres que sea un poco más robusto ahora mismo, solo modifica el Dockerfile para usar Gunicorn:

En `requirements.txt` agrega:
```
gunicorn==21.2.0