import random


class Ship:
    def __init__(self, coordinates):
        self.coordinates = coordinates
        self.hits = set()

    def is_sunk(self):
        return len(self.hits) == len(self.coordinates)


class Board:
    def __init__(self, ships):
        self.board_size = 6
        self.ships = ships
        self.board = [['О' for _ in range(self.board_size)] for _ in range(self.board_size)]
        self.previous_shots = set()

    def display_board(self):
        print("   | 1 | 2 | 3 | 4 | 5 | 6 |")
        for i in range(self.board_size):
            print(f"{i + 1} | {' | '.join(self.board[i])} |")

    def place_ships(self):
        for ship in self.ships:
            for coordinate in ship.coordinates:
                row, col = coordinate
                self.board[row][col] = '■'

    def check_shot(self, row, col):
        if (row, col) in self.previous_shots:
            raise ValueError("Вы уже стреляли в эту клетку.")

        self.previous_shots.add((row, col))

        for ship in self.ships:
            if (row, col) in ship.coordinates:
                ship.hits.add((row, col))
                self.board[row][col] = 'X'
                if ship.is_sunk():
                    print("Корабль потоплен!")
                return True

        self.board[row][col] = 'T'
        return False

    def is_game_over(self):
        for ship in self.ships:
            if not ship.is_sunk():
                return False
        return True


def generate_ships():
    ships = []

    while len(ships) < 7:
        size = 3 if len(ships) == 0 else 2 if len(ships) < 3 else 1
        coordinates = generate_ship_coordinates(size)

        if is_valid_ship(coordinates, ships):
            ships.append(Ship(coordinates))

    return ships


def generate_ship_coordinates(size):
    coordinates = []

    start_row = random.randint(0, 5)
    start_col = random.randint(0, 5)
    is_horizontal = random.choice([True, False])

    if is_horizontal and start_col + size <= 6:
        for col in range(start_col, start_col + size):
            coordinates.append((start_row, col))
    elif not is_horizontal and start_row + size <= 6:
        for row in range(start_row, start_row + size):
            coordinates.append((row, start_col))
    else:
        return generate_ship_coordinates(size)

    return coordinates


def is_valid_ship(coordinates, ships):
    for ship in ships:
        for coordinate in coordinates:
            row, col = coordinate
            if (row, col) in ship.coordinates:
                return False

    return True


def get_player_shot():
    while True:
        try:
            row = int(input("Введите номер строки для выстрела (1-6): "))
            col = int(input("Введите номер столбца для выстрела (1-6): "))
            if row < 1 or row > 6 or col < 1 or col > 6:
                raise ValueError("Неверные координаты.")
            return row - 1, col - 1
        except ValueError as e:
            print(f"Ошибка: {e}. Попробуйте снова.")


import random


class Ship:
    def __init__(self, coordinates):
        self.coordinates = coordinates
        self.hits = set()

    def is_sunk(self):
        return len(self.hits) == len(self.coordinates)


class Board:
    def __init__(self, ships):
        self.board_size = 6
        self.ships = ships
        self.board = [['О' for _ in range(self.board_size)] for _ in range(self.board_size)]
        self.previous_shots = set()

    def display_board(self):
        print("   | 1 | 2 | 3 | 4 | 5 | 6 |")
        for i in range(self.board_size):
            print(f"{i + 1} | {' | '.join(self.board[i])} |")

    def place_ships(self):
        for ship in self.ships:
            for coordinate in ship.coordinates:
                row, col = coordinate
                self.board[row][col] = '■'

    def check_shot(self, row, col):
        if (row, col) in self.previous_shots:
            raise ValueError("Вы уже стреляли в эту клетку.")

        self.previous_shots.add((row, col))

        for ship in self.ships:
            if (row, col) in ship.coordinates:
                ship.hits.add((row, col))
                self.board[row][col] = 'X'
                if ship.is_sunk():
                    print("Корабль потоплен!")
                return True

        self.board[row][col] = 'T'
        return False

    def is_game_over(self):
        for ship in self.ships:
            if not ship.is_sunk():
                return False
        return True


def generate_ships():
    ships = []

    while len(ships) < 7:
        size = 3 if len(ships) == 0 else 2 if len(ships) < 3 else 1
        coordinates = generate_ship_coordinates(size)

        if is_valid_ship(coordinates, ships):
            ships.append(Ship(coordinates))

    return ships


def generate_ship_coordinates(size):
    coordinates = []

    start_row = random.randint(0, 5)
    start_col = random.randint(0, 5)
    is_horizontal = random.choice([True, False])

    if is_horizontal and start_col + size <= 6:
        for col in range(start_col, start_col + size):
            coordinates.append((start_row, col))
    elif not is_horizontal and start_row + size <= 6:
        for row in range(start_row, start_row + size):
            coordinates.append((row, start_col))
    else:
        return generate_ship_coordinates(size)

    return coordinates


def is_valid_ship(coordinates, ships):
    for ship in ships:
        for coordinate in coordinates:
            row, col = coordinate
            if (row, col) in ship.coordinates:
                return False

    return True


def get_player_shot():
    while True:
        try:
            row = int(input("Введите номер строки для выстрела (1-6): "))
            col = int(input("Введите номер столбца для выстрела (1-6): "))
            if row < 1 or row > 6 or col < 1 or col > 6:
                raise ValueError("Неверные координаты.")
            return row - 1, col - 1
        except ValueError as e:
            print(f"Ошибка: {e}. Попробуйте снова.")


def main():
    print("Добро пожаловать в игру 'Морской бой'!")

    player_board = Board(generate_ships())
    computer_board = Board(generate_ships())

    player_board.place_ships()
    computer_board.place_ships()

    player_turn = True

    while not player_board.is_game_over() and not computer_board.is_game_over():
        print("Игровое поле игрока:")
        player_board.display_board()
        print("Игровое поле компьютера:")
        computer_board.display_board()

        if player_turn:
            print("Ход игрока:")
            row, col = get_player_shot()
            try:
                shot_result = computer_board.check_shot(row, col)
                if shot_result:
                    print("Вы попали в корабль противника!")
                else:
                    print("Промах!")
                player_turn = False
            except ValueError as e:
                print(f"Ошибка: {e}. Попробуйте снова.")

        else:
            print("Ход компьютера:")
            row, col = random.randint(0, 5), random.randint(0, 5)
            try:
                shot_result = player_board.check_shot(row, col)
                if shot_result:
                    print("Компьютер попал в ваш корабль!")
                else:
                    print("Компьютер промахнулся!")
                player_turn = True
            except ValueError:
                continue

    if player_board.is_game_over():
        print("Поздравляем, вы победили!")
    elif computer_board.is_game_over():
        print("К сожалению, вы проиграли.")


if __name__ == "__main__":
    main()
