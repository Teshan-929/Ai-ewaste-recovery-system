import sqlite3
from decision_engine import calculate_net_value, make_decision


# Connect to database
connection = sqlite3.connect("ewaste.db")
cursor = connection.cursor()


# Get all components from database
cursor.execute("""
SELECT
    id,
    manufacturer,
    part_number,
    component_type,
    estimated_resale_value,
    scrap_value,
    extraction_cost,
    testing_cost,
    shipping_cost
FROM components
""")

components = cursor.fetchall()


print("==========================================")
print("       E-WASTE RECOVERY SYSTEM")
print("==========================================")


total_recovery_value = 0


# Process each component
for component in components:

    (
        component_id,
        manufacturer,
        part_number,
        component_type,
        estimated_resale_value,
        scrap_value,
        extraction_cost,
        testing_cost,
        shipping_cost
    ) = component

    # Calculate net recovery value
    net_value = calculate_net_value(
        estimated_resale_value,
        extraction_cost,
        testing_cost,
        shipping_cost
    )

    # Make recovery decision
    decision = make_decision(
        net_value,
        scrap_value
    )

    print("------------------------------------------")
    print("Component ID:", component_id)
    print("Manufacturer:", manufacturer)
    print("Part Number:", part_number)
    print("Component Type:", component_type)
    print("Estimated Resale Value: $", estimated_resale_value)
    print("Scrap Value: $", scrap_value)
    print("Extraction Cost: $", extraction_cost)
    print("Testing Cost: $", testing_cost)
    print("Shipping Cost: $", shipping_cost)
    print("Net Recovery Value: $", net_value)
    print("Decision:", decision)

    # Add recoverable value to total
    if decision == "RECOVER":
        total_recovery_value += net_value


print("------------------------------------------")
print("Total Recovery Value: $", total_recovery_value)
print("==========================================")

connection.close()