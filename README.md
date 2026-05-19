# Detección de Fusarium TR4 con Random Forest

Sistema de clasificación basado en **Random Forest** para detectar zonas de cultivo de banano y plátano en riesgo de infección por *Fusarium oxysporum* cubense Raza Tropical 4 (TR4), una de las amenazas fitosanitarias más graves para los cultivos latinoamericanos.

---

## ¿Qué es este proyecto?

Este proyecto simula un sistema de monitoreo agrícola inteligente que analiza datos de **sensores de suelo y ambiente** para predecir si una zona de cultivo está en riesgo de infección por Fusarium TR4.

Se desarrolló como ejemplo práctico del modelo **Random Forest** en el contexto de ensambles estadísticos en Machine Learning.

---

## ¿Por qué Fusarium TR4?

El hongo *Fusarium oxysporum* cubense TR4 representa una amenaza crítica para la industria bananera colombiana y latinoamericana:

- Colombia detectó TR4 en 2019 en La Guajira
- Amenaza las 584.000 ha de banano y plátano sembradas en el país
- Persiste en el suelo por décadas sin posibilidad de erradicación
- La detección temprana es clave para evitar pérdidas millonarias

---

## ¿Cómo funciona?

El modelo analiza **5 variables de sensores** por zona de cultivo:

| Sensor | Descripción |
|---|---|
| `pH_suelo` | Acidez del suelo (4.5 - 7.5) |
| `humedad_suelo` | Humedad del suelo en % (30 - 95%) |
| `temperatura` | Temperatura del suelo en °C (18 - 35°C) |
| `conductividad` | Conductividad eléctrica del suelo |
| `humedad_ambiente` | Humedad relativa del ambiente (40 - 100%) |

Y predice si la zona está sana o infectada, junto con la probabilidad de infección.

---

## Resultados del modelo

El modelo alcanza un **97% de accuracy** sobre datos de prueba.

| Métrica | Sano | Infectado |
|---|---|---|
| Precision | 0.96 | 1.00 |
| Recall | 1.00 | 0.75 |
| F1-score | 0.98 | 0.86 |

### Importancia de cada sensor

![Feature Importance](feature_importance.png)

La **temperatura**, **humedad del suelo** y **pH** son los factores más determinantes para la detección del hongo, resultado consistente con la biología del TR4, que prospera en suelos cálidos, húmedos y ácidos.

---

## Cómo ejecutarlo

### 1. Clonar el repositorio
```bash
git clone https://github.com/sebasvcx/Fusarium-Random-Forest.git
cd Fusarium-Random-Forest
```

### 2. Crear entorno virtual e instalar dependencias
```bash
python3 -m venv venv
source venv/bin/activate
pip install scikit-learn pandas matplotlib seaborn
```

### 3. Ejecutar
```bash
python3 fusarium_rf.py
```

---

## Estructura del proyecto

```
Fusarium-Random-Forest/
├── fusarium_rf.py          # Código principal
├── feature_importance.png  # Gráfica de importancia de sensores
└── README.md
```

---

## Tecnologías

- Python 3.x
- scikit-learn 1.8
- pandas 3.0
- matplotlib 3.10
- seaborn 0.13

---

## Contexto académico

Proyecto desarrollado para la asignatura **Introducción a la Inteligencia Artificial** como demostración práctica del modelo **Random Forest** dentro de los métodos de ensamble estadístico en Machine Learning.