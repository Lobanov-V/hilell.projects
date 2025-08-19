import re

def clean_html(input_filename, output_filename='cleaned.txt'):
    with open(input_filename, 'r', encoding='utf-8') as infile:
        lines = infile.readlines()

    cleaned_lines = []
    for line in lines:
        no_tags = re.sub(r'<.*?>', '', line)
        if no_tags.strip():
            cleaned_lines.append(no_tags.strip())

    with open(output_filename, 'w', encoding='utf-8') as outfile:
        for line in cleaned_lines:
            outfile.write(line + '\n')

import codecs
def delete_html_tags(html_file, result_file='cleaned.txt'):
      with codecs.open(html_file, 'r', 'utf-8') as file:
           html = file.read()