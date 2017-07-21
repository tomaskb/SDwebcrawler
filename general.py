import os


# Cada projeto é uma pasta diferente
def create_project_dir(directory):
    if not os.path.exists(directory):
        print('Creating directory ' + directory)
        os.makedirs(directory)


#Cria as filas
def create_data_files(project_name, base_url):
    queue = os.path.join(project_name , 'queue.txt')
    crawled = os.path.join(project_name,"crawled.txt")
    if not os.path.isfile(queue):
        write_file(queue, base_url)
    if not os.path.isfile(crawled):
        write_file(crawled, '')


# Crias os arquivos
def write_file(path, data):
    with open(path, 'w') as f:
        f.write(data)


#Adiciona os dados no arquivo
def append_to_file(path, data):
    with open(path, 'a') as file:
        file.write(data + '\n')


# Dele o conteúdo do arquivo
def delete_file_contents(path):
    open(path, 'w').close()


#Le o arquivo e converte para um set
def file_to_set(file_name):
    results = set()
    with open(file_name, 'rt') as f:
        for line in f:
            results.add(line.replace('\n', ''))
    return results


#Separa o set em linhas, cada linha é uma nova tarefa na fila
def set_to_file(links, file_name):
    with open(file_name,"w") as f:
        for l in sorted(links):
            f.write(l+"\n")