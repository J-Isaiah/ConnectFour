class ConnectFourError(Exception):
    """Base class for all Connect-Four-related errors."""

    pass


class InvalidMoveError(ConnectFourError):
    """Raised when a move is not within valid columns."""

    pass


class ColumnFullError(ConnectFourError):
    """Raised when attempting to place a piece in a full column."""

    pass


class GameOverError(ConnectFourError):
    """Raised when someone tries to make a move after the game is already over."""

    pass
