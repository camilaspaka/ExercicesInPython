raw_time = 8594
minutes, seconds = divmod(raw_time, 60)
hours, minutes = divmod(minutes, 60)
print(f"{raw_time}´s {hours}h {minutes}m {seconds}s")