# Pasteleria-3-leches

## Instrucciones para usar Git

---

## Configuración inicial

* git config --global user.name "Nombre"

* git config --global user.email "Email"

Listar parametros anteriores

* git config --global --list

* Para clonar nuestro repositorio usar este comando "git clone https://github.com/Byfa96/Pasteleria-3-leches.git"

* Para listar las ramas se usa git branch y para cambiar a su rama se usa git checkout "nombre-de-la-rama"

* Para hacer commits y guardar una versión de tu repositorio actual debes primero añadir los cambios antes de hacer el commit

para esto

* git add . 
el punto significa añadir todo

* Para verificar que cambios hay añadido debes hacer un git status y si se añadio algo que no querías puedes hacer un git reset

* Si te sientes conforme, debes hacer un git commit -m 'Mensaje explicando los cambios'
---

## IMPORTANTE

Es importante saber que las ramas no se actualizan solas, así que hay ciertos procedimientos para subir cambios.

Lo primero es que desde su rama cambien a la rama main

Desde main deben hacer un "git pull origin main" para traer todos los cambios en caso de que hayan, esto con el proposito de evitar conflictos.

Una vez hecho el pull y actualizar la rama main, debes volver a tu rama con git checkout y mezclar los cambios de main con tu rama con un git merge main

Ahora con tu rama mezclada con main y en caso de haber, los conflictos resueltos, debes ir a la rama main de nuevo
con git checkout main y mezclar main con tu rama con un git merge "nombre-de-tu-rama" y listo, ese es el proceso.

Ejemplo con ramas inventadas main y rama1

git branch (para verificar tu rama actual)

git checkout main
git pull origin main
git checkout rama1
git merge main
git checkout main
git merge rama1

Ese sería el proceso