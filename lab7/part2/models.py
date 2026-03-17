# models.py - Anime Class Hierarchy

class Anime:
    """Base class representing an Anime title."""

    def __init__(self, title, studio, episodes):
        self.title = title
        self.studio = studio
        self.episodes = episodes

    def describe(self):
        return f"'{self.title}' by {self.studio} — {self.episodes} episodes"

    def watch(self):
        return f"Now watching: {self.title}..."

    def __str__(self):
        return f"Anime({self.title}, {self.studio}, {self.episodes} eps)"


# ── Child Class 1 ──────────────────────────────────────────────────────────────

class ShounenAnime(Anime):
    """A battle/adventure anime aimed at young male audiences."""

    def __init__(self, title, studio, episodes, power_system, rival):
        super().__init__(title, studio, episodes)
        self.power_system = power_system
        self.rival = rival

    def train(self):
        return f"{self.title}: Training with {self.power_system} to surpass {self.rival}!"

    # Override describe()
    def describe(self):
        base = super().describe()
        return f"{base} | Shounen | Power: {self.power_system} | Rival: {self.rival}"

    def __str__(self):
        return f"ShounenAnime({self.title})"


# ── Child Class 2 ──────────────────────────────────────────────────────────────

class RomanceAnime(Anime):
    """A romance / slice-of-life anime."""

    def __init__(self, title, studio, episodes, couple, setting):
        super().__init__(title, studio, episodes)
        self.couple = couple
        self.setting = setting

    def confess(self):
        a, b = self.couple
        return f"{self.title}: {a} finally confesses to {b} under the cherry blossoms 🌸"

    # Override describe()
    def describe(self):
        base = super().describe()
        pair = " & ".join(self.couple)
        return f"{base} | Romance | Couple: {pair} | Setting: {self.setting}"

    def __str__(self):
        return f"RomanceAnime({self.title})"


# ── Child Class 3 ──────────────────────────────────────────────────────────────

class IsekaïAnime(Anime):
    """An isekai (transported to another world) anime."""

    def __init__(self, title, studio, episodes, protagonist, cheat_ability):
        super().__init__(title, studio, episodes)
        self.protagonist = protagonist
        self.cheat_ability = cheat_ability

    def reincarnate(self):
        return (f"{self.title}: {self.protagonist} is transported to another world "
                f"and awakens '{self.cheat_ability}'!")

    # Override watch()
    def watch(self):
        return (f"Now watching {self.title} — "
                f"where {self.protagonist} breaks every rule with {self.cheat_ability}.")

    # Override describe()
    def describe(self):
        base = super().describe()
        return (f"{base} | Isekai | Protagonist: {self.protagonist} "
                f"| Cheat: {self.cheat_ability}")

    def __str__(self):
        return f"IsekaiAnime({self.title})"
