from enum import Enum


class SourceType(Enum):
    CROUTINES = "coroutines"
    SERIALIZATION = "serialization"

    def get_filepath(self):
        if self.CROUTINES:
            return "./data/coroutines/git_hisitory_logs_each_month.csv"
        elif self.SERIALIZATION:
            return "./data/serialization/git_hisitory_logs_each_month.csv"
