import json
import time
from cvplibrary.auditlogger import alog
from cvplibrary import Device, CVPGlobalVariables, GlobalVariableNames
ip = CVPGlobalVariables.getValue(GlobalVariableNames.CVP_IP)
scriptArgs = CVPGlobalVariables.getValue(GlobalVariableNames.SCRIPT_ARGS)
alog("running shut_host_links from script")
d = Device(ip)
Output = d.runCmds(["enable","configure","maintenance","unit shut-host-links","quiesce"])
maintmode=False
time.sleep(5)
numoftries=0
while (maintmode is False and numoftries<5):
   Output = d.runCmds(["show maintenance"])
   if Output[0]["response"]["units"]["shut-host-links"]["adminState"]=="underMaintenance":
      maintmode = True
      alog("Under maintenance")
   else:
      alog("Entering maintenance")
      time.sleep(30)
   numoftries+=1