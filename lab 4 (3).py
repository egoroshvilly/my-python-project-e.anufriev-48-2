# Импортируем модуль SeqIO из библиотеки Biopython для работы с последовательностями
from Bio import SeqIO

# Загружаем наш файл GenBank
genbank_file = "merged_sequences.gb"

# Используем функцию SeqIO.parse для последовательного чтения всех записей из GenBank файла
# Формат файла указываем как "genbank"
for record in SeqIO.parse(genbank_file, "genbank"):

    # Выводим ID текущей записи для информативности
    print(f"Обработка записи: {record.id}")

    # Проходим по всем мРНК (mRNA) в записи
    for feature in record.features:
        # Проверяем, является ли эта feature мРНК (type == "mRNA") — т.е. информационная РНК
        if feature.type == "mRNA":
            # Создаем пустой список, в котором будем хранить белковые последовательности,
            # полученные с этой мРНК
            protein_sequences = []
            # feature.location — объект, описывающий координаты feature на последовательности
            # Если feature.location является комплексным, анализируем каждую часть отдельно
            # (в GenBank возможны сложные участки с интронами и экзонами)
            # Обходим все отдельные локации в данном feature.location

            for location in feature.location:
                # Проверяем, есть ли кодирующая последовательность (CDS)

                if location.type == "CDS":

                    # Извлекаем последовательность и трансформируем
                    seq = record.seq[location.start:location.end]

                    protein = seq.translate()
                    # Трансляция ДНК в белковую последовательность
                    protein_sequences.append(str(protein))
                    print(f"Белковая последовательность: {protein}")