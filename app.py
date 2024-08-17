from flask import Flask, render_template, send_from_directory, request
import os

app = Flask(__name__)

# Número de arquivos por página
PER_PAGE = 5

@app.route('/imagens')
def imagens():
    media_folder = request.args.get('media_folder', '/')
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', PER_PAGE, type=int)
    width = request.args.get('width', 100, type=int)  # Largura em porcentagem, padrão é 100

    if not os.path.exists(media_folder):
        return "Diretório não encontrado!", 404

    arquivos = os.listdir(media_folder)
    imagens = [arquivo for arquivo in arquivos if arquivo.endswith(('.png', '.jpg', '.jpeg', '.gif'))]

    start = (page - 1) * per_page
    end = start + per_page
    imagens_pagina = imagens[start:end]

    total_imagens = len(imagens)
    total_paginas = (total_imagens // per_page) + (total_imagens % per_page > 0)

    return render_template('imagens.html', imagens=imagens_pagina, pagina=page, total_paginas=total_paginas, per_page=per_page, width=width, media_folder=media_folder)

@app.route('/videos')
def videos():
    media_folder = request.args.get('media_folder', '/')
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', PER_PAGE, type=int)
    width = request.args.get('width', 100, type=int)  # Largura em porcentagem, padrão é 100

    if not os.path.exists(media_folder):
        return "Diretório não encontrado!", 404

    arquivos = os.listdir(media_folder)
    videos = [arquivo for arquivo in arquivos if arquivo.endswith(('.mp4', '.avi', '.mov', '.mkv'))]

    start = (page - 1) * per_page
    end = start + per_page
    videos_pagina = videos[start:end]

    total_videos = len(videos)
    total_paginas = (total_videos // per_page) + (total_videos % per_page > 0)

    return render_template('videos.html', videos=videos_pagina, pagina=page, total_paginas=total_paginas, per_page=per_page, width=width, media_folder=media_folder)

@app.route('/media/<path:nome_arquivo>')
def mostrar_arquivo(nome_arquivo):
    media_folder = request.args.get('media_folder', '/')
    if not os.path.exists(media_folder):
        return "Diretório não encontrado!", 404
    return send_from_directory(media_folder, nome_arquivo)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
