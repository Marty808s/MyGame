import random
from config import SCREEN_WIDTH, SCREEN_HEIGHT, ENEMY_COUNT
from entities.mob import Mob

def spawn_mob(mobs, already_spawned, spawned_counter):
    if already_spawned:
        return mobs, spawned_counter, already_spawned
    if spawned_counter >= ENEMY_COUNT:
        already_spawned = True
        return mobs, spawned_counter, already_spawned
    spawned_counter += 1
    edge = random.choice(["top", "bottom", "left", "right"])
    if edge == "top":
        x, y = random.randint(32, SCREEN_WIDTH - 32), -32
    elif edge == "bottom":
        x, y = random.randint(32, SCREEN_WIDTH - 32), SCREEN_HEIGHT
    elif edge == "left":
        x, y = -32, random.randint(32, SCREEN_HEIGHT - 32)
    else:  # right
        x, y = SCREEN_WIDTH, random.randint(32, SCREEN_HEIGHT - 32)
    mobs.append(Mob(x, y))
    if spawned_counter >= ENEMY_COUNT:
        already_spawned = True
    return mobs, spawned_counter, already_spawned