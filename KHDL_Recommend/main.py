import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
from sklearn.metrics import classification_report

# List of common encodings to try
encodings = ['utf-8', 'utf-8-sig', 'latin1', 'iso-8859-1']

for enc in encodings:
    try:
        # Attempt to read the CSV file with the current encoding
        df = pd.read_csv('search_terms.csv', encoding=enc)
        print(f"Successfully loaded CSV with encoding: {enc}")
        break
    except UnicodeDecodeError as e:
        print(f"Failed to load CSV with encoding {enc}: {e}")

# If df is successfully loaded, continue with the processing
if 'df' in locals():
    # Define keywords that indicate a product-related search term
    keywords = ['Giá', 'mua', 'shop', 'buy']

    # Add a 'Label' column based on whether the search term contains any of the keywords
    df['Label'] = df['term'].apply(lambda term: 1 if any(keyword.lower() in term.lower() for keyword in keywords) else 0)

    # Save the updated DataFrame back to a new CSV file
    new_filename = 'search_terms_labeled.csv'
    df.to_csv(new_filename, index=False, encoding=enc)
    print(f"Labels have been saved to '{new_filename}' with encoding: {enc}")

    # Features and labels
    X = df['term']
    y = df['Label']

    # Vectorize features using TF-IDF
    vectorizer = TfidfVectorizer()
    X_vectorized = vectorizer.fit_transform(X)

    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X_vectorized, y, test_size=0.2, random_state=42)

    # Train a Support Vector Machine (SVM) classifier
    svm_classifier = SVC(kernel='linear')
    svm_classifier.fit(X_train, y_train)

    # Predictions on the testing set
    y_pred = svm_classifier.predict(X_test)

    # Evaluation
    print("\nClassification Report:\n")
    print(classification_report(y_test, y_pred))

    # Displaying 5 sample predictions
    sample_indices = X_test[:5].nonzero()[0]
    sample_search_terms = df.iloc[sample_indices]['term'].values
    sample_predictions = pd.DataFrame({'term': sample_search_terms[:5], 'Predicted Label': y_pred[:5]})

    print("\nSample Predictions:\n")
    print(sample_predictions)

    # Chọn ra các từ khóa từ DataFrame có nhãn dự đoán là 1
    predicted_labels = svm_classifier.predict(X_vectorized)

    # Lấy chỉ mục của các từ khóa có nhãn dự đoán là 1
    indices_label_1 = [i for i, label in enumerate(predicted_labels) if label == 1]

    # In ra các từ khóa có nhãn dự đoán là 1
    print("Suggested Product Related Search Terms (Label 1):\n")
    print(df.iloc[indices_label_1]['term'])

    # Tạo một danh sách chứa các từ khóa có nhãn 1
    import pandas as pd

    # Giả sử df đã được tạo từ các bước trước và chứa các từ khóa
    label_1_keywords = df.iloc[indices_label_1]['term'].tolist()
    print(label_1_keywords)


    sanpham_df = pd.read_csv('sanpham.csv', encoding='latin1')
    print(sanpham_df)

    # Nếu sanpham_df đã được đọc thành công, tiếp tục xử lý
    if 'sanpham_df' in locals():
        # Tạo danh sách các sản phẩm tương đồng
        similar_products = []

        # Lọc các sản phẩm chứa từ khóa trong label_1_keywords
        for keyword in label_1_keywords:
            # Tìm kiếm sản phẩm có tên chứa từ khóa
            sanpham_df['SAN_PHAM'] = sanpham_df['SAN_PHAM'].str.lower()
            label_1_keywords = [keyword.lower() for keyword in label_1_keywords]

        # Loại bỏ các sản phẩm trùng lặp
        # Lọc các sản phẩm chứa ít nhất một từ trong từ khóa
    for keyword in label_1_keywords:
        keyword_words = keyword.split()  # Chia từ khóa thành các từ riêng lẻ
        for _, row in sanpham_df.iterrows():
            product_name = row['SAN_PHAM']
            product_words = product_name.split()  # Chia tên sản phẩm thành các từ riêng lẻ
            if any(word in product_words for word in keyword_words):
                similar_products.append(product_name)

        # Loại bỏ các sản phẩm trùng lặp
    similar_products = list(set(similar_products))

    # In ra danh sách các sản phẩm tương đồng
    if similar_products:
        print("\nSimilar Products:\n")
        for product in similar_products:
            print(product)
    else:
        print("\nNo similar products found.")
else:
    print("Failed to load the CSV file with all attempted encodings.")
