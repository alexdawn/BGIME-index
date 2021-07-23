import csv
from collections import defaultdict, namedtuple
HEADER = ['issue', 'section', 'name', 'pages', 'reference']
data = defaultdict(list)
index = defaultdict(list)

Article = namedtuple('Article', ['name', 'issue', 'pages'])

def filter_comments(row):
    return row[0:2] != '//'

with open('index.csv') as file:
    csv_reader =  csv.reader(
        filter(filter_comments, file), 
        delimiter=',', quotechar='"'
    )
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            assert [n.strip() for n in row] == HEADER, f"{row} != {HEADER}"
        else:
            try:
                if len(row) != 0:
                    issue, section, name, pages, refs = row
                    data[section.strip()].append(Article(name, issue, 'p' + pages))
                    for ref in refs.split(';'):
                        index[ref.strip()].append((issue, 'p' + pages))
            except:
                raise RuntimeError(row)
        line_count += 1


def format_list(data):
    return [f'* {x.issue:<6} - {x.name:<50} - {x.pages:>6}\n' for x in data]


with open('index.md', 'w') as file:
    file.write(', '.join(list(data.keys())))
    file.write('\n')
    file.write('# Guides\n')
    file.writelines(format_list(data['guide']))
    file.write('\n')
    file.write('# Rules\n')
    file.writelines(format_list(data['playing special']))
    file.write('\n')
    file.writelines(format_list(data['playing']))
    file.write('\n')
    file.write('# Army Lists\n')
    file.writelines(format_list(data['army list']))
    file.write('\n')
    file.write('# Campaigns\n')
    file.writelines(format_list(data['campaign special']))
    file.write('\n')
    file.writelines(format_list(data['campaign']))
    file.write('\n')
    file.write('# Scenarios\n')
    file.writelines(format_list(data['scenario']))
    file.write('\n')
    file.write('# Battle Reports\n')
    file.writelines(format_list(data['battle report']))
    file.write('\n')
    file.write('# Painting\n')
    file.writelines(format_list(data['painting special']))
    file.write('\n')
    file.writelines(format_list(data['painting']))
    file.write('\n')
    file.write('# Modelling\n')
    file.writelines(format_list(data['modelling special']))
    file.write('\n')
    file.writelines(format_list(data['modelling']))
    file.write('\n')
    for k, v in sorted(index.items()):
        i = ", ".join(x[0] for x in v)
        file.write(f'{k} - {i}\n')
