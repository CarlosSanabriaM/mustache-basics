import chevron

from mustache_basics.utils import get_abspath_from_project_source_root

TEMPLATES_DIR_PATH = get_abspath_from_project_source_root('files')
MAIN_TEMPLATE_PATH = get_abspath_from_project_source_root('files/main-template.mustache')


# Lambdas
def to_uppercase(text, render):
    return render(text).upper()


DATA = {
    "title": "Example Markdown file",
    "html_meta_tag": '<meta charset="UTF-8">',
    "section": [
        {
            "title": "Section 1",
            "paragraph": "This is the content of the section 1."
        },
        {
            "title": "Section 2",
            "paragraph": "This is the content of the section 2."
        }
    ],
    "people": [
        {
            "name": "John",
            "age": 27,
            "nationality": "american"
        },
        {
            "name": "Andrea",
            "age": 35,
            "nationality": "italian"
        }
    ],
    "link": {
        "url": "https://github.com/noahmorrison/chevron",
        "text": "Chevron GitHub project"
    },
    "to_uppercase": to_uppercase,
    "empty_list": [],
    "false_value": False
}

if __name__ == '__main__':
    with open(MAIN_TEMPLATE_PATH, 'r') as f:
        print(chevron.render(f, DATA, partials_path=TEMPLATES_DIR_PATH))
