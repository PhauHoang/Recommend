import pandas as pd

# Danh sách sản phẩm mới
new_products = [
    "Áo thun nữ",
    "Quần jeans nam",
    "Sim Mobifone",
    "Điện thoại Huawei",
    "Giày sandal nữ",
    "Túi xách nữ",
    "Đồng hồ nam",
    "Đồng hồ nữ",
    "Áo khoác nam",
    "Quần lửng nữ",
    "Sim trả sau",
    "Tai nghe Bluetooth",
    "Balo học sinh",
    "Đèn LED chiếu sáng",
    "Máy tính xách tay",
    "Áo hoodie nam",
    "Quần áo bơi nữ",
    "Mũ snapback nam",
    "Máy ảnh DSLR",
    "Bình nước thể thao",
    "Máy sưởi",
    "Chăn điện",
    "Tivi smart TV",
    "Nệm ngủ",
    "Bàn làm việc",
    "Điều hòa không khí",
    "Tủ lạnh",
    "Bếp từ",
    "Máy giặt",
    # Thêm các sản phẩm khác tại đây
]


# Đọc tệp CSV hiện có


# Tạo DataFrame cho sản phẩm mới
new_df = pd.DataFrame({'term': new_products, 'Label': 1})

# Kết hợp DataFrame mới với DataFrame hiện có
combined_df = pd.concat([new_df], ignore_index=True)

# Lưu DataFrame kết hợp vào tệp CSV
combined_df.to_csv('sanpham.csv', index=False)

print("Dữ liệu đã được thêm vào tệp combined_search_terms.csv")
