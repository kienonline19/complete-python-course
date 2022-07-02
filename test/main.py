raw_time = 8594

minutes, seconds = divmod(raw_time, 60)

print(minutes, seconds)
hours, minutes = divmod(minutes, 60)

print("{}s = {}h {}m {}s".format(raw_time, hours, minutes, seconds))
