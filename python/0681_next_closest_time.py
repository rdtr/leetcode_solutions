class Solution:
    def nextClosestTime(self, time):
        appearance = set()
        for ch in time:
            if ch != ':':
                appearance.add(ch)

        time = self.increment(time)
        while True:
            found = True
            for ch in time:
                if ch != ':' and ch not in appearance:
                    time = self.increment(time)
                    found = False
                    break
            if found:
                break
        return time

    def increment(self, time):
        if time[4] != '9':
            return time[:4] + str(int(time[4]) + 1)
        if time[3] != '5':
            print(time)
            return time[:3] + str(int(time[3]) + 1) + '0'

        if time[:2] == '23':
            return '00:00'
        elif time[1] == '9':
            return str(int(time[0]) + 1) + '0:00'
        else:
            return time[0] + str(int(time[1]) + 1) + ':00'
