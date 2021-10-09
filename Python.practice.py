#List of counties
counties=["Arapahoe", "Denver", "Jefferson"]
#Test output to see list of counties
print(counties)
#Create dictionary for counties with county as key and voters as value
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
#Create a list of dictionaries where keys are county and registered voters and each county are values
voting_data = [{"county":"Arapahoe", "registered_voters": 422829}, {"county":"Denver", "registered_voters": 463353}, {"county":"Jefferson", "registered_voters": 432438}]
#Test output
print(voting_data)
print(counties_dict)

with open(file_to_load) as election_data:
#To do: Read and analyze data here.
# Read the file object with the reader function.
    file_reader = csv.reader(election_data)
#The total number of votes cast.
#A complete list of candidates who recevied votes.
#The percentage of votes each candidate won. 
#The total number of votes each candiate won.
#The winner of the election based on the popular vote.
    # Print the file object.
    print(election_data)

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:
    # Write some data to the file.
    txt_file.write("Counties in the Election\n-------------------------\nArapahoe\nDenver\nJefferson")

# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Print each row in the CSV file.
for row in file_reader:
    print(row)