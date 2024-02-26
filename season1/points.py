import json
import pathlib

from season1.events import EVENTS_MEMES

POINTS_FILE = "season1/data/points.json"

class OgscPointsValues:
    GRAND_OPENING_PARTICIPATION = 50
    SURVEY_PARTICIPATION = 100
    MEME_PARTICIPATION = 5
    MEME_WIN = 25
    CLIP_PARTICIPATION = 10
    CLIP_WIN = 50
    CLIP_MULTIPLIER = 1.5


class OgscPointsTableKeys:
    GRAND_OPENING = "grand_opening"
    SURVEY = "survey"
    MEME_WIN = {i+1: f"memes_{i+1}_win" for i in range(len(EVENTS_MEMES))}
    MEME_PARTICIPATION = {i+1: f"memes_{i+1}_participation" for i in range(len(EVENTS_MEMES))}


class OgscPointsTable:
    def __init__(self):
        self.table: dict[str, dict[str, int]] = {}
        self.read(POINTS_FILE)
    
    def read(self, path: str | pathlib.Path) -> None:
        try:
            with open(path) as f:
                self.table = json.load(f)
        except:
            self.table = {}

    def write(self, path: str | pathlib.Path) -> None:
        with open(path, "w") as f:
            return json.dump(self.table, f)

    def points(self, user_id: int) -> dict[str, int] | None:
        return self.table.get(str(user_id), None)

    def total_points(self, user_id: int) -> int | None:
        points = self.points(user_id)
        if points is None:
            return None
        return sum(points.values())

    def set_points(self, user_id: int, key: str, points: int) -> None:
        str_user_id = str(user_id)
        if str_user_id not in self.table:
            self.table[str_user_id] = {}
        self.table[str_user_id][key] = points
        self.write(POINTS_FILE)

if __name__ == "__main__":
    t = OgscPointsTable()

    t.set_points(1, OgscPointsTableKeys.GRAND_OPENING, 100)
    t.set_points(2, OgscPointsTableKeys.GRAND_OPENING, 100)
    t.set_points(3, OgscPointsTableKeys.GRAND_OPENING, 100)