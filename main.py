from Stack_class import Stack


def is_correct_str(S:str) -> str:
    pairs_op = {'{':'}', '(':')', '[':']'}
    pairs_cl={'}':'{',')':'(', ']':'['}
    input_list = list(S)
    st1 = Stack(input_list)
    st2 = Stack(list())
    i = st1.size()-1
    while i != 0:
        el = st1.data[i] # рассматриваемый элемент стэка
        if not(el in pairs_op.keys() or el in pairs_cl.keys()):
           return 'В строке содержатся символы, несоответствующие шаблону!'
        if el in pairs_cl.keys():
            st2.push(el)
        if pairs_op.get(el) != None:
            if st2.peek() == pairs_op[el]:
                st2.pop()
            else:
                return 'Несбалансированно'
        i -= 1
    return 'Сбалансированно'


if __name__ == "__main__":
    inp_s ='(([]))'



    inp_s_2 ='(}{()r)})'

    inp_s_3 = '])(){'

    print(is_correct_str(inp_s_3))



