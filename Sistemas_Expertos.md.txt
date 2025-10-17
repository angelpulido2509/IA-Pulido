# ⚙️ Sistemas Expertos (SE)

Un Sistema Experto (SE) es un programa informático que **emula el razonamiento y la toma de decisiones** de un experto humano en un campo específico y bien definido (dominio). Son una de las primeras y más exitosas ramas de la IA Convencional.

---

## 1. Componentes Clave

Los Sistemas Expertos se diferencian de los programas tradicionales porque separan el conocimiento de su procesamiento.

### Base de Conocimiento
* Contiene la información de alto nivel del dominio: **Hechos** (datos brutos) y **Reglas Heurísticas** (reglas de inferencia, usualmente en formato "SI-ENTONCES").
* Esta es la "experiencia" codificada del experto humano.

### Motor de Inferencia
* Es el "cerebro" del SE; la parte que procesa y encadena las reglas de la Base de Conocimiento para llegar a una conclusión o recomendación.
* **Métodos comunes:**
    * **Encadenamiento hacia adelante (Forward Chaining):** Razona a partir de los datos de entrada para alcanzar una conclusión.
    * **Encadenamiento hacia atrás (Backward Chaining):** Parte de una conclusión o hipótesis para verificar los hechos necesarios que la sustentan.

### Interfaz de Usuario
* Permite la comunicación entre el usuario y el sistema.
* Debe ser capaz de ofrecer **explicaciones** sobre el proceso de razonamiento seguido para justificar la conclusión.

### Módulo de Adquisición de Conocimiento
* Herramientas utilizadas por los ingenieros de conocimiento para ingresar y actualizar el conocimiento de los expertos humanos en la Base de Conocimiento.

---

## 2. Aplicaciones y Ventajas

### Aplicaciones Típicas
* **Diagnóstico:** Identificación de fallas en maquinaria o enfermedades (ej. el famoso sistema **MYCIN**).
* **Configuración y Diseño:** Sistemas para configurar pedidos complejos de equipos.
* **Planificación:** Planificación de rutas y logística.

### Ventajas de los SE
* **Permanencia del Conocimiento:** El conocimiento experto no se pierde (como sucede cuando un experto humano se jubila).
* **Rapidez y Consistencia:** Ofrecen conclusiones de forma rápida y aplican las reglas de manera uniforme.
* **Acceso Masivo:** Permiten que el conocimiento experto esté disponible para muchos usuarios.