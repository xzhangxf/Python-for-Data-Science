import sys


def ft_tqdm(lst: range):
    total = len(lst)

    for i, item in enumerate(lst, start=1):
        percent = i / total
        bar_len = 60
        filled_len = int(bar_len * percent)
        bar = '=' * filled_len + '>' + ' ' * (bar_len - filled_len - 1)
        count_display = f"{i}/{total}"

        sys.stdout.write(f"\r{int(percent * 100):3}%|[{bar}]| {count_display}")
        sys.stdout.flush()
        yield item

    # print()
