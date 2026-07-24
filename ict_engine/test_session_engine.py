from datetime import time

from ict_engine.session_engine import SessionEngine

engine = SessionEngine()

print(engine.get_session(time(16, 0)))
print(engine.get_session(time(21, 0)))
print(engine.get_session(time(10, 0)))