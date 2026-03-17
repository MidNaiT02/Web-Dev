# main.py - Demonstrates OOP concepts using the Anime hierarchy

from models import Anime, ShounenAnime, RomanceAnime, IsekaïAnime

# ── 1. Instantiate objects ─────────────────────────────────────────────────────

base_anime = Anime(
    title="Cowboy Bebop",
    studio="Sunrise",
    episodes=26
)

naruto = ShounenAnime(
    title="Naruto",
    studio="Pierrot",
    episodes=220,
    power_system="Chakra & Ninjutsu",
    rival="Sasuke"
)

toradora = RomanceAnime(
    title="Toradora",
    studio="J.C.Staff",
    episodes=25,
    couple=("Ryuuji", "Taiga"),
    setting="High School"
)

re_zero = IsekaïAnime(
    title="Re:Zero",
    studio="White Fox",
    episodes=25,
    protagonist="Subaru Natsuki",
    cheat_ability="Return by Death"
)

# ── 2. Store in a list ────────────────────────────────────────────────────────

anime_list = [base_anime, naruto, toradora, re_zero]

# ── 3. Iterate and call methods ───────────────────────────────────────────────

print("=" * 60)
print("  ALL ANIME — __str__ representation")
print("=" * 60)
for anime in anime_list:
    print(anime)           # calls __str__

print()
print("=" * 60)
print("  POLYMORPHISM — describe() (overridden in each child)")
print("=" * 60)
for anime in anime_list:
    print(anime.describe())   # polymorphic call
    print()

print("=" * 60)
print("  POLYMORPHISM — watch() (overridden in IsekaiAnime)")
print("=" * 60)
for anime in anime_list:
    print(anime.watch())
print()

# ── 4. Child-class unique methods ─────────────────────────────────────────────

print("=" * 60)
print("  UNIQUE METHODS per child class")
print("=" * 60)
print(naruto.train())
print(toradora.confess())
print(re_zero.reincarnate())
print()

# ── 5. isinstance check ───────────────────────────────────────────────────────

print("=" * 60)
print("  isinstance() checks (Inheritance verification)")
print("=" * 60)
for anime in anime_list:
    print(f"{anime.title:15} → is Anime: {isinstance(anime, Anime)}"
          f" | type: {type(anime).__name__}")
