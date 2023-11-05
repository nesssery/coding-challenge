from datetime import datetime
import os
from apscheduler.schedulers.background import BackgroundScheduler
from utils import checkUserViews

        
def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(checkUserViews.runUpdate, 'interval', minutes=1)
    scheduler.start()