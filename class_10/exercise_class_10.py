name: str = 'Igor Farias'
height: float = 1.80
weight: int = 78
imc: float = round(weight / (height ** 2), 2)  ## round() is used to round a number to a specified number of decimal places

print(name, 'has', height, 'meters of height,')
print('weighs', weight, 'kg and his IMC is', imc)