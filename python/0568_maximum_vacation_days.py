class Solution:
    def maxVacationDays(self, flights: List[List[int]], days: List[List[int]]) -> int:
        cityNum = len(flights)
        weekNum = len(days[0])

        DP = [0 for _ in range(cityNum)]
        prevCities = set()

        # initialize DP on first week
        for city, ok in enumerate(flights[0]):
            if city == 0 or ok == 1:
                prevCities.add(city)
                DP[city] = days[city][0]

        # get maximum vactionNum per week and per city
        res = 0
        for week in range(1, weekNum):
            visitingCities = set()
            newDP = [0 for _ in range(cityNum)]
            for city in prevCities:
                for destination, ok in enumerate(flights[city]):
                    if ok or destination == city:
                        visitingCities.add(destination)
                        newDP[destination] = max(DP[city] + days[destination][week], newDP[destination])

                        res = max(res, newDP[destination])

            DP, prevCities = newDP, visitingCities
        return res
