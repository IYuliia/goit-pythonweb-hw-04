import os
import argparse
import asyncio
import logging
import shutil
from pathlib import Path

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


async def copy_file(file_path: Path, output_folder: Path):
    try:
        file_extension = file_path.suffix.lower()
        extension_folder = output_folder / file_extension[1:]
        extension_folder.mkdir(parents=True, exist_ok=True)
        destination_path = extension_folder / file_path.name
        shutil.copy(file_path, destination_path)
        logging.info(f"Файл {file_path.name} успішно скопійовано до {destination_path}")
    except Exception as e:
        logging.error(f"Помилка при копіюванні файлу {file_path.name}: {e}")


async def read_folder(source_folder: Path, output_folder: Path):
    try:
        if not source_folder.exists():
            logging.error(f"Вихідна папка {source_folder} не існує!")
            return
        if not output_folder.exists():
            output_folder.mkdir(parents=True, exist_ok=True)
        tasks = []
        for file_path in source_folder.rglob('*'):
            if file_path.is_file():
                tasks.append(copy_file(file_path, output_folder))
        await asyncio.gather(*tasks)
    except Exception as e:
        logging.error(f"Помилка при обробці папки {source_folder}: {e}")


def create_output_folder(output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        logging.info(f"Output folder created: {output_folder}")


def main():
    parser = argparse.ArgumentParser(description="Сортування файлів за розширенням.")
    parser.add_argument("source_folder", type=str, help="Шлях до вихідної папки")
    parser.add_argument("output_folder", type=str, help="Шлях до цільової папки")

    args = parser.parse_args()

    source_folder = Path(args.source_folder)
    output_folder = Path(args.output_folder)

    create_output_folder(output_folder)

    asyncio.run(read_folder(source_folder, output_folder))


if __name__ == "__main__":
    main()
