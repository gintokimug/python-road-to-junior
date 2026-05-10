def series_sum(n):
    total_sum = 0
    for char in range(n):
        denominator = 1 +(3 * char)
        total_sum += 1 / denominator
    return f"{total_sum:.2f}"

example = 123
print(series_sum(example))


def series_sum(n):
    return '{:.2f}'.format(sum(1.0/(3 * i + 1) for i in range(n)))
example = 123
print(series_sum(example))