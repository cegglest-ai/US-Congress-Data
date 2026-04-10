import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    # Load the data
    df = pd.read_csv('data_aging_congress.csv')
    
    # Filter for the two main political parties: 100 (Democrat) and 200 (Republican)
    main_parties_df = df[df['party_code'].isin([100, 200])].copy()
    
    # Map party codes to human-readable names
    main_parties_df['party'] = main_parties_df['party_code'].map({100: 'Democrat', 200: 'Republican'})
    
    # Create the dot plot (stripplot)
    plt.figure(figsize=(10, 6))
    
    # Using seaborn stripplot for a clean distribution dot plot
    # alpha=0.3 adds transparency to deal with overplotting (many dots)
    # jitter=True spreads the dots horizontally to see the density
    sns.stripplot(
        data=main_parties_df,
        x='party',
        y='age_years',
        hue='party',
        palette={'Democrat': 'blue', 'Republican': 'red'},
        alpha=0.3,
        jitter=True,
        size=3,
        legend=False
    )
    
    # Add title and labels
    plt.title('Age Distribution in Congress by Political Party')
    plt.xlabel('Political Party')
    plt.ylabel('Age (Years)')
    
    # Adding grid for y axis
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    
    # Save the plot
    plt.tight_layout()
    plt.savefig('age_distribution_parties.png')
    print("Plot saved to 'age_distribution_parties.png'")
    
    # Show the plot
    plt.show()

if __name__ == "__main__":
    main()
