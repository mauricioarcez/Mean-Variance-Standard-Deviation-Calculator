import numpy as np

def calculate(list):
  if len(list) != 9:
    raise ValueError("List must contain nine numbers.")
  arr = np.array(list).reshape((3,3))

  calculations = {
    'mean' : None,
    'variance' : None,
    'standard deviation' : None,
    'max' : None,
    'min' : None,
    'sum' : None,
  }

  means = []
  means.append(arr.mean(axis=0).tolist())
  means.append(arr.mean(axis=1).tolist())
  means.append(arr.mean().tolist())
  calculations['mean'] = means

  variances = []
  variances.append(arr.var(axis=0).tolist())
  variances.append(arr.var(axis=1).tolist())
  variances.append(arr.var().tolist())
  calculations['variance'] = variances

  standard_d =[]
  standard_d.append(arr.std(axis=0).tolist())
  standard_d.append(arr.std(axis=1).tolist())
  standard_d.append(arr.std().tolist())
  calculations['standard deviation'] = standard_d 

  maximum = []
  maximum.append(arr.max(axis=0).tolist())
  maximum.append(arr.max(axis=1).tolist())
  maximum.append(arr.max().tolist())
  calculations['max'] = maximum

  minimum = []
  minimum.append(arr.min(axis=0).tolist())
  minimum.append(arr.min(axis=1).tolist())
  minimum.append(arr.min().tolist())
  calculations['min'] = minimum

  summary = []
  summary.append(arr.sum(axis=0).tolist())
  summary.append(arr.sum(axis=1).tolist())
  summary.append(arr.sum().tolist())
  calculations['sum'] = summary

  return calculations