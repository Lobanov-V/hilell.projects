import re
import codecs


def clean_html(input_filename: str, output_filename: str = 'cleaned.txt') -> None:
    with open(input_filename, 'r', encoding='utf-8') as infile:
        lines: list[str] = infile.readlines()

    cleaned_lines: list[str] = []
    for line in lines:
        no_tags: str = re.sub(r'<.*?>', '', line)
        if no_tags.strip():
            cleaned_lines.append(no_tags.strip())

    with open(output_filename, 'w', encoding='utf-8') as outfile:
        for line in cleaned_lines:
            outfile.write(line + '\n')


def delete_html_tags(html_file: str, result_file: str = 'cleaned.txt') -> None:
    with codecs.open(html_file, 'r', 'utf-8') as file:
        html: str = file.read()