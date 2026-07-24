from datetime import datetime
from core.logger import AgentLogger


class SessionEngine:

    def __init__(self):

        self.current_session = "NONE"

    def get_session(self, current_time=None):

        if current_time is None:
            current_time = datetime.now().time()

        hour = current_time.hour
        minute = current_time.minute

        total_minutes = hour * 60 + minute

        # London Kill Zone
        if 15 * 60 <= total_minutes <= 18 * 60:

            self.current_session = "LONDON"

        # New York Kill Zone
        elif 20 * 60 + 30 <= total_minutes <= 23 * 60 + 30:

            self.current_session = "NEW_YORK"

        else:

            self.current_session = "OUTSIDE_SESSION"

        AgentLogger.info(
            f"Trading Session: {self.current_session}"
        )

        return self.current_session