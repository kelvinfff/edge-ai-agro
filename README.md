# Edge AI na Automação Agrícola
Demonstração prática de inteligência artificial processada localmente
(Edge AI) para tomada de decisão em irrigação, sem dependência de nuvem.
## O que o projeto faz
Simula leituras de um sensor de umidade do solo e mostra como um
dispositivo local pode decidir irrigar automaticamente quando o solo
atinge 25% de umidade — tudo processado no próprio hardware.
## Conteúdo
| Arquivo | Descrição |
|---------|-----------|
| `demo_simples.py` | Gera dados sintéticos e plota o gráfico de irrigação |
| `requirements.txt` | Dependências (numpy, matplotlib) |
| `grafico_irrigacao_edge.png` | Gráfico gerado para apresentação |
## Como executar
```bash
pip install -r requirements.txt
python3 demo_simples.py
O gráfico será salvo em grafico_irrigacao_edge.png.
Licença
MIT