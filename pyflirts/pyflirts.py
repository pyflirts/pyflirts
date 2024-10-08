import random
from typing import Any, Generator, Literal, get_args
from .en_flirts import en_flirts
from .errors import LanguageNotFoundError, CategoryNotFoundError

all_flirts = {
    "en": en_flirts,
}

LANGUAGES = Literal["en"]
CATEGORIES = Literal["normal", "crazy", "all"]

LANGUAGE_VALUES = set(get_args(LANGUAGES))
CATEGORY_VALUES = set(get_args(CATEGORIES))

def get_flirts(language: LANGUAGES = "en", category: CATEGORIES = "normal") -> list[str]:
    """
    genrate a list of all the flirts line from the given language and category
    """
    try:
        flirts = all_flirts[language]
    except KeyError:
        raise LanguageNotFoundError(f"There is No such language: {language}")
    try:
        return flirts[category]
    except KeyError:
        raise CategoryNotFoundError("There is No such category %s in language %s" % (category, language))

def get_flirt(language: LANGUAGES = "en", category: CATEGORIES = "normal") -> str:
    """
    genrate a single flirt line from the given language and category
    """
    flirts = get_flirts(language, category)
    return random.choice(flirts)

def forever(language: LANGUAGES = "en", category: CATEGORIES = "normal") -> Generator[str, Any, Any]:
    """
    Generate flirt lines while codes running ( forever )
    """
    while True:
      get_flirts(language, category)
