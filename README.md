# 🎮 Jogo Top-Down em Pygame Zero

Este projeto é um **jogo 2D top-down** desenvolvido em **Python utilizando Pygame Zero**. O objetivo principal é demonstrar conceitos de lógica de jogos, organização de código em classes, animações simples e controle de estados de jogo.

---

## 🧠 Visão Geral do Código

O projeto é dividido em módulos, cada um com uma responsabilidade clara:

### `game.py`

Arquivo principal do jogo. É responsável por:

* Definir o tamanho da janela (`WIDTH`, `HEIGHT`)
* Controlar os estados do jogo (início, jogando, game over)
* Gerenciar inimigos, projéteis e obstáculos
* Controlar pontuação, spawn de inimigos e música
* Implementar as funções obrigatórias do Pygame Zero (`update`, `draw`)

### `player.py`

Contém a classe `Player`, responsável por:

* Movimentação do personagem (W, A, S, D)
* Animações (idle e walk)
* Lançamento de facas
* Colisão com obstáculos e limites da tela

### `enemy.py`

Define a classe `Enemy`, que:

* Suporta diferentes tipos de inimigos (ex: coelho, abelha, minhoca)
* Possui animações (idle, walk, dead)
* Segue o jogador automaticamente
* Trata vida, morte e tempo de exibição do sprite morto

### `obstacle.py`

Responsável pelos obstáculos do cenário:

* Utiliza sprites de parede
* Bloqueia movimentação do jogador e da maioria dos inimigos
* Alguns inimigos (ex: abelha) ignoram colisão

### `background.py`

Implementa o fundo do jogo utilizando **tiles**, repetindo um sprite de grama para preencher toda a tela.

### `knife.py`

Classe do projétil lançado pelo jogador:

* Move-se em direção ao mouse
* Detecta colisão com inimigos
* É removido ao sair da tela

### `crosshair.py`

Controla a mira que acompanha a posição do mouse.

---

## 🕹️ Controles Básicos

* **W A S D** → movimentar personagem
* **Mouse** → mirar
* **Clique esquerdo** → lançar faca
* **Espaço** → iniciar o jogo / reiniciar após Game Over

---

## ▶️ Como Executar o Projeto no VS Code

### Pré-requisitos

* Python **3.10 ou superior** instalado
* Extensão **Python** instalada no VS Code

### 1️⃣ Instalar o Pygame Zero

No terminal do VS Code:

```bash
pip install pgzero
```

### 2️⃣ Estrutura básica esperada

```
mygame/
│── game.py
│── player.py
│── enemy.py
│── obstacle.py
│── background.py
│── knife.py
│── crosshair.py
│── images/
│── sounds/
```

### 3️⃣ Executar o jogo

No terminal integrado do VS Code, dentro da pasta do projeto:

```bash
pgzrun game.py
```

O jogo será iniciado em uma nova janela.

---

## 🖼️ Imagens do Projeto

```
<img width="798" height="594" alt="menu" src="https://github.com/user-attachments/assets/cc167a7c-b24f-471d-a82f-f76ac188d44d" />
<img width="798" height="591" alt="gameplay" src="https://github.com/user-attachments/assets/5e75b127-4a5b-489a-9241-e79660da8d3b" />
<img width="798" height="593" alt="game_over" src="https://github.com/user-attachments/assets/d88376d7-d20c-4234-b55c-dda416b05164" />
```

---

## 🎞️ GIF do Jogo

> 📌 **Adicione aqui um GIF demonstrando o gameplay**

```
![gif](https://github.com/user-attachments/assets/03449ef2-18cf-416d-87f8-fc6b3ef531c2)
```

---

## 📌 Observação Final

Este projeto foi desenvolvido com foco em **aprendizado**, explorando organização de código, lógica de jogos e boas práticas iniciais em Python com Pygame Zero.

Ele serve como uma base sólida para evoluções futuras, como fases, power-ups, barra de vida e novos tipos de inimigos.
