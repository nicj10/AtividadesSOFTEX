import numpy as np

tabuleiro = [["[ ]" for _ in range(8)] for _ in range(8)]

tabuleiro[1] = ["pea" for _ in range(8)]  # peões pretos
tabuleiro[6] = ["pea" for _ in range(8)]  # peões brancos

pecas = ["tor", "cav", "bis", "rai", "rei", "bis", "cav", "tor"]

tabuleiro[0] = pecas[:]  
tabuleiro[7] = pecas[:]  

print(np.array(tabuleiro))
