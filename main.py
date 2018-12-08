from decimal import Decimal


def avarage_fun(name):
    ''' Calculation of the arithmetic average '''
    with open('rate.txt', 'r') as f_in:
        text = f_in.readlines()
        for line in text:
            if name in line:
                new_list = line.split()[2:]
                amount = sum(Decimal(i) for i in new_list)
                avarage_ = amount / 4
                print("_" * len(line), '\n')
                print(line, end='')
                print('Cредний показатель рейтинга:', avarage_)
                print("_" * len(line))
                return avarage_


def _rate(name):
    ''' Calculation of the rating among players '''
    with open('rate.txt', 'r') as f_in:
        text = f_in.readlines()
        for line in text:
            if name in line:
                one_list = line.split()[2:]
                fir_list = []
                for i in one_list:
                    fir_list.append(float(i))
                one_list = fir_list
                amount = sum(one_list)
                avarage_ = amount / 4
        _list = []
        for line in text:
            if 'NAME' not in line:
                new_list = line.split()[2:]
                int_list = []
                for n in new_list:
                    int_list.append(float(n))
                new_list = int_list
                amount_1 = sum(new_list)
                rate = amount_1 / 4
                _list.append(rate)
        _list = sorted(_list)[::-1]
        if avarage_ in _list:
            print('Рейтинг игрока среди остальных футболистов:', _list.index(avarage_) + 1)
        return _list.index(avarage_) + 1


# Main function.
def main():
    name = input('Введите имя игрока(на английском языке):')
    avarage_fun(name)
    _rate(name)


# File name checking and main run.
if __name__ == '__main__':
    main()