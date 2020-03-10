#import dependencies
import csv
fileToLoad="electionData.csv"
fileToOutput="electionAnalysis.txt"
#1 Total number of votes
totalVotes=0
candidateOptions=[]
candidateVotes={}
winningCandidate=""
winningCount=0
with open(fileToLoad) as electionData
    reader=csv.DictReader(electionData)
    for row in reader:
        totalVotes=totalVotes+1
        candidateName=row["Candidate"]
#2 List of candidates who recieved votes
        #Add Candidate if the name is not already in the dictionary
        if candidateName not in candidateOptions:
            candidateOptions.append(candidateName)
            candidateVotes[candidateName]=0
        candidateVotes[candidateName]=candidateVotes[candidateName]+1
#4 Number of votes for each candidate
with open(fileToOutput,"w") as txtFile:
    electionResults=(
    f"\nElection Results\n"
    f"-----------------------\n"
    f"Total Votes:{total_votes}\n"
    )
    print(electionResults)
    txtFile.write(electionResults)
#3 Percentage of votes for each candidate
    for candidate in candidateVotes:
        votes=candidateVotes.get(candidate)
        votePercentage=float(votes) / float(totalVotes) * 100
#5 Winner of the election by popular vote
        if(votes>winningCount):
            winningCount=votes
            winningCandidate=candidate
        voterOutput= f"{candidate}: {votePercentage:.3f}% ({votes})\n"
        print(voterOutput)
        txtFile.write(voterOutput)
    winningCandidateSummary =(
        f"-----------------------\n"
        f"Winner:{winningCandidate}"
    )
    print(winningCandidateSummary)
    txtFile.write(winningCandidateSummary)
