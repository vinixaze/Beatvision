# 🥁 BeatVision: Virtual Drum Kit

O **BeatVision** é um kit de bateria virtual de alta performance que utiliza **Visão Computacional** e **Inteligência Artificial** para transformar movimentos das mãos no ar em sons de bateria em tempo real [1, 2]. O projeto é focado em baixa latência, arquitetura limpa e uma experiência fluida para músicos que desejam praticar sem a necessidade de hardware físico caro [3, 4].

---

## 🚀 Funcionalidades e Roadmap

O desenvolvimento é dividido em Sprints modulares para garantir a robustez de cada componente [5, 6]:

- [x] **Sprint 1: Arquitetura Base** - Estrutura de pastas, gerenciamento de logs (Loguru) e captura de câmera [7].
- [ ] **Sprint 2: Hand Tracking (Em progresso)** - Detecção de 21 pontos das mãos com MediaPipe, identificação de lateralidade e cálculo de velocidade [6-8].
- [ ] **Sprint 3: Drum Engine** - Criação de zonas de impacto virtual e detecção de colisão [3].
- [ ] **Sprint 4: Áudio Engine** - Integração de samples (Kick, Snare, Hi-Hat) com baixa latência via Pygame/SoundDevice [3].
- [ ] **Sprint 5: Interface & HUD** - Calibração visual e interface para o usuário [3].
- [ ] **Sprint 6: Polimento** - Otimizações de performance e documentação final [3].

---

## 🛠️ Tecnologias Utilizadas

Este projeto utiliza o que há de mais moderno no ecossistema Python para processamento de imagem e som [9-11]:

- **Linguagem:** Python 3.12+
- **Visão Computacional:** OpenCV e MediaPipe
- **Processamento de Áudio:** Pygame, SoundDevice e SoundFile
- **Gestão de Dados:** Pydantic para configurações e validações
- **Logging:** Loguru para monitoramento profissional
- **Futuro:** Planejada integração/migração para **Java** para maior performance concorrente.

---

## 📦 Estrutura do Projeto

A arquitetura segue padrões de modularidade para facilitar a manutenção e futura expansão [7, 12, 13]:

```text
vision-engine/
├── src/
│   └── beatvision/
│       ├── camera.py        # Gerenciamento de captura de vídeo
│       ├── hand_tracker.py  # IA e Processamento com MediaPipe
│       ├── renderer.py      # Desenho de elementos visuais na tela
│       ├── app.py           # Orquestração principal da aplicação
│       └── config.py        # Parâmetros e definições do sistema
├── run.py                   # Ponto de entrada do projeto
├── requirements.txt         # Dependências do sistema
└── README.md
🔧 Instalação e Execução
Pré-requisitos
Python 3.12 ou superior
Ambiente virtual (venv) recomendado
Passo a Passo
Clone o repositório:
Crie e ative o ambiente virtual:
Instale as dependências:
Execute a aplicação:
🤝 Contribuição
Este é um projeto pessoal em desenvolvimento ativo. Sinta-se à vontade para abrir Issues ou enviar Pull Requests.
👤 Autor
Vinícius Azevedo - @vinixaze
