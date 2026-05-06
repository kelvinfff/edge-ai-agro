#!/usr/bin/env python3
"""
Demonstracao simples: Edge AI na Irrigacao Agricola
Gera 1 grafico claro para apresentacao de 10 minutos.
"""

import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ============================================================
# Dados simulados: sensor de umidade do solo ao longo do tempo
# ============================================================
np.random.seed(42)

# 200 leituras de sensor (~3 horas, 1 leitura/min)
leituras = 200
umidade = np.zeros(leituras)
umidade[0] = 45  # começa úmido

# Simulacao: solo seca naturalmente (~0.3% por leitura)
# Quando atinge 25%, irriga e volta para 50%
chuva = np.zeros(leituras)  # 0 = não irrigou, 1 = irrigou

for i in range(1, leituras):
    # Solo seca naturalmente + ruído
    umidade[i] = umidade[i-1] - 0.30 + np.random.normal(0, 0.5)

    # Se solo seco demais → irriga
    if umidade[i] < 25:
        umidade[i] = 50
        chuva[i] = 1
    else:
        chuva[i] = 0

# ============================================================
# Grafico único para a apresentação
# ============================================================
plt.rcParams.update({
    "figure.dpi": 150,
    "axes.titlesize": 15,
    "axes.labelsize": 13,
    "xtick.labelsize": 10,
    "ytick.labelsize": 10,
})

fig, ax = plt.subplots(figsize=(12, 6))

# Linha da umidade do solo
ax.plot(umidade, color="#2E86C1", linewidth=2, label="Umidade do solo (%)")

# Limiar de 25%
ax.axhline(y=25, color="#E74C3C", linestyle="--", linewidth=2, alpha=0.8,
           label="Limiar: 25% (aciona irrigação)")

# Destacar zonas onde irrigou
eventos = np.where(chuva == 1)[0]
for e in eventos:
    ax.axvline(x=e, color="#F39C12", alpha=0.25, linewidth=3)

# Primeiro evento com legenda
ax.axvline(x=eventos[0], color="#F39C12", alpha=0.4, linewidth=3,
           label=f"Irrigação acionada ({len(eventos)} vezes)")

# Anotação: "dispositivo local"
ax.annotate(
    "Decisão ocorre no\npróprio dispositivo\n(sem nuvem)",
    xy=(60, 55),
    fontsize=12,
    color="#7D3C98",
    fontweight="bold",
    bbox=dict(boxstyle="round,pad=0.5", facecolor="#E8DAEF", edgecolor="#7D3C98", alpha=0.9),
)

# Anotação: métricas principais
ax.annotate(
    f"Modelo: 6.7 KB\nResposta: microssegundos\nSem internet necessária",
    xy=(140, 55),
    fontsize=12,
    color="#1E8449",
    fontweight="bold",
    bbox=dict(boxstyle="round,pad=0.5", facecolor="#D5F5E3", edgecolor="#1E8449", alpha=0.9),
)

ax.set_xlabel("Leituras do sensor (1 por minuto)")
ax.set_ylabel("Umidade do Solo (%)")
ax.set_title("Edge AI na Irrigação: decisão local sem depender da nuvem", fontweight="bold")
ax.legend(loc="lower left", fontsize=10)
ax.set_ylim(0, 70)
ax.grid(True, alpha=0.3)

plt.tight_layout()
caminho = "grafico_irrigacao_edge.png"
fig.savefig(caminho, bbox_inches="tight")
plt.close(fig)

print(f"Grafico salvo em: {os.path.abspath(caminho)}")
print(f"Irrigações acionadas: {len(eventos)} vezes em {leituras} leituras")
