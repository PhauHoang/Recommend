import os
import sqlite3
import csv

if __name__ == '__main__':
    # Khai báo đường dẫn tới tệp dữ liệu lịch sử của người dùng (Windows Chrome)
    data_path = os.path.expanduser('~') + r"\AppData\Local\CocCoc\Browser\User Data\Default\History"
    # Đảm bảo Chrome đã đóng trước khi truy cập vào cơ sở dữ liệu

    # Thực hiện kết nối
    conn = sqlite3.connect(data_path)

    # Lấy con trỏ của cơ sở dữ liệu
    cursor = conn.cursor()

    # Truy vấn để lấy dữ liệu từ bảng keyword_search_terms
    cursor.execute("SELECT term FROM keyword_search_terms")

    # Lấy tên cột
    column_names = [description[0] for description in cursor.description]

    # Lấy dữ liệu từ các dòng
    rows = cursor.fetchall()

    # Đóng kết nối
    conn.close()

    # Lưu dữ liệu thành tệp CSV
    csv_file_path = "search_terms.csv"
    with open(csv_file_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        # Viết tên cột vào tệp CSV
        writer.writerow(column_names)
        # Viết dữ liệu từ các dòng vào tệp CSV
        writer.writerows(rows)

    print("Data saved to:", csv_file_path)
