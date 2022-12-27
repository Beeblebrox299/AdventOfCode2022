snafu_file = "data/25_snafu.txt"

def convert_snafu_to_decimal(snafu: str) -> int:
    digit_dict = {'=': -2, '-': -1, '0': 0, '1': 1, '2': 2}
    total = 0
    length = len(snafu)
    for i in range(0, length):
        num = digit_dict[snafu[i]]
        decimal_value = num * (5 ** (length - i - 1))
        total += decimal_value
    return total


def convert_decimal_to_snafu(decimal: int) -> str:
    digit_dict = {-2: '=', -1: '-', 0: '0', 1: '1', 2: '2'}
    snafu = '2'
    max_power = 0
    while 2 * (5 ** max_power) < decimal:
        max_power += 1
        snafu += '2'
    for i in range(0, len(snafu)):
        digit = -2
        snafu = snafu[:i] + digit_dict[digit] + snafu[i + 1:]
        while convert_snafu_to_decimal(snafu) < decimal:
            digit += 1
            snafu = snafu[:i] + digit_dict[digit] + snafu[i + 1:]
    return snafu


def get_total(filename: str) -> str:
    total = 0
    with open(filename) as file:
        for line in file:
            line = line.replace("\n", "")
            total += convert_snafu_to_decimal(line)
    return convert_decimal_to_snafu(total)


print(get_total(snafu_file))
