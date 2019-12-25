class ErisMap:
    """Class defining a map of Eris"""

    def __init__(self, init_map=None):
        if init_map is not None:
            self.map = init_map
        else:
            self.map = [["."] * 5] * 5
        self.minute = 0
        self.scores = [self.calc_diversity_score()]

    def is_bug(self, j, i):
        """Return whether the current cell is a bug or not, outside the range returns false."""
        if j < 0 or i < 0:
            is_a_bug = False
        else:
            try:
                # Only is a bug if =="#"
                is_a_bug = self.map[j][i] == "#"
            except IndexError:
                is_a_bug = False
        return is_a_bug

    def num_bugs_adjacent(self, j, i):
        """Return the number of bugs adjacent to a square in the cell."""
        num_bugs = 0
        indices_to_test = [(0, -1), (0, +1), (-1, 0), (+1, 0)]
        for t in indices_to_test:
            is_a_bug = self.is_bug(j + t[0], i + t[1])
            if is_a_bug:
                num_bugs += 1
        return num_bugs

    def update(self):
        n = [
            [".", ".", ".", ".", ".",],
            [".", ".", ".", ".", ".",],
            [".", ".", ".", ".", ".",],
            [".", ".", ".", ".", ".",],
            [".", ".", ".", ".", ".",],
        ]
        next_minute = n
        for j in range(5):
            for i in range(5):
                num_bugs_adj = self.num_bugs_adjacent(j, i)
                # print(
                #     "At cell {},{} there are {} bugs around".format(j, i, num_bugs_adj)
                # )
                if self.map[j][i] == "#" and num_bugs_adj != 1:
                    # Bug dies unless there is exactly one bug adjacent
                    # print("Death")
                    next_minute[j][i] = "."
                elif self.map[j][i] == "#":
                    next_minute[j][i] = "#"
                elif self.map[j][i] == "." and (num_bugs_adj == 1 or num_bugs_adj == 2):
                    # An empty space becomes infested if exactly one or two bugs adjanent
                    # print("Birth")
                    next_minute[j][i] = "#"
                else:
                    next_minute[j][i] = "."
        self.minute += 1
        self.map = next_minute
        self.scores.append(self.calc_diversity_score())

    def state_printer(self):
        print(
            "After {} minutes, with a biodiversity rating of {}:".format(
                self.minute, self.scores[-1]
            )
        )
        for j in range(5):
            print("{}{}{}{}{}".format(*self.map[j]))
        # print(self.scores)

    def calc_diversity_score(self):
        score = 0
        for j in range(5):
            for i in range(5):
                if self.map[j][i] == "#":
                    score += 2 ** (5 * j + i)
        return score

    def find_first_repeating(self, print_states=False):
        while True:
            self.update()
            if print_states:
                self.state_printer()
            latest_score = self.scores[-1]
            if latest_score in self.scores[:-1]:
                print(
                    "Found repeated score! Biodiversity rating = {}".format(
                        latest_score
                    )
                )
                break
            else:
                pass


# example puzzle
i = [
    [".", ".", ".", ".", "#"],
    ["#", ".", ".", "#", "."],
    ["#", ".", ".", "#", "#"],
    [".", ".", "#", ".", "."],
    ["#", ".", ".", ".", "."],
]

# problem puzzle
#      #.###
#      .....
#      #..#.
#      ##.##
#      ..#.#


k = [
    ["#", ".", "#", "#", "#"],
    [".", ".", ".", ".", "."],
    ["#", ".", ".", "#", "."],
    ["#", "#", ".", "#", "#"],
    [".", ".", "#", ".", "#"],
]


a = ErisMap(k)

print("Initial state:")
a.state_printer()

a.find_first_repeating(print_states=True)
#
# for n in range(5):
#     a.update()
