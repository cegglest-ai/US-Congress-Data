import pandas as pd
import matplotlib.pyplot as plt

def main():
    # Load the data
    df = pd.read_csv('data_aging_congress.csv')
    
    # We want to count unique congress people, so we drop duplicate bioguide_ids
    unique_members = df.drop_duplicates(subset=['bioguide_id'])
    
    # Count the number of people in each generation
    generation_counts = unique_members['generation'].value_counts()
    
    # Create the bar graph
    plt.figure(figsize=(10, 6))
    generation_counts.plot(kind='bar', color='skyblue', edgecolor='black')
    
    # Add title and labels
    plt.title('Number of Unique Congress Members per Generation')
    plt.xlabel('Generation')
    plt.ylabel('Number of Members')
    plt.xticks(rotation=45, ha='right')
    
    # Adding grid for y axis
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    
    # Save the plot
    plt.tight_layout()
    plt.savefig('generation_counts.png')
    print("Plot saved to 'generation_counts.png'")
    
    # Show the plot
    plt.show()

if __name__ == "__main__":
    main()
