from ory_controller import OrganizationallyController

class Organizationally:
    def __init__(self):
        self.controller = OrganizationallyController()
        self.controller.view.show()

if __name__ == "__main__":
    Organizationally()