import time
import os #unused
import subprocess #unused
import math as m
import tkinter as tk

def convert_sec(sec):
    if(sec >= 3600): #more than an hour?
        hours = sec / 3600
        hours_remainder = hours - m.floor(hours)
        mins = hours_remainder * 60
        mins_remainder = mins - m.floor(mins)
        sec = mins_remainder * 60
    else: #second case, as zero hours breaks above case
        hours = 0
        mins = sec / 60
        mins_remainder = mins - m.floor(mins)
        sec = mins_remainder * 60
    #formatting up to 3 decimals in seconds for accuracy    
    return "Time Lapsed = {0}:{1}:{2}".format(int(hours),int(mins),"{:.3f}".format(sec))
	# print("Time Lapsed = {0}:{1}:{2}".format(int(hours),int(mins),"{:.3f}".format(sec)))
	
def convert_min(min): #redundant for this project, but useful for later conversions if the user provides this input
	if(min >= 60): #more than an hour?
		hours = min/60
		hours_remainder = hours - m.floor(hours)
		mins = hours_remainder * 60
		mins_remainder = mins - m.floor(mins)
		sec = mins_remainder * 60
	else: #second case, as zero hours breaks above case
		hours = 0
		mins = m.floor(min)
		mins_remainder = min - mins
		sec = mins_remainder * 60
	#formatting up to 3 decimals in seconds for accuracy
	print("Time Lapsed = {0}:{1}:{2}".format(int(hours),int(mins),"{:.3f}".format(sec)))
	
def convert_hour(hour): #redundant for this project, but useful for later conversions if the user provides this input
	if(hour > 0): #more than an hour?
		hours = hour
		hours_remainder = hours - m.floor(hours)
		mins = hours_remainder * 60
		mins_remainder = mins - m.floor(mins)
		sec = mins_remainder * 60
	else: #second case, as zero hours breaks above case
		hours = 0
		mins = 0
		sec = 0
	print("Time Lapsed = {0}:{1}:{2}".format(int(hours),int(mins),"{:.3f}".format(sec)))
# #testing manual input
# input("Press a button to start")
# start_time = time.time()

# input("Press a button to stop")
# end_time = time.time()

# total_time = end_time - start_time
# convert_sec(total_time)

window = tk.Tk()
#title the window
window.title("Stopwatch")
pressedFlag = False #stops time and logs it/updates text, or it starts time and displays that it's working
resetFlag = True #adds previous time if spamming start/stop
start_time = 0#= time.time()
end_time = 0# = time.time()
total_time = 0 #= end_time - start_time

def startStop():
	global pressedFlag
	global total_time 
	global end_time
	global start_time
	global resetFlag
	if pressedFlag == False:
		if resetFlag == False:
			start_time = time.time()
			pressedFlag = True
			timeDisplay.configure(state='normal')
			timeDisplay.delete('1.0', tk.END)
			timeDisplay.insert('end', "Tracking Time NOW!", 'center')
			timeDisplay.configure(state='disabled')
		else:
			start_time = time.time()
			pressedFlag = True
			timeDisplay.configure(state='normal')
			timeDisplay.delete('1.0', tk.END)
			timeDisplay.insert('end', "Tracking Time NOW!", 'center')
			timeDisplay.configure(state='disabled')
	else: #pressed flag == true
		if resetFlag == False:
			end_time = time.time()
			total_time += end_time - start_time
			pressedFlag = False
			timeDisplay.configure(state='normal')
			timeDisplay.delete('1.0', tk.END)
			timeDisplay.insert('end', convert_sec(total_time), 'center')
			timeDisplay.configure(state='disabled')
		else:
			start_time = time.time()
			end_time = time.time()
			total_time = end_time - start_time
			pressedFlag = False
			timeDisplay.configure(state='normal')
			timeDisplay.delete('1.0', tk.END)
			timeDisplay.insert('end', convert_sec(total_time), 'center')
			timeDisplay.configure(state='disabled')
	resetFlag = False
	
def reset():
	global pressedFlag
	global total_time 
	global end_time
	global start_time
	global resetFlag
	resetFlag = True
	pressedFlag = False
	total_time = 0 
	start_time = 0
	end_time = 0
	timeDisplay.configure(state='normal')
	timeDisplay.delete('1.0', tk.END)
	timeDisplay.insert('end', "Press Start/Stop to Begin", 'center')
	timeDisplay.configure(state='disabled')
	
startStopButton = tk.Button(window, text="Start/Stop", background = "light green", command = startStop)
resetButton = tk.Button(window, text="Reset", background = "light grey", command = reset)
timeDisplay = tk.Text(master=window)#, height=6, width=154)
timeDisplay.tag_config("center", justify = tk.CENTER)
timeDisplay.insert('end', "Press Start/Stop to Begin", 'center')
timeDisplay.configure(state='disabled')
# locations
timeDisplay.grid(column=0, row=0)
startStopButton.grid(column=0, row=1)
resetButton.grid(column=0, row=2)


