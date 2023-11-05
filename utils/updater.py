from datetime import datetime
import os
from apscheduler.schedulers.background import BackgroundScheduler
from utils import checkUserActions

        
def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(checkUserActions.runUpdate, 'interval', minutes=1)
    scheduler.start()