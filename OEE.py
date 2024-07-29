import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Define OEE function
def oee(A, B, C, D, E, F):
    if B <= A and D <= C and E == D and F <= E:
        Profits = [100]
        Profits.append(B/A*100)
        Profits.append(B/A*100)
        Profits.append(D/C*Profits[2])
        Profits.append(D/C*Profits[2])
        Profits.append(F/E*Profits[4])

        Loss = [0]
        Loss.append(Profits[0]-Profits[1])
        Loss.append(Profits[1]-Profits[2])
        Loss.append(Profits[2]-Profits[3])
        Loss.append(Profits[3]-Profits[4])

        ind = [0, 1, 2, 3, 4, 5]
        width = 0.85
        
        plt.figure(figsize=(20, 10))
        plt.barh(ind, Profits, width, color='#03C03C')
        plt.barh(ind, Loss, width, left=Profits, color='red')
        plt.axvline(85, linestyle='dashed', color='black', label='World Class OEE')
        plt.axvline(60, linestyle='dashdot', color='black', label='Typical OEE')
        plt.axvline(40, linestyle='dotted', color='black', label='Low OEE')
        plt.gca().invert_yaxis()
        plt.yticks([])
        plt.text(0, 0, 'Total Available Time', horizontalalignment='left')
        plt.text(0, 1, 'Run Time', horizontalalignment='left')
        plt.text(Profits[1], 1, 'Time Losses', horizontalalignment='left')
        plt.text(0, 2, 'Production Capacity', horizontalalignment='left')
        plt.text(0, 3, 'Actual Production', horizontalalignment='left')
        plt.text(Profits[3], 3, 'Speed Losses', horizontalalignment='left')
        plt.text(0, 4, 'Product Output', horizontalalignment='left')
        plt.text(0, 5, 'Actual Good Products', horizontalalignment='left')
        plt.text(Profits[5], 5, 'Defective Units', horizontalalignment='left')
        plt.xlabel('Percentage')
        plt.title('Overall Equipment Efficiency')
        plt.legend()

        return round(Profits[-1], 2)
    else:
        if B > A:
            return 'Error: The run time cannot be greater than the total available time.'
        if D > C:
            return 'Error: The actual production cannot be greater than the production capacity.'
        if E != D:
            return 'Error: The product output must be equal to actual production.'
        if F > E:
            return 'Error: The actual good products cannot be greater than the product output.'

# Streamlit interface
st.title("Overall Equipment Effectiveness (OEE) Calculator")

# Input fields
A = st.number_input("Total Available Time", min_value=0)
B = st.number_input("Run Time", min_value=0)
C = st.number_input("Production Capacity", min_value=0)
D = st.number_input("Actual Production", min_value=0)
E = st.number_input("Product Output", min_value=0)
F = st.number_input("Actual Good Products", min_value=0)

# Calculate and display results
result = oee(A, B, C, D, E, F)
st.write(f"Overall Equipment Effectiveness: {result}%")

# Plot OEE chart
if isinstance(result, float):
    fig, ax = plt.subplots()
    ind = [0, 1, 2, 3, 4, 5]
    Profits = [100]
    Profits.append(B/A*100)
    Profits.append(B/A*100)
    Profits.append(D/C*Profits[2])
    Profits.append(D/C*Profits[2])
    Profits.append(F/E*Profits[4])
    Loss = [0]
    Loss.append(Profits[0]-Profits[1])
    Loss.append(Profits[1]-Profits[2])
    Loss.append(Profits[2]-Profits[3])
    Loss.append(Profits[3]-Profits[4])
    width = 0.85
    
    ax.barh(ind, Profits, width, color='#03C03C')
    ax.barh(ind, Loss, width, left=Profits, color='red')
    ax.axvline(85, linestyle='dashed', color='black', label='World Class OEE')
    ax.axvline(60, linestyle='dashdot', color='black', label='Typical OEE')
    ax.axvline(40, linestyle='dotted', color='black', label='Low OEE')
    ax.invert_yaxis()
    ax.yaxis.set_visible(False)
    ax.text(0, 0, 'Total Available Time', horizontalalignment='left')
    ax.text(0, 1, 'Run Time', horizontalalignment='left')
    ax.text(Profits[1], 1, 'Time Losses', horizontalalignment='left')
    ax.text(0, 2, 'Production Capacity', horizontalalignment='left')
    ax.text(0, 3, 'Actual Production', horizontalalignment='left')
    ax.text(Profits[3], 3, 'Speed Losses', horizontalalignment='left')
    ax.text(0, 4, 'Product Output', horizontalalignment='left')
    ax.text(0, 5, 'Actual Good Products', horizontalalignment='left')
    ax.text(Profits[5], 5, 'Defective Units', horizontalalignment='left')
    ax.set_xlabel('Percentage')
    ax.set_title('Overall Equipment Efficiency')
    ax.legend()
    
    st.pyplot(fig)
else:
    st.write(result)
