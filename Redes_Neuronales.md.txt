# 🧠 Redes Neuronales Artificiales (RNA)

Las Redes Neuronales Artificiales (RNA o ANN) son modelos computacionales inspirados en la estructura y función interconectada de las **neuronas biológicas** del cerebro. Son el componente fundamental del **Aprendizaje Profundo (Deep Learning)**.

---

## 1. Concepto y Neurona Artificial

### La Neurona (Perceptrón)
* Es la unidad básica de la red. Recibe múltiples **entradas (datos)**, las combina y produce una única **salida**.
* **Componentes Clave:**
    * **Pesos (Weights):** Valores que miden la importancia de cada entrada. Estos son los que se **aprenden** durante el entrenamiento.
    * **Función de Activación:** Decide si la neurona debe "activarse" (transmitir una señal) y qué tan fuerte. Introduce la **no linealidad** necesaria para resolver problemas complejos.

### Arquitectura de Capas
Una RNA se organiza en capas de neuronas:
* **Capa de Entrada (Input Layer):** Recibe los datos iniciales.
* **Capas Ocultas (Hidden Layers):** Realizan la mayor parte del procesamiento y la extracción de características. El **Deep Learning** utiliza múltiples capas ocultas.
* **Capa de Salida (Output Layer):** Produce el resultado final (ej: la clasificación, la predicción).

---

## 2. Proceso de Aprendizaje

El aprendizaje de una red neuronal es un proceso iterativo de ajuste de pesos:

### Propagación hacia Adelante (Forward Propagation)
1.  Los datos pasan desde la Capa de Entrada, a través de las Capas Ocultas, hasta la Capa de Salida, generando una predicción.

### Cálculo del Error (Función de Costo)
2.  Se mide la diferencia (error) entre la predicción de la red y el valor real esperado.

### Retropropagación (Backpropagation)
3.  El error se propaga hacia atrás a través de la red, desde la salida hasta las capas iniciales.
4.  El algoritmo **ajusta iterativamente los pesos** de la red para minimizar el error, utilizando un optimizador (ej. Descenso de Gradiente).

---

## 3. Tipos Comunes de Redes

| Tipo de Red | Abreviatura | Aplicación Principal |
| :--- | :--- | :--- |
| **Perceptrón Multicapa** | MLP | Clasificación y regresión general. |
| **Redes Neuronales Convolucionales**| CNN | Procesamiento de Imágenes, Visión Artificial y Video. |
| **Redes Neuronales Recurrentes** | RNN / LSTM | Procesamiento de Lenguaje Natural (PLN) y Series de Tiempo (datos secuenciales). |