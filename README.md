# Palpite Mega Sena

Este projeto gera palpites aleatórios para a Mega Sena, com números únicos e organizados em ordem crescente.

## 📂 Estrutura do Projeto

```
palpites-mega-sena/
│── 📄 .gitignore
│── 📄 README.md
│── 📄 palpite_mega_sena.py
└── 📂 tests/
    └── 📄 test_mega_sena.py
```

## 🚀 Como Usar

1. Clone o repositório:
   ```bash
    git clone https://github.com/LuanBrito01/palpites-mega-sena.git
    cd palpites-mega-sena

   ```

2. Execute o script:
   ```bash
   python palpite_mega_sena.py
   ```

3. Insira a quantidade de jogos desejada e receba os números sorteados.

## 🧪 Testes

Para rodar os testes, utilize:
```bash
pytest tests/
```

---

# Arquivos do Projeto

## `palpite_mega_sena.py`

```python
from random import randint
from time import sleep

loteria = []
jogos = []
print('-' * 30)
print(f'{"💰 PALPITES PARA A MEGA SENA 💰":^30}')
print('-' * 30)
qtd = int(input('Quantos serão sorteados? '))
total = 1
while total <= qtd:
    cont = 0
    while True:
        num = randint(1, 61)
        if num not in loteria:
            loteria.append(num)
            cont += 1
        if cont >= 6:
            break
    loteria.sort()
    jogos.append(loteria[:])
    loteria.clear()
    total += 1
print()
print(f'-=-' * 3, f' SORTEANDO {qtd} JOGOS ', '-=-' * 3)
print()
for i, j in enumerate(jogos):
    print(f'JOGO {i+1}: {j}')
    sleep(1)
print()
print('-=-' * 3, ' BOA SORTE 🤞🤩 ', '-=-' * 3)
```

## `tests/test_mega_sena.py`

```python
import pytest
from palpite_mega_sena import randint

def test_randint_range():
    num = randint(1, 61)
    assert 1 <= num <= 61
```

## `.gitignore`

```
__pycache__/
*.pyc
*.pyo
```
