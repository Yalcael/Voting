candidate1 = input("Enter the name of the first candidate: ")
candidate2 = input("Enter the name of the second candidate: ")

candidate1_votes = 0
candidate2_votes = 0

voter_id = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
number_of_voters = len(voter_id)

while True:
    if not voter_id:
        print("Voting is complete")
        if candidate1_votes > candidate2_votes:
            percentage = (candidate1_votes / number_of_voters) * 100
            print(f"{candidate1} has won the election with {percentage}% of votes")
        elif candidate2_votes > candidate1_votes:
            percentage = (candidate2_votes / number_of_voters) * 100
            print(f"{candidate2} has won the election with {percentage}% of votes")
        else:
            print("Equality !")
        break

    voter = int(input("Enter your voter ID: "))
    if voter in voter_id:
        print("You can vote")
        voter_id.remove(voter)
        print("To vote for candidate1, press 1")
        print("To vote for candidate2, press 2")

        vote = int(input("Enter your vote: "))
        if vote == 1:
            candidate1_votes += 1
            print("Thank you for voting candidate 1.")
        elif vote == 2:
            candidate2_votes += 1
            print("Thank you for voting candidate 2.")
        else:
            print("Invalid vote. Please try again with 1 or 2.")
    else:
        print("You have already voted or your voter ID is invalid. Please try again.")
