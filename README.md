# 🍔 Burger Queen - Sistema de Pedidos Django

Bienvenido a **Burger Queen**, un proyecto simple de Django diseñado para principiantes. Este sistema permite gestionar un menú de productos y recibir pedidos de clientes.

## 📋 Requisitos Previos

Antes de empezar, asegúrate de tener instalado **Python** en tu ordenador.
Puedes verificarlo abriendo una terminal y escribiendo:

```bash
python --version
# O en algunos sistemas Linux/Mac:
python3 --version
```

---

## 🚀 Guía de Instalación y Ejecución

Sigue estos pasos para levantar el proyecto en tu máquina local (Windows, Mac o Linux).

### 1. Clonar o Descargar el Proyecto
Si tienes este código en una carpeta, abre tu terminal (CMD, PowerShell o Terminal) y navega hasta la carpeta del proyecto:

```bash
cd ruta/a/burguer_queen
```

### 2. Crear un Entorno Virtual
Es una buena práctica aislar las librerías del proyecto.

**En Windows:**
```bash
python -m venv venv
.\venv\Scripts\activate
```

**En Mac / Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```
*(Verás que aparece `(venv)` al principio de tu línea de comandos)*.

### 3. Instalar Dependencias
Las librerías necesarias están listadas en `requirements.txt`. Instálalas con pip:

```bash
pip install -r requirements.txt
```

> Incluye `Django`, `djangorestframework` y `Pillow` (para manejar imágenes de productos).

### 4. Preparar la Base de Datos
Django usa una base de datos SQLite por defecto. Necesitamos crear las tablas iniciales:

```bash
python manage.py migrate
```

### 5. Crear un Usuario Administrador
Para poder entrar al panel de administración y agregar productos (hamburguesas, bebidas, etc.):

```bash
python manage.py createsuperuser
```
*Sigue las instrucciones (usuario, correo y contraseña).*

### 6. Levantar el Servidor
¡Es hora de encender la cocina! 🔥

```bash
python manage.py runserver
```

Abre tu navegador y ve a: **http://127.0.0.1:8000/**

---

## 📂 Estructura del Proyecto

El proyecto está organizado de la siguiente manera:

- **`core/`**: Es el corazón del proyecto (configuraciones, URLs principales).
- **`pedidos/`**: Es la "app" donde vive la lógica de nuestro negocio.
- **`db.sqlite3`**: Tu base de datos local (se crea al ejecutar migrate).
- **`manage.py`**: El control remoto para ejecutar comandos de Django.

---

## 📦 Modelos de Datos (Base de Datos)

El sistema utiliza 3 tablas principales (definidas en `pedidos/models.py`):

1. **Categoria** 🏷️
   - Sirve para agrupar productos (ej: "Bebidas", "Hamburguesas").
   - Campo: `nombre`.

2. **Producto** 🍔
   - Los ítems que vendemos.
   - Campos: `nombre`, `precio`, `descripcion`.
   - Relación: Pertenece a una **Categoria**.

3. **Pedido** 📝
   - Registra cuando un cliente compra algo.
   - Campos: `nombre_cliente`, `direccion`, `fecha_registro`.
   - Relación: Está vinculado a un **Producto**.

---

## 🖥️ Cómo Usar el Sistema

1. **Panel de Administración:**
   - Ve a `http://127.0.0.1:8000/admin/`
   - Loguéate con el superusuario que creaste.
   - **¡Importante!** Crea algunas *Categorías* y *Productos* aquí primero para que aparezcan en el menú.

2. **Ver el Menú:**
   - Ve a `http://127.0.0.1:8000/menu/`
   - Verás la lista de productos disponibles.

3. **Hacer un Pedido:**
   - Ve a `http://127.0.0.1:8000/menu/pedido/`
   - Llena el formulario para pedir un producto.

---

## 🛠️ Comandos Útiles

| Acción | Comando |
|--------|---------|
| Crear migraciones (si cambias models.py) | `python manage.py makemigrations` |
| Aplicar migraciones a la BD | `python manage.py migrate` |
| Correr el servidor | `python manage.py runserver` |
| Crear superusuario | `python manage.py createsuperuser` |
| Poblar datos de ejemplo | `python manage.py seed_data` |

¡Disfruta programando con Django!
