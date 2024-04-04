import matplotlib.pyplot as plt

# Define the models and their corresponding accuracies
models = ['Logistic Regression', 'SVM', 'Decision Tree', 'KNN']
accuracies = [0.8333333333333334, 0.8333333333333334, 0.8333333333333334, 0.8333333333333334]

# Create a bar chart
plt.figure(figsize=(10, 6))
plt.bar(models, accuracies, color='skyblue')

# Add title and labels
plt.title('Model Accuracy Comparison')
plt.xlabel('Classification Models')
plt.ylabel('Accuracy')
plt.ylim(0.8, 0.85)  # Set y-axis limits for better visualization

# Display the accuracy values on top of the bars
for i, accuracy in enumerate(accuracies):
    plt.text(i, accuracy + 0.002, round(accuracy, 2), ha='center', va='bottom')

plt.show()