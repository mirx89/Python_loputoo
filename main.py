
from Controller import Controller


class final:

    def __init__(self):
        Controller(db_name).main()


if __name__ == "__main__":
    db_name = None

    final()
