from ting_file_management.queue import Queue


def line_ocurrences_report(line: int, content: str, show_cont: bool = False):
    if show_cont:
        return {
            "linha": line + 1,
            "conteudo": content
        }
    return {
        "linha": line + 1
    }


def exists_word(word: str, instance: Queue, show_cont: bool = False):
    occurrences_files = list()

    # verifica dentro de cada arquivo se a palavra existe
    for index in (range(instance.__len__())):

        ocurrences_lines = list()
        file_data = instance.search(index)['linhas_do_arquivo']

        # verifica dentro de cada linha do arquivo se a palavra existe
        for line in range(len(file_data)):
            if word.casefold() in file_data[line].casefold():
                ocurrences_lines.append(
                    line_ocurrences_report(line, file_data[line], show_cont)
                )

        if len(ocurrences_lines) > 0:
            occurrences_files.append({
                "palavra": word,
                "arquivo": instance.search(index)['nome_do_arquivo'],
                "ocorrencias": ocurrences_lines
            })

    return occurrences_files


def search_by_word(word: str, instance: Queue):
    return exists_word(word, instance, True)
