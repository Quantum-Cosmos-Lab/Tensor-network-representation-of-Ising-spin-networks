from pennylane import numpy as np
import pandas as pd

def split_key(key, res):
    key_res = ''
    key_proj = ''
    for i in range(len(key)):
        if i in res:
            key_res+=key[i]
        else:
            key_proj+=key[i]
    return key_res, key_proj

def proj_probs(probs, n_wires, res):
    c = dict()
    for i in range(len(probs)):
        k=format(i,'0'+str(n_wires)+'b')
        key_res, key_proj = split_key(k,res)
        if key_proj==len(key_proj)*'0':
            c[key_res] = probs[i]
    return c[len(key_res)*'0']/np.sum(list(c.values()))

def save_params(params, file_name):
    temp = [params[0]]
    for layer in params[1]:
        temp.append(np.append(layer[:,0],np.nan))
        temp.append(np.concatenate([[np.nan],layer[:,1]]))
    pd.DataFrame(np.transpose(temp)).to_csv(file_name, index=False)

def load_params(file_name):
    data = pd.read_csv(file_name)
    temp = []
    for col in data:
        vals = data[col].values
        temp.append(vals[~np.isnan(vals)])
    temp2 = []
    for i in range((len(temp)-1)//2):
        temp2.append(np.transpose(temp[1+2*i:1+2*i+2]))
    return [temp[0],np.array(temp2)]