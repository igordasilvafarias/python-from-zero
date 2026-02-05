name: str = 'Igor Farias'
height: float = 1.80
weight: float = 78.0
bmi: float = weight / (height ** 2)

text_1 = f'{name} is {height:.2f} meters tall, weighs {weight:.2f}kg and his BMI is {bmi:.2f}'

print(text_1)
