from .models import Task
from .utils import random_planet, random_character, random_ship
import random

VERBS = ["hunt", "kill", "capture"]

def ensure_tasks(min_count: int = 10) -> None:
    count = Task.objects.count()
    if count >= min_count:
        return

    to_create = min_count - count
    Task.objects.bulk_create([
        Task(
            planet_name=random_planet(),
            character_name=random_character(),
            ship_name=random_ship(),
            verb=random.choice(VERBS),   # assign verb here once and for all
            is_completed=False
        )
        for _ in range(to_create)
    ])