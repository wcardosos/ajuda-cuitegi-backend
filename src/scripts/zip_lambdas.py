import os
import re
import shutil

def verify_custom_import(file_line: str) -> bool:
    FROM_REGEX = r'^from\s'
    IMPORT_REGEX = r'\simport\s'

    return re.search(FROM_REGEX, file_line) and re.search(IMPORT_REGEX, file_line)

def verify_folder_exists(folder: str) -> bool:
    return os.path.exists(folder)


def get_filename_from_import_string(import_string: str) -> str:
    FILENAME_REGEX = r'\w+$'

    filename = re.search(FILENAME_REGEX, import_string).group(0)

    return filename

def get_import_strings(filepath: str) -> list:
    with open(filepath, 'r') as file:
        lines = file.readlines()

        import_strings_lines = list(filter(lambda line: verify_custom_import(line), lines))

        import_strings = list(map(lambda line: line.replace('\n', ''), import_strings_lines))

        return import_strings

def get_path_file(import_string: str) -> str:
    PACKAGE_REGEX = r'src.\w+.\w+'
    
    module: str = re.search(PACKAGE_REGEX, import_string).group(0)

    path: str = module.replace('.', '/')

    path_file = path + '.py'

    return path_file

def get_project_root_folder() -> str:
    current_folder = os.getcwd()

    src_folder = current_folder.replace('/src/scripts', '')

    return src_folder

def get_up_folder(folder: str) -> str:
    UP_FOLDER_REGEX = r'\/\w+.py$'

    up_folder = re.sub(UP_FOLDER_REGEX, '', folder)

    return up_folder

def create_folder(folder: str) -> None:
    os.mkdir(folder)

def create_project_folders(handler_folder: str) -> None:
    os.mkdir(f'{handler_folder}/src')
    os.mkdir(f'{handler_folder}/src/entities')
    os.mkdir(f'{handler_folder}/src/errors')
    os.mkdir(f'{handler_folder}/src/providers')
    os.mkdir(f'{handler_folder}/src/repositories')

def create_files(handler: str) -> None:
    root_folder = get_project_root_folder()
    src_folder = f'{root_folder}/src'

    file_folder = f'{src_folder}/handlers/{handler}.py'
    import_strings_list = get_import_strings(file_folder)

    paths_files_imported_by_handler = list(map(
        lambda import_string: get_path_file(import_string),
        import_strings_list
    ))

    lambdas_folder = f'{src_folder}/lambdas'
    if not verify_folder_exists(lambdas_folder):
        create_folder(lambdas_folder)
    
    handler_folder = f'{lambdas_folder}/{handler}'
    if not verify_folder_exists(handler_folder):
        create_folder(handler_folder)
        create_project_folders(handler_folder)

    for path_file in paths_files_imported_by_handler:
        path_file_folder = get_up_folder(path_file)

        module_lambda_folder = f'{handler_folder}/{path_file_folder}'
        if not verify_folder_exists(path_file_folder):
            create_folder(module_lambda_folder)
        
        ORIGINAL_FILE = f'{root_folder}/{path_file}'
        shutil.copy(ORIGINAL_FILE, module_lambda_folder)
