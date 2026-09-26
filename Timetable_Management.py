"""
Student Timetable Management System
------------------------------------

"""



days_order = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

timetable = {day: [] for day in days_order}


def add_class(day, subject, start_time, end_time, class_type):
    entry = (subject, start_time, end_time, class_type)
    timetable[day].append(entry)
    print(f"Added: {subject} on {day} ({start_time}-{end_time}, {class_type})")


def check_clashes():
    clash_found = False
    for day in days_order:
        classes = timetable[day]
        n = len(classes)
        for i in range(n):
            for j in range(i + 1, n):
                if classes[i][1] == classes[j][1]:  # same start_time
                    print(f"Clash on {day}: '{classes[i][0]}' and "
                          f"'{classes[j][0]}' both at {classes[i][1]}")
                    clash_found = True
    if not clash_found:
        print("No clashes found. Timetable is clean.")


def remove_duplicate_entries():
    for day in days_order:
        unique_classes = []
        for entry in timetable[day]:
            if entry not in unique_classes:
                unique_classes.append(entry)
        removed = len(timetable[day]) - len(unique_classes)
        timetable[day] = unique_classes
        if removed > 0:
            print(f"Removed {removed} duplicate entr(y/ies) from {day}")
    print("Duplicate check complete.")


def periods_per_day():
    counts = {}
    for day in days_order:
        counts[day] = len(timetable[day])
    return counts


def busiest_day():
    counts = periods_per_day()
    max_day = days_order[0]
    max_count = counts[max_day]
    for day in days_order:
        if counts[day] > max_count:
            max_count = counts[day]
            max_day = day
    print(f"Busiest day: {max_day} with {max_count} period(s)")



def kth_least_busy_day(k):
    counts = periods_per_day()
    day_count_list = list(counts.items())

    n = len(day_count_list)
    for i in range(n):
        for j in range(n - i - 1):
            if day_count_list[j][1] > day_count_list[j + 1][1]:
                day_count_list[j], day_count_list[j + 1] = \
                    day_count_list[j + 1], day_count_list[j]  # Module 3: Exchange

    if 1 <= k <= n:
        day, count = day_count_list[k - 1]
        print(f"{k}th least busy day: {day} with {count} period(s)")
    else:
        print("Invalid value of k")


def subject_wise_count():
    subject_count = {}
    for day in days_order:
        for entry in timetable[day]:
            subject = entry[0]
            if subject in subject_count:
                subject_count[subject] += 1
            else:
                subject_count[subject] = 1

    print("Subject-wise weekly class count:")
    for subject, count in subject_count.items():
        print(f"  {subject}: {count} class(es) per week")


def swap_periods(day1, index1, day2, index2):
    try:
        temp = timetable[day1][index1]
        timetable[day1][index1] = timetable[day2][index2]
        timetable[day2][index2] = temp
        print(f"Swapped period {index1 + 1} of {day1} with "
              f"period {index2 + 1} of {day2}")
    except IndexError:
        print("Invalid period index given. Swap failed.")


def view_timetable(reverse=False):
    display_days = days_order[::-1] if reverse else days_order
    for day in display_days:
        print(f"\n{day}:")
        if not timetable[day]:
            print("  No classes scheduled")
        else:
            for entry in timetable[day]:
                subject, start, end, class_type = entry
                print(f"  {start}-{end}  {subject}  ({class_type})")


def partition_theory_lab(day):
    theory_classes = []
    lab_classes = []
    for entry in timetable[day]:
        if entry[3] == "Theory":
            theory_classes.append(entry)
        else:
            lab_classes.append(entry)

    print(f"\nTheory classes on {day}:")
    for entry in theory_classes:
        print(f"  {entry[0]} at {entry[1]}")

    print(f"Lab classes on {day}:")
    for entry in lab_classes:
        print(f"  {entry[0]} at {entry[1]}")



def run_verification():
    print("Running basic verification checks...")
    total_before = sum(len(timetable[d]) for d in days_order)
    remove_duplicate_entries()
    total_after = sum(len(timetable[d]) for d in days_order)
    if total_after <= total_before:
        print("Verification passed: duplicate removal did not increase entries.")
    else:
        print("Verification failed: unexpected increase in entries.")



def main():
    while True:
        print("\n------ Student Timetable Management System ------")
        print("1. Add a class")
        print("2. View timetable")
        print("3. View timetable (reverse day order)")
        print("4. Check for clashes")
        print("5. Remove duplicate entries")
        print("6. Show busiest day")
        print("7. Show subject-wise class count")
        print("8. Swap two periods")
        print("9. Partition a day into Theory and Lab classes")
        print("10. Find Kth least busy day")
        print("11. Run verification checks")
        print("12. Exit")

        choice = input("Enter your choice (1-12): ")

        if choice == "1":
            day = input("Enter day (e.g., Monday): ")
            subject = input("Enter subject: ")
            start_time = input("Enter start time (e.g., 09:00): ")
            end_time = input("Enter end time (e.g., 10:00): ")
            class_type = input("Enter class type (Theory/Lab): ")
            if day in timetable:
                add_class(day, subject, start_time, end_time, class_type)
            else:
                print("Invalid day entered.")

        elif choice == "2":
            view_timetable(reverse=False)

        elif choice == "3":
            view_timetable(reverse=True)

        elif choice == "4":
            check_clashes()

        elif choice == "5":
            remove_duplicate_entries()

        elif choice == "6":
            busiest_day()

        elif choice == "7":
            subject_wise_count()

        elif choice == "8":
            day1 = input("Enter first day: ")
            index1 = int(input("Enter period number on first day: ")) - 1
            day2 = input("Enter second day: ")
            index2 = int(input("Enter period number on second day: ")) - 1
            if day1 in timetable and day2 in timetable:
                swap_periods(day1, index1, day2, index2)
            else:
                print("Invalid day entered.")

        elif choice == "9":
            day = input("Enter day to partition: ")
            if day in timetable:
                partition_theory_lab(day)
            else:
                print("Invalid day entered.")

        elif choice == "10":
            k = int(input("Enter value of k: "))
            kth_least_busy_day(k)

        elif choice == "11":
            run_verification()

        elif choice == "12":
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 12.")


if __name__ == "__main__":
    main()