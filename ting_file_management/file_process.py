from ting_file_management.queue import Queue
from ting_file_management.file_management import txt_importer


def process(path_file, instance: Queue):
    path_file_list = [
        instance.search(i)['nome_do_arquivo'] for i in range(len(instance))
    ]

    if path_file not in path_file_list:
        data_file = txt_importer(path_file)
        dict_data = {
            "nome_do_arquivo": path_file,
            "qtd_linhas": len(data_file),
            "linhas_do_arquivo": data_file
        }

        instance.enqueue(dict_data)
        print(dict_data)


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
