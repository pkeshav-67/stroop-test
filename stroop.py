import random
import time
import matplotlib.pyplot as plt

colors = ["BLUE", "YELLOW", "RED", "GREEN"]
codes = {"BLUE": 34, "YELLOW": 33, "RED": 31, "GREEN": 32}
results = []
print("Welcome to the Stroop Effect Test!")
print("You will be shown a color word in a certain ink color.")
print("Your task is to type the color of the ink, not the word itself.")
print("Use the following keys for colors: r = RED, y = YELLOW, g = GREEN, b = BLUE")
print("Press Enter to start...")
input()
plan = [True] * 10 + [False] * 10
random.shuffle(plan)
for congruent in plan:
    word = random.choice(colors)
    if congruent: ink_name = word
    else:
        ink_name = random.choice(colors)
        while ink_name == word:
            ink_name = random.choice(colors)
    ink = codes[ink_name]
    print(f"\033[{ink}m{word}\033[0m")
    start = time.perf_counter()
    answer = input("Type the color (r, y, g, b): ").strip().lower()
    end = time.perf_counter()
    x = end - start
    correct = ink_name[0].lower()
    if answer == correct or answer == ink_name.lower():
        print(f"Correct! {x:.2f} seconds")
        status = "Correct"
    else:
        print("WRONG")
        status = "Wrong"
    if congruent:
        results.append({"congruent": True, "correct": status == "Correct", "RT": x})
    else:
        results.append({"congruent": False, "correct": status == "Correct", "RT": x})
fast = []
slow = []

for result in results:
    if result["congruent"]:
        if result["correct"]:
            fast.append(result["RT"])

    else:
        if result["correct"]:
            slow.append(result["RT"])
fast_mean = sum(fast)/len(fast) if fast else 0
slow_mean = sum(slow)/len(slow) if slow else 0
if fast:
    print(f"Average RT for congruent: {fast_mean:.2f} seconds. ({len(fast)} correct out of 10)")
if slow:
    print(f"Average RT for incongruent: {slow_mean:.2f} seconds. ({len(slow)} correct out of 10)")
print("Stroop effect:", (slow_mean - fast_mean) if fast and slow else "N/A")

plt.bar(["Congruent", "Incongruent"], [fast_mean, slow_mean], color=["blue", "red"])
plt.ylabel("Reaction Time (seconds)")
plt.title("Stroop Effect Test Results")
plt.savefig("stroop_results.png")