import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Smart Rent Calculator",
    page_icon="🏠",
    layout="centered"
)
# Sidebar
st.sidebar.title("🏠 About Project")

st.sidebar.success("✅ Python Mini Project")

st.sidebar.info(
    """
    This Smart Rent Calculator helps roommates split:
    
    ✔️ Flat Rent
    
    ✔️ Food Expenses
    
    ✔️ Electricity Bill
    
    equally among all members.
    """
)

st.sidebar.subheader("🛠️ Technologies Used")

st.sidebar.write("• Python")
st.sidebar.write("• Streamlit")

#st.sidebar.subheader("👩‍💻 Developed By")

#st.sidebar.write("Mansi")


# Title
st.title("🏠 Smart Rent Calculator")
st.markdown("### Calculate rent easily for roommates or flatmates")

st.divider()

# Inputs
rent = st.number_input("🏡 Enter Total Room/Flat Rent", min_value=0)

food = st.number_input("🍕 Enter Food Ordered Amount", min_value=0)

electricity_spend = st.number_input("⚡ Enter Total Electricity Units", min_value=0)

charge_per_unit = st.number_input("💡 Enter Charge Per Unit", min_value=0)

persons = st.number_input("👨‍👩‍👧 Number of Persons Living", min_value=1)

st.divider()

# Button
if st.button("Calculate Rent"):

    total_bill = electricity_spend * charge_per_unit

    total_amount = food + rent + total_bill

    per_person = total_amount / persons

    st.success(f"💰 Each person should pay ₹ {per_person:.2f}")


    #create tabel 
    import pandas as pd

    data = {
        "Category": ["Rent", "Food", "Electricity"],
        "Amount": [rent, food, total_bill]
    }

    df = pd.DataFrame(data)

    st.dataframe(df)


#chart
   # st.bar_chart(df.set_index("Category"))

    import matplotlib.pyplot as plt
    fig, ax = plt.subplots()
    ax.bar(df["Category"], df["Amount"])
    ax.set_xlabel("Expense Category")
    ax.set_ylabel("Amount")
    st.pyplot(fig)
    


    highest = df.loc[df["Amount"].idxmax()]
    st.warning(
    f"📊 Highest expense is {highest['Category']} costing ₹ {highest['Amount']}"
)


    # Extra Information
    st.info(f"""
    🏠 Rent = ₹ {rent}
    
    🍕 Food Cost = ₹ {food}
    
    ⚡ Electricity Bill = ₹ {total_bill}
    
    👥 Total Persons = {persons}
    """)

    st.markdown("---")
st.caption("Created with using Python and Streamlit")