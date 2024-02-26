from helpers.tickets.flight_tickets_helper import flighttickethelper

fth = flighttickethelper(src="ewr",dest="del",flightdate="12/10/2010",flight="CO82")

f = fth.get_flights()

for x in f:
    print(x["time"])

