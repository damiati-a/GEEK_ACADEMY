"""
modo collections - deque

Podemos dizer que o deque é uma lista de alta performance.


"""
from collections import deque
deq = deque('damiati')
print(deq)

# adicionar elementos no deque

deq.append('jajajaja')  # adiciona sempre no final
print(deq)

deq.appendleft('ajaja')  #adiciona no começo
print(deq)

deq.popleft()  # da para remover tanto pelo final, quanto pelo começo.
print(deq)
