"""
Utility helpers that pull random data from https://swapi.info
and assemble Jedi-Hunter task sentences.
"""

import random
import requests

SWAPI_BASE = "https://swapi.info/api"

# ----------------------------------------------------------------------
# Low-level helpers
# ----------------------------------------------------------------------
def _fetch_list(endpoint: str) -> list[dict]:
    """
    Return the full JSON list for an endpoint such as 'people', 'planets',
    'starships'.  If anything goes wrong we return an empty list.
    """
    url = f"{SWAPI_BASE}/{endpoint.strip('/')}"          # no trailing slash
    try:
        res = requests.get(url, timeout=10)
        res.raise_for_status()
        data = res.json()
        if isinstance(data, list):
            return data
    except requests.RequestException:
        pass
    return []  # fall-back


def _random_name(endpoint: str) -> str:
    """
    Pick a random object from the given SWAPI list endpoint and
    return its 'name'.  Falls back to 'Unknown' if necessary.
    """
    items = _fetch_list(endpoint)
    if not items:
        return "Unknown"
    return random.choice(items).get("name", "Unknown")


# ----------------------------------------------------------------------
# Public API used by your views / templates
# ----------------------------------------------------------------------
def random_planet()    -> str: return _random_name("planets")
def random_character() -> str: return _random_name("people")
def random_ship()      -> str: return _random_name("starships")


VERBS = ["hunt", "kill", "capture"]


def generate_task() -> str:
    """
    Return one fully-formatted task sentence, e.g.

        "Go to planet Naboo and hunt Luke Skywalker using ship X-wing"
    """
    return (
        f"Go to planet {random_planet()} and "
        f"{random.choice(VERBS)} {random_character()} "
        f"using ship {random_ship()}"
    )