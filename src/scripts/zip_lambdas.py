import re


def get_path_file(import_str: str) -> str:
    PACKAGE_REGEX = r'src.\w+.\w+'
    FILE_REGEX = r'\w+$'
    
    module: str = re.search(PACKAGE_REGEX, import_str).group(0)
    object_imported: str = re.search(FILE_REGEX, import_str).group(0)

    path: str = module.replace('.', '/')
    filename: str = '/' + object_imported + '.py'

    path_file = path + filename

    return path_file

def verify_custom_import(file_line: str) -> bool:
    FROM_REGEX = r'^from\s'
    IMPORT_REGEX = r'\simport\s'

    return re.search(FROM_REGEX, file_line) and re.search(IMPORT_REGEX, file_line)

def get_import_strings(filepath: str) -> list:
    with open(filepath, 'r') as file:
        lines = file.readlines()

        import_strings_lines = list(filter(lambda line: verify_custom_import(line), lines))

        import_strings = list(map(lambda line: line.replace('\n', ''), import_strings_lines))

        return import_strings
