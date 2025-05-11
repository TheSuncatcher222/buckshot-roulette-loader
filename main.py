import random


class LobbySettings:
    """Настройки лобби."""

    PLAYERS_COUNT: int = 4


class Settings:
    """Системные настройки."""

    MIN_LIVE_RATIO: float = 0.2
    MAX_LIVE_RATIO: float = 0.7
    MAX_BULLETS_COUNT: int = 8
    MAGAZINE_CAPACITY: int = 4
    LIVE_BULLET: str = '🔴'
    BLANK_BULLET: str = '🔵'

    @classmethod
    def get_bullet_symbol(self, is_live: bool) -> str:
        return self.LIVE_BULLET if is_live else self.BLANK_BULLET


NUMS_MAPPER: dict[int, str] = {
    1: '1️⃣',
    2: '2️⃣',
    3: '3️⃣',
    4: '4️⃣',
    5: '5️⃣',
    6: '6️⃣',
    7: '7️⃣',
    8: '8️⃣',
}


def charge_bullets():
    if not (2 <= LobbySettings.PLAYERS_COUNT <= 4):
        raise ValueError("Необходимо от 2 до 4 игроков")

    total: int = random.randint(LobbySettings.PLAYERS_COUNT, Settings.MAX_BULLETS_COUNT)
    if total > 6:
        min_live: int = 3
    elif total > 4:
        min_live: int = 2
    else:
        min_live: int = 1

    min_live: int = max(min_live, int(total * Settings.MIN_LIVE_RATIO))
    max_live: int = max(min_live, int(total * Settings.MAX_LIVE_RATIO))
    num_live: int = random.randint(min_live, max_live)
    return [True] * num_live + [False] * (total - num_live)


def display_bullets():
    bullets: list[bool] = charge_bullets()

    random.shuffle(bullets)
    print(
        'Скажи игрокам, что в игре:\n'
        f'{NUMS_MAPPER[bullets.count(True)]}{Settings.LIVE_BULLET} и {NUMS_MAPPER[bullets.count(False)]}{Settings.BLANK_BULLET}\n'
        'Или покажи им гильзы:\n'
        f'{"".join([Settings.get_bullet_symbol(bullet) for bullet in bullets])}'
    )

    print('-'*28)

    random.shuffle(bullets)
    if len(bullets) > Settings.MAGAZINE_CAPACITY:
        middle: int = (len(bullets) + 1) // 2
        bullets.insert(middle, ' | ')
    print(
        'Заряжай патроны в магазин,\n'
        'каждую секцию справа-налево:\n'
        f'{"".join([Settings.get_bullet_symbol(bullet) if isinstance(bullet, bool) else bullet for bullet in bullets])}\n'
        'Не забудь передернуть цевьё!'
    )
    

if __name__ == '__main__':
    display_bullets()
