🥁 BeatVision
BeatVision é um kit de bateria virtual de alta performance que utiliza Visão Computacional para transformar movimentos das mãos no ar em sons de bateria em tempo real. O projeto foca em baixa latência, arquitetura limpa e uma experiência de usuário fluida para bateristas e entusiastas.
🚀 Funcionalidades (Roadmap)
O projeto está sendo desenvolvido em Sprints modulares:
Sprint 1: Arquitetura Base (Concluído) - Estrutura de pastas, gerenciamento de câmera e logs profissionais
.
Sprint 2: Hand Tracking (Em andamento) - Detecção de mãos com MediaPipe, extração de coordenadas e cálculo de velocidade
.
Sprint 3: Drum Engine - Zonas de impacto virtual e detecção de colisão
.
Sprint 4: Áudio Engine - Integração de samples de alta qualidade (Kick, Snare, Hi-Hat) com baixa latência
.
Sprint 5: Interface & HUD - Calibração visual e interface para o usuário
.
Sprint 6: Polimento - Otimizações de performance e documentação final
.
🛠️ Tecnologias Utilizadas
Este projeto utiliza ferramentas modernas do ecossistema Python para garantir robustez e performance:
Linguagem: Python 3.12+
Visão Computacional: OpenCV e MediaPipe
Áudio: Pygame e SoundDevice
Gestão de Dados: Pydantic para configurações
Logging: Loguru para rastreamento de eventos
📦 Estrutura do Projeto
A arquitetura segue padrões de modularidade para facilitar a manutenção:
vision-engine/
├── src/
│   └── beatvision/
│       ├── camera.py        # Gerenciamento de captura de vídeo [10]
│       ├── hand_tracker.py  # Processamento de IA com MediaPipe [10]
│       ├── renderer.py      # Desenho de elementos visuais na tela [10]
│       ├── app.py           # Orquestração principal da aplicação [10]
│       └── config.py        # Parâmetros e definições do sistema [10]
├── run.py                   # Ponto de entrada do projeto [11]
├── requirements.txt         # Dependências do sistema [8, 9]
└── README.md
🔧 Instalação e Execução
Pré-requisitos
Python 3.12 ou superior
Ambiente virtual (venv)
Passo a Passo
Clone o repositório:
Crie e ative o ambiente virtual:
Instale as dependências:
Execute a aplicação:
🤝 Contribuição
Este é um projeto pessoal em desenvolvimento ativo. Sinta-se à vontade para abrir Issues ou enviar Pull Requests.
👤 Autor
- Vinícius Azevedo - @vinixaze
