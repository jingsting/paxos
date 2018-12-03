from Meeting import Meeting, strList2Meeting
import RadioSend
import ElectionManager

class CommandProcessor:
    def __init__(self,hostname):
        self.hostname = hostname
        index, self.MaxIndex = findIndexFromTXTFile(hostname)
        if index < 0:
            raise ValueError("Can not find the hostname in knownhosts_udp.txt")
        self.rs = RadioSend.RadioSend(index,hostname)
        self.em = ElectionManager.ElectionManager(hostname,self.rs)

    def processSCHEDULE(self, userInput):
        return ""

    def processCANCEL(self, userInput):
        return ""

    def processVIEW(self):
        return ""

    def processMYVIEW(self):
        return ""

    def processLOG(self):
        return ""

    def processLEADER(self):
        return self.em.getLeader()

    def processRECEIVE_create(self, inputStr):
        return ""

    def processRECEIVE_cancel(self, inputStr):
        return ""

    def processHEARTBEAT(self, inputStr):
        return ""

    def processHEARTBEAT_reply(self, inputStr):
        return ""

    def processELECTION_start(self, inputStr):
        return ""

    def processELECTION_alive(self, inputStr):
        return ""

    def processELECTION_victory(self, inputStr):
        return ""

#==============================================================================
#                               Helpers
#==============================================================================

# return index representing line number in TXT
# return -1 when no data inside txt matches given hostname
def findIndexFromTXTFile(hostname):
    index = -1
    counter = 0
    with open("knownhosts_udp.txt") as fp:
        line = fp.readline()
        while line:
            siteLines = line.strip('\n').split(' ')
            if hostname == siteLines[0]:
                index = counter
            counter += 1
            line = fp.readline()
    return index, counter
