#Watch Time Calculator

import random
#populate your account with videos 
print("Part 1 - What are the titles of the videos in on your Tiktok account? ")
videos = []
video_name = input("Come up with some video titles ('exit' to stop):")
#Ask the user for the titles of your videos until they say "exit"
while video_name != "exit":
    videos.append(video_name)
    video_name = input("Come up with some video titles ('exit' to stop):")
print(videos)

#set the times to your videos
print("Part 2 - How long is each video on your account?")
video_times = {}
for i in videos:
    time = int(input(f'Enter the length of {i} in minutes:'))
    video_times[i] = time
print(video_times)

#total watch time
print("Part 3 - Let's talk about watch time.")
sub_count = int(input("How many subscribers do I have?"))
total_watch_time = 0
for i in range(sub_count):
    video1 = random.choice(videos)
    video2 = random.choice(videos)
total_watch_time = (video_times[video1] + video_times[video2])* sub_count

#Calculate the total time
print(f"Total watch time across all subscribers is: {total_watch_time} minutes")


