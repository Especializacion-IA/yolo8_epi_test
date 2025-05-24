# YOLOv8 EPI Detection

Este proyecto utiliza **YOLOv8** para detectar elementos de protección individual (EPI) como:

- Cascos  
- Guantes  
- Chalecos  
- Mascarillas  
- Personas  
- Elementos ausentes como `no_gloves`, `no_helmet`, etc.

---

⚠️ **IMPORTANTE:**  
El dataset original **NO está incluido** en este repositorio, por lo que **no es posible reentrenar la red directamente**.  
Sin embargo, puedes usar el modelo ya entrenado (`best.pt`) para ejecutar inferencias sobre nuevas imágenes.

📉 **Estado del modelo:**  
El modelo fue entrenado durante **30 épocas**.  
Actualmente **no es perfecto** y está en fase de mejora, pero ya es funcional para pruebas.

---

## 🛠 Requisitos

- Python ≥ 3.10  
- [Ultralytics YOLOv8](https://docs.ultralytics.com/)  
- OpenCV, Pandas, Matplotlib  

Instalación recomendada:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

## 📷 Cómo usar

Coloca tus imágenes en la carpeta `test_images/`

**Formato permitido:** `.jpg`.

Ejecuta el script de inferencia:

```bash
python infer.py test_images/nombre_de_la_imagen.jpg
```

> Si no proporcionas un nombre, se usará `test_images/casco3.jpg` por defecto.

El script:

- Muestra una ventana con la imagen procesada y los objetos detectados.  
- Imprime el conteo de objetos (por clase).  
- Imprime la cantidad de personas detectadas (`person`).  
- Guarda la imagen con anotaciones en la carpeta `runs/detect/predict/`.

---

## 📁 Estructura de carpetas

```
YOLOv8_EPI_Safety/
├── infer.py              # Inferencia con modelo entrenado
├── train.py              # Script de entrenamiento (no funcional sin dataset)
├── runs/                 # Carpeta de resultados
├── test_images/          # Carpeta donde subir imágenes para testear
├── requirements.txt      # Dependencias necesarias
├── README.md             # Este archivo
└── ...
```

---

## 🚧 Entrenamiento

Aunque `train.py` está disponible, **no funcionará sin el dataset original**.  
Si deseas reentrenar:

1. Consigue el dataset (por ejemplo, desde Roboflow).  
2. Ajusta las rutas en `dataset/data.yaml`.  
3. Lanza el entrenamiento con:

```bash
python train.py
```
⚠️ Advertencia: El dataset original era grande (≈2.5 GB), por eso fue eliminado del repositorio.
---

## 🧠 Autor

Este proyecto forma parte de un estudio sobre el uso de visión por computador para la detección de riesgos laborales.  
El modelo se encuentra en evolución y sigue siendo optimizado.
