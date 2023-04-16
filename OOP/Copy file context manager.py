import os


class FileCopyManager:

    def __init__(self, source_file_path, destination_file_path):
        self.source_file_path = source_file_path
        self.destination_file_path = destination_file_path

    def __enter__(self):
        self.source_file = open(self.source_file_path, 'r')
        self.source_content = self.source_file.read()

        if not self.source_content:
            raise ValueError('Source file is empty')

        return self.source_content

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.destination_file = open(self.destination_file_path, 'w')
        self.destination_file.write(self.source_content)
        print('File copied successfully!')

        self.source_file.close()
        self.destination_file.close()


if __name__ == '__main__':
    base_dir = os.getcwd()
    source_file_pth = os.path.join(base_dir, 'source_file.txt')
    destination_file_pth = os.path.join(base_dir, 'destination_file.txt')

    with FileCopyManager(source_file_pth, destination_file_pth) as file_content:
        pass
