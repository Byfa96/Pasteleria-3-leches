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

Una vez hecho el pull y actualizar la rama main, debes volver a tu rama con git checkout y mezclar los cambios de main con tu rama con un git merge main, haces un commit de fusión si hubieron cambios  
git commit -m "Commit de fusión" y luego desde tu rama haces un git push origin nombre-de-tu-rama

Ahora con tu rama mezclada con main y en caso de haber conflictos, estos esten resueltos, debes ir a la rama main de nuevo  
con git checkout main y mezclar main con tu rama con un git merge "nombre-de-tu-rama", finalmente un git push origin main para subir tus cambios y listo, ese es el proceso.  

Ejemplo con ramas inventadas main y rama1

git branch (para verificar tu rama actual, en este ejemplo se asume que estas en rama1)

- git checkout main  
- git pull origin main  
- git checkout rama1  
- git merge main  
- git commit -m "commit de fusión"  
- git push origin rama1  
- git checkout main  
- git merge rama1  
- git push origin main  
Ese sería el proceso  

---

Comandos random con cierta utilidad

git restore //Restaura tus archivos a como estaban en el ultimo commit en tu rama local (NO USAR SI TIENES CAMBIOS EN TUS ARCHIVOS, SOLAMENTE SI DESHACER CAMBIOS).

git clean -fd //Borra todos los archivos nuevos creados que no estaban en el último commit, al igual que el anterior, no usar si tienes cambios y no quieres deshacerlos.