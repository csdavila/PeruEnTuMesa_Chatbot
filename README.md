# PeruEnTuMesa_Chatbot

# 🤖 Asistente Virtual de Comida Peruana vía WhatsApp

Este proyecto implementa un **asistente virtual inteligente** para un negocio de comida peruana que responde mensajes de WhatsApp en tiempo real. Utiliza **Flask**, **Firebase**, **transformers de Hugging Face** y la **API de WhatsApp Business**.

---

## 🚀 Características

- 🧠 Respuestas inteligentes usando un modelo de lenguaje (LLaMA).
- 📱 Integración completa con la API de WhatsApp.
- 🔎 Consulta de precios e ingredientes desde Firestore.
- 📝 Listado dinámico del menú.
- 🗣️ Interacción conversacional natural con los usuarios.
- 🔐 Token de acceso largo a la API de Meta (Facebook).

---

## 📦 Requisitos

Instala las dependencias con:

```bash
pip install -r requirements.txt
```

requirements.txt:
flask
transformers
requests
bitsandbytes
firebase_admin
torch

## 🔧 Configuración
Clona el repositorio y entra en el directorio:

```bash
git clone https://github.com/csdavila/PeruEnTuMesa_Chatbot.git
cd PeruEnTuMesa_Chatbot
```

Agrega tu archivo de credenciales Firebase:

Coloca el archivo JSON de servicio de Firebase en la raíz del proyecto y nómbralo:
peruentumesa-firebase-adminsdk-fbsvc-d7adfe37e5.json

Configura las variables de entorno:

Crea un archivo .env (o exporta en el entorno):
VERIFY_TOKEN=mi_token_unico_12345
ACCESS_TOKEN=tu_token_de_acceso_largo

Modifica el modelo si es necesario:
model_name = "csdavila/Llama-3.2"

## ▶️ Ejecución

```bash
python app.py
```

## 🌐 Webhook de WhatsApp
La ruta /whatsapp acepta dos métodos:

GET: para la verificación del webhook de Meta.

POST: para recibir y procesar mensajes entrantes.

## 💬 Funcionalidades del Asistente
Consultas disponibles:
Precio de un plato:

"¿Cuánto cuesta el lomo saltado?"

Ingredientes:

"¿Qué lleva el ají de gallina?"

Ver menú:

"¿Qué platos tienen?"

Hacer pedido:

"Quiero pedir ceviche"

Otras preguntas:

El modelo responderá usando IA si no se detecta una intención específica.

## 🔐 Obtener Token de Acceso Largo
Utiliza el siguiente script para intercambiar un token de acceso corto por uno de larga duración:


```bash
python obtener_token_largo.py
```

El token se guardará en long_lived_token.txt.


## 🧾 Licencia
Este proyecto es de uso libre con fines educativos o personales.
Para uso comercial, consulta los términos de la API de Meta y Hugging Face.