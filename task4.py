import pandas as pd
import matplotlib.pyplot as plt
import calendar

def main():
    # Load the data
    df = pd.read_csv('data_aging_congress.csv')
    
    # Drop duplicate congressmen to get unique people
    unique_members = df.drop_duplicates(subset=['bioguide_id']).copy()
    
    # Convert the birthday column to datetime so it's easy to extract the month
    unique_members['birthday'] = pd.to_datetime(unique_members['birthday'], errors='coerce')
    
    # Extract the month as an integer (1 to 12)
    unique_members['birth_month'] = unique_members['birthday'].dt.month
    
    # Remove any missing birthday entries just in case
    unique_members = unique_members.dropna(subset=['birth_month'])
    
    # Count people born in each month and sort by month index
    month_counts = unique_members['birth_month'].value_counts().sort_index()
    
    # Map the integers back into full month strings
    month_labels = [calendar.month_name[int(m)] for m in month_counts.index]
    
    # Create the pie chart
    plt.figure(figsize=(10, 8))
    
    colors = plt.cm.Pastel1.colors + plt.cm.Pastel2.colors
    
    plt.pie(
        month_counts,
        labels=month_labels,
        autopct='%1.1f%%',
        startangle=90,
        colors=colors,
        wedgeprops={'edgecolor': 'white'}
    )
    
    # Equal aspect ratio ensures that pie is drawn as a circle
    plt.axis('equal')
    plt.title('Birth Months of U.S. Congress Members')
    
    # Save the plot
    plt.tight_layout()
    plt.savefig('birth_month_distribution.png')
    print("Plot saved to 'birth_month_distribution.png'")
    
    # Show the plot
    plt.show()

if __name__ == "__main__":
    main()
