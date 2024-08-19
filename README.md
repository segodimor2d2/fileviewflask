# fileviewflask

Uma serviço Flask para visualizar arquivos de um servidor

## Instalação

```bash
python -m venv novaPasta
cd novaPasta
source bin/activate

pip install --upgrade pip

pip install flask

git clone git@github.com:segodimor2d2/fileviewflask.git
cd fileviewflask
python app.py
```

## Como usar

Acesse a aplicação em http://localhost:8080

http://192.168.15.5:8080

http://localhost:8080/imagens?media_folder=
/home/segodimo/images/familiaGM/fotosFamiliaGM/esconerFotos/
&page=1&per_page=5&width=100

http://192.168.15.5:8080/imagens?media_folder=/Users/recstyle/Desktop/fotos_antigas&page=1&per_page=5&width=100

http://localhost:8080/imagens?media_folder=/home/segodimo/images/familiaGM/fotosFamiliaGM/esconerFotos/&page=1&per_page=5&width=100



