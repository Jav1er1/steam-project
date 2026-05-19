import requests
import sys
import os

# =========================
# VARIABLES DE ENTORNO
# =========================

API_KEY = os.getenv("STEAM_API_KEY")
STEAM_ID = os.getenv("STEAM_ID")

BASE_URL = "http://api.steampowered.com"

# =========================
# VALIDAR VARIABLES
# =========================

def verificar_config():

    if not API_KEY:
        print("❌ ERROR: STEAM_API_KEY no configurada")
        sys.exit(1)

    if not STEAM_ID:
        print("❌ ERROR: STEAM_ID no configurado")
        sys.exit(1)

# =========================
# MANEJO DE ERRORES
# =========================

def manejar_error(respuesta, mensaje):

    if respuesta.status_code == 401:
        print("❌ ERROR 401: API KEY inválida")
        sys.exit(1)

    elif respuesta.status_code == 404:
        print("❌ ERROR 404: Recurso no encontrado")
        sys.exit(1)

    elif respuesta.status_code == 500:
        print("❌ ERROR 500: Error del servidor")
        sys.exit(1)

    elif respuesta.status_code != 200:
        print(f"❌ ERROR HTTP {respuesta.status_code}: {mensaje}")
        sys.exit(1)

    try:
        return respuesta.json()

    except:
        print("❌ ERROR: JSON inválido")
        sys.exit(1)

# =========================
# OBTENER PERFIL
# =========================

def obtener_perfil():

    try:

        url = f"{BASE_URL}/ISteamUser/GetPlayerSummaries/v0002/"

        params = {
            "key": API_KEY,
            "steamids": STEAM_ID
        }

        r = requests.get(url, params=params, timeout=10)

        data = manejar_error(r, "No se pudo obtener perfil")

        players = data.get("response", {}).get("players", [])

        if not players:
            print("❌ ERROR: Perfil no encontrado")
            sys.exit(1)

        return players[0]

    except requests.exceptions.Timeout:
        print("❌ ERROR: Timeout")
        sys.exit(1)

    except requests.exceptions.ConnectionError:
        print("❌ ERROR: Sin internet")
        sys.exit(1)

    except Exception as e:
        print(f"❌ ERROR DESCONOCIDO: {e}")
        sys.exit(1)

# =========================
# OBTENER NIVEL
# =========================

def obtener_nivel():

    url = f"{BASE_URL}/IPlayerService/GetSteamLevel/v1/"

    params = {
        "key": API_KEY,
        "steamid": STEAM_ID
    }

    r = requests.get(url, params=params)

    data = manejar_error(r, "No se pudo obtener nivel")

    return data.get("response", {}).get("player_level", "Desconocido")

# =========================
# OBTENER JUEGOS
# =========================

def obtener_juegos():

    url = f"{BASE_URL}/IPlayerService/GetOwnedGames/v0001/"

    params = {
        "key": API_KEY,
        "steamid": STEAM_ID,
        "include_appinfo": True
    }

    r = requests.get(url, params=params)

    data = manejar_error(r, "No se pudieron obtener juegos")

    juegos = data.get("response", {}).get("games")

    if juegos is None:
        print("❌ ERROR: Perfil privado")
        sys.exit(1)

    return juegos

# =========================
# MOSTRAR INFO
# =========================

def mostrar_info(perfil, nivel, juegos):

    print("\n======================")
    print("👤 PERFIL")
    print("======================")

    print(f"Nombre: {perfil.get('personaname')}")
    print(f"Nivel Steam: {nivel}")
    print(f"Cantidad Juegos: {len(juegos)}")

    horas = sum(j.get("playtime_forever", 0) for j in juegos) / 60

    print(f"Horas Totales: {horas:.2f}")

    top = sorted(
        juegos,
        key=lambda x: x.get("playtime_forever", 0),
        reverse=True
    )[:5]

    print("\n🔥 TOP 5 JUEGOS")

    for j in top:
        print(
            f"- {j.get('name')} "
            f"({j.get('playtime_forever',0)/60:.2f} hrs)"
        )

# =========================
# MAIN
# =========================

def main():

    verificar_config()

    print("🔄 Obteniendo datos Steam...")

    perfil = obtener_perfil()

    nivel = obtener_nivel()

    juegos = obtener_juegos()

    mostrar_info(perfil, nivel, juegos)

if __name__ == "__main__":
    main()

