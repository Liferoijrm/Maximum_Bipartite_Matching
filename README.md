# Modified SPA Algorithm (MEM Version)

**Autores:**  
- Élvis Miranda  
- Gustavo Alves 
- Pedro Marcinoni

---

## 📌 Descrição do Projeto

Este projeto implementa uma variação do **algoritmo SPA (Student–Project Allocation)** descrito em **Abraham, Irving & Manlove (2007)**, adaptado para produzir um **MEM — Maximum Engineering Matching**.

A modificação adiciona:

- Regras de substituição, onde estudantes com maior prioridade podem substituir outros em projetos cheios
- Critérios de desempate usando **nota** e **ordem de preferência**
- Execução até que todos os estudantes estejam alocados ou tenham proposto para todos os projetos possíveis

A implementação segue arquitetura modular organizada em pastas.

---

## 📁 Estrutura do Diretório
```
MAXIMUM_BIPARTITE_MATCHING
├── .venv
├── data
│   └── data.txt
├── models
│   ├── __pycache__
│   ├── __init__.py
│   ├── project.py
│   └── student.py
├── src
│   ├── __pycache__
│   ├── __init__.py
│   ├── main.py
│   ├── preprocessing.py
│   └── SPAallocation.py
├── .gitignore
└── LICENSE
```

---

## ⚙️ Como Executar o Projeto

### 1. (Opcional) Instalar dependências

Caso exista um arquivo `requirements.txt`:

```bash
pip install -r requirements.txt
```
### 2. Certifique-se de estar no diretório raiz do projeto
```bash
ex:
cd C:/Maximum_Bipartite_Matching
```
### 3. Execute o programa com:
```bash
python -m src.main
```
Esse comando garante que os imports absolutos funcionem corretamente dentro da estrutura de pacotes do Python.

## 📝 Referência Principal
Abraham, D. J., Irving, R. W., & Manlove, D. F. (2007).
Two Algorithms for the Student–Project Allocation Problem.
Journal of Discrete Algorithms.
