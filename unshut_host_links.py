import json
import time
from cvplibrary.auditlogger import alog
from cvplibrary import Device, CVPGlobalVariables, GlobalVariableNames
ip = CVPGlobalVariables.getValue(GlobalVariableNames.CVP_IP)
scriptArgs = CVPGlobalVariables.getValue(GlobalVariableNames.SCRIPT_ARGS)
alog("running unshut_host_links from script")
d = Device(ip)
Output = d.runCmds(["enable","configure","maintenance","unit shut-host-links","no quiesce"])
maintmode=True
time.sleep(5)
numoftries=0
while (maintmode is True and numoftries<5):
   Output = d.runCmds(["show maintenance"])
   if Output[0]["response"]["units"]["shut-host-links"]["adminState"]=="active":
      maintmode = False
      alog("Exited maintenance")
   else:
      alog("Still under maintenance")
      time.sleep(30)
   numoftries+=1