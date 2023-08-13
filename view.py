import action


class view:
    _action = None
    _arr_action = []

    def __init__(self):
        self._action = 0

        self._arr_action = {

            1: "New note",
            2: "Editing a note",
            3: "Deleting a note",
            4: "Find note by ID",
            5: "Find note by TITLE",
            6: "List of notes",
            0: "Exit"
        }

    def get_action(self):
        return self._action

    def get_arr_action(self):
        return self._arr_action

    def strin_rep(self, st: str):
        st = st.replace("-", "").replace(",", ".").split(".")[0]
        return st

    def show_text(self, arr):
        for key, value in arr.items():
            print(f"{key} - {value}")

    def get_number(self):
        inp = self.strin_rep(input())
        if inp.isdigit() and int(inp) >= 0:
            return int(inp)

    def set_action(self):
        while True:
            print("Choose an action:\n")
            self.show_text(self._arr_action)
            self._action = self.get_number()
            if 0 <= self._action < len(self._arr_action):
                break

    def menu(self):
        while True:
            self.set_action()
            if self._action == 0:
                exit("\nThank you. Goodbye.")
            elif self._action == 1:
                action.add_note()
            elif self._action == 2:
                action.edit_note()
            elif self._action == 3:
                action.delete_note()
            elif self._action == 4:
                action.view_note()
            elif self._action == 5:
                action.view_search_title()
            elif self._action == 6:
                action.view_all_notes()