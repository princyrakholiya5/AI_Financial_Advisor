import matplotlib.pyplot as plt

def create_chart(expenses, savings):

    labels = ["Expenses", "Savings"]
    values = [expenses, savings]

    fig, ax = plt.subplots()

    ax.pie(values, labels=labels, autopct="%1.1f%%")

    ax.set_title("Financial Distribution")

    return fig