import shutil


class FileHandler:
    def copy(self, file_path: str, destination_folder: str) -> None:
        shutil.copy(file_path, destination_folder)

    def move(self, file: str, destination_folder: str) -> None:
        shutil.move(file, destination_folder)

    def zip_folder(self, zip_file_name: str, source_folder: str, destination_folder: str) -> None:
        shutil.make_archive(zip_file_name, 'zip', source_folder)

        filename = f'{zip_file_name}.zip'

        self.move(filename, destination_folder)
