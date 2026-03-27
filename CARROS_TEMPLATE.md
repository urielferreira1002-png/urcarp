# 🚗 Páginas Individuais de Carros - URCA RP

## Status: ✅ Sistema Implementado

Foram criadas páginas individuais para os carros da loja. Veja abaixo o status das páginas criadas:

### Carros Normais ✅
- ✅ `carro-audi-a6.html` - Audi A6
- ✅ `carro-gmc-sierra.html` - GMC Sierra  
- ✅ `carro-gmc-yukon.html` - GMC Yukon
- ✅ `carro-toyota-hilux.html` - Toyota Hilux
- ✅ `carro-cadillac-escalade.html` - Cadillac Escalade
- ⏳ Outros 9 carros (podem ser criados com o template abaixo)

### Pacote VIP ✅
- ✅ `carro-audi-rs7.html` - Audi RS7
- ⏳ Outros 11 carros VIP

### Pacote VIP+ ✅
- ✅ `carro-ferrari-488.html` - Ferrari 488 GTB
- ⏳ Outros 12 carros VIP+

---

## 📋 Template para Criar Mais Carros

Copie e adapte este template para cada novo carro:

```html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>[NOME DO CARRO] | URCA RP</title>
  <link rel="stylesheet" href="style.css">
  <link rel="stylesheet" href="menu-style.css">
  <style>
    .carro-detalhe { max-width: 1200px; margin: 0 auto; padding: 40px 20px; }
    .carro-hero { display: grid; grid-template-columns: 1fr 1fr; gap: 40px; align-items: center; }
    .carro-imagem { position: relative; overflow: hidden; border-radius: 15px; box-shadow: 0 0 40px rgba(139, 0, 255, 0.2); }
    .carro-imagem img { width: 100%; height: auto; display: block; border-radius: 15px; }
    .carro-info h1 { color: #d6b87c; font-size: 48px; margin-bottom: 10px; }
    .carro-info-data { color: #888; margin-bottom: 30px; }
    .descricao { color: #bbb; line-height: 1.8; margin: 20px 0; font-size: 15px; }
    .preco-info { background: linear-gradient(135deg, #8b00ff, #00ffff); border-radius: 10px; padding: 20px; margin: 30px 0; text-align: center; }
    .preco-info .valor { color: #fff; font-size: 32px; font-weight: 700; margin: 10px 0; }
    .especificacoes { background: rgba(139, 0, 255, 0.1); border: 1px solid rgba(139, 0, 255, 0.3); border-radius: 10px; padding: 25px; margin: 30px 0; }
    .especificacoes h3 { color: #d6b87c; margin-bottom: 20px; text-transform: uppercase; font-size: 14px; }
    .spec-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 20px; }
    .spec-item { display: flex; justify-content: space-between; padding: 10px 0; border-bottom: 1px solid rgba(139, 0, 255, 0.2); }
    .spec-label { color: #aaa; font-size: 14px; }
    .spec-valor { color: #fff; font-weight: 600; }
    .botoes { display: grid; grid-template-columns: 1fr 1fr; gap: 15px; margin-top: 30px; }
    .btn { padding: 15px 30px; border: none; border-radius: 8px; font-size: 16px; font-weight: 600; cursor: pointer; transition: all 0.3s ease; text-transform: uppercase; letter-spacing: 1px; }
    .btn-comprar { background: linear-gradient(135deg, #8b00ff, #00ffff); color: #fff; box-shadow: 0 10px 30px rgba(139, 0, 255, 0.3); }
    .btn-comprar:hover { transform: translateY(-2px); box-shadow: 0 15px 40px rgba(139, 0, 255, 0.4); }
    .btn-voltar { background: rgba(139, 0, 255, 0.2); color: #fff; border: 1px solid rgba(139, 0, 255, 0.5); }
    @media (max-width: 768px) {
      .carro-hero { grid-template-columns: 1fr; }
      .carro-info h1 { font-size: 32px; }
      .botoes { grid-template-columns: 1fr; }
    }
  </style>
</head>
<body>
  <header class="header-urca">
    <div class="header-content">
      <h1>🎮 URCA RP</h1>
      <div class="header-actions">
        <button class="hamburger-btn" onclick="toggleHeaderMenu()">
          <span></span><span></span><span></span>
        </button>
        <nav class="header-menu" id="headerMenu">
          <div class="header-menu-title">NAVEGAÇÃO</div>
          <a href="index.html">🏠 Início</a>
          <a href="loja.html" class="active">🚗 Loja</a>
          <a href="urca-rp.html">🎮 URCA RP</a>
          <a href="vip.html">💎 VIP</a>
          <a href="conta.html">👤 Conta</a>
          <hr>
          <a href="https://discord.gg" target="_blank">💬 Discord</a>
        </nav>
      </div>
    </div>
  </header>

  <section class="carro-detalhe">
    <div class="carro-hero">
      <div class="carro-imagem">
        <img src="/imagens/[NOME_IMAGEM].jpg" alt="[NOME DO CARRO]">
      </div>
      <div class="carro-info">
        <h1>[NOME DO CARRO]</h1>
        <p class="carro-info-data">[DESCRIÇÃO BREVE]</p>
        <p class="descricao">[DESCRIÇÃO COMPLETA DO CARRO]</p>
        <div class="preco-info">
          <div>Preço</div>
          <div class="valor">R$ [PREÇO]</div>
          <div style="font-size: 12px; color: rgba(255,255,255,0.7);">In-game currency</div>
        </div>
        <div class="especificacoes">
          <h3>📊 Especificações</h3>
          <div class="spec-grid">
            <div class="spec-item"><span class="spec-label">Velocidade Máxima</span><span class="spec-valor">[VEL] km/h</span></div>
            <div class="spec-item"><span class="spec-label">Aceleração</span><span class="spec-valor">[ACEL] seg</span></div>
            <div class="spec-item"><span class="spec-label">Torque</span><span class="spec-valor">[TORQUE] Nm</span></div>
            <div class="spec-item"><span class="spec-label">Potência</span><span class="spec-valor">[HP] HP</span></div>
            <div class="spec-item"><span class="spec-label">Tipo</span><span class="spec-valor">[TIPO]</span></div>
            <div class="spec-item"><span class="spec-label">Bancos</span><span class="spec-valor">[BANCOS] pessoas</span></div>
          </div>
        </div>
        <div class="botoes">
          <button class="btn btn-comprar" onclick="comprarCarro('[NOME DO CARRO]', [PREÇO])">🛒 COMPRAR AGORA</button>
          <button class="btn btn-voltar" onclick="window.location.href='loja.html'">← VOLTAR LOJA</button>
        </div>
      </div>
    </div>
  </section>

  <script src="script.js"></script>
  <script src="menu-script.js"></script>
</body>
</html>
```

---

## 🔗 Como Linkar na loja.html

Para cada carro, update o botão para um link:

### Carros Normais:
```html
<a href="carro-[nome-arquivo].html" class="comprar">VER DETALHES</a>
```

### Carros VIP:
```html
<a href="carro-[nome-arquivo].html" class="comprar vip-btn" style="display: block; text-align: center; text-decoration: none;">VER DETALHES</a>
```

### Carros VIP+:
```html
<a href="carro-[nome-arquivo].html" class="comprar vipplus-btn" style="display: block; text-align: center; text-decoration: none;">VER DETALHES</a>
```

---

## 📝 Dicas Importantes

1. **Nomes de arquivo**: Use padrão kebab-case: `carro-nome-modelo.html`
2. **Imagens**: Verifique os nomes das imagens em `/imagens/` antes de linkar
3. **Cores VIP**: Use padrão dourado (`#d6b87c`) para destaque VIP
4. **Cores VIP+**: Use gradiente vermelho (`#ff4757, #ff6b7a`) para destaque VIP+
5. **Especificações**: Adapte conforme o tipo de veículo

---

## ✨ Próximos Passos Sugeridos

1. Criar as 9 páginas restantes de carros normais
2. Criar as 11 páginas restantes de carros VIP  
3. Criar as 12 páginas restantes de carros VIP+
4. Adicionar galeria de imagens em cada página
5. Adicionar avaliações/reviews de usuários

---

**Criado em**: 23 de março de 2026
**Sistema**: URCA RP - Loja de Carros
