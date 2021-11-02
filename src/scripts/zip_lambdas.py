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
