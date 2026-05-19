import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix

# Semilla para que los resultados sean reproducibles
np.random.seed(42)

# Simulamos 300 zonas de cultivo con sus mediciones de sensores
n = 300

data = pd.DataFrame({
    'pH_suelo':         np.random.uniform(4.5, 7.5, n),
    'humedad_suelo':    np.random.uniform(30, 95, n),
    'temperatura':      np.random.uniform(18, 35, n),
    'conductividad':    np.random.uniform(0.1, 2.5, n),
    'humedad_ambiente': np.random.uniform(40, 100, n),
})

# Regla realista: Fusarium TR4 prospera en suelos ácidos,
# húmedos y cálidos
infectado = (
    (data['pH_suelo'] < 6.0) &
    (data['humedad_suelo'] > 65) &
    (data['temperatura'] > 25)
).astype(int)

data['infectado'] = infectado

print(data.head(10))
print(f"\nZonas infectadas: {infectado.sum()} / {n}")

# Separar features (X) y variable objetivo (y)
X = data.drop('infectado', axis=1)
y = data['infectado']

# Dividir en entrenamiento (80%) y prueba (20%)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

modelo = RandomForestClassifier(
    n_estimators=100,  # 100 árboles
    max_depth=5,       # profundidad máxima por árbol
    random_state=42
)
modelo.fit(X_train, y_train)

# Evaluar el modelo
y_pred = modelo.predict(X_test)
print("\n--- RESULTADOS DEL MODELO ---")
print(classification_report(y_test, y_pred,
      target_names=['Sano', 'Infectado']))

# Feature Importance - qué sensores importan más
importancias = pd.Series(
    modelo.feature_importances_,
    index=X.columns
).sort_values(ascending=False)

plt.figure(figsize=(8, 5))
sns.barplot(x=importancias.values, y=importancias.index, palette='viridis')
plt.title('Importancia de cada sensor para detectar Fusarium TR4')
plt.xlabel('Importancia')
plt.ylabel('Sensor')
plt.tight_layout()
plt.savefig('feature_importance.png')
plt.show()
print("\nImportancia por sensor:")
print(importancias)

# Predecir una zona nueva con sus mediciones de sensores
zona_nueva = pd.DataFrame([{
    'pH_suelo': 5.2,
    'humedad_suelo': 80.0,
    'temperatura': 28.5,
    'conductividad': 1.2,
    'humedad_ambiente': 75.0
}])

prediccion = modelo.predict(zona_nueva)[0]
probabilidad = modelo.predict_proba(zona_nueva)[0]

print("\n--- PREDICCIÓN ZONA NUEVA ---")
print(f"pH: 5.2 | Humedad suelo: 80% | Temperatura: 28.5°C")
print(f"Resultado: {'🔴 INFECTADA' if prediccion == 1 else '🟢 SANA'}")
print(f"Probabilidad de infección: {probabilidad[1]*100:.1f}%")

# Matriz de confusión
cm = confusion_matrix(y_test, y_pred)

plt.figure(figsize=(6, 5))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
            xticklabels=['Sano', 'Infectado'],
            yticklabels=['Sano', 'Infectado'])
plt.title('Matriz de Confusión - Fusarium TR4')
plt.ylabel('Real')
plt.xlabel('Predicción')
plt.tight_layout()
plt.savefig('confusion_matrix.png')
plt.show()