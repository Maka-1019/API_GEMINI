import requests
import sys

def verificar_configuracion():
    print("--- Verificación de Entorno Virtual ---")

    if hasattr(sys, 'real_prefix') or (sys.base_prefix != sys.prefix):
        print("✅ Entorno Virtual ACTIVO")
    else:
        print("❌ Entorno Virtual NO activo")

    print(f"📍 Python en uso: {sys.executable}")

    try:
        response = requests.get("https://www.google.com", timeout=5)
        print("🌐 Conexión a internet: OK")
    except Exception as e:
        print(f"⚠️ Error de conexión: {e}")

if __name__ == "__main__":
    verificar_configuracion()
