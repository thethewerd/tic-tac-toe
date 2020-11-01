class SimpleGame:
    def __init__(self, name):
        self.name = name
        self.space_a_1 = " "
        self.space_a_2 = " "
        self.space_a_3 = " "
        self.space_b_1 = " "
        self.space_b_2 = " "
        self.space_b_3 = " "
        self.space_c_1 = " "
        self.space_c_2 = " "
        self.space_c_3 = " "
    def hello(self):
        print("i'm a simple game named " + self.name)
    def make_move(self, player_symbol, space_name):
        if space_name == "a1":
            if self.space_a_1 != " ":
                print("NOOOO!")
            self.space_a_1 = player_symbol
        if space_name == "a2":
            if self.space_a_2 != " ":
                print("NOOOO!")
            self.space_a_2 = player_symbol
        if space_name == "a3":
            if self.space_a_3 != " ":
                print("NOOOO!")
            self.space_a_3 = player_symbol
        if space_name == "b1":
            if self.space_b_1 != " ":
                print("NOOOO!")
            self.space_b_1 = player_symbol
        if space_name == "b2":
            if self.space_b_2 != " ":
                print("NOOOO!")
            self.space_b_2 = player_symbol
        if space_name == "b3":
            if self.space_b_3 != " ":
                print("NOOOO!")
            self.space_b_3 = player_symbol
        if space_name == "c1":
            if self.space_c_1 != " ":
                print("NOOOO!")
            self.space_c_1 = player_symbol
        if space_name == "c2":
            if self.space_c_2 != " ":
                print("NOOOO!")
            self.space_c_2 = player_symbol
        if space_name == "c3":
            if self.space_c_3 != " ":
                print("NOOOO!")
            self.space_c_3 = player_symbol
    def show_board(self):
        print()
        print(self.name)
        print(self.space_a_1 + " " + "|" + self.space_b_1 + " " + "|" + self.space_c_1)
        print(self.space_a_2 + " " + "|" + self.space_b_2 + " " + "|" + self.space_c_2)
        print(self.space_a_3 + " " + "|" + self.space_b_3 + " " + "|" + self.space_c_3)
        print()