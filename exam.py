import re
from typing import List, NamedTuple, Optional, Tuple

from pyquery import PyQuery
from requests.exceptions import ConnectionError

Skill = NamedTuple('Skill', [('label', str), ('items', List[str])])
Syllabus = NamedTuple('Syllabus', [('label', str), ('skills', List[Skill])])
SyllabusList = List[Syllabus]
# TODO: Add preperation sources to Syllabus

regex_exam_id = '[A-Z0-9]{2,3}-[0-9]{3}'


def _exam_url(exam_id='list'):
    return 'https://www.microsoft.com/en-us/learning/exam-{}.aspx'.format(exam_id)


def _download_html(url: str) -> Optional[PyQuery]:
    try:
        return PyQuery(url=url, encoding='utf-8')
    except ConnectionError:
        print('Connection error')
        return None


def get_syllabuses(exam_id: str) -> Optional[SyllabusList]:
    doc = _download_html(_exam_url(exam_id))
    if not doc:
        return None

    d = doc('#question-types')
    dt_elements = d('dt')
    ul_elements = d('dd > ul:first')

    return [
        Syllabus(
            label=dt_elements[ul_elements.index(ul)].text_content(),
            skills=[
                Skill(
                    label=li.text.strip(),
                    items=[
                        m.capitalize() for m in re.findall(
                            r'\s*(.+?)\s*(?:;|$)',
                            re.sub(r'\s+', ' ', li[0].text_content()),
                            flags=re.DOTALL
                        )
                    ] if len(li) > 0 else []
                ) for li in ul.getchildren()
            ]
        ) for ul in ul_elements
    ]


def get_valid_ids() -> Optional[Tuple[str]]:
    doc = _download_html(_exam_url())
    if not doc:
        return None

    a_elements = doc('#exam-list-all-cert-h2 + div a')
    matches = (re.match('^{}'.format(regex_exam_id),
                        a.text_content()).group(0) for a in a_elements)
    return tuple(matches)
