import time
from plyer import notification


if __name__ == "__main__":
    
    while True:
        notification.notify(
            title = "**Time to Chill Out",
            message = "Taking breaks allows your brain and body to get the necessary recharge it needs to keep going",
            timeout = 20
        )
        time.sleep(30)


        