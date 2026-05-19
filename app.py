import requests
import os
import time
from difflib import get_close_matches

API_KEY = os.getenv("STEAM_API_KEY")
STEAM_ID = os.getenv("STEAM_ID")

if not API_KEY:
    print("❌ ERROR: STEAM_API_KEY no configurada")
    exit()

def limpiar():
    os.system("clear")

def pausa():
    input("\nPresione ENTER para continuar...")

def buscar_juego():

    limpiar()

    print("================================")
    print("    BUSCAR JUEGO EN MI CUENTA")
    print("================================")

    nombre = input("\nIngrese nombre del juego: ")

    print("\n🔄 Buscando en tu biblioteca...\n")

    url = f"https://api.steampowered.com/IPlayerService/GetOwnedGames/v1/?key={API_KEY}&steamid={STEAM_ID}&include_appinfo=true"

    try:

        response = requests.get(url, timeout=10)

        data = response.json()

        juegos = data["response"].get("games", [])

        encontrados = []

        for juego in juegos:

            juego_nombre = juego.get("name", "")

            if nombre.lower() in juego_nombre.lower():

                encontrados.append(juego)

        if encontrados:

            encontrados = sorted(
                encontrados,
                key=lambda x: x.get("playtime_forever", 0),
                reverse=True
            )

            for juego in encontrados:

                horas = round(
                    juego.get("playtime_forever", 0) / 60,
                    1
                )

                print(f"🎮 {juego['name']}")
                print(f"⏰ Horas jugadas: {horas}")
                print(f"🆔 APP ID: {juego['appid']}")
                print("--------------------------------")

        else:

            print("❌ No se encontraron juegos en tu biblioteca")

    except Exception as e:

        print(f"❌ Error: {e}")

    pausa()

def top_juegos_globales():

    limpiar()

    print("================================")
    print("       TOP JUEGOS GLOBALES")
    print("================================\n")

    juegos = [
        "Counter-Strike 2",
        "Dota 2",
        "PUBG",
        "Apex Legends",
        "Rust",
        "GTA V",
        "Naraka Bladepoint",
        "Wallpaper Engine",
        "War Thunder",
        "Dead By Daylight"
    ]

    for i, juego in enumerate(juegos, start=1):

        print(f"{i}. 🎮 {juego}")

        time.sleep(0.2)

    pausa()

def mi_perfil():

    limpiar()

    print("================================")
    print("           MI PERFIL")
    print("================================")

    url = f"https://api.steampowered.com/ISteamUser/GetPlayerSummaries/v2/?key={API_KEY}&steamids={STEAM_ID}"

    response = requests.get(url)

    data = response.json()

    player = data["response"]["players"][0]

    print(f"\n🎮 Nombre: {player.get('personaname')}")
    print(f"🌐 Perfil: {player.get('profileurl')}")
    print(f"🖼️ Avatar: {player.get('avatarfull')}")

    estado = player.get("personastate")

    estados = {
        0: "Desconectado",
        1: "Online",
        2: "Ocupado",
        3: "Ausente",
        4: "Durmiendo",
        5: "Quiere intercambiar",
        6: "Quiere jugar"
    }

    print(f"🟢 Estado: {estados.get(estado)}")

    pausa()

def mis_juegos():

    limpiar()

    print("================================")
    print("       MIS JUEGOS TOP")
    print("================================\n")

    url = f"https://api.steampowered.com/IPlayerService/GetOwnedGames/v1/?key={API_KEY}&steamid={STEAM_ID}&include_appinfo=true"

    response = requests.get(url)

    data = response.json()

    juegos = data["response"].get("games", [])

    juegos_ordenados = sorted(
        juegos,
        key=lambda x: x.get("playtime_forever", 0),
        reverse=True
    )

    for juego in juegos_ordenados[:10]:

        horas = round(juego["playtime_forever"] / 60, 1)

        print(f"🎮 {juego['name']}")
        print(f"⏰ Horas jugadas: {horas}")
        print("--------------------------------")

    pausa()

def buscar_usuario():

    limpiar()

    print("================================")
    print("        BUSCAR USUARIO")
    print("================================")

    steamid = input("\nIngrese SteamID64: ")

    url = f"https://api.steampowered.com/ISteamUser/GetPlayerSummaries/v2/?key={API_KEY}&steamids={steamid}"

    response = requests.get(url)

    data = response.json()

    players = data["response"]["players"]

    if len(players) == 0:

        print("❌ Usuario no encontrado")
        pausa()
        return

    player = players[0]

    print(f"\n🎮 Nombre: {player.get('personaname')}")
    print(f"🌐 Perfil: {player.get('profileurl')}")
    print(f"🖼️ Avatar: {player.get('avatarfull')}")

    pausa()

def comparar_perfiles():

    limpiar()

    print("================================")
    print("       COMPARAR PERFILES")
    print("================================")

    otro = input("\nIngrese SteamID64 a comparar: ")

    url1 = f"https://api.steampowered.com/IPlayerService/GetOwnedGames/v1/?key={API_KEY}&steamid={STEAM_ID}&include_appinfo=true"

    url2 = f"https://api.steampowered.com/IPlayerService/GetOwnedGames/v1/?key={API_KEY}&steamid={otro}&include_appinfo=true"

    data1 = requests.get(url1).json()
    data2 = requests.get(url2).json()

    juegos1 = data1["response"].get("games", [])
    juegos2 = data2["response"].get("games", [])

    total1 = len(juegos1)
    total2 = len(juegos2)

    horas1 = sum(j["playtime_forever"] for j in juegos1) / 60
    horas2 = sum(j["playtime_forever"] for j in juegos2) / 60

    print("\n========== RESULTADOS ==========\n")

    print(f"🎮 Tus juegos: {total1}")
    print(f"🎮 Juegos otro usuario: {total2}")

    print(f"\n⏰ Tus horas: {round(horas1,1)}")
    print(f"⏰ Horas otro usuario: {round(horas2,1)}")

    comunes = []

    ids2 = [j["appid"] for j in juegos2]

    for juego in juegos1:

        if juego["appid"] in ids2:
            comunes.append(juego["name"])

    print(f"\n🤝 Juegos en común: {len(comunes)}")

    for juego in comunes[:10]:
        print(f"🎮 {juego}")

    pausa()

def menu():

    while True:

        limpiar()

        print("================================")
        print("       STEAM MANAGER PRO")
        print("================================")
        print("1. Buscar juegos de mi biblioteca")
        print("2. Ver top juegos globales")
        print("3. Ver mi perfil")
        print("4. Ver mis juegos más jugados")
        print("5. Buscar usuario Steam")
        print("6. Comparar perfiles")
        print("7. Salir")
        print("================================")

        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            buscar_juego()

        elif opcion == "2":
            top_juegos_globales()

        elif opcion == "3":
            mi_perfil()

        elif opcion == "4":
            mis_juegos()

        elif opcion == "5":
            buscar_usuario()

        elif opcion == "6":
            comparar_perfiles()

        elif opcion == "7":

            print("\n👋 Cerrando aplicación...")
            time.sleep(1)

            break

        else:

            print("\n❌ Opción inválida")
            time.sleep(1)

menu()