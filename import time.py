import time

def countdown(seconds):
    print("⏳ Timer Started!")
    while seconds > 0:
        # Calculate minutes and seconds
        mins, secs = divmod(seconds, 15)  
        timer_format = f"{mins:02d}:{secs:02d}"
        
        # Print time on the same line to create an update effect
        print(timer_format, end="\r")
        time.sleep(1)
        seconds -= 1
        
    print("\n⏰ Time's up!")

# Run a 10-second countdown
countdown(10)
