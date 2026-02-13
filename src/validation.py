def validate_data(df):

    print("\n🔍 Starting Data Validation Checks...\n")

    issues = []

    # 1️⃣ Null Values
    null_values = df.drop(columns=["profit_margin_adjusted"]).isnull().sum()


    if null_values.sum() > 0:
        issues.append("Null values found")

    # 2️⃣ Duplicate Rows
    duplicate_rows = df.duplicated().sum()
    print("duplicate_rows :", duplicate_rows)

    if duplicate_rows > 0:
        issues.append("Duplicate rows found")

    # 3️⃣ Negative Sales
    negative_sales = (df["sales"] < 0).sum()
    print("negative_sales_rows :", negative_sales)

    if negative_sales > 0:
        issues.append("Negative sales found")

    # 4️⃣ Negative Shipping Days
    negative_shipping = (df["shipping_days"] < 0).sum()
    print("negative_shipping_days :", negative_shipping)

    if negative_shipping > 0:
        issues.append("Negative shipping days found")

    # 5️⃣ Invalid Discount (>100%)
    invalid_discount = (df["discount"] > 1).sum()
    print("invalid_discount_rows :", invalid_discount)

    if invalid_discount > 0:
        issues.append("Invalid discount values found")

    # 6️⃣ Extreme Profit Margin (>200% or < -200%)
    extreme_profit = (
    (df["profit_margin_raw"] > 200) |
    (df["profit_margin_raw"] < -200)
).sum()
    print("extreme_profit_margin_rows :", extreme_profit)

    # 7️⃣ Invalid Date Check
    invalid_dates = df["order_date"].isnull().sum()
    print("invalid_date_rows :", invalid_dates)

    if invalid_dates > 0:
        issues.append("Invalid dates found")

    print("\n✅ Data Validation Completed\n")

    # Final Validation Status
    if len(issues) > 0:
        return {
            "status": "failed",
            "issues": issues
        }
    else:
        return {
            "status": "passed",
            "issues": []
        }
