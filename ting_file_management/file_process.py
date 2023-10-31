from ting_file_management.queue import Queue
from ting_file_management.file_management import txt_importer
import sys


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


def remove(instance: Queue):
    if instance.__len__() == 0:
        return print("Não há elementos")

    removed = instance.dequeue()
    print(f"Arquivo {removed['nome_do_arquivo']} removido com sucesso")


def file_metadata(instance: Queue, position):
    try:
        queue_data = instance.search(position)
        print(queue_data)
    except IndexError:
        return print("Posição inválida", file=sys.stderr)
