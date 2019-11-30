def display_all_data(train, items, item_categories, shops, test):
	# all data at once
	start = '\033[1m'
	end = '\033[0m'
	print()
	print(start + "Train" + end)
	print(train.shape)
	display(train.head(5))
	print()
	print(start + "Items" + end)
	print(items.shape)
	display(items.head(5))
	print()
	print(start + "Item_categories" + end)
	print(item_categories.shape)
	display(item_categories.head(5))
	print()
	print(start + "Shops" + end)
	print(shops.shape)
	display(shops.head(5))
	print()
	print(start + "Test" + end)
	print(test.shape)
	display(test.head(5))

def downcast_dtypes(df):
    float_cols = [c for c in df if df[c].dtype == "float64"]
    int_cols = [c for c in df if df[c].dtype in ["int64", "int32"]]
    df[float_cols] = df[float_cols].astype(np.float32)
    df[int_cols] = df[int_cols].astype(np.int16)
    return df
