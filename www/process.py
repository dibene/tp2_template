from database import Database
from models import Sample

import random
import time
import signal
import sys

class GracefulKiller:
    kill_now = False
    def __init__(self):
        signal.signal(signal.SIGINT, self.exit_gracefully)
        signal.signal(signal.SIGTERM, self.exit_gracefully)

    def exit_gracefully(self, signum, frame):
        self.kill_now = True


def main(session):
    killer = GracefulKiller()
    while(1):
        sample = Sample()
        sample.humidity = random.randint(0,100)
        sample.pressure = random.randint(0,100)
        sample.temperature = random.randint(0,100)
        sample.windspeed = random.randint(0,100)
        
        session.add(sample)
        session.commit()

        print("Add new sample: %s %s %s %s" % (sample.humidity,  sample.pressure, sample.temperature, sample.windspeed))
        sys.stdout.flush()

        time.sleep(1)
        if killer.kill_now:
            session.close()
            break

if __name__ == '__main__':
    print("process samples sensor on ")

    db = Database()
    session = db.get_session()
    
    main(session)
    