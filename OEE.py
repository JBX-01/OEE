import streamlit as st
import matplotlib.pyplot as plt

# Define OEE function
def oee(A, B, C, D, E, F):
    # Check for zero values and other edge cases
    if A == 0:
        return 'Error: Total Available Time cannot be zero.'
    if C == 0:
        return 'Error: Production Capacity cannot be zero.'
    if E == 0:
        return 'Error: Product Output cannot be zero.'
    if B > A:
        return 'Error: The run time cannot be greater than the total available time.'
    if D > C:
        return 'Error: The actual production cannot be greater than the production capacity.'
    if E != D:
        return 'Error: The product output must be equal to actual production.'
    if F > E:
        return 'Error: The actual good products cannot be greater than the product output.'

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
    Loss.append(Profits[4]-Profits[5])

    ind = [0, 1, 2, 3, 4, 5]
    width = 0.85
    
    fig, ax = plt.subplots(figsize=(20, 10))
    
    # Plot profits bars
    ax.barh(ind, Profits, width, color='#03C03C', label='Profits')
    
    # Plot losses bars
    ax.barh(ind, Loss, width, left=Profits, color='red', label='Losses')
    
    # Plot OEE universal benchmarks
    ax.axvline(85, linestyle='dashed', color='black', label='World Class OEE')
    ax.axvline(60, linestyle='dashdot', color='black', label='Typical OEE')
    ax.axvline(40, linestyle='dotted', color='black', label='Low OEE')
    
    # Invert y-axis
    ax.invert_yaxis()
    
    # Hide y-axis labels
    ax.yaxis.set_visible(False)
    
    # Add OEE components
    ax.text(0, 0, 'Total Available Time', horizontalalignment='left')
    ax.text(0, 1, 'Run Time', horizontalalignment='left')
    ax.text(Profits[1], 1, 'Time Losses', horizontalalignment='left')
    ax.text(0, 2, 'Production Capacity', horizontalalignment='left')
    ax.text(0, 3, 'Actual Production', horizontalalignment='left')
    ax.text(Profits[3], 3, 'Speed Losses', horizontalalignment='left')
    ax.text(0, 4, 'Product Output', horizontalalignment='left')
    ax.text(0, 5, 'Actual Good Products', horizontalalignment='left')
    ax.text(Profits[5], 5, 'Defective Units', horizontalalignment='left')

    # Add x-axis label
    ax.set_xlabel('Percentage')
    
    # Add plot title
    ax.set_title('Overall Equipment Efficiency')
    
    # Show plot legends
    ax.legend()

    # Return OEE value
    return round(Profits[-1], 2)

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
if isinstance(result, str):
    st.error(result)
else:
    st.write(f"Overall Equipment Effectiveness: {result}%")
    
    # Plot OEE chart
    st.pyplot(plt.gcf())
