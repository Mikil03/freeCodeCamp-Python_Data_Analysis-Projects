import numpy as np

def calculate(list):

    n = len(list)
    if n != 9:
        raise ValueError("List must contain nine numbers.")
    
    calculations = {
    'mean': [[],[]],
    'variance': [[],[]],
    'standard deviation': [[],[]],
    'max': [[],[]],
    'min': [[],[]],
    'sum': [[],[]]
    }

    list = np.array(list)
    arr = np.array(list).reshape(3,3)
    
    for j in range(3):
        calculations['mean'][0].append(float(arr[:, j].mean()))
        calculations['max'][0].append(int(arr[:, j].max()))
        calculations['min'][0].append(int(arr[:, j].min()))
        calculations['sum'][0].append(int(arr[:, j].sum()))
        calculations['variance'][0].append(float(arr[:, j].var()))
        calculations['standard deviation'][0].append(float(arr[:, j].std()))

    for i in range(3):
        calculations['mean'][1].append(float(arr[i, :].mean()))
        calculations['max'][1].append(int(arr[i, :].max()))
        calculations['min'][1].append(int(arr[i, :].min()))
        calculations['sum'][1].append(int(arr[i, :].sum()))
        calculations['variance'][1].append(float(arr[i, :].var()))
        calculations['standard deviation'][1].append(float(arr[i, :].std()))

    calculations['mean'].append(float(list.mean()))
    calculations['max'].append(int(list.max()))
    calculations['min'].append(int(list.min()))
    calculations['sum'].append(int(list.sum()))
    calculations['variance'].append(float(list.var()))
    calculations['standard deviation'].append(float(list.std()))


    return calculations