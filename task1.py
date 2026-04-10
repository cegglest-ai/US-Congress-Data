import pandas as pd
import matplotlib.pyplot as plt

def main():
    # Load the data
    df = pd.read_csv('data_aging_congress.csv')
    
    # Calculate the average age for each Congress
    avg_age_per_congress = df.groupby('congress')['age_years'].mean().reset_index()
    
    # Create the line graph
    plt.figure(figsize=(10, 6))
    plt.plot(avg_age_per_congress['congress'], avg_age_per_congress['age_years'], marker='o', linestyle='-')
    
    # Add title and labels
    plt.title('Average Age of the U.S. Congress Over Time')
    plt.xlabel('Congress Number')
    plt.ylabel('Average Age (Years)')
    plt.grid(True)
    
    # Save the plot
    plt.tight_layout()
    plt.savefig('average_age_congress.png')
    
    # Show the plot
    plt.show()

if __name__ == "__main__":
    main()
