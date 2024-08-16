# Proyecto de Gestión de Estudiantes, Profesores, Cursos y Blog

Este proyecto es una aplicación web que permite gestionar información sobre estudiantes, profesores, cursos y ofrece funcionalidades adicionales para un blog, donde los usuarios registrados pueden interactuar, crear y comentar en publicaciones. A continuación se describe cómo configurar y probar el proyecto.

## Estructura del Proyecto

1. **Base de Datos**: 
   - **Descripción**: Base de datos que contiene tablas para Estudiantes, Profesores, Cursos y la nueva funcionalidad del blog.
   - **Archivos**: `database.sql` (o el archivo SQL que utilices para importar la base de datos).

2. **Archivos HTML**:
   - **Descripción**: Archivos HTML para la interfaz de usuario.
   - **Archivos**:
     - `estudiantes.html`
     - `profesores.html`
     - `cursos.html`
     - `precios.html`
     - `entregables.html`
     - `creacurso.html`
     - `crearestudiante.html`
     - **Nuevos Archivos**:
       - `newpost.html`
       - `edit_post.html`
       - `delete_post.html`
       - `post_detail.html`
       - `login_register.html`
       - `user_register.html`
       - `profile.html`

## Configuración Inicial

1. **Importar la Base de Datos**:
   - Importa el archivo SQL en tu sistema de gestión de bases de datos (MySQL, PostgreSQL, SQLite, etc.).
   - Asegúrate de que las tablas `Estudiantes`, `Profesores`, `Cursos`, y las tablas relacionadas con el blog (por ejemplo, `Posts`, `Comentarios`, `Usuarios`) estén correctamente creadas y pobladas con datos de ejemplo si es necesario.

2. **Configurar el Servidor Web**:
   - Si estás usando un servidor web local como XAMPP, WAMP o MAMP, coloca los archivos HTML en el directorio correspondiente (por ejemplo, `htdocs` en XAMPP).

## Pruebas y Funcionalidades

### 1. Página de Estudiantes

- **Archivo**: `estudiantes.html`
- **Funcionalidad**: Muestra una lista de estudiantes. Puedes realizar operaciones como agregar, editar o eliminar estudiantes (dependiendo de la implementación).
- **Instrucciones**: 
  1. Abre `estudiantes.html` en tu navegador.
  2. Verifica que se muestre la lista de estudiantes importados desde la base de datos.
  3. Prueba las funcionalidades disponibles (si están implementadas).

### 2. Página de Profesores

- **Archivo**: `profesores.html`
- **Funcionalidad**: Muestra una lista de profesores. Permite realizar operaciones relacionadas con profesores.
- **Instrucciones**:
  1. Abre `profesores.html` en tu navegador.
  2. Verifica que se muestre la lista de profesores importados desde la base de datos.
  3. Prueba las funcionalidades disponibles (si están implementadas).

### 3. Página de Cursos

- **Archivo**: `cursos.html`
- **Funcionalidad**: Muestra una lista de cursos. Permite gestionar información relacionada con los cursos.
- **Instrucciones**:
  1. Abre `cursos.html` en tu navegador.
  2. Verifica que se muestre la lista de cursos importados desde la base de datos.
  3. Prueba las funcionalidades disponibles (si están implementadas).

### 4. Página de Precios

- **Archivo**: `precios.html`
- **Funcionalidad**: Muestra una lista de cursos. Permite visualizar los precios relacionados con los cursos.
- **Instrucciones**:
  1. Abre `precios.html` en tu navegador.
  2. Verifica que se muestre la lista de precios de los cursos importados desde la base de datos.
  3. Prueba las funcionalidades disponibles (si están implementadas).

### 5. Página de Entregables

- **Archivo**: `entregables.html`
- **Funcionalidad**: Muestra la base de datos de los alumnos y cursos vigentes.
- **Instrucciones**:Indicar manualmente `/entregables`, dado que no se integró ningún HTML directo.
  1. Abre `entregables.html` en tu navegador.
  2. Verifica que se muestre la lista de cursos y estudiantes importados desde la base de datos.
  3. Prueba las funcionalidades disponibles (si están implementadas).

### 6. Página de Crear Curso

- **Archivo**: `creacurso.html`
- **Funcionalidad**: Te permite crear un nuevo curso.
- **Instrucciones**: Indicar manualmente `/crearcurso`, dado que no se integró ningún HTML directo.
  1. Abre `creacurso.html` en tu navegador.
  2. Crea un nuevo curso en la base de datos.
  3. Prueba las funcionalidades disponibles (si están implementadas).

### 7. Página de Crear Estudiante

- **Archivo**: `crearestudiante.html`
- **Funcionalidad**: Te permite crear un nuevo estudiante.
- **Instrucciones**: Indicar manualmente `/creaestudiante`, dado que no se integró ningún HTML directo.
  1. Abre `crearestudiante.html` en tu navegador.
  2. Crea un nuevo estudiante en la base de datos.
  3. Prueba las funcionalidades disponibles (si están implementadas).

### 8. Blog y Gestión de Usuarios

#### a. Página de Crear Nuevo Post

- **Archivo**: `newpost.html`
- **Funcionalidad**: Permite a los usuarios registrados crear un nuevo post en el blog.
- **Instrucciones**:
  1. Abre `newpost.html` en tu navegador.
  2. Completa el formulario para crear un nuevo post.
  3. Verifica que el post se muestre en la lista de publicaciones del blog.

#### b. Página de Editar Post

- **Archivo**: `edit_post.html`
- **Funcionalidad**: Permite a los usuarios registrados editar un post existente.
- **Instrucciones**:
  1. Abre `edit_post.html` en tu navegador.
  2. Modifica el contenido del post existente.
  3. Verifica que los cambios se reflejen correctamente en la publicación del blog.

#### c. Página de Eliminar Post

- **Archivo**: `delete_post.html`
- **Funcionalidad**: Permite a los usuarios registrados eliminar un post existente.
- **Instrucciones**:
  1. Abre `delete_post.html` en tu navegador.
  2. Selecciona el post que deseas eliminar.
  3. Verifica que el post se haya eliminado correctamente de la lista de publicaciones.

#### d. Página de Detalle del Post

- **Archivo**: `post_detail.html`
- **Funcionalidad**: Muestra el detalle de un post específico. Permite a los usuarios leer el contenido completo del post y ver los comentarios.
- **Instrucciones**:
  1. Abre `post_detail.html` en tu navegador.
  2. Verifica que el detalle del post se muestre correctamente.
  3. Comprueba que los comentarios del post se visualicen adecuadamente.

#### e. Página de Inicio de Sesión y Registro

- **Archivo**: `login_register.html`
- **Funcionalidad**: Permite a los usuarios iniciar sesión o registrarse en la plataforma.
- **Instrucciones**:
  1. Abre `login_register.html` en tu navegador.
  2. Usa el formulario para iniciar sesión o registrarte.
  3. Verifica que el inicio de sesión y el registro funcionen correctamente.

#### f. Página de Registro de Usuario

- **Archivo**: `user_register.html`
- **Funcionalidad**: Permite a los usuarios registrarse en la plataforma.
- **Instrucciones**:
  1. Abre `user_register.html` en tu navegador.
  2. Completa el formulario para registrar un nuevo usuario.
  3. Verifica que el usuario se registre correctamente y pueda iniciar sesión.

#### g. Página de Perfil de Usuario

- **Archivo**: `profile.html`
- **Funcionalidad**: Muestra y permite a los usuarios gestionar su perfil.
- **Instrucciones**:
  1. Abre `profile.html` en tu navegador.
  2. Revisa y edita la información del perfil del usuario.
  3. Verifica que los cambios se guarden correctamente.

## Notas Adicionales

- Asegúrate de que tu servidor web esté en funcionamiento y que la base de datos esté correctamente configurada antes de probar las páginas HTML.
- Si encuentras algún problema, verifica los archivos de configuración del servidor y los scripts de conexión a la base de datos.
- Para las nuevas funcionalidades de blog y gestión de usuarios, asegúrate de tener un sistema de autenticación y autorización adecuado.

## Contribuciones

Si deseas contribuir a este proyecto, por favor sigue estos pasos:

1. Realiza un fork del repositorio.
2. Crea una nueva rama (`git checkout -b feature/nueva-funcionalidad`).
3. Realiza los cambios y haz commit (`git commit -am 'Añadir nueva funcionalidad'`).
4. Envía un pull request.