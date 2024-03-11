import sys
from dataclasses import dataclass
@dataclass
class Stack:
    input_string : str

    def __str__(self):
        res  = ''.join(self.input_string)
        return res

    def is_empty(self):
        '''
        проверка стека на пустоту. Метод возвращает True или False
        '''
        return bool(self.input_string)

    def push(self, item : str):
        '''
        добавляет новый элемент на вершину стека. Метод ничего не возвращает
        '''
        self.input_string += item

    def pop(self):
        '''
        удаляет верхний элемент стека. Стек изменяется. Метод возвращает верхний элемент стека
        '''
        remove = self.input_string[-1]
        res = self.input_string[:len(self.input_string)-1:]
        self.input_string = res
        return remove
    def peek(self):
        '''
        возвращает верхний элемент стека, но не удаляет его. Стек не меняется
        '''
        return self.input_string[-1]
    def size(self):
        '''
        возвращает количество элементов в стеке
        '''
        return len(self.input_string)

    def compare(self):
        pattern = {
            '(':')',
            '{':'}',
            '[':']',
            ')':'(',
            '}':'{',
            ']':'['
        }
        swicher = True
        if self.size() % 2 == 0:
            lenght = int(self.size()/2)
            first = self.input_string[0:lenght]
            second = ''.join([i for i in self.input_string[:lenght-1: -1]])
            for a, b in zip(first, second):
                if pattern[a] == b:
                    continue

                else:
                    swicher = False
                    break

        else:
            swicher = False


        if swicher:
            return 'Сбалансированно'
        else:
            return 'Несбалансированно'


    def balance(self):
        if self.size() % 2 == 0:
            pattern = {
                '(': ')',
                '{': '}',
                '[': ']',
                ')': '(',
                '}': '{',
                ']': '['
            }
            opo_string = self.input_string[::-1]
            opo = Stack(opo_string)
            for _ in self.input_string:
                if pattern[self.pop()] != opo.pop():
                    return 'Несбалансированно'
                    break
            else:
                 return 'Сбалансированно'

        else:
            return 'Несбалансированно'

if __name__ == "__main__":
    task_1 = '(((([{}]))))'
    task_2 = '[([])((([[[]]])))]{()}'
    task_3 = '{{[()]}}'
    task_4 = '}{}'
    task_5 = '{{[(])]}}'
    task_6 = '[[{())}]'

    list_of_tasks = [task_1, task_2, task_3, task_4, task_5, task_6]
    for i in list_of_tasks:
        res = Stack(i) 
        print(res.balance(), res.compare())









