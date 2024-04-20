print("Hello Git2!")
# git add para añadir fichero para hacer commit
# git status para ver los ficheros actualizados para hacer commit
# git commit para hacer fotografia de nuestro proyecto git
# git log para ver los commits 

# git checkout "fichero en git" para volver a la version del commit

#  git log --graph --pretty=oneline "para modificar git log una linea"
# git log --graph --decorate --all --oneline
# git config --global alias."alias sin comillas" "git log --graph --decorate --all --oneline"
# el anterior codigo sirve para añadir un nuevo comando usando git alias

# git checkout para moverse de ramas
# ejemplo git chekout "nombre del fichero sin comillas"
# ejemplo 2 git checkout codigo Hash
# ejemplo 3 git checkout HEAD "para usar este commit como principal"
# codigo hash se puede obtener usando git log
# en nuestro caso podemos usar git tree y usar la abreviacion
"""
# git reset --hard codigo hash para volver a un commit y eliminar
# todo commit posterior a este
# git reset reflog para restaurar git reset --hard
# usado git reflog tendremos que cambiar el main
# podemos usar git reset --hard con el codigo hash
# del ultimo commit que teniamos
"""
# git tag "id:clase_1" para añadir un id al commit
# añadir git tag "nombre a elegir" sin comillas

# git add . para añadir todos los ficheros actualizados
# git tag para ver los tags

# para moverse a un tag usar: 
# git checkout tags/nombre del tag

# usar git checkout main para volver a la rama main

# para borrar un commit usar git revert
# añade un nuevo commit al final "mejor no usar"




