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

def update_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Atualizar grid-template-columns para 3 colunas
    content = re.sub(
        r'\.botoes\s*\{\s*grid-template-columns:\s*1fr\s+1fr\s*;\s*\}',
        '.botoes { grid-template-columns: 1fr 1fr 1fr; }',
        content
    )

    # 2. Adicionar botão Discord no HTML
    # Procurar pela seção de botões e adicionar o Discord
    discord_button = '          <a href="https://discord.gg/ZgWVdm4H" target="_blank" class="btn btn-discord">💬 DISCORD</a>\n'

    # Encontrar onde adicionar o botão Discord (antes do fechamento da div .botoes)
    pattern = r'(\s*<button class="btn btn-voltar"[^>]*>← VOLTAR LOJA</button>\s*)(\s*</div>\s*)'
    if re.search(pattern, content):
        content = re.sub(pattern, r'\1' + discord_button + r'\2', content)

    # 3. Adicionar CSS do botão Discord
    # Encontrar onde adicionar após .btn-voltar:hover
    css_pattern = r'(\.btn-voltar:hover\s*\{\s*background:\s*rgba\(\d+,\s*\d+,\s*\d+,\s*0\.3\);\s*\})'

    discord_css = '''
    .btn-discord {
      background: linear-gradient(135deg, #5865f2, #4752c4);
      color: #fff;
      border: 1px solid rgba(88, 101, 242, 0.5);
      transition: all 0.3s ease;
    }

    .btn-discord:hover {
      background: linear-gradient(135deg, #4752c4, #3c45a5);
      transform: translateY(-2px);
      box-shadow: 0 15px 40px rgba(88, 101, 242, 0.4);
    }'''

    if re.search(css_pattern, content):
        content = re.sub(css_pattern, r'\1' + discord_css, content)

    # Salvar o arquivo
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Atualizado: {file_path}")

# Processar todos os arquivos
for car_file in car_files:
    file_path = os.path.join(directory, car_file)
    if os.path.exists(file_path):
        update_file(file_path)
    else:
        print(f"Arquivo não encontrado: {file_path}")

print("Processamento concluído!")