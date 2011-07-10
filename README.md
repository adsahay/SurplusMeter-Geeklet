## Geektool script for SurplusMeter

[SurplusMeter](http://www.skoobysoft.com/utilities/utilities.html) is a broadband monitoring tool for Mac, for those of us with limited data plans.  

[Geektool](http://projects.tynsoe.org/en/geektool/) is an awesome utility to customize a Mac desktop with all sorts of useful (or plain eye candy) information.

I exceeded my monthly data plan today, and decided to write this script for displaying a summary of my broadband usage on my desktop. 

### Installation:

1. Download the script somewhere.
2. Go to System Preferences -> Geektool.
3. Drag-n-drop a new "Shell" type of Geeklet. 
4. In the "Command" field provide "python /path/to/broadband_usage.py" with the correct path to the file.
5. Since the script uses python string formatting, it seems to format correctly when using a fixed type font like Monaco or Courier, and a little disturbed otherwise.

### Notes:

1. "Month so far" shows the broadband usage data for your current monthly cycle, based on the starting date provided to SurplusMeter. The "Limit" is the total monthly broadband limit.
2. It shows data in MB only. Feel free to tinker with the script if you prefer GB.
