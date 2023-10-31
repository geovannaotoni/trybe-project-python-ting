from ting_file_management.queue import Queue


def exists_word(word: str, instance: Queue):
    occurrences_files = list()

    # verifica dentro de cada arquivo se a palavra existe
    for index in (range(instance.__len__())):

        ocurrences_lines = list()
        file_data = instance.search(index)['linhas_do_arquivo']

        # verifica dentro de cada linha do arquivo se a palavra existe
        for line in range(len(file_data)):
            if word.casefold() in file_data[line].casefold():
                ocurrences_lines.append({"linha": line + 1})

        if len(ocurrences_lines) > 0:
            occurrences_files.append({
                "palavra": word,
                "arquivo": instance.search(index)['nome_do_arquivo'],
                "ocorrencias": ocurrences_lines
            })

    return occurrences_files


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
