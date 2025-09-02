## 3) Relatório Técnico

### 3.1 Análise de Complexidade por Contagem de Operações (número de comparações)

**Ideia:**  
- Bases:
  - `n = 1` → 0 comparações.  
  - `n = 2` → 1 comparação (decide quem é menor/maior).
- Passo recursivo (`n ≥ 3`): divide em duas metades, resolve recursivamente e **combina** com **2 comparações** (para `min` e `max`).

**Recorrência do número de comparações `C(n)` (para n par):**  
- `C(1) = 0`  
- `C(2) = 1`  
- `C(n) = C(n/2) + C(n/2) + 2 = 2*C(n/2) + 2`

**Solução para `n = 2^k`:**  
- `C(2) = 1`  
- `C(4) = 2*1 + 2 = 4`  
- `C(8) = 2*4 + 2 = 10`  
- `C(16) = 2*10 + 2 = 22`  
Observa-se o padrão: `C(n) = (3n/2) - 2`.  
Para `n` ímpar (ou `n` não potência de 2), o valor segue a mesma **ordem** e fica **≤ ⌈3n/2⌉ - 2**.

**Conclusão temporal por contagem:** o número de comparações cresce **linearmente** com `n` ⇒ **O(n)**.

---

### 3.2 Análise da Complexidade Ciclomática

A seguir está o grafo de fluxo da função `maxmin_select`, modelado com **cada retorno como nó de saída explícito**:

#### Nós (N):
- N1: Início da função.  
- N2: Verificação `n == 0`.
- N3: Saída por exceção (sequência vazia).  
- N4: Verificação `n == 1`.  
- N5: Retorno `(arr[0], arr[0])`.  
- N6: Verificação `n == 2`.  
- N7: Comparação `a <= b`.  
- N8: Retorno `(a, b)` (caso `a <= b`).  
- N9: Retorno `(b, a)` (caso `a > b`).  
- N10: Cálculo de `mid` e divisão do arranjo.  
- N11: Chamada recursiva esquerda.  
- N12: Chamada recursiva direita.  
- N13: Comparação `mn1 <= mn2` para o menor.  
- N14: Comparação `mx1 >= mx2` para o maior.  
- N15: Retorno `(mn, mx)` final.  
- N16: Saída da função (nó final comum).  

**Número total de nós: N = 16.**

---

#### Arestas (E):
- N1 → N2  
- N2 → N3 (se verdadeiro)  
- N2 → N4 (se falso)  
- N3 → N16  
- N4 → N5 (se verdadeiro)  
- N4 → N6 (se falso)  
- N5 → N16  
- N6 → N7 (se verdadeiro)  
- N6 → N10 (se falso)  
- N7 → N8 (se verdadeiro)  
- N7 → N9 (se falso)  
- N8 → N16  
- N9 → N16  
- N10 → N11  
- N11 → N12  
- N12 → N13  
- N13 → N14  
- N14 → N15  
- N15 → N16  

**Número total de arestas: E = 19.**

---

#### Cálculo:
- N = 16  
- E = 19  
- P = 1  

> M = E - N + 2P = 19 - 16 + 2(1) = **5**

**Resultado:** A complexidade ciclomática da função `maxmin_select` é **5**, o que indica 5 caminhos independentes de execução.

---

### 3.3 Análise da Complexidade Assintótica (Teorema Mestre)

Considere a recorrência da **duração** (tempo) da versão divide-and-conquer:
```

T(n) = 2*T(n/2) + O(1)

```

**Perguntas solicitadas:**
1. **Identifique a, b, f(n):**  
   - a = 2  
   - b = 2  
   - f(n) = O(1)

2. **Calcule log_b(a):**  
   - log_2(2) = 1 → p = 1

3. **Caso do Teorema Mestre:**  
   - f(n) = O(n^(p - ε)) com ε = 1  
   - Portanto, **Caso 1** do Teorema Mestre.

4. **Solução assintótica:**  
   - T(n) = Θ(n)

**Conclusão:** O tempo de execução do algoritmo é **linear** Θ(n).
