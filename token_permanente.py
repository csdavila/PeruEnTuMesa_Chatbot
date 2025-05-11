import requests

APP_ID = '970590888620767'
APP_SECRET = 'ccb75fe3e9c91386b9b6860108cf71d9'
SHORT_LIVED_TOKEN = 'EAANyv00jct8BOyfdi2ZCVqHbZCGZAlk6nR8UZAUZB8umwAFN9nQnNK4dBL8LDnSgO02cW7696FO8QfV5FrFlnl3x4ZA7alOPUSGEQk5RePMOUsv1ek2iEL5UgP95aPYy0uuX20GERB9msmjibZAZA4u5DvucEAPLlxFNQJXJYm5Hc5DlZChCZCOng8kEHwvG4pn0iIrJD5miFAG1VxGgJXyLp3aFk1'

url = f"https://graph.facebook.com/v19.0/oauth/access_token?grant_type=fb_exchange_token&client_id={APP_ID}&client_secret={APP_SECRET}&fb_exchange_token={SHORT_LIVED_TOKEN}"


response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    long_lived_token = data['access_token']
    expires_in = data.get('expires_in', 'unknown')
    print(f"Token de larga duración obtenido:\n{long_lived_token}")
    print(f"Este token expira en aproximadamente {expires_in} segundos (~{expires_in/3600/24:.1f} días).")

    #Guardar en un archivo de texto
    with open('long_lived_token.txt', 'w') as f:
        f.write(long_lived_token)
    print("Token guardado en 'long_lived_token.txt'")
else:
    print(f"Error al obtener token largo: {response.text}")