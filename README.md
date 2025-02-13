# update-property

Este proyecto es una utilidad para actualizar propiedades de objetos en JavaScript de manera segura y eficiente, incluso cuando las propiedades están profundamente anidadas.

## 🚀 Características

- Actualiza propiedades de objetos anidados utilizando una cadena de ruta.
- Crea la propiedad si no existe en el objeto.
- Devuelve `true` si la propiedad se actualizó o creó con éxito.
- Devuelve `false` si el argumento proporcionado no es un objeto.

## 📦 Instalación

1. Clona el repositorio:

   ```sh
   git clone https://github.com/HenryJulian3/update-property.git
   cd update-property
   ```

2. Instala las dependencias:

   ```sh
   npm install
   ```

## 🛠 Uso

1. Importa la función en tu proyecto:

   ```javascript
   const updateProperty = require('update-property');
   ```

2. Utiliza la función para actualizar una propiedad anidada:

   ```javascript
   const obj = {
     n: {
       p: {
         m: true
       }
     }
   };

   const result = updateProperty('n.p.m', obj, false);
   console.log(result); // true
   console.log(obj.n.p.m); // false
   ```

## 📋 Notas

- Si la propiedad no existe en el objeto, la función la creará automáticamente.
- Si el argumento proporcionado no es un objeto, la función devolverá `false`.

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Siéntete libre de abrir un issue o enviar un pull request.

## 📜 Licencia

Este proyecto está bajo la Licencia MIT.
