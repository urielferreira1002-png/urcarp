import os
import re

# Diretório dos arquivos
directory = r"c:\Users\aprendiz.sistemas01\Downloads\teste urca"

# Arquivos de carro (excluindo o audi-a6 que já foi feito)
car_files = [
    "carro-nissan-armada.html",
    "carro-mustang-gt500.html",
    "carro-lexus-gs-f.html",
    "carro-lamborghini-huracan.html",
    "carro-gmc-yukon.html",
    "carro-gmc-sierra.html",
    "carro-ford-raptor.html",
    "carro-ford-f250.html",
    "carro-ferrari-488.html",
    "carro-dodge-ram.html",
    "carro-dodge-challenger-demon.html",
    "carro-crown-vic.html",
    "carro-corvette-zr1.html",
    "carro-camaro-zl1.html",
    "carro-camaro-ss-drag.html",
    "carro-cadillac-escalade.html",
    "carro-cadillac-atsv.html",
    "carro-audi-rs7.html",
    "carro-toyota-hilux.html",
    "carro-toyota-supra-a90.html",
    "carro-toyota-prius.html",
    "carro-subaru-wrx-sti.html",
    "carro-range-rover-velar.html",
    "carro-porsche-panamera-techart.html",
    "carro-nissan-patrol.html",
    "carro-vw-passat.html"
]

def update_buy_button(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Substituir o botão de compra para link do Discord
    # Padrão: <button class="btn btn-comprar" onclick="comprarCarro('...')">🛒 COMPRAR AGORA</button>
    # Para: <a href="https://discord.gg/ZgWVdm4H" target="_blank" class="btn btn-comprar">🛒 COMPRAR AGORA</a>

    pattern = r'<button class="btn btn-comprar" onclick="comprarCarro\(\'[^\']+\',\s*\d+\)">🛒 COMPRAR AGORA</button>'
    replacement = '<a href="https://discord.gg/ZgWVdm4H" target="_blank" class="btn btn-comprar">🛒 COMPRAR AGORA</a>'

    content = re.sub(pattern, replacement, content)

    # Salvar o arquivo
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Atualizado: {file_path}")

# Processar todos os arquivos
for car_file in car_files:
    file_path = os.path.join(directory, car_file)
    if os.path.exists(file_path):
        update_buy_button(file_path)
    else:
        print(f"Arquivo não encontrado: {file_path}")

print("Processamento concluído!")