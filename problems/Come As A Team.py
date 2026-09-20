"""Come As A Team"""

def main():
    """Main Function"""
    total = 0
    team, member = map(int, input().split())

    if 1 <= team <= 10 and 1 <= member <= 20:
        for i in range(team):
            score = list(map(int, input().split()))
            total += sum(score)
            print(f"Team {i + 1}: Average = {sum(score) / member:.2f}, Max = {max(score)}")

        print(f"Total Score of All Teams = {total}")
    else:
        print("Data Incorrect")

main()
