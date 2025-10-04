import matplotlib.pyplot as plt

def show(data_for_viz_first, data_for_viz_second):

    plt.figure(figsize=(12, 6))
    bars = plt.bar(data_for_viz_first['Country'], data_for_viz_first['Population'], color='lightblue', edgecolor='navy', alpha=0.7, width=0.5)

    plt.title('Население стран', fontsize=16, fontweight='bold')
    plt.xlabel('Страны', fontsize=12)
    plt.ylabel('Население', fontsize=12)
    plt.xticks(rotation=45)
    plt.grid(axis='y', alpha=0.3)

    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2., height, f'{height:,}'.replace(',', ''), ha='center', va='bottom', fontsize=9)

    plt.tight_layout()
    plt.show()

    change = data_for_viz_second['Births'] - data_for_viz_second['Deaths']

    plt.figure(figsize=(12, 6))
    bars = plt.bar(data_for_viz_first['Country'], change, color='lightblue', edgecolor='navy', alpha=0.7, width=0.5)

    plt.title('Население стран', fontsize=16, fontweight='bold')
    plt.xlabel('Страны', fontsize=12)
    plt.ylabel('Рост', fontsize=12)
    plt.xticks(rotation=45)
    plt.grid(axis='y', alpha=0.3)

    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2., height, f'{height:,}'.replace(',', ''), ha='center', va='bottom', fontsize=9)

    plt.tight_layout()
    plt.show()
