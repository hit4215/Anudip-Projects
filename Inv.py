import streamlit as st

# -----------------------------
# Dictionary to Store Inventory
# -----------------------------
if "inventory" not in st.session_state:
    st.session_state.inventory = {}

inventory = st.session_state.inventory

st.set_page_config(page_title="Inventory Management System", page_icon="📦")

st.title("📦 Inventory Management System")

menu = st.sidebar.selectbox(
    "Select Operation",
    [
        "Add Product",
        "View Products",
        "Search Product",
        "Update Product",
        "Delete Product"
    ]
)

# -----------------------------
# Add Product
# -----------------------------
if menu == "Add Product":

    st.header("➕ Add Product")

    product_id = st.text_input("Product ID")
    name = st.text_input("Product Name")
    quantity = st.number_input("Quantity", min_value=0, step=1)
    price = st.number_input("Price", min_value=0.0)

    if st.button("Add Product"):

        if product_id in inventory:
            st.error("Product ID already exists!")

        elif product_id == "" or name == "":
            st.warning("Please fill all fields.")

        else:
            inventory[product_id] = {
                "Name": name,
                "Quantity": quantity,
                "Price": price
            }

            st.success("Product Added Successfully!")

# -----------------------------
# View Products
# -----------------------------
elif menu == "View Products":

    st.header("📋 Product List")

    if inventory:

        for pid, details in inventory.items():

            st.write(f"### {details['Name']}")
            st.write(f"**Product ID:** {pid}")
            st.write(f"**Quantity:** {details['Quantity']}")
            st.write(f"**Price:** ₹{details['Price']}")
            st.divider()

    else:
        st.info("Inventory is Empty.")

# -----------------------------
# Search Product
# -----------------------------
elif menu == "Search Product":

    st.header("🔍 Search Product")

    product_id = st.text_input("Enter Product ID")

    if st.button("Search"):

        if product_id in inventory:

            product = inventory[product_id]

            st.success("Product Found")

            st.write("### Product Details")
            st.write("Name:", product["Name"])
            st.write("Quantity:", product["Quantity"])
            st.write("Price: ₹", product["Price"])

        else:
            st.error("Product Not Found!")

# -----------------------------
# Update Product
# -----------------------------
elif menu == "Update Product":

    st.header("✏ Update Product")

    product_id = st.text_input("Product ID")

    if product_id in inventory:

        product = inventory[product_id]

        name = st.text_input("Product Name", value=product["Name"])
        quantity = st.number_input(
            "Quantity",
            value=product["Quantity"],
            min_value=0
        )

        price = st.number_input(
            "Price",
            value=float(product["Price"]),
            min_value=0.0
        )

        if st.button("Update"):

            inventory[product_id] = {
                "Name": name,
                "Quantity": quantity,
                "Price": price
            }

            st.success("Product Updated Successfully!")

    elif product_id != "":
        st.error("Product Not Found!")

# -----------------------------
# Delete Product
# -----------------------------
elif menu == "Delete Product":

    st.header("🗑 Delete Product")

    product_id = st.text_input("Product ID")

    if st.button("Delete"):

        if product_id in inventory:

            del inventory[product_id]

            st.success("Product Deleted Successfully!")

        else:
            st.error("Product Not Found!")