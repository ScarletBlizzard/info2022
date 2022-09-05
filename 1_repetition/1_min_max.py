sequence = []

number = input()
while number != 'End':
    sequence.append(int(number))
    number = input()

length = len(sequence)
mean = sum(sequence) / length 

print("max: {max}, min: {min}, mean: {mean}, deviation: {deviation}"
        .format(
            max=max(sequence),
            min=min(sequence),
            mean=mean,
            deviation=(sum([(x-mean)**2 for x in sequence]) / length)**0.5
        )
)

