import random


class Settings:
    PLAYERS_COUNT: int = 4
    MIN_LIVE_RATIO: float = 0.2
    MAX_LIVE_RATIO: float = 0.7
    LIVE_BULLET: str = '🔴'
    BLANK_BULLET: str = '🔵'

    @classmethod
    def get_bullet(self, is_live: bool) -> str:
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
    9: '9️⃣',
    10: '🔟',
}


def print_line():
    print('-'*40)


def charge_bullets():
    if not (2 <= Settings.PLAYERS_COUNT <= 4):
        raise ValueError("Необходимо от 2 до 4 игроков")

    total: int = random.randint(Settings.PLAYERS_COUNT, Settings.PLAYERS_COUNT + 4)
    min_live: int = max(1, int(total * Settings.MIN_LIVE_RATIO))
    max_live: int = max(min_live, int(total * Settings.MAX_LIVE_RATIO))
    num_live: int = random.randint(min_live, max_live)
    return [True] * num_live + [False] * (total - num_live)


def display_bullets():
    bullets: list[bool] = charge_bullets()

    random.shuffle(bullets)
    print(
        f'Скажи игрокам, что в игре:\n{NUMS_MAPPER[bullets.count(True)]}{Settings.LIVE_BULLET} '
        f'и {NUMS_MAPPER[bullets.count(False)]}{Settings.BLANK_BULLET}'
    )
    print(f'Или покажи им гильзы:\n{"".join([Settings.get_bullet(bullet) for bullet in bullets])}')
    
    print_line()
    random.shuffle(bullets)
    print(f'Порядок патронов в игре:\n{"".join([Settings.get_bullet(bullet) for bullet in bullets])}')
    
    print_line()
    print('Заряди патроны в магазин/дуло в порядке:')
    middle: int = 5 if len(bullets) <= 5 else (len(bullets) + 1) // 2
    for p in (bullets[:middle], bullets[middle:]):
        if p:
            print(
                f'{''.join([Settings.get_bullet(bullet) for bullet in p[:0:-1]])}/'
                f'{Settings.get_bullet(p[0])}'
            )


if __name__ == '__main__':
    display_bullets()
