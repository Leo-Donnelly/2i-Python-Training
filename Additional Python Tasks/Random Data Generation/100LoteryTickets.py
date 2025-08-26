import random

def get_amount_tickets():
    numTickets = int(input("How many tickets would you like?"))
    return numTickets

def generate_random_tickets(numTickets):
    tickets = []
    for x in range(numTickets):
        ticket = random.randrange(1000000000, 9999999999)
        tickets.append(ticket) 
        print(tickets[x])
    
    return tickets

def select_winners(tickets):
    winners = random.sample(sorted(tickets), 2)

    print("The winners of the lottery tickets are:", winners)


def main():
    numTickets = get_amount_tickets()
    tickets = generate_random_tickets(numTickets)
    select_winners(tickets)

main()