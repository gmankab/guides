with open('settings.xml', 'rt') as f:
    xml = f.read()
for intag, outtag, out in (
    ('Program', 'data', 'rawprogram'),
    ('Patch', 'patches', 'patch'),
):
    for pr in xml.split(f'<{intag}')[1:]:
        num, data = pr.split('>', 1)
        lines = filter(
            lambda x: x, map(
                lambda x: x.strip(),
                data.split(f'</{intag}')[0].split('\n')
            )
        )
        with open(f'{out}{num}.xml', 'wt') as f:
            print(f'<?xml version="1.0" ?>\n<{outtag}>', file=f)
            for line in lines:
                print(' ', line, file=f)
            print(f'</{outtag}>', file=f)

