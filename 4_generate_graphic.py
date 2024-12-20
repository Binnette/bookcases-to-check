import matplotlib.pyplot as plt
import pandas as pd

# Constants for file paths
HISTORY_FILE = 'assets/bookcase_count_history.csv'
GRAPHIC_FILE = 'assets/bookcase_count_history.png'
PIE_CHART_FILE = 'assets/bookcase_distribution_pie_chart.png'

# Short names for regions
region_short_names = {
    'Île-de-France': 'IDF',
    'Nouvelle-Aquitaine': 'NA',
    'Auvergne-Rhône-Alpes': 'ARA',
    'Occitanie': 'OCC',
    'Grand Est': 'GE',
    'Hauts-de-France': 'HDF',
    'Pays de la Loire': 'PDL',
    'Bretagne': 'BRT',
    'Bourgogne-Franche-Comté': 'BFC',
    'Normandie': 'NMD',
    'Centre-Val de Loire': 'CVL',
    'Provence-Alpes-Côte d\'Azur': 'PACA',
    'Corse': 'CRS'
}

def generate_graphic():
    # Read the CSV file into a DataFrame
    df = pd.read_csv(HISTORY_FILE)
    
    # Convert the Date column to datetime
    df['date'] = pd.to_datetime(df['date'])

    # Plot the data over time
    plt.figure(figsize=(10, 6))
    plt.plot(df['date'], df['total'], marker='o', linestyle='-')
    plt.title('Number of Bookcases Extracted Over Time', fontsize=16)
    plt.xlabel('Date', fontsize=14)
    plt.ylabel('Number of Bookcases', fontsize=14)
    plt.grid(True)
    plt.xticks(rotation=45, fontsize=12)
    plt.yticks(fontsize=12)
    plt.tight_layout()
    plt.savefig(GRAPHIC_FILE)
    plt.close()

    # Generate a pie chart for the last row of the CSV
    last_row = df.iloc[-1]
    labels = df.columns[3:]  # Skip the first three columns: date, total, out_of_region
    sizes = last_row[labels]

    # Sort labels and sizes by the number of bookcases
    sorted_labels_sizes = sorted(zip(labels, sizes), key=lambda x: x[1], reverse=True)
    sorted_labels, sorted_sizes = zip(*sorted_labels_sizes)

    def make_autopct(values):
        def my_autopct(pct, index):
            total = sum(values)
            short_name = region_short_names[sorted_labels[index]]
            return f"{short_name}\n{pct:.1f}%"
        return my_autopct

    fig, ax = plt.subplots(figsize=(12, 8))
    wedges, texts, autotexts = ax.pie(
        sorted_sizes,
        autopct=lambda pct: make_autopct(sorted_sizes)(
            pct, sorted_sizes.index(int(round(pct * sum(sorted_sizes) / 100.0)))
        ),
        startangle=140,
        colors=plt.cm.Paired.colors,
        textprops={'fontsize': 12},
        pctdistance=0.9  # Set the text distance to 75%
    )

    # Create legend with sorted labels and sizes without short names
    legend_labels = [f"{label} - {size} ({round(size / sum(sorted_sizes) * 100, 1)}%)" for label, size in zip(sorted_labels, sorted_sizes)]
    ax.legend(wedges, legend_labels, title=f"Total: {last_row['total']}", loc="center left", bbox_to_anchor=(1, 0.5), fontsize='large')

    plt.title(f'Bookcase Distribution by Region on {last_row["date"].date()}', fontsize=16)
    plt.axis('equal')  # Equal aspect ratio ensures that pie chart is drawn as a circle.
    plt.subplots_adjust(left=0.1, right=0.75, top=0.9, bottom=0.1)  # Adjust layout to minimize white space
    plt.savefig(PIE_CHART_FILE, bbox_inches="tight")
    plt.close()

if __name__ == "__main__":
    generate_graphic()
