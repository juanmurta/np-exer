import numpy as np

# Criando dados aleatórios como início
rng = np.random.default_rng(seed=42)
respostas = rng.integers(low=0, high=10, size=210, endpoint=True)
print(respostas)

respostas_reshape = np.reshape(respostas, (7, 30))
print(respostas_reshape)

# média geral de satisfação do cliente
media_geral = np.mean(respostas_reshape)
print(media_geral)

# média diária de satisfação do cliente
media_diaria = np.mean(respostas_reshape, axis=1)
print(media_diaria)