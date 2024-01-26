import random
from more_itertools import unique_everseen


def generate_unique_pairings(students, machines, weeks):
  pairings_schedule = []

  for week in range(1, weeks + 1):
    random.shuffle(students)
    random.shuffle(machines)
    if len(students) % 2 != 0:
      students.append(
          "TBD")  # Adding a placeholder student if the count is odd
    pairs = [(students[i], students[i + 1])
             for i in range(0, len(students), 2)]
    # Ensure unique pairs for the week
    unique_pairs = list(unique_everseen(pairs))

    week_pairings = []
    for pair, machine in zip(unique_pairs, machines):
      week_pairings.append({'Pair': pair, 'Machine': machine})
    pairings_schedule.append({'Week': week, 'Pairings': week_pairings})
  return pairings_schedule


def print_schedule(pairings_schedule):
  for week in pairings_schedule:
    print(f"Week {week['Week']}:")
    for pair_number, pair in enumerate(week['Pairings'], start=1):
      print(
          f"Pair {pair_number}: {pair['Pair'][0]} & {pair['Pair'][1]} (Machine: {pair['Machine']})"
      )
    print()


# Example usage:
# NOTE: use 'TBD' as a placeholder for students who are not available for the week
students_list = [
    'Forrest', 'Arwa', 'Emelissa', 'Bethany', 'Jordan', 'Sheidy', 'Nathan',
    'Quentin', 'Amanda', 'Natalie', 'Leyna', 'Julisa', 'Toofant', 'TBD'
]

# NOTE: the number of machines should be equal to the number of pairs!
machines_list = ["Epic", "Affiniti1", "Affiniti2", "S70", "GE1", "GE2", "GE3"]

number_of_weeks = 17
unique_pairings_schedule = generate_unique_pairings(students_list,
                                                    machines_list,
                                                    number_of_weeks)

# Print the schedule
print_schedule(unique_pairings_schedule)
