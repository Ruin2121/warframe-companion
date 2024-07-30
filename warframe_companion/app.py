from cleo.application import Application

from warframe_companion.src.commands.main_command import MainCommand


class App(Application):
    """
    App
    """

    def __init__(self) -> None:
        super().__init__(name="warframe-companion", version="0.1.0")
        self._default_command = "main"


def main() -> int:
    """
    Main entry point for the application.
    """
    app = App()
    app.add(MainCommand())

    exit_code: int = app.run()

    return exit_code


if __name__ == "__main__":
    main()
