import os

import win32file
import win32event
import win32con
import urllib
import urllib2
import time
import shutil

dirpath = r"C:\Users\Owner\Dropbox\Project\UI"
dirpathcopy = r"C:\Program Files\Apache Software Foundation\Apache2.2\htdocs\6868\UI"
path_to_watch = os.path.abspath (dirpath)
path_to_copy = os.path.abspath (dirpathcopy)

#
# FindFirstChangeNotification sets up a handle for watching
#  file changes. The first parameter is the path to be
#  watched; the second is a boolean indicating whether the
#  directories underneath the one specified are to be watched;
#  the third is a list of flags as to what kind of changes to
#  watch for. We're just looking at file additions / deletions.
#
change_handle = win32file.FindFirstChangeNotification (
  path_to_watch,
  0,
  win32con.FILE_NOTIFY_CHANGE_LAST_WRITE | win32con.FILE_NOTIFY_CHANGE_SIZE | win32con.FILE_NOTIFY_CHANGE_FILE_NAME 
)

#
# Loop forever, listing any file changes. The WaitFor... will
#  time out every half a second allowing for keyboard interrupts
#  to terminate the loop.
#
try:
  old_path_contents = dict ([(f, None) for f in os.listdir (path_to_watch)])
  while 1:
    result = win32event.WaitForSingleObject (change_handle, 500)

    #
    # If the WaitFor... returned because of a notification (as
    #  opposed to timing out or some error) then look for the
    #  changes in the directory contents.
    #
    if result == win32con.WAIT_OBJECT_0:
      print "copying files"
      new_path_contents = dict ([(f, None) for f in os.listdir (path_to_watch) if os.path.isfile(path_to_watch + "\\" + f)] )
##      added = [f for f in new_path_contents if not f in old_path_contents]
##      deleted = [f for f in old_path_contents if not f in new_path_contents]
##      if added:
      for filename in new_path_contents:
        shutil.copy2(path_to_watch + "\\" + filename, path_to_copy + "\\" + filename)
            
            #here we are sending the record event to the demo site
            #the (empty) second argument makes it a POST request
      win32file.FindNextChangeNotification (change_handle)

finally:
  win32file.FindCloseChangeNotification (change_handle)
