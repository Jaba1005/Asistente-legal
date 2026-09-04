# Asistente Legal/Normativo – Universidad Konrad Lorenz 

Este repositorio contiene un chatbot construido con la librería `google-genai` (Gemini) que actúa como asistente legal/normativo de la Universidad Konrad Lorenz. Responde preguntas sobre reglamentos y normativas de la universidad, y mantiene un historial de conversación con dos interacciones de ejemplo precargadas para dar contexto al modelo desde el inicio.

## 📁 Estructura del repositorio

```
Asistente-legal/
├──.env
├── asistente.py   # Chatbot: Asistente Legal/Normativo
└── README.md
```

<img width="374" height="270" alt="image" src="https://github.com/user-attachments/assets/4bf5ff2d-0b56-4545-9d4b-674d4ad3399d" />


## ✅ Requisitos previos

- Una cuenta de Google AI Studio con una **API Key** de Gemini. Puedes generarla en: https://aistudio.google.com/apikey

## ⚙️ Instalación paso a paso

### 1. Clonar el repositorio

```bash
git clone https://github.com/Jaba1005/Asistente-legal.git
cd Asistente-legal
```

### 2. Crear y activar un entorno virtual (recomendado)

```bash
python -m venv venv

venv\Scripts\activate
```

### 3. Instalar las dependencias

Este proyecto usa dos librerías principales: `google-genai` (SDK de Gemini) y `python-dotenv` (para leer variables de entorno). Instálalas con:

```bash
pip install google-genai python-dotenv
```

### 4. Configurar la API Key

Crea un archivo llamado `.env` en la raíz del proyecto (mismo nivel que `asistente.py`) con el siguiente contenido:

```
GENAI_API_KEY=tu_api_key_aqui
```
---

## 🧪 Ejercicio — Asistente Legal/Normativo (`asistente.py`)

**¿Qué hace?** Simula un asistente legal/normativo de la Universidad Konrad Lorenz, especializado en reglamentos y contratos de la institución. Responde de forma concisa y segura, con base en las normas universitarias, y rechaza cualquier pregunta que no esté relacionada con la normativa institucional. Además, mantiene manualmente un historial de conversación (`conversation_history`) que incluye dos interacciones de ejemplo precargadas (sobre inasistencias), de modo que el modelo conserva contexto desde el arranque del programa.



**Cómo usarlo:**
1. Escribe tu pregunta relacionada con la normativa de la universidad cuando el programa te lo pida (`Usuario: `).
2. El asistente responderá en la consola, basándose en el contexto de reglamentos/contratos.
3. Escribe `salir`, `exit` o `quit` para terminar la conversación.

```markdown
![Salida - Asistente Legal/Normativo]
```
`system_instruction`.)*

```markdown
![Salida - Rechazo de pregunta fuera de tema]
```
<img width="1458" height="974" alt="image" src="https://github.com/user-attachments/assets/cb2c5ea0-5ff0-4e96-831a-8d181a7c71ad" />

<img width="1463" height="994" alt="image" src="https://github.com/user-attachments/assets/ade8d3da-211a-4a35-bb12-e2809b104c85" />

