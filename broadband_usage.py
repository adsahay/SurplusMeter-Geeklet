# -*- coding: utf8 -*-

############################################################
#   surplusmeter_geeklet
#
#   @author Aditya Sahay
#   @abstract Displays a summary of 
#   bandwidth usage from SurplusMeter
############################################################

import calendar
from datetime import datetime
from xml.etree.ElementTree import ElementTree

ESCAPE_HEADER_MARKUP = u"\033[1m" # defauls to bold
ESCAPE_PAST_DUE_COLOR = u"\033[31m" # defaults to red
ESCAPE_AVAILABLE_COLOR = u"\033[32m" # defaults to green
ESCAPE_CANCEL = u"\033[0m" # resets all text atributes you may have set

data_file = '/Users/adsahay/Library/Application Support/SurplusMeter/surplusmeter_data.plist'

# parse the plist file and build a dictionary
tree = ElementTree()
d = tree.parse(data_file).find('dict')
usage = {}
# to convert bytes to mb
mb = 1024 * 1024

for i in range(len(d)):
    # items are alternately key and value.
    if not i % 2 == 0:
        usage[d[i-1].text] = d[i].text if d[i].text else d[i].tag
        
#print usage
today = datetime.today()
days_this_month = calendar.monthrange(today.year, today.month)[1]
allowance = int(usage['downloadLimit']) * 1024
t_allowance = allowance / days_this_month

# Month so far
download = int(usage['bytesDown'])/mb
upload = int(usage['bytesUp'])/mb
total = download + upload

# Today
t_download = int(usage['todaysBytesDown'])/mb
t_upload = int(usage['todaysBytesUp'])/mb
t_total = t_download + t_upload

# limits
include_uploads = usage['downloadLimitIncludesUploads'] == 'true'
limit = allowance - total if include_uploads else allowance - download
percent = limit * 100 / allowance
t_limit = t_allowance - t_total if include_uploads else t_allowance - t_download
t_percent = t_limit * 100 / t_allowance

# format and output
# color code - green says available, red says over
limit_color = ESCAPE_PAST_DUE_COLOR if limit < 0 else ESCAPE_AVAILABLE_COLOR
t_limit_color = ESCAPE_PAST_DUE_COLOR if t_limit < 0 or limit < 0 else ESCAPE_AVAILABLE_COLOR
# header
print ESCAPE_HEADER_MARKUP + '{0:15}{1:^15}{2:^10}'.format(' ', 'Month so far', 'Today') + ESCAPE_CANCEL
# usage info
print '{0}{1:>12}{2}{3:>10} MB{4:>10} MB'.format(ESCAPE_HEADER_MARKUP, 'Download:', ESCAPE_CANCEL, download, t_download)
print '{0}{1:>12}{2}{3:>10} MB{4:>10} MB'.format(ESCAPE_HEADER_MARKUP, 'Upload:', ESCAPE_CANCEL, upload, t_upload)
print ''
print '{0}{1:>12}{2}{3:>10} MB{4:>10} MB'.format(ESCAPE_HEADER_MARKUP, 'Total:', ESCAPE_CANCEL, total, t_total)
print '{0}{1:>12}{2}{3:>10} MB{4:>10} MB'.format(ESCAPE_HEADER_MARKUP, 'Limit:', ESCAPE_CANCEL, allowance, t_allowance)
#print '{0}{1:>12}{2}{3:>10} GB{4:>10.2} GB'.format(ESCAPE_HEADER_MARKUP, '', ESCAPE_CANCEL, allowance/1024.0, t_allowance/1024.0)
# color-coded "Remaining" limit
print ''
print '{0}{1:>12}{2}{5}{3:>10} MB{2}{6}{4:>10} MB{2}'.format(ESCAPE_HEADER_MARKUP, 'Remaining:', ESCAPE_CANCEL, limit, t_limit, limit_color, t_limit_color)
print '{1:>12}{5}{3:>12}%{2}{6}{4:>12}%{2}'.format(ESCAPE_HEADER_MARKUP, ' ', ESCAPE_CANCEL, percent, t_percent, limit_color, t_limit_color)
