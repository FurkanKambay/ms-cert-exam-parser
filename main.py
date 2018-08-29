import re
import sys
from json import dump as dumpjson
from pathlib import Path
from typing import List

from exam import SyllabusList, get_syllabuses, get_valid_ids, regex_exam_id

out_path = Path('out')
out_path.mkdir(exist_ok=True)


def out_json(out_file: Path, syllabuses: SyllabusList, indent=2) -> Path:
    jobj = [
        {
            'label': syllabus.label,
            'skills': [
                {
                    'label': skill.label,
                    'items': skill.items
                } for skill in syllabus.skills
            ]
        } for syllabus in syllabuses
    ]

    with out_file.open('w') as f:
        dumpjson(jobj, f, ensure_ascii=False, indent=indent)


def dump(exam_id: str):
    try:
        expected_path = out_path / '{}.json'.format(exam_id)
        if expected_path.exists():
            print('Cached exam found: {}'.format(exam_id))
            return None
    except FileNotFoundError:
        pass

    print('Downloading exam {}...'.format(exam_id))
    res = get_syllabuses(exam_id)
    if res:
        out_json(expected_path, res)
        parent_path = out_path.resolve()
        print('Exam {} output folder: {}'.format(exam_id, parent_path))
    else:
        print('Error.')


def print_invalid():
    print('Please pass in valid exam IDs.')
    print('Example: main.py 98-381 98-361')


def main(args: List[str]):
    cache_file_path = out_path / 'valid_ids'

    try:
        with open(cache_file_path) as f:
            valid_ids = f.read().splitlines()
            is_valid = len(valid_ids) > 1 and all(
                re.match('^{}$'.format(regex_exam_id), line) for line in valid_ids)
    except FileNotFoundError:
        is_valid = False

    if not is_valid:
        print('Downloading valid exam IDs...')
        valid_ids = get_valid_ids()
        with open(cache_file_path, 'w') as f:
            f.writelines(['{}\n'.format(i) for i in valid_ids])

    ids = set(args).intersection(valid_ids)
    if ids:
        print(ids)
        for exam_id in ids:
            dump(exam_id)
    else:
        print_invalid()


if __name__ == '__main__':
    if len(sys.argv) > 1:
        if sys.argv[1] == '--clear':
            import shutil
            shutil.rmtree(out_path, ignore_errors=True)
        else:
            main(sys.argv[1:])
    else:
        print_invalid()
