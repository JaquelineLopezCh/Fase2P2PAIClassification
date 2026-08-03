# Sistema Inteligente para la Clasificación Automática de Facturas P2P mediante Inteligencia Artificial

## Descripción del proyecto

Este proyecto implementa una aplicación web basada en Inteligencia Artificial para apoyar el proceso **Procure to Pay (P2P)**. La solución permite clasificar automáticamente la descripción de una factura utilizando un modelo de Machine Learning y exponer el resultado mediante una interfaz web y una API REST desarrollada con Flask.

La aplicación fue desarrollada como parte del proyecto integrador de la asignatura **Gestión de Proyectos de Inteligencia Artificial**, considerando buenas prácticas de desarrollo, integración, contenerización y despliegue.

## Objetivo

Desarrollar una solución técnica funcional que permita:

- Clasificar automáticamente descripciones de facturas.
- Integrar un modelo de Machine Learning con una API REST.
- Implementar una interfaz web para el usuario.
- Contenerizar la aplicación utilizando Docker.
- Preparar el proyecto para un despliegue en la nube.

## Arquitectura del sistema

```text
Usuario
  -> Frontend HTML/CSS/JavaScript
  -> Solicitud POST /predict
  -> Backend Flask API REST
  -> Modelo Machine Learning
  -> Respuesta JSON
  -> Resultado visible en pantalla
```

## Tecnologías utilizadas

- Python 3.12
- Flask
- HTML5
- CSS3
- JavaScript
- Scikit-Learn
- Pandas
- Joblib
- Docker
- Docker Compose
- GitHub

## Estructura del proyecto

```text
P2P-AI-Classification/
  api/
    routes.py
  model/
    train.csv
    train_model.py
    model.pkl
  static/
    style.css
    script.js
  templates/
    index.html
  docs/
  screenshots/
  app.py
  Dockerfile
  docker-compose.yml
  requirements.txt
  README.md
```

## Instalación local

```bash
git clone https://github.com/USUARIO/P2P-AI-Classification.git
cd P2P-AI-Classification
pip install -r requirements.txt
python model/train_model.py
python app.py
```

Abrir en el navegador:

```text
http://localhost:5000
```

## Ejecución con Docker

Construir la imagen:

```bash
docker build -t p2p-ai .
```

Ejecutar el contenedor:

```bash
docker run -p 5000:5000 p2p-ai
```

También se puede utilizar Docker Compose:

```bash
docker compose up --build
```

## Endpoints

### Página principal

```http
GET /
```

### Clasificación

```http
POST /predict
```

Ejemplo de solicitud:

```json
{
  "text": "Purchase order for office supplies"
}
```

Respuesta esperada:

```json
{
  "prediction": "PO Invoice"
}
```

### Estado del servicio

```http
GET /health
```

Respuesta esperada:

```json
{
  "status": "UP",
  "application": "P2P AI Classification",
  "model_loaded": true
}
```

### Versión

```http
GET /version
```

## Modelo de Inteligencia Artificial

El modelo fue entrenado utilizando ejemplos relacionados con el proceso P2P. Para la clasificación se emplea un pipeline de Scikit-Learn con TF-IDF Vectorizer y Logistic Regression.

Categorías objetivo:

- PO Invoice
- Non PO Invoice
- Credit Memo

## Pruebas sugeridas

- Factura con orden de compra: `Purchase order for office supplies`
- Factura sin orden de compra: `Hotel reimbursement`
- Nota de crédito: `Credit note from supplier`
- Texto vacío
- Solicitud JSON inválida
- Health check del servicio

## Posibles mejoras

- Integración con SAP.
- Consumo de OCR para lectura automática de facturas.
- Entrenamiento con un conjunto de datos más amplio.
- Autenticación mediante JWT.
- Base de datos para almacenar resultados.
- Pipeline CI/CD para despliegue continuo.

## Autora

Jaqueline López Chaidez

Asignatura: **Gestión de Proyectos de Inteligencia Artificial**

## Licencia

Proyecto desarrollado únicamente con fines académicos.
